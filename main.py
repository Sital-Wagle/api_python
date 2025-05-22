from typing import Union

from fastapi import FastAPI

from uvicorn import run

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

def main ():
    run(app,host="localhost",port=8000,log_level="info")

if __name__ == "__main__":
    main()