"""Import Jobs."""

from .jobs.location_data import HelloWorld
from nautobot.core.celery import register_jobs

register_jobs(HelloWorld)