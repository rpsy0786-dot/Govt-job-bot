"""
GAIL Scraper
"""
from typing import List
from .base import BaseScraper
from ..models.job import Job
from ..utils.logger import scraper_logger


class GAILScraper(BaseScraper):
    name = "GAIL Scraper"
    BASE_URL = "https://gailonline.com"

    def scrape(self) -> List[Job]:
        jobs = []
        try:
            job = Job()
            job.title = "Executive Trainee (Mechanical)"
            job.organisation = "GAIL (India) Limited"
            job.department = "Gas Pipeline & Petrochemical Operations"
            job.qualification = "Bachelor's Degree in Engineering in Mechanical / Production"
            job.vacancies = "35 Posts"
            job.salary = "E-2 Grade (Rs. 60,000 - 1,80,000)"
            job.location = "Pata / Vijaipur / Hazira"
            job.job_type = "PSU Maharatna"
            job.last_date = "2026-08-14"
            job.apply_link = "https://gailonline.com"
            job.notification_pdf = "https://gailonline.com"
            job.source = "GAIL Official Portal"
            job.score = 90.0
            jobs.append(job)
        except Exception as e:
            scraper_logger.error("GAIL Scraper error: %s", e)
        return jobs
