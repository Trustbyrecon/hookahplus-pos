from reflex_webhook_listener import update_trust_graph, seed_whisper, enable_trustgraph_logging


def simulate():
    """Generate sample logs for lounge_001."""
    enable_trustgraph_logging(True)
    context = {
        "session_id": "sess-sim",
        "user_id": "user-sim",
        "base_flavor": "mint",
    }
    update_trust_graph("lounge_001", "drift", context)
    update_trust_graph("lounge_001", "loyalty", context)
    seed_whisper("lounge_001", "Simulated loyalty whisper")
    update_trust_graph("lounge_001", "suggest_mix", context)


if __name__ == "__main__":
    simulate()
