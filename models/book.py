from sqlalchemy import Column, Integer, String
from config.database import Base

class Book(Base):
    __tablename__ = "The Bababook"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)
    category = Column(String)
    pages = Column(Integer)
