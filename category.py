"""
Category Filter Handlers: /psu, /railway, /defence, /central, /state, /teaching
"""
import html

from telegram import Update
from telegram.ext import ContextTypes

from ..database import Database
from ..notifier import format_job

db = Database()


async def _send_category(update: Update, keyword: str, label: str):
    jobs = db.get_jobs_by_type(keyword)
    if not jobs:
        await update.message.reply_text(
            f"❌ No {html.escape(label)} job notifications found currently."
        )
        return

    await update.message.reply_text(
        f"🏛️ Found <b>{len(jobs)}</b> {html.escape(label)} notification(s):",
        parse_mode="HTML",
    )
    for job in jobs[:5]:
        await update.message.reply_text(format_job(job), parse_mode="HTML", disable_web_page_preview=True)


async def psu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await _send_category(update, "psu", "PSU")


async def railway(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await _send_category(update, "railway", "Railway")


async def defence(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await _send_category(update, "defence", "Defence")


async def central(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await _send_category(update, "central", "Central Government")


async def state(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await _send_category(update, "state", "State Government")


async def teaching(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await _send_category(update, "teaching", "Teaching")
