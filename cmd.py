from reflex_webhook_listener import app

def activateWebhookEndpoint(host='0.0.0.0', port=5000):
    """Activate the webhook Flask endpoint for local testing."""
    app.run(host=host, port=port)

if __name__ == '__main__':
    activateWebhookEndpoint()
