import sqlalchemy as db
from fastapi_micro_service.env.databaseConnexion import engine, metadata, connection

async def brandGetAll():
    brands = db.Table('brands', metadata, autoload=True, autoload_with=engine)
    query = db.select([
        brands.columns.id,
        brands.columns.name,
    ])
    ResultProxy = connection.execute(query)
    return ResultProxy.fetchall()