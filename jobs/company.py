"""
created by Nagaj at 06/05/2021
"""
from jobs.job import Job, JobDetails


class CompanyProfile:
    def __init__(self, name, location, employees: range, vision=None, mission=None):
        self.name = name
        self.location = location
        self.employees = employees
        self.vision = vision
        self.mission = mission
        self.jobs_posts = []

    def __repr__(self):
        return self.name

    def post_job(self, job: Job):
        self.jobs_posts.append(job)
        job.company = self

    @staticmethod
    def add_job_details(job: Job, joddetails: JobDetails):
        job.jobdetails = joddetails

    def __getitem__(self, item):
        return self.jobs_posts[item]

    def delete_post(self, job):
        jobs = self.jobs_posts
        if job in jobs:
            self.jobs_posts.remove(job)
            print(f"Job <{job}> Was deleted!")
            Job.available_jobs.remove(job)
