import sqlalchemy as db
from fastapi_micro_service.env.databaseConnexion import engine, metadata, connection

async def optionGetAll(website : str):
    options = db.Table('options', metadata, autoload=True, autoload_with=engine)
    query = db.select([
        options.columns.id,
        options.columns.name,
        options.columns.value,
        options.columns.unit,
        options.columns.id_parent
    ])

    ResultProxy = connection.execute(query)
    return ResultProxy.fetchall()