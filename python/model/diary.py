from datetime import date

from pydantic import BaseModel


class Diary(BaseModel):
    date: date
    content: str
