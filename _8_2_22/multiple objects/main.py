# put method in fastapi

#library  imports
from typing import Optional
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


#create the app object
app = FastAPI()



class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None



#opens automatically on http://127.0.0.1:8004/
@app.get("/")
def read_root():
    return {"Hello": "India"}

#route with the single parameter route with http://127.0.0.1:8004/items/give item id here
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

#
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

#run api with uvicorn
if _name_ == '_main_':
    uvicorn.run(app,debug=True,port=8004)