# Reflex Deployment Manifest

This repository hosts minimal scripts used by Hookah+ POS to test Reflex workflows.

## Available scripts

- `reflex_webhook_listener.py` – Flask endpoint that routes webhook triggers to local scripts.
- `flavor_sync.py` – placeholder script. It currently logs the lounge ID passed to it.
- `reflex_session.py` – placeholder script. It logs the user and base flavor supplied.

These placeholders ensure the webhook listener does not fail even when the real
business logic is not yet implemented. Replace them with actual implementations
as the project evolves.
