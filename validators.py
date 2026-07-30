"""
Job Validator
"""
from typing import Tuple, List
from ..models.job import Job


class JobValidator:

    @staticmethod
    def validate(job: Job) -> Tuple[bool, List[str]]:
        errors = []
        if not job.title or len(job.title.strip()) < 3:
            errors.append("Invalid or missing title")
        if not job.organisation:
            errors.append("Missing organisation name")
        if not job.apply_link or not job.apply_link.startswith("http"):
            errors.append("Invalid or non-HTTP apply link")

        return len(errors) == 0, errors
