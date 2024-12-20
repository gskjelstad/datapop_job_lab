from nautobot.apps.jobs import Job, register_jobs

class HelloWorld(Job):
    def run(self):
        self.logger.debug("Hello, first job")

register_jobs(HelloWorld)