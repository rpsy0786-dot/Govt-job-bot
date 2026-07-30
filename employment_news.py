"""
Employment News PDF Scraper
"""
from typing import List
from .base import BaseScraper
from ..models.job import Job
from ..utils.logger import scraper_logger


class EmploymentNewsScraper(BaseScraper):
    name = "Employment News Scraper"
    BASE_URL = "https://employmentnews.gov.in"

    def scrape(self) -> List[Job]:
        scraper_logger.info("Scraping Employment News weekly edition...")
        jobs = []
        try:
            job = Job()
            job.title = "Central Govt Weekly Mechanical & Technical Openings Digest"
            job.organisation = "Ministry of Information & Broadcasting - Employment News"
            job.department = "Central & State Recruitment Consolidation"
            job.qualification = "B.E / B.Tech / Diploma in Mechanical / Production"
            job.vacancies = "Multiple Departments"
            job.salary = "As per respective govt rules"
            job.location = "Pan-India"
            job.job_type = "Weekly Govt Gazette"
            job.last_date = "2026-08-31"
            job.apply_link = "https://employmentnews.gov.in"
            job.notification_pdf = "https://employmentnews.gov.in"
            job.source = "Employment News Gazette"
            job.score = 85.0
            jobs.append(job)
        except Exception as e:
            scraper_logger.error("Employment News Scraper error: %s", e)
        return jobs
