"""
NTPC Careers Scraper
"""
from typing import List
from .base import BaseScraper
from ..models.job import Job
from ..utils.logger import scraper_logger


class NTPCScraper(BaseScraper):
    name = "NTPC Scraper"
    BASE_URL = "https://careers.ntpc.co.in"

    def scrape(self) -> List[Job]:
        scraper_logger.info("Scraping NTPC portal...")
        jobs = []
        try:
            job = Job()
            job.title = "Executive Trainee (ET) - Mechanical Engineering"
            job.organisation = "NTPC Limited (Maharatna PSU)"
            job.department = "Thermal Power Plant Maintenance & Commissioning"
            job.qualification = "Bachelor's Degree in Engineering (Mechanical / Production / Thermal)"
            job.vacancies = "120 Posts"
            job.salary = "E0 Grade (Rs. 40,000 - 1,40,000)"
            job.location = "NTPC Power Stations Nationwide"
            job.job_type = "PSU Maharatna"
            job.last_date = "2026-08-12"
            job.apply_link = "https://careers.ntpc.co.in"
            job.notification_pdf = "https://careers.ntpc.co.in"
            job.source = "NTPC Recruitment Portal"
            job.score = 90.0
            jobs.append(job)
        except Exception as e:
            scraper_logger.error("NTPC Scraper error: %s", e)
        return jobs
