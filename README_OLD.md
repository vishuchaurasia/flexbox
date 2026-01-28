# FlexBook (Flaskshop) – local setup (Windows)

This repo contains:

- **Backend**: Flask app (`app.py`, package `flaskshop/`)
- **Frontend**: Webpack build in `frontend/` that outputs to `flaskshop/static/build/`

## Prereqs

- Python **3.9+**
- Node.js **18+** (you already have Node 20)

## Backend setup (PowerShell)

From the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip setuptools wheel
.\.venv\Scripts\python -m pip install --no-compile -r requirements.txt
```

## Frontend setup (PowerShell)

```powershell
cd frontend
npm ci
npm run build
cd ..
```

This generates assets in `flaskshop/static/build/` for the Flask app to serve.

## Configure DB (SQLite default)

This project defaults to MySQL, but for local dev we use SQLite via `.env`:

- `DB_URI=sqlite:///flaskshop.db`

You can change it anytime (or set `DB_URI` in your shell).

## Initialize database + run

```powershell
# Create tables
.\.venv\Scripts\python -m flask --app app createdb

# (Optional) Seed demo data
.\.venv\Scripts\python -m flask --app app seed

# Run
.\.venv\Scripts\python -m flask --app app run --debug
```

Open `http://127.0.0.1:5000`.

## Optional services

- **Redis**: set `USE_REDIS=true` and run redis locally (default: off)
- **Elasticsearch**: set `USE_ES=true` and run ES locally (default: off)

