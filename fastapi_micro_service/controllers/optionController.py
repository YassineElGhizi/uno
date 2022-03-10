import sqlalchemy as db

async def optionGetAll(website : str):
    engine = db.create_engine('mysql://root@localhost/exemple_supero2')
    connection = engine.connect()
    metadata = db.MetaData()
    if website == 'uno':
        options = db.Table('options', metadata, autoload=True, autoload_with=engine)
        query = db.select([
             options.columns.id,
             options.columns.name,
             options.columns.value,
             options.columns.unit,
             options.columns.id_parent
             ]).where(
            db.and_(
                options.columns.id_parent != None,
                options.columns.id_parent.in_([1, 152, 143, 156, 3, 4, 2, 5, 6, 187]))
            )

        ResultProxy = connection.execute(query)
        return ResultProxy.fetchall()

    if website == 'electroplanet-iphone':
        options = db.Table('options', metadata, autoload=True, autoload_with=engine)
        query = db.select([
             options.columns.id,
             options.columns.name,
             options.columns.value,
             options.columns.unit,
             options.columns.id_parent
             ]).where(
            db.and_(
                options.columns.id_parent != None,
                options.columns.id_parent.in_([1, 152, 143, 156, 3, 4, 2, 5, 6, 187]))
            )

        ResultProxy = connection.execute(query)
        return ResultProxy.fetchall()
    return None