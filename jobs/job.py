"""
created by Nagaj at 06/05/2021
"""
from typing import Union


class JobDetails:
    def __init__(
            self, experience: Union[list, str, int], career_level, education_level, job_category, salary=None
    ):
        self.experience = experience
        self.career_level = career_level
        self.job_category = job_category
        self.education_level = education_level
        self.salary = "Confidential" if salary is None else salary
        self.description = []
        self.requirements = []

    def __repr__(self):
        info = f"{self.experience}-{self.career_level}-{self.job_category}-{self.education_level}"
        if self.salary:
            return f"{info}-{self.salary}"
        return info


class Job:
    available_jobs = []

    def __init__(self, title, company=None, jobdetails=None):
        self.title = title
        self.company = company
        self.jobdetails = jobdetails
        self.applies = 0
        Job.available_jobs.append(self)

    def __repr__(self):
        return self.title

    def __getitem__(self, item):
        return Job.available_jobs[item]

    def show_job_details(self):
        print(f"Title: {self.title}")
        print(f"Company: {self.company}")
        self.show_optional_details()

    def show_optional_details(self):
        if self.jobdetails:
            print(f"Experience: {self.jobdetails.experience}")
            if self.jobdetails.salary:
                print(f"Salary: {self.jobdetails.salary}")
            else:
                print("Salary: Confidential")
