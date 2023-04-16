# practice_FastAPI

## sample_code
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/alpha/{b}")
async def read_param(b):
    return "this is " + b
# 위와 같이 하면 전달인자 받을 수 있다.



