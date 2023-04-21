# practice_FastAPI

## sample_code
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/alpha/{b}")
async def read_param(b):
    return "this is " + b
# 위와 같이 하면 전달인자 받을 수 있다.


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/") # items/?skip=1&limit=2 이런 식으로 전달 가능
async def read_item(skip: int = 0, limit: int = 10): # 전하는 값이 없으면 default값 사용.
    return fake_items_db[skip : skip + limit] # 여기서 limit은 list slicing 갯수로 작용한다.

temp = {}

@app.get("/items/{item_id}")
async def add_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    if item_id in temp:
        return "{item_id} is in values"
    else:
        temp[item_id] = "item_id"+str(item_id) # 이렇게 받는 값들을 걸러내며 저장할 수 있다.
        return temp







