from fastapi import FastAPI, Body
import uvicorn
import logging
from typing import List, Optional

from controllers.optionController import optionGetAll
logging.basicConfig(
    filename='fastapi.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s'
)
app = FastAPI()

@app.get("/options")
async def get_option(website : str):
    return await optionGetAll(website)

@app.post("/products")
async def insert_product(website : str , importance : List = Body(...)):
    return importance


if __name__ == "__main__":
    uvicorn.run("api:app", port=9999, reload=True)
