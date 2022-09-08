import json
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
import requests

app = FastAPI()

#url = "/mock-data/persons1.json"

@app.get("/")
def read_root():
    return getjson_person()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def getjson_person():
    with open('/mock-data/pers1.json') as f:
        data = json.load(f)
        return(data)
    