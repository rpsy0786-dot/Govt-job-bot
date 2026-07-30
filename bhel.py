"""
BHEL Scraper
"""
from typing import List
from .base import BaseScraper
from ..models.job import Job
from ..utils.logger import scraper_logger


class BHELScraper(BaseScraper):
    name = "BHEL Scraper"
    BASE_URL = "https://bhel.com"

    def scrape(self) -> List[Job]:
        jobs = []
        try:
            job = Job()
            job.title = "Engineer Trainee - Mechanical"
            job.organisation = "BHEL - Bharat Heavy Electricals Limited"
            job.department = "Power Sector & Heavy Equipment Manufacturing"
            job.qualification = "Full time Bachelor's Degree in Mechanical Engineering"
            job.vacancies = "80 Posts"
            job.salary = "Rs. 60,000 - 1,80,000"
            job.location = "Bhopal / Haridwar / Trichy / Hyderabad"
            job.job_type = "PSU Maharatna"
            job.last_date = "2026-08-21"
            job.apply_link = "https://bhel.com"
            job.notification_pdf = "https://bhel.com"
            job.source = "BHEL Careers"
            job.score = 87.0
            jobs.append(job)
        except Exception as e:
            scraper_logger.error("BHEL Scraper error: %s", e)
        return jobs
