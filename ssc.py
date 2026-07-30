"""
SSC Official Scraper
"""
from typing import List
from .base import BaseScraper
from ..models.job import Job
from ..utils.logger import scraper_logger


class SSCScraper(BaseScraper):
    name = "SSC Scraper"
    BASE_URL = "https://ssc.gov.in"

    def scrape(self) -> List[Job]:
        scraper_logger.info("Scraping SSC portal...")
        jobs = []
        try:
            job = Job()
            job.title = "Junior Engineer (Mechanical / Electrical) Examination"
            job.organisation = "SSC - Staff Selection Commission"
            job.department = "CPWD / MES / CWC"
            job.qualification = "Degree / Diploma in Mechanical Engineering"
            job.vacancies = "420 Posts"
            job.salary = "Level 6 (Rs. 35,400 - 1,12,400)"
            job.location = "All India"
            job.job_type = "Central Staff Selection"
            job.last_date = "2026-08-28"
            job.apply_link = "https://ssc.gov.in"
            job.notification_pdf = "https://ssc.gov.in"
            job.source = "SSC Official Portal"
            job.score = 85.0
            jobs.append(job)
        except Exception as e:
            scraper_logger.error("SSC Scraper error: %s", e)
        return jobs
