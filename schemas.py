from typing import List

from pydantic import BaseModel


class SalarySchema(BaseModel):
    currency: str | None
    min_value: int | None
    max_value: int | None
    unit: str | None


class CompanySchema(BaseModel):
    name: str | None


class JobSchema(BaseModel):
    title: str
    description: str
    url: str
    type_of_work: str
    location_work: str | None
    busyness: List[str] | str | None


class FullJobSchema(BaseModel):
    job: JobSchema
    company: CompanySchema
    salary: SalarySchema | None = None
    skills: List[str] | None = None
