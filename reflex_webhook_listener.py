from flask import Flask, request, jsonify
import subprocess
import threading
import datetime
import json
import os

app = Flask(__name__)

# Write Trust Graph log
def update_trust_graph(lounge_id, trigger, context=None):
    if context is None:
        context = {}
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

# Background worker
def run_codex_script(script_path, args=None):
    if args is None:
        args = []
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
        threading.Thread(target=run_codex_script, args=("flavor_sync.py", [lounge_id])).start()
    elif trigger == "loyalty":
        threading.Thread(target=run_codex_script, args=("loyalty_reflex.py", [session_id])).start()
    elif trigger == "suggest_mix":
        threading.Thread(target=run_codex_script, args=("reflex_session.py", [user_id, base_flavor])).start()
    else:
        return jsonify({"status": "unknown trigger"}), 400

    return jsonify({"status": "reflex executed", "trigger": trigger}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
