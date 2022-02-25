from fastapi import FastAPI, Body, HTTPException, Depends
import uvicorn
import logging
from typing import List

from fastapi_micro_service.controllers.optionController import optionGetAll
from fastapi_micro_service.controllers.productController import storeProduct
from fastapi_micro_service.controllers.brandController import brandGetAll
from fastapi_micro_service.models.mapper import Mapper
from fastapi_micro_service.middleware.authHandler import AuthHandler
auth_handler = AuthHandler()

logging.basicConfig(
    filename='fastapi.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s'
)
app = FastAPI()

authorizer_mappers = [
    {
        'username' : 'uno_mapper' ,
        'password' : '$2b$12$j1Xs6HvX7iZ9D70vulcrx.J99lQBPPujXPk5F8VZKgt2qSERr4axm' #unoMapperSupero2022
    },
    {
        'username' : 'yassine',
        'password' : '$2b$12$TNUBGgPruzd0yZ61VC8auOoxVN/uc0D65bGy5OQGHsUsQtikF2kWi' #dataengeneeradmin
    }
]

@app.get("/options")
# async def get_option(website : str):
async def get_option(website : str , user_name=Depends(auth_handler.auth_wrapper)):
    return await optionGetAll(website)

@app.post("/products")
# async def insert_product(website : str, importance : List = Body(...)):
async def insert_product(website : str, importance : List = Body(...) , user_name=Depends(auth_handler.auth_wrapper)):
    return await storeProduct(website , importance)

@app.get("/brands")
async def get_brands(website : str):
# async def get_brands(website : str , user_name=Depends(auth_handler.auth_wrapper)):
    return await brandGetAll(website)


@app.post('/login')
def login(reqBody : dict = Body(...)):
    m = Mapper(reqBody['username'] , reqBody['password'])
    pswd = None
    for u in authorizer_mappers:
        if m.username == u['username']:
            pswd = u['password']
    if (pswd is None) or (not auth_handler.verify_password(m.password, pswd)):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    return {'token': auth_handler.encode_token(m.username)}

@app.get('/protected')
def protected(user_name=Depends(auth_handler.auth_wrapper)):
    return { 'server_response': f'user : {user_name} is Authorised' }


if __name__ == "__main__":
    uvicorn.run("api:app", port=9999, reload=True, debug=True)
