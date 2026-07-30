"""
Job Data Model
AI Powered Government Jobs Telegram Bot
"""

from dataclasses import dataclass


@dataclass
class Job:
    """
    Plain data holder representing a single government job notification.
    Every field defaults to an empty/neutral value so scrapers can build
    an instance with `Job()` and set only the fields they have data for.
    """
    title: str = ""
    organisation: str = ""
    department: str = ""
    qualification: str = ""
    experience: str = ""
    age_limit: str = ""
    vacancies: str = ""
    salary: str = ""
    location: str = ""
    job_type: str = ""
    advertisement_no: str = ""
    notification_date: str = ""
    last_date: str = ""
    application_mode: str = ""
    apply_link: str = ""
    notification_pdf: str = ""
    description: str = ""
    source: str = ""
    score: float = 0.0
    notified: bool = False

    def __repr__(self) -> str:
        return f"<Job title={self.title!r} organisation={self.organisation!r} score={self.score}>"
