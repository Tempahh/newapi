
from fastapi import FastAPI, Query, HTTPException, status
from pathlib import Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    brand: Optional[str] = None
    price: float
    

class updateitem(BaseModel):
    name: Optional[str] = None
    brand: Optional[str] = None
    price: Optional[float] = None
    

inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description= "id  you want to see.", gt=0)):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str= None, title='name', desc='item name'):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
        
    raise HTTPException(status_code=404, detail='item id not found')

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return{"Item id already exists"}
    inventory[item_id]= item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id:int, item: updateitem):
    if item_id not in inventory:
        return{"Error": "Item ID already exists."}
    
    if item.name != None:
        inventory[item_id].name = item.name

    if item.price != None:    
        inventory[item_id].price = item.price

    if item.brand != None:    
        inventory[item_id].brand = item.brand

    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = ...,desc="id you want to delete", gt=0):
    if item_id not in inventory:
        return{"error": "id does not exist"}
    del inventory[item_id]
    return{'Sucess': 'item deleted'}