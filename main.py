"""
created by Nagaj at 06/05/2021
"""
from jobs.company import CompanyProfile
from jobs.job import Job, JobDetails

vodafone = CompanyProfile("Vodafone", "SmartVillage", range(500, 2000))
huawei = CompanyProfile("Huawei", "SmartVillage", range(1000, 3000))

python = Job("Python Developer")
backend = Job("backend Developer")
java = Job("Java Developer")
php = Job("PHP Developer")
devops = Job("Devops Engineer")

jobs = Job.available_jobs[:2]  # limit for test

for job in jobs:
    job.show_job_details()
    print("#" * 100)

huawei.post_job(devops)
huawei.post_job(backend)
huawei.post_job(java)
print("*" * 100)

for job in huawei:
    print(job, job.company)

print(devops.jobdetails)
# todo : make category object
devops_details = JobDetails(experience=[3, 5], career_level="non-manager", education_level="Bachelor's",
                            job_category="IT",
                            )

java_details = JobDetails(experience=[3, 5], career_level="non-manager", education_level="Bachelor's",
                          job_category="IT",
                          salary=3000)
huawei.add_job_details(devops, devops_details)
huawei.add_job_details(java, java_details)
print(devops.jobdetails)
print(java.jobdetails)
