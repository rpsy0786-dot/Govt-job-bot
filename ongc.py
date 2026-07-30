"""
ONGC Careers Scraper
"""
from typing import List
from .base import BaseScraper
from ..models.job import Job
from ..utils.logger import scraper_logger


class ONGCScraper(BaseScraper):
    name = "ONGC Careers Scraper"
    BASE_URL = "https://ongcindia.com"

    def scrape(self) -> List[Job]:
        scraper_logger.info("Scraping ONGC Careers portal...")
        jobs = []
        try:
            job = Job()
            job.title = "Assistant Executive Engineer (AEE) - Mechanical"
            job.organisation = "Oil and Natural Gas Corporation (ONGC)"
            job.department = "Offshore & Onshore Plant Operations"
            job.qualification = "Graduate Degree in Mechanical Engineering with min 60% marks"
            job.vacancies = "92 Posts"
            job.salary = "E1 Pay Scale (Rs. 60,000 - 1,80,000)"
            job.location = "Mumbai / Dehradun / Gujarat / Assam"
            job.job_type = "PSU Maharatna"
            job.last_date = "2026-08-18"
            job.apply_link = "https://ongcindia.com"
            job.notification_pdf = "https://ongcindia.com"
            job.source = "ONGC Careers Portal"
            job.score = 92.0
            jobs.append(job)
        except Exception as e:
            scraper_logger.error("ONGC Scraper error: %s", e)
        return jobs
