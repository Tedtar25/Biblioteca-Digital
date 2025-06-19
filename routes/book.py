from fastapi import APIRouter, Path, Body, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from config.database import Session
from models.book import Book as BookModel
from middlewares.jwt_bearer import JWTBearer
from services.book import BookService
from schemas.book import BookCreate, Book

book_router = APIRouter()

@book_router.get('/books', tags=['Books'], response_model=List[Book], dependencies=[Depends(JWTBearer())])
def get_books():
    db = Session()
    result = BookService(db).get_books()
    return jsonable_encoder(result)

@book_router.get('/books/{id}', tags=['Books'], response_model=Book, dependencies=[Depends(JWTBearer())])
def get_book(id: int = Path(ge=1)):
    db = Session()
    result = BookService(db).get_book(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Libro no encontrado"})
    return jsonable_encoder(result)

@book_router.get('/books/search/', tags=['Books'], response_model=List[Book], dependencies=[Depends(JWTBearer())])
def get_books_by_category(category: str = Query(min_length=1, max_length=50)):
    db = Session()
    result = BookService(db).get_books_by_category(category)
    return jsonable_encoder(result)

@book_router.post('/books', tags=['Books'], response_model=dict, dependencies=[Depends(JWTBearer())])
def create_book(book: BookCreate = Body(...)):
    db = Session()
    BookService(db).create_book(book)
    return JSONResponse(content={"message": "Aleluya hermano, ¡has cargado un nuevo libro!"}, status_code=201)

@book_router.put('/books/{id}', tags=['Books'], response_model=dict, dependencies=[Depends(JWTBearer())])
def update_book(id: int, book: BookCreate = Body(...)):
    db = Session()
    result = BookService(db).get_book(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Libro no encontrado"})
    BookService(db).update_book(id, book)
    return JSONResponse(content={"message": "Ding Ding! Libro actualizado correctamente"})

@book_router.delete('/books/{id}', tags=['Books'], response_model=dict, dependencies=[Depends(JWTBearer())])
def delete_book(id: int):
    db = Session()
    result = BookService(db).get_book(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Libro no encontrado"})
    BookService(db).delete_book(id)
    return JSONResponse(content={"message": "Hasta la vista, Baby!"})
