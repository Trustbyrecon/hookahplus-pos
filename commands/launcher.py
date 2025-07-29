# commands/launcher.py

def dispatch_command(cmd):
    match cmd:
        case "cmd.deployOperatorDashboard()":
            deploy_operator_dashboard()
        case "cmd.enableWhisperJournal()":
            enable_whisper_journal(scope="loyalty")
        case "cmd.activateSessionReplay()":
            activate_session_replay()
        case _:
            print(f"[⚠️] Unknown command: {cmd}")

def deploy_operator_dashboard():
    print("[🚀] Deploying Operator Dashboard...")
    import os
    os.system("npm run build && npm run export")

def enable_whisper_journal(scope="loyalty"):
    print(f"[🌀] Injecting Whisper Journal overlay for scope: {scope}")
    # Modify the dashboard layout to enable loyalty-triggered Whisper view
    with open("src/components/WhisperOverlay.tsx", "a") as f:
        f.write(f"\n// Activated overlay for {scope}")

def activate_session_replay():
    print("[🎞️] Activating session replay visual hooks...")
    # Stub hook for replay events
    with open("src/hooks/useReplay.ts", "w") as f:
        f.write("// Session replay tracking injected")

if __name__ == "__main__":
    import sys
    dispatch_command(sys.argv[1])
