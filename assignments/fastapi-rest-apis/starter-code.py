from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="My API", description="A simple REST API built with FastAPI")

# Define a data model for items
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# In-memory storage (in a real app, you'd use a database)
items = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}

# TODO: Add your endpoints here

# Example GET endpoint to get all items
@app.get("/items/", response_model=List[Item])
def read_items():
    return items

# Example POST endpoint to create an item
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

# TODO: Add more endpoints as per the assignment requirements