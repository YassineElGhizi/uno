import sqlalchemy as db

engine = db.create_engine('mysql://root@localhost/exemple_supero2')


async def brandGetAll(website : str):
    if website == 'uno':
        connection = engine.connect()
        metadata = db.MetaData()
        options = db.Table('brands', metadata, autoload=True, autoload_with=engine)
        query = db.select([
             options.columns.id,
             options.columns.name,
             ]).where(
                options.columns.Specialite.like("[\"5\"]")
            )

        ResultProxy = connection.execute(query)
        return ResultProxy.fetchall()
    return None