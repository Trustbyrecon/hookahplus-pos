# codex_cmd_launcher.py
import subprocess
import os

def cmd_dispatch(command: str):
    if command == "cmd.deployOperatorDashboard()":
        print("🚀 Deploying Hookah+ Operator Dashboard...")
        subprocess.run(["npm", "run", "build-dashboard"])
        print("✅ Dashboard deployed.")
    elif command == "cmd.deployPreorderFlow()":
        print("🚀 Deploying Preorder Flow...")
        subprocess.run(["npm", "run", "build-preorder"])
    elif command == "cmd.deployReflexWebhook()":
        print("⚙️ Starting Reflex Webhook listener (mock mode)...")
        os.system("python reflex_webhook_listener.py")
    elif command == "cmd.deployReflexUI()":
        print("🚀 Deploying Reflexive UI...")
        subprocess.run(["python", "../Hookahplus/cmd_dispatcher.py", "deployReflexUI"])
    elif command.startswith("cmd.renderReflexLoyalty(") and command.endswith(")"):
        user_id = command[len("cmd.renderReflexLoyalty("):-1]
        user_id = user_id.strip("'\"")
        print(f"🎯 Rendering Reflex loyalty for {user_id}...")
        subprocess.run(["python", "../Hookahplus/cmd_dispatcher.py", "renderReflexLoyalty", user_id])
    elif command == "cmd.injectReflexHeatmap()":
        print("🔥 Injecting Reflex Heatmap...")
        subprocess.run(["python", "../Hookahplus/cmd_dispatcher.py", "injectReflexHeatmap"])
    elif command == "cmd.enableWhisperJournal({ scope: 'loyalty' })":
        print("📘 Loyalty Whisper Journal enabled.")
    else:
        print(f"❓ Unknown command: {command}")
