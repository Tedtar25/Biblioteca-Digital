from models.book import Book as BookModel
from schemas.book import BookCreate

class BookService:

    def __init__(self, db) -> None:
        self.db = db

    def get_books(self):
        return self.db.query(BookModel).all()
    
    def get_book(self, id: int):
        return self.db.query(BookModel).filter(BookModel.id == id).first()
    
    def get_books_by_category(self, category: str):
        return self.db.query(BookModel).filter(BookModel.category == category).all()
    
    def create_book(self, book: BookCreate):
        new_book = BookModel(**book.dict())
        self.db.add(new_book)
        self.db.commit()
        return

    def update_book(self, id: int, data: BookCreate):
        book = self.db.query(BookModel).filter(BookModel.id == id).first()
        book.title = data.title
        book.author = data.author
        book.year = data.year
        book.category = data.category
        book.pages = data.pages
        self.db.commit()
        return book

    def delete_book(self, id: int):
        self.db.query(BookModel).filter(BookModel.id == id).delete()
        self.db.commit()
        return
