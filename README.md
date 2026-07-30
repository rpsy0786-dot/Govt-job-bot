# 🤖 AI-Powered Government Jobs Telegram Bot

A complete Python Web Scraper and Telegram Bot system that automatically monitors 16+ Indian Government Recruitment Portals (DRDO, ONGC, RRB Railways, NTPC, ISRO, BARC, UPSC, SSC, IOCL, HPCL, BPCL, GAIL, BHEL, BEL, NPCIL) for **Mechanical Engineering** and Government job openings.

---

## ⚡ Features
- 🏛️ **16+ Automated Scrapers:** Scrapes official `.gov.in` and `.nic.in` portals daily.
- 🎯 **AI Relevancy Classifier:** Filters jobs matching Mechanical Engineering, B.Tech/Diploma, and 0-8 yrs experience.
- 🛡️ **URL Health Assurance:** Uses domain fallback mapping ensuring links never fail or link to invalid URLs.
- 🚀 **GitHub Actions Automated Cron:** Automatically executes scrapers every day at 09:00 AM IST without requiring a server.
- 📲 **Telegram Channel/Bot Integration:** Delivers rich HTML formatted notifications.

---

## 🛠️ How to Deploy on GitHub (Free & Automated)

### Step 1: Create a GitHub Repository
1. Click **Download ZIP Package** in the app.
2. Extract the files and upload or push them to your GitHub repository:
```bash
git init
git add .
git commit -m "Initial commit - Govt Jobs Telegram Bot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/govt-jobs-telegram-bot.git
git push -u origin main
```

### Step 2: Configure GitHub Secrets
1. Go to your GitHub Repository -> **Settings** -> **Secrets and variables** -> **Actions**.
2. Click **New repository secret**:
   - `TELEGRAM_BOT_TOKEN`: Your Bot Father token (e.g., `7123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ12345`)
   - `TELEGRAM_CHAT_ID`: Your Telegram User ID or Channel Chat ID (e.g., `-100123456789`)

### Step 3: Trigger Workflow
Go to **Actions** tab -> **Daily Government Jobs Scraper & Telegram Notifier** -> Click **Run workflow**.

---

## 💻 Local Execution

```bash
# 1. Clone repository & enter folder
cd govt-jobs-telegram-bot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file
cp .env.example .env
# Edit .env with your TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID

# 4. Run Scraper Pipeline & Telegram Bot
python -m bot.main
```

---

## ⚠️ Known Limitations (please read before relying on this in production)

- **Scrapers currently return placeholder/sample data, not live-scraped listings.** Each scraper module (`bot/scrapers/*.py`) has working HTTP + BeautifulSoup helpers via `BaseScraper.fetch()` / `BaseScraper.soup()`, but the individual `scrape()` methods return one hardcoded sample `Job` instead of parsing the fetched HTML. Each government portal has its own page structure (and changes it periodically), so wiring up real selectors needs to be done and verified per-site — selectors weren't guessed for sites that couldn't be verified live, since a wrong guess fails silently rather than raising an error you'd notice.
- **`jobs.db` is committed back to the repo by the GitHub Actions workflow** so duplicate-detection history survives across scheduled runs (Actions runners are ephemeral and would otherwise forget every job already sent, re-notifying you daily). If you'd rather not commit a binary DB file to Git history, swap this for an external store (e.g. a small Postgres/Supabase instance, or a cache) — the `Database` class only assumes a local SQLite file path, not any Actions-specific coupling.
- **Chat ID and Bot Token are shared secrets, not per-user.** The bot notifies one configured `TELEGRAM_CHAT_ID`; `/today`, `/search`, `/psu` etc. all read from the same shared `jobs.db`. Multi-user preferences (the `Profile` model exists but isn't wired into filtering yet) would need per-chat storage to support multiple recipients with different filters.

---
