
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Union[str, None] = None # 이 부분은 3.10부터 표현하는 방법이 좀 바뀜
    price: float
    tax: Union[float, None] = None
    sample: str


app = FastAPI()




@app.post("/items/")
async def create_item(item: Item):
    return item

'''
{
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5,
	  "sample":"Yes BABA"
}

위와 같이 보내면 똑같이 응답 옴 (당연한게 return item이므로)
'''


