# Hookah+ POS

This repository contains a minimal starter setup for the Hookah+ point of sale dashboard and Netlify Functions.

## Project Structure

- `app/dashboard` – Frontend dashboard assets. Currently contains a placeholder `index.html`.
- `netlify/functions` – Serverless functions used by Netlify. Includes a sample `hello.js` function.
- `netlify.toml` – Netlify configuration pointing to the above directories.

## Setup

1. Install Node.js (v18 or later recommended).
2. Install project dependencies:
   ```bash
   npm install
   ```
3. Build the project:
   ```bash
   npm run build
   ```

## Local Development

To test the Netlify Functions and dashboard locally, you can use the Netlify CLI:

```bash
npm install -g netlify-cli
netlify dev
```

This will serve the contents of `app/dashboard` and emulate function calls from `netlify/functions`.

## Deployment

1. Push this repository to a Git provider (GitHub, GitLab, etc.).
2. Connect the repository to Netlify and ensure the **Base directory** is `app/dashboard` and the **Functions directory** is `netlify/functions` (already configured in `netlify.toml`).
3. Netlify will run `npm run build` and deploy the contents of `dist`.

Feel free to replace the placeholder files with your actual dashboard code and functions.

## Testing Loyalty Flow

You can simulate the loyalty trigger locally using the included helper script:

```bash
python loyalty_replay_simulation.py
```

The script posts a sample payload to the webhook and invokes `loyalty_reflex.py`,
allowing you to verify the reflex flow without deploying.
