"""
Main Application Entry Point
AI Powered Government Jobs Telegram Bot
"""
import argparse
from telegram.ext import ApplicationBuilder, CommandHandler
from .config import TELEGRAM_BOT_TOKEN, SEND_TIME
from .database import Database
from .notifier import TelegramNotifier
from .scraper_manager import ScraperManager
from .pipeline import JobPipeline
from .handlers.start import start_command, help_command
from .handlers.search import today_command, search_command, stats_command
from .handlers.category import psu, railway, defence, central, state, teaching
from .utils.logger import bot_logger


def run_pipeline_once():
    bot_logger.info("=== Starting Daily Job Scraping Pipeline Execution ===")
    db = Database()
    notifier = TelegramNotifier()
    manager = ScraperManager()
    pipeline = JobPipeline(database=db, notifier=notifier)

    scraped_jobs = manager.run_all()
    bot_logger.info("Scraped total %d raw job items.", len(scraped_jobs))

    final_jobs = pipeline.process(scraped_jobs)
    bot_logger.info("Pipeline processed %d valid, non-duplicate jobs.", len(final_jobs))


def start_bot_polling():
    if not TELEGRAM_BOT_TOKEN or "YOUR_TELEGRAM" in TELEGRAM_BOT_TOKEN:
        bot_logger.error("Please configure TELEGRAM_BOT_TOKEN in .env file before starting polling.")
        return

    bot_logger.info("Initializing Telegram Bot Handlers...")
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("today", today_command))
    app.add_handler(CommandHandler("search", search_command))
    app.add_handler(CommandHandler("stats", stats_command))
    app.add_handler(CommandHandler("psu", psu))
    app.add_handler(CommandHandler("railway", railway))
    app.add_handler(CommandHandler("defence", defence))
    app.add_handler(CommandHandler("central", central))
    app.add_handler(CommandHandler("state", state))
    app.add_handler(CommandHandler("teaching", teaching))

    bot_logger.info("Telegram Bot started listening for incoming commands...")
    app.run_polling()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Govt Jobs Telegram Bot")
    parser.add_argument("--cron", action="store_true", help="Run scraper pipeline once and exit (for GitHub Actions)")
    args = parser.parse_args()

    if args.cron:
        run_pipeline_once()
    else:
        # Run scraping on startup once
        run_pipeline_once()
        # Start Telegram Bot Polling
        start_bot_polling()
