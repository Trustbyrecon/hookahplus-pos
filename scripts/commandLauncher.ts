import { execSync } from 'child_process';

export const cmd = {
  deployOperatorDashboard: (): void => {
    execSync('npm run build', { stdio: 'inherit' });
    execSync('npx netlify deploy --dir=dist --prod', { stdio: 'inherit' });
  }
};

export default cmd;

if (require.main === module) {
  const command = process.argv[2] as keyof typeof cmd | undefined;
  if (!command || !(command in cmd)) {
    console.error('Usage: ts-node scripts/commandLauncher.ts <command>');
    console.error('Available commands:', Object.keys(cmd).join(', '));
    process.exit(1);
  }
  cmd[command]();
}
