from reflex_webhook_listener import app
import json

payload = {
    "trigger": "loyalty",
    "lounge_id": "test_lounge",
    "session_id": "test_session"
}

with app.test_client() as client:
    response = client.post(
        "/hooks/aliethia",
        data=json.dumps(payload),
        content_type="application/json"
    )
    print("Status:", response.status_code)
    print("Body:", response.json)
