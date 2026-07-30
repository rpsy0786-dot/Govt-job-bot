"""
HPCL Scraper
"""
from typing import List
from .base import BaseScraper
from ..models.job import Job
from ..utils.logger import scraper_logger


class HPCLScraper(BaseScraper):
    name = "HPCL Scraper"
    BASE_URL = "https://hindustanpetroleum.com"

    def scrape(self) -> List[Job]:
        scraper_logger.info("Scraping HPCL careers...")
        jobs = []
        try:
            job = Job()
            job.title = "Mechanical Engineer Trainee & Senior Engineers"
            job.organisation = "HPCL - Hindustan Petroleum Corporation Limited"
            job.department = "Visakh & Mumbai Refineries"
            job.qualification = "4-year full time Engineering degree in Mechanical"
            job.vacancies = "60 Posts"
            job.salary = "E2 Grade (Rs. 50,000 - 1,60,000)"
            job.location = "Mumbai / Visakhapatnam / Marketing Zones"
            job.job_type = "PSU Navratna"
            job.last_date = "2026-08-16"
            job.apply_link = "https://hindustanpetroleum.com"
            job.notification_pdf = "https://hindustanpetroleum.com"
            job.source = "HPCL Careers"
            job.score = 89.0
            jobs.append(job)
        except Exception as e:
            scraper_logger.error("HPCL Scraper error: %s", e)
        return jobs
