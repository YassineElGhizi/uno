import sqlalchemy as db
import datetime


engine = db.create_engine('mysql://root@localhost/supero_api')
connection = engine.connect()
metadata = db.MetaData()


def myTempStamp():
    now = datetime.datetime.now()
    return "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)


def get(query):
    connection = engine.connect()
    return connection.execute(query).fetchall()
