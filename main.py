from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware  # 👈 Agregado

from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routes.book import book_router
from routes.user import user_router

app = FastAPI()
app.title = "cesar livery "
app.version = "6.6.6"

# 👇 Configuración CORS
origins = [
    "http://localhost:3000",
    "http://143.198.144.8", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(ErrorHandler)
app.include_router(book_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)

@app.get("/", tags=["Home"])
def message():
    return HTMLResponse(
        content="Bienvenido a la Biblioteca Digital. Libros de Voodoo a tan solo $10 pesos.",
        status_code=200
    )
