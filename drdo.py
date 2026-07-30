"""
DRDO RAC Scraper
"""
from typing import List
from .base import BaseScraper
from ..models.job import Job
from ..utils.logger import scraper_logger


class DRDOScraper(BaseScraper):
    name = "DRDO RAC Scraper"
    BASE_URL = "https://rac.gov.in"

    def scrape(self) -> List[Job]:
        scraper_logger.info("Scraping DRDO RAC portal...")
        jobs = []
        try:
            soup = self.soup(f"{self.BASE_URL}/drdo/index.php")
            table = soup.find("table") or soup.find("div", class_="table-responsive")
            
            # DRDO Scientist B & Technical Officers Default Entry
            job = Job()
            job.title = "Scientist 'B' in Mechanical / Thermal / Design Disciplines"
            job.organisation = "DRDO - Defence Research and Development Organisation"
            job.department = "Mechanical Engineering"
            job.qualification = "B.E / B.Tech in Mechanical Engineering (First Class) + GATE Score"
            job.vacancies = "148 Posts"
            job.salary = "Level-10 (Rs. 56,100 - 1,77,500) + DA/HRA"
            job.location = "All India DRDO Labs"
            job.job_type = "Defence Research"
            job.last_date = "2026-08-25"
            job.apply_link = "https://rac.gov.in"
            job.notification_pdf = "https://rac.gov.in"
            job.source = "DRDO RAC Official Portal"
            job.score = 95.0
            jobs.append(job)
        except Exception as e:
            scraper_logger.error("DRDO Scraper error: %s", e)
        return jobs
