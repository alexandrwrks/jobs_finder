import asyncio
import json

from bs4 import BeautifulSoup
from httpx import AsyncClient, ConnectError, HTTPError, ReadError

from schemas import CompanySchema, FullJobSchema, JobSchema, SalarySchema


class Base(Exception):
    pass

class NotEnough(Base):
    pass

async def job_info(link: str, client: AsyncClient) -> FullJobSchema:

        response = await client.get(url=link)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        scripts = soup.find_all(
            "script",
            attrs={"type":"application/ld+json"}
        )

        job_script = None
        for script in scripts:
            vacancy_script = json.loads(script.string)
            if vacancy_script.get("@type") == "JobPosting":
                job_script = vacancy_script
                break

        if job_script is None:
            raise

        skills = [
            tag.get_text(strip=True)
            for tag in soup.select("span[title]")
        ]

        company = soup.find("div", class_="mb-1")
        company_name = None
        if company is not None:
            company_name = company.find("a").get_text()


        job_conditions = await full_job_conditions(job_script, company_name)
        job_conditions.skills = skills

        return job_conditions


async def full_job_conditions(job_data: dict | None, company_name: str | None) -> FullJobSchema:
    if job_data is not None:
        full_job_information = FullJobSchema(
            job=get_job_information(job_data),
            company=CompanySchema(name=company_name),
            salary=get_job_salary(job_data)
        )

        return full_job_information

    raise

def get_job_information(data: dict) -> JobSchema:
    if type(data.get("applicantLocationRequirements")) == dict:
        busyness = data["applicantLocationRequirements"]["name"]
    elif type(data.get("applicantLocationRequirements")) == list:
        busyness = []
        for d in data["applicantLocationRequirements"]:
            busyness.append(d.get("name"))
    else:
        busyness = None

    return JobSchema(
        title=data["title"],
        description=data["description"],
        url=data["url"],
        type_of_work=data.get("employmentType"),
        location_work=data["jobLocationType"] if "jobLocationType" in data else None,
        busyness=busyness
    )

def get_job_salary(data: dict) -> SalarySchema | None:
    salary = data.get("baseSalary")
    if salary:
        value = salary.get("value")

        return SalarySchema(
            currency=salary["currency"],
            min_value=value["minValue"],
            max_value=value["maxValue"],
            unit=value["unitText"],
        )

    return None

if __name__ == "__main__":
    asyncio.run(job_info("https://talanto.work/jobs/588e2fa1-16a7-473c-a234-15b2c90861f3"))