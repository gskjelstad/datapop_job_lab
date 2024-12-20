import os

from nautobot.extras.datasources.git import ensure_git_repository
from nautobot.apps.jobs import Job, register_jobs, ObjectVar, BooleanVar
from nautobot.ipam.models import Namespace
from nautobot.dcim.models import (
    Location,
)
from nautobot.extras.models import (
    DynamicGroup,
    JobResult,
    Job as extras_job,
)
class HelloWorld(Job):

    def run(self):
        self.logger.debug("Hello, first job")

register_jobs(HelloWorld)