from pathlib import Path
from reflex_webhook_listener import app, enable_trustgraph_logging

def activateWebhookEndpoint(host='0.0.0.0', port=5000):
    """Activate the webhook Flask endpoint for local testing."""
    app.run(host=host, port=port)

def enableTrustGraphLogging(enable=True):
    """Enable or disable Trust Graph logging."""
    enable_trustgraph_logging(enable)

def injectWhisperOverlay(loyaltyOnly=True):
    """Inject the Whisper Journal overlay script into the dashboard.

    If loyaltyOnly is True, the overlay automatically opens only when the
    dashboard is loaded with ``?loyalty=1`` in the query string. Otherwise the
    overlay opens on every visit.
    """
    dashboard_path = Path("app/dashboard/index.html")
    if not dashboard_path.exists():
        print("Dashboard file not found", dashboard_path)
        return

    html = dashboard_path.read_text()
    marker = "<!-- WHISPER_OVERLAY -->"
    if marker in html:
        print("Whisper overlay already injected")
        return

    condition = "params.get('loyalty') === '1'" if loyaltyOnly else "true"
    snippet = f"""
  {marker}
  <script>
    document.addEventListener('DOMContentLoaded', function() {{
      const params = new URLSearchParams(window.location.search);
      if ({condition}) {{
        document.getElementById('show-whisper').click();
      }}
    }});
  </script>"""

    if "</body>" in html:
        html = html.replace("</body>", snippet + "\n</body>")
    else:
        html += "\n" + snippet + "\n"

    dashboard_path.write_text(html)
    print("Whisper overlay injected")

if __name__ == '__main__':
    enableTrustGraphLogging(True)
    activateWebhookEndpoint()
