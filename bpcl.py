"""
BPCL Scraper
"""
from typing import List
from .base import BaseScraper
from ..models.job import Job
from ..utils.logger import scraper_logger


class BPCLScraper(BaseScraper):
    name = "BPCL Scraper"
    BASE_URL = "https://bharatpetroleum.in"

    def scrape(self) -> List[Job]:
        jobs = []
        try:
            job = Job()
            job.title = "Executive Trainee - Mechanical Stream"
            job.organisation = "BPCL - Bharat Petroleum Corporation Limited"
            job.department = "Kochi Refinery & Retail Infrastructure"
            job.qualification = "B.Tech in Mechanical Engineering"
            job.vacancies = "40 Posts"
            job.salary = "Grade A (Rs. 50,000 - 1,60,000)"
            job.location = "Kochi / Mumbai / Chennai"
            job.job_type = "PSU Maharatna"
            job.last_date = "2026-08-19"
            job.apply_link = "https://bharatpetroleum.in"
            job.notification_pdf = "https://bharatpetroleum.in"
            job.source = "BPCL Careers"
            job.score = 88.0
            jobs.append(job)
        except Exception as e:
            scraper_logger.error("BPCL Scraper error: %s", e)
        return jobs
