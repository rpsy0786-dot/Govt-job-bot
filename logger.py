"""
Unified Logging Configuration
"""
import logging
import sys


def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


bot_logger = setup_logger("GovtJobsBot")
scraper_logger = setup_logger("ScraperEngine")
database_logger = setup_logger("Database")
telegram_logger = setup_logger("TelegramNotifier")
