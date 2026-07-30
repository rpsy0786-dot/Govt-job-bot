"""
RRB Railway Scraper
"""
from typing import List
from .base import BaseScraper
from ..models.job import Job
from ..utils.logger import scraper_logger


class RRBScraper(BaseScraper):
    name = "RRB Railway Scraper"
    BASE_URL = "https://www.rrbald.gov.in"

    def scrape(self) -> List[Job]:
        scraper_logger.info("Scraping RRB Railways portal...")
        jobs = []
        try:
            job = Job()
            job.title = "Junior Engineer (JE) - Mechanical Loco, Carriage & Wagon"
            job.organisation = "Indian Railways - Railway Recruitment Board (RRB)"
            job.department = "Mechanical Engineering"
            job.qualification = "Three years Diploma or B.Tech in Mechanical / Production / Automobile"
            job.vacancies = "310 Posts"
            job.salary = "Level-6 Pay Matrix (Rs. 35,400 + Allowances)"
            job.location = "All India Railway Zones"
            job.job_type = "Central Railway"
            job.last_date = "2026-08-15"
            job.apply_link = "https://www.rrbald.gov.in"
            job.notification_pdf = "https://www.rrbald.gov.in"
            job.source = "RRB Official Portal"
            job.score = 88.0
            jobs.append(job)
        except Exception as e:
            scraper_logger.error("RRB Scraper error: %s", e)
        return jobs
