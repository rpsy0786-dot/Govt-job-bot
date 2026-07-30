"""
Duplicate Detector
"""
import hashlib
from typing import List, Set
from ..models.job import Job


class DuplicateDetector:

    @staticmethod
    def generate_hash(job: Job) -> str:
        text = f"{job.organisation}_{job.title}_{job.last_date}".lower().strip()
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    @classmethod
    def filter_new_jobs(cls, scraped_jobs: List[Job], existing_jobs: List[Job], existing_hashes: Set[str]) -> List[Job]:
        new_jobs = []
        seen_in_batch = set()

        for job in scraped_jobs:
            h = cls.generate_hash(job)
            if h not in existing_hashes and h not in seen_in_batch:
                seen_in_batch.add(h)
                new_jobs.append(job)

        return new_jobs
