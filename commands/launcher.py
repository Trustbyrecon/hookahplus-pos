# commands/launcher.py

def dispatch_command(cmd):
    match cmd:
        case "cmd.deployOperatorDashboard()":
            deploy_operator_dashboard()
        case "cmd.enableWhisperJournal()":
            enable_whisper_journal(scope="loyalty")
        case "cmd.activateSessionReplay()":
            activate_session_replay()
        case "cmd.deployReflexUI()":
            deploy_reflex_ui()
        case cmd if cmd.startswith("cmd.renderReflexLoyalty(") and cmd.endswith(")"):
            user_id = cmd[len("cmd.renderReflexLoyalty("):-1]
            user_id = user_id.strip("'\"")
            render_reflex_loyalty(user_id)
        case "cmd.injectReflexHeatmap()":
            inject_reflex_heatmap()
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

def deploy_reflex_ui():
    print("[🚀] Deploying Reflexive UI...")
    import subprocess
    subprocess.run(["python", "../Hookahplus/cmd_dispatcher.py", "deployReflexUI"])

def render_reflex_loyalty(user_id):
    print(f"[🎯] Rendering Reflex loyalty for {user_id}...")
    import subprocess
    subprocess.run(["python", "../Hookahplus/cmd_dispatcher.py", "renderReflexLoyalty", user_id])

def inject_reflex_heatmap():
    print("[🔥] Injecting Reflex Heatmap...")
    import subprocess
    subprocess.run(["python", "../Hookahplus/cmd_dispatcher.py", "injectReflexHeatmap"])

if __name__ == "__main__":
    import sys
    dispatch_command(sys.argv[1])
