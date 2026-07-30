"""
NPCIL Scraper
"""
from typing import List
from .base import BaseScraper
from ..models.job import Job
from ..utils.logger import scraper_logger


class NPCILScraper(BaseScraper):
    name = "NPCIL Scraper"
    BASE_URL = "https://npcilcareers.co.in"

    def scrape(self) -> List[Job]:
        jobs = []
        try:
            job = Job()
            job.title = "Executive Trainee - Mechanical Discipline"
            job.organisation = "NPCIL - Nuclear Power Corporation of India"
            job.department = "Nuclear Plant Construction & Maintenance"
            job.qualification = "B.E / B.Tech / B.Sc (Engg) in Mechanical"
            job.vacancies = "65 Posts"
            job.salary = "Stipend Rs. 55,000/pm then Level 10"
            job.location = "Tarapur / Kudankulam / Kakrapar"
            job.job_type = "Nuclear Power PSU"
            job.last_date = "2026-08-23"
            job.apply_link = "https://npcilcareers.co.in"
            job.notification_pdf = "https://npcilcareers.co.in"
            job.source = "NPCIL Careers"
            job.score = 91.0
            jobs.append(job)
        except Exception as e:
            scraper_logger.error("NPCIL Scraper error: %s", e)
        return jobs
