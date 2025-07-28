import json
from reflex_webhook_listener import update_trust_graph, seed_whisper

def handler(event, context):
    if event.get("httpMethod") != "POST":
        return {"statusCode": 405, "body": "Method Not Allowed"}

    try:
        data = json.loads(event.get("body") or "{}")
    except json.JSONDecodeError:
        return {"statusCode": 400, "body": "Invalid JSON"}

    trigger = data.get("trigger")
    lounge_id = data.get("lounge_id")
    session_id = data.get("session_id")
    user_id = data.get("user_id")
    base_flavor = data.get("base_flavor")

    if not trigger or not lounge_id:
        return {"statusCode": 400, "body": "Missing trigger or lounge_id"}

    update_trust_graph(lounge_id, trigger, {
        "session_id": session_id,
        "user_id": user_id,
        "base_flavor": base_flavor,
    })

    if trigger == "loyalty":
        seed_whisper(lounge_id, f"Loyalty replay for session {session_id}")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"status": "reflex executed", "trigger": trigger})
    }
