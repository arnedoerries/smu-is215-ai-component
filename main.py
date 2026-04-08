import datetime
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal

from archetype_prediction import predict_character_archetype
from user_db_manager import retrieve_user_data_product, retrieve_entire_user_database


app = FastAPI()

class UserCharacterDescription(BaseModel):
    user_id: str = Field(..., min_length=10, max_length=10, pattern="^[0-9]{10}$")
    user_first_name: str
    user_last_name: str
    character_description: str

class NewBookCharacter(BaseModel):
    book_id: str = Field(..., min_length=10, max_length=10, pattern="^[0-9]{10}$")
    book_title: str
    book_published_date: datetime.date
    book_short_summary: str
    character_name: str
    gender: Literal["male", "female", "other"]
    character_description: str

class UserDataProduct(BaseModel):
    user_id: str = Field(..., min_length=10, max_length=10, pattern="^[0-9]{10}$")

@app.post("/getArchetypePrediction/")
async def create_item(item: UserCharacterDescription):
    return predict_character_archetype(item.user_id, item.user_first_name, item.user_last_name, item.character_description)

@app.post("/addNewBookCharacter/")
async def create_item(item: NewBookCharacter):
    return {"Success"}

@app.get("/retrieveSingleUserDataProduct/")
async def read_item(item: UserDataProduct):
    return retrieve_user_data_product(item.user_id)

@app.get("/retrieveAllUserDataProducts/")
async def read_item():
    return retrieve_entire_user_database()

