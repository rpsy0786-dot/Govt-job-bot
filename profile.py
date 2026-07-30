"""
User Preference Profile Model
AI Powered Government Jobs Telegram Bot
"""

from dataclasses import dataclass, field
from typing import List

from ..config import (
    QUALIFICATIONS,
    MAX_EXPERIENCE,
    PREFERRED_LOCATIONS,
    PREFERRED_DEPARTMENTS,
)


@dataclass
class Profile:
    """
    Represents the user's job-matching preferences, seeded from config.py.
    Kept as a separate object (rather than hardcoding config everywhere)
    so future features (e.g. per-user profiles via /setprefs) can build
    on top of it without touching the ranking/classification logic.
    """
    qualifications: List[str] = field(default_factory=lambda: list(QUALIFICATIONS))
    max_experience: int = MAX_EXPERIENCE
    preferred_locations: List[str] = field(default_factory=lambda: list(PREFERRED_LOCATIONS))
    preferred_departments: List[str] = field(default_factory=lambda: list(PREFERRED_DEPARTMENTS))
