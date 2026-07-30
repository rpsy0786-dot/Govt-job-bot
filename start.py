"""
Start and Help Command Handlers
"""
from telegram import Update
from telegram.ext import ContextTypes


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_msg = (
        "<b>🤖 Welcome to AI-Powered Government Jobs Alert Bot!</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "I track and monitor <b>16+ official government portals</b> daily for "
        "<b>Mechanical Engineering</b> & Govt postings.\n\n"
        "<b>⚡ Quick Commands:</b>\n"
        "• /today - View jobs posted today\n"
        "• /psu - View PSU notifications (ONGC, NTPC, IOCL...)\n"
        "• /defence - View DRDO, ISRO, BARC, BEL openings\n"
        "• /railway - View Railway & RRB notifications\n"
        "• /search mechanical - Search by keyword\n"
        "• /stats - Scraper & database health check\n"
        "• /help - Display full user guide\n\n"
        "<i>All links redirect directly to official government portals (.gov.in / .nic.in).</i>"
    )
    await update.message.reply_text(welcome_msg, parse_mode="HTML")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_msg = (
        "<b>📖 Bot User Guide & Supported Commands</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "1. <b>/today</b> - Get latest daily government alerts.\n"
        "2. <b>/search &lt;keyword&gt;</b> - Search database for specific posts.\n"
        "3. <b>/psu</b> - Filters Maharatna & Navratna PSUs.\n"
        "4. <b>/defence</b> - DRDO, ISRO, BARC, BEL recruitment.\n"
        "5. <b>/railway</b> - RRB & Indian Railways postings.\n"
        "6. <b>/stats</b> - View scraper stats & database status.\n"
    )
    await update.message.reply_text(help_msg, parse_mode="HTML")
