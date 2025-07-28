from flask import Flask, request, jsonify, send_from_directory
import subprocess
import threading
import datetime
import json
import os

app = Flask(__name__)

# Flag controlling whether trust graph events are written to disk
ENABLE_TRUSTGRAPH_LOGGING = True

def enable_trustgraph_logging(enable: bool = True):
    """Toggle trust graph logging."""
    global ENABLE_TRUSTGRAPH_LOGGING
    ENABLE_TRUSTGRAPH_LOGGING = enable

# Write Trust Graph log
def update_trust_graph(lounge_id, trigger, context={}):
    if not ENABLE_TRUSTGRAPH_LOGGING:
        return

    log_dir = "trustgraph_logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{lounge_id}_trustgraph.jsonl")

    entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "lounge_id": lounge_id,
        "trigger": trigger,
        "context": context
    }

    with open(log_file, "a") as f:
        f.write(json.dumps(entry) + "\n")

    print(f"🧭 TrustGraph updated: {entry}")

# Seed a Whisper message for loyalty replay
def seed_whisper(lounge_id, message):
    log_dir = "whisper_seeds"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{lounge_id}_whispers.jsonl")

    entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "lounge_id": lounge_id,
        "message": message,
    }

    with open(log_file, "a") as f:
        f.write(json.dumps(entry) + "\n")

    print(f"\U0001F5E3 Whisper seeded: {entry}")

# Background worker
def run_codex_script(script_path, args=[]):
    try:
        subprocess.run(['python', script_path] + args, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e}")

@app.route("/hooks/aliethia", methods=["POST"])
def aliethia_hook():
    data = request.get_json()

    trigger = data.get("trigger")
    lounge_id = data.get("lounge_id")
    session_id = data.get("session_id", None)
    user_id = data.get("user_id", None)
    base_flavor = data.get("base_flavor", None)

    print(f"\U0001F4E5 Received Reflex Trigger: {trigger} from {lounge_id}")

    # Update Trust Graph
    update_trust_graph(
        lounge_id=lounge_id,
        trigger=trigger,
        context={
            "session_id": session_id,
            "user_id": user_id,
            "base_flavor": base_flavor
        }
    )

    # Logic routes
    if trigger == "drift":
        threading.Thread(target=run_codex_script, args=["flavor_sync.py", [lounge_id]]).start()
    elif trigger == "loyalty":
        threading.Thread(target=run_codex_script, args=["loyalty_reflex.py", [session_id]]).start()
        seed_whisper(lounge_id, f"Loyalty replay for session {session_id}")
    elif trigger == "suggest_mix":
        threading.Thread(target=run_codex_script, args=["reflex_session.py", [user_id, base_flavor]]).start()
    else:
        return jsonify({"status": "unknown trigger"}), 400

    return jsonify({"status": "reflex executed", "trigger": trigger}), 200


@app.route("/dashboard")
def dashboard():
    return send_from_directory("app/dashboard", "index.html")


@app.route("/preorder")
def preorder():
    return send_from_directory("app/dashboard", "preorder.html")


@app.route("/whisper/<lounge_id>", methods=["GET"])
def get_whispers(lounge_id):
    log_file = os.path.join("whisper_seeds", f"{lounge_id}_whispers.jsonl")
    entries = []
    if os.path.exists(log_file):
        with open(log_file) as f:
            entries = [json.loads(line) for line in f if line.strip()]
    return jsonify(entries), 200


@app.route("/trustgraph/<lounge_id>", methods=["GET"])
def get_trust_graph(lounge_id):
    log_file = os.path.join("trustgraph_logs", f"{lounge_id}_trustgraph.jsonl")
    entries = []
    if os.path.exists(log_file):
        with open(log_file) as f:
            entries = [json.loads(line) for line in f if line.strip()]
    return jsonify(entries), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
