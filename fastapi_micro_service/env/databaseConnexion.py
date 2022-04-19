import sqlalchemy as db
import datetime


engine = db.create_engine('mysql://root@localhost/supero_api')
connection = engine.connect()
metadata = db.MetaData()


def myTempStamp():
    now = datetime.datetime.now()
    return "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)


def get(query):
    #Connection Needes to refreshed Because FASTAPI is async
    connection = engine.connect()
    return connection.execute(query).fetchall()
