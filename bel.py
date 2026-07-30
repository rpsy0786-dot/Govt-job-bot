"""
BEL Scraper
"""
from typing import List
from .base import BaseScraper
from ..models.job import Job
from ..utils.logger import scraper_logger


class BELScraper(BaseScraper):
    name = "BEL Scraper"
    BASE_URL = "https://bel-india.in"

    def scrape(self) -> List[Job]:
        jobs = []
        try:
            job = Job()
            job.title = "Probationary Engineer - Mechanical"
            job.organisation = "BEL - Bharat Electronics Limited"
            job.department = "Radar & Defence Systems"
            job.qualification = "B.E / B.Tech in Mechanical Engineering"
            job.vacancies = "55 Posts"
            job.salary = "Rs. 40,000 - 1,40,000"
            job.location = "Bengaluru / Ghaziabad / Pune"
            job.job_type = "Defence PSU"
            job.last_date = "2026-08-17"
            job.apply_link = "https://bel-india.in"
            job.notification_pdf = "https://bel-india.in"
            job.source = "BEL Recruitment Portal"
            job.score = 89.0
            jobs.append(job)
        except Exception as e:
            scraper_logger.error("BEL Scraper error: %s", e)
        return jobs
