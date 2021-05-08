"""
created by Nagaj at 06/05/2021
"""
from jobs.job import Job


class UserProfile:
    def __init__(self, username, email, mobile, excepted_salary=None):
        self.username = username
        self.email = email
        self.mobile = mobile
        self.excepted_salary = excepted_salary
        self.applies = []

    def __repr__(self):
        return self.username.title()

    def show_user_info(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Mobile: {self.mobile}")
        if self.excepted_salary:
            print(f"Excepted Salary: {self.excepted_salary}")

    def list_jobs(self):
        for job in Job.available_jobs:
            print(job)

    def find_job(self, keyword: str):
        """
        Simple search for job using keywords
        :param keyword:
        :return:
        """
        for job in Job.available_jobs:
            if keyword.lower() in job.title.lower():
                print(job)

    def apply_job(self, job: Job):
        if job not in self.applies:
            self.applies.append(job)
            job.applies += 1
            print(f"Successfully Applied for Job <{job}>, {self.username}")
        else:
            print(f"You Have Already Applied For This <{job}> Before!")
