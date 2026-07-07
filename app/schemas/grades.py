from pydantic import BaseModel


class GradesSchema(BaseModel):
    junior: bool = False
    mid: bool = False
    senior: bool = False
    lead: bool = False