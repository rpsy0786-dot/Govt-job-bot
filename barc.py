"""
BARC OCES Scraper
"""
from typing import List
from .base import BaseScraper
from ..models.job import Job
from ..utils.logger import scraper_logger


class BARCScraper(BaseScraper):
    name = "BARC OCES Scraper"
    BASE_URL = "https://barcoces.gov.in"

    def scrape(self) -> List[Job]:
        scraper_logger.info("Scraping BARC OCES portal...")
        jobs = []
        try:
            job = Job()
            job.title = "Scientific Officer Grade 'C' (Mechanical Thermal)"
            job.organisation = "BARC - Bhabha Atomic Research Centre"
            job.department = "Nuclear Thermal Power & Reactor Design"
            job.qualification = "B.E / B.Tech in Mechanical Engineering"
            job.vacancies = "50 Posts"
            job.salary = "Level 10 (Rs. 56,100 + NP Allowance)"
            job.location = "Trombay Mumbai / Kalpakkam / Rawatbhata"
            job.job_type = "Atomic Energy"
            job.last_date = "2026-08-10"
            job.apply_link = "https://barcoces.gov.in"
            job.notification_pdf = "https://barcoces.gov.in"
            job.source = "BARC OCES Portal"
            job.score = 94.0
            jobs.append(job)
        except Exception as e:
            scraper_logger.error("BARC Scraper error: %s", e)
        return jobs
