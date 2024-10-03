from pydantic import BaseModel,Field

class Book(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    auther: str = Field(..., min_length=1,max_length=100)
    year: int =Field(...,gt=1900, lt=2100)


class BookResponse(BaseModel):
    title: str
    author: str