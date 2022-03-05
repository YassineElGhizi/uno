import sqlalchemy as db

engine = db.create_engine('mysql://root@localhost/exemple_supero2')
async def brandGetAll():
    connection = engine.connect()
    metadata = db.MetaData()
    options = db.Table('brands', metadata, autoload=True, autoload_with=engine)
    query = db.select([
        options.columns.id,
        options.columns.name,
    ])
    ResultProxy = connection.execute(query)
    return ResultProxy.fetchall()