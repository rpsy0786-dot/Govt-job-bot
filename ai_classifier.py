"""
AI Relevancy Classifier
"""
from ..models.job import Job
from ..config import QUALIFICATIONS, PREFERRED_DEPARTMENTS


class AIClassifier:

    @staticmethod
    def classify(job: Job) -> Job:
        score = 50.0  # Base score
        text = f"{job.title} {job.qualification} {job.description} {job.department}".lower()

        for qual in QUALIFICATIONS:
            if qual.lower() in text:
                score += 25.0
                break

        for dept in PREFERRED_DEPARTMENTS:
            if dept.lower() in text:
                score += 15.0
                break

        if "gate" in text or "b.tech" in text or "b.e" in text:
            score += 10.0

        job.score = min(score, 100.0)
        return job
