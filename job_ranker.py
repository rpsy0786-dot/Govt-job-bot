"""
Job Ranker Utility
"""
from typing import List
from ..models.job import Job


class JobRanker:

    @staticmethod
    def rank(jobs: List[Job], profile=None) -> List[Job]:
        return sorted(jobs, key=lambda j: j.score, reverse=True)
