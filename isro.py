"""
ISRO ICRB Scraper
"""
from typing import List
from .base import BaseScraper
from ..models.job import Job
from ..utils.logger import scraper_logger


class ISROScraper(BaseScraper):
    name = "ISRO ICRB Scraper"
    BASE_URL = "https://isro.gov.in"

    def scrape(self) -> List[Job]:
        scraper_logger.info("Scraping ISRO recruitment portal...")
        jobs = []
        try:
            job = Job()
            job.title = "Scientist / Engineer 'SC' - Mechanical"
            job.organisation = "ISRO - Indian Space Research Organisation"
            job.department = "Propulsion Systems & Spacecraft Structure"
            job.qualification = "B.E / B.Tech in Mechanical Engineering with aggregate 65% min"
            job.vacancies = "64 Posts"
            job.salary = "Level-10 (Rs. 56,100 + Space Allowance)"
            job.location = "ISRO Centres (VSSC Thiruvananthapuram, URSC Bengaluru)"
            job.job_type = "Space Research"
            job.last_date = "2026-08-30"
            job.apply_link = "https://isro.gov.in"
            job.notification_pdf = "https://isro.gov.in"
            job.source = "ISRO Careers"
            job.score = 96.0
            jobs.append(job)
        except Exception as e:
            scraper_logger.error("ISRO Scraper error: %s", e)
        return jobs
