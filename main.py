import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Literal

from orchestrator import predict_for_user_and_add_to_user_db, predict_for_new_character_and_add_to_book_db
from user_db_manager import retrieve_user_data_product, retrieve_entire_user_database
from book_db_manager import retrieve_book_data_product, retrieve_entire_book_database, recommend_books_based_on_archetype


app = FastAPI()

origins = [
    "https://bookrec.aotd.cloud"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserCharacterDescriptionInput(BaseModel):
    user_id: str = Field(..., min_length=10, max_length=10, pattern="^[0-9]{10}$")
    user_first_name: str
    user_last_name: str
    character_description: str

class NewBookCharacterInput(BaseModel):
    book_id: str = Field(..., min_length=10, max_length=10, pattern="^[0-9]{10}$")
    book_title: str
    book_published_date: datetime.date
    book_genre: Literal["Fantasy", "Science Fiction", "Romance", "Historical Fiction", "Coming of Age", "Adventure"]
    book_short_summary: str
    character_name: str
    character_gender: Literal["male", "female", "either"]
    character_description: str

class BookRecommendationInput(BaseModel):
    book_genre: Literal["Fantasy", "Science Fiction", "Romance", "Historical Fiction", "Coming of Age", "Adventure"]
    character_gender_preference: Literal["either", "female", "male"]
    archetype_index: int = Field(..., ge=0, le=3)

class UserDataProductInput(BaseModel):
    user_id: str = Field(..., min_length=10, max_length=10, pattern="^[0-9]{10}$")

class BookDataProductInput(BaseModel):
    book_id: str = Field(..., min_length=10, max_length=10, pattern="^[0-9]{10}$")

# This first endpoint allows us to identify the character archetype for the user
@app.post("/predictCharacterArchetypeForUser/")
async def create_item(item: UserCharacterDescriptionInput):
    return predict_for_user_and_add_to_user_db(item.user_id, item.user_first_name, item.user_last_name, item.character_description)

# Once the character archetype is given, this second endpoint allows us to recommend books and characters that match the preference
@app.post("/getBookRecommendationsForArchetype/")
async def read_item(item: BookRecommendationInput):
    return recommend_books_based_on_archetype(item.book_genre, item.character_gender_preference, item.archetype_index)

# This second endpoint is for adding new characters for newly released books so that users can get it recommended
@app.post("/addNewBookCharacter/")
async def create_item(item: NewBookCharacterInput):
    return predict_for_new_character_and_add_to_book_db(item.book_id, item.book_title, item.book_published_date, item.book_genre, item.book_short_summary, item.character_name, item.character_gender, item.character_description)

# The following four endpoints are for easily retrieving all data stored in this microservice for analytics and other purposes.
@app.get("/retrieveSingleUserDataProduct/")
async def read_item(item: UserDataProductInput):
    return retrieve_user_data_product(item.user_id)

@app.get("/retrieveAllUserDataProducts/")
async def read_item():
    return retrieve_entire_user_database()

@app.get("/retrieveSingleBookDataProduct/")
async def read_item(item: BookDataProductInput):
    return retrieve_book_data_product(item.book_id)

@app.get("/retrieveAllBookDataProducts/")
async def read_item():
    return retrieve_entire_book_database()
