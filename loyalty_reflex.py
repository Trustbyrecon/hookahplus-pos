import sys

if __name__ == "__main__":
    session_id = sys.argv[1] if len(sys.argv) > 1 else ""
    print(f"🎉 Loyalty reflex executed for session {session_id}")
