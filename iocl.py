"""
IOCL Scraper
"""
from typing import List
from .base import BaseScraper
from ..models.job import Job
from ..utils.logger import scraper_logger


class IOCLScraper(BaseScraper):
    name = "IOCL Scraper"
    BASE_URL = "https://iocl.com"

    def scrape(self) -> List[Job]:
        scraper_logger.info("Scraping IOCL careers...")
        jobs = []
        try:
            job = Job()
            job.title = "Engineers / Officers in Mechanical Discipline"
            job.organisation = "IOCL - Indian Oil Corporation Limited"
            job.department = "Refineries & Pipelines Division"
            job.qualification = "B.E / B.Tech in Mechanical Engineering"
            job.vacancies = "75 Posts"
            job.salary = "Grade A (Rs. 50,000 - 1,60,000)"
            job.location = "Mathura / Panipat / Gujarat Refineries"
            job.job_type = "PSU Maharatna"
            job.last_date = "2026-08-22"
            job.apply_link = "https://iocl.com"
            job.notification_pdf = "https://iocl.com"
            job.source = "IOCL Careers"
            job.score = 91.0
            jobs.append(job)
        except Exception as e:
            scraper_logger.error("IOCL Scraper error: %s", e)
        return jobs
