from reflex_webhook_listener import app, enable_trustgraph_logging

def activateWebhookEndpoint(host='0.0.0.0', port=5000):
    """Activate the webhook Flask endpoint for local testing."""
    app.run(host=host, port=port)

def enableTrustGraphLogging(enable=True):
    """Enable or disable Trust Graph logging."""
    enable_trustgraph_logging(enable)

if __name__ == '__main__':
    enableTrustGraphLogging(True)
    activateWebhookEndpoint()
