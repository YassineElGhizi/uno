from fastapi import FastAPI, Body, HTTPException, Depends
import uvicorn
from typing import List

from fastapi_micro_service.controllers.optionController import optionGetAll
from fastapi_micro_service.controllers.productController import storeProduct, productNames
from fastapi_micro_service.controllers.brandController import brandGetAll
from fastapi_micro_service.models.mapper import Mapper
from fastapi_micro_service.middleware.authHandler import AuthHandler
from fastapi_micro_service.services.bestPriceByIdParentGroup import performeUpdateBestPrice,bestPirceByIdParent
from fastapi_micro_service.controllers.product_historyController import price_history


auth_handler = AuthHandler()
app = FastAPI()

authorized_mappers = [
    {
        'username' : 'uno_mapper' ,
        'password' : '$2b$12$j1Xs6HvX7iZ9D70vulcrx.J99lQBPPujXPk5F8VZKgt2qSERr4axm' #unoMapperSupero2022
    },
    {
        'username' : 'yassine',
        'password' : '$2b$12$TNUBGgPruzd0yZ61VC8auOoxVN/uc0D65bGy5OQGHsUsQtikF2kWi' #dataengeneeradmin
    },
    {
        'username': 'electroplanet_mapper',
        'password': '$2b$12$geHVMsN5dpbKAjJsGw90EeDVJJK.6ywQ7SvZq85lWJsSPwRgNHZ66'  # electroplanetMapperSupero2022
    }
]

@app.get("/options")
async def get_option(website : str ,user_name=Depends(auth_handler.auth_wrapper) ):
    return await optionGetAll(website)

@app.post("/products")
async def insert_product(website : str, list_of_products : List = Body(...) , user_name=Depends(auth_handler.auth_wrapper)):
    await storeProduct(website , list_of_products)
    performeUpdateBestPrice(bestPirceByIdParent())
    price_history()
    return {'status' : '200 ok'}

@app.get("/brands")
async def get_brands(user_name=Depends(auth_handler.auth_wrapper)):
    return await brandGetAll()


@app.post('/login')
def login(reqBody : dict = Body(...)):
    m = Mapper(reqBody['username'] , reqBody['password'])
    pswd = None
    for u in authorized_mappers:
        if m.username == u['username']:
            pswd = u['password']
    if (pswd is None) or (not auth_handler.verify_password(m.password, pswd)):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    return {'token': auth_handler.encode_token(m.username)}

@app.get('/test')
def test():
    return 'App is Working'

@app.get('/protected')
def protected(user_name=Depends(auth_handler.auth_wrapper)):
    return { 'server_response': f'user : {user_name} is Authorised' }


if __name__ == "__main__":
    uvicorn.run("api:app", port=9999, reload=True, debug=True)
