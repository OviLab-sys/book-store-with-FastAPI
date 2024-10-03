from fastapi import FastAPI
from model.models import Book, BookResponse

app = FastAPI()

@app.post("/book")
async def creat_book(book: Book) -> Book:
    return book 

@app.get("/allbooks")
async def all_books() ->list[BookResponse]:
    return [
            {
                "id": 1,
                "title": "1984",
                "author": "George Orwell"},
            {
                "id": 1,
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",}
    ]