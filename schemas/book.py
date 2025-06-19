from pydantic import BaseModel, Field
from typing import Optional

class BookCreate(BaseModel):  # solo para entrada
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    year: int = Field(ge=1000, le=2100)
    category: str = Field(min_length=1, max_length=50)
    pages: int = Field(gt=0)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Coloca el nombre de tu libro",
                "author": "Coloca el nombre del autor",
                "year": 2000,
                "category": "Coloca la categoría del libro",
                "pages": 100
            }
        }

class Book(BookCreate):  # para salida
    id: int

    class Config:
        orm_mode = True
