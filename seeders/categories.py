import pymysql

# Create a connection object
dbServerName = "127.0.0.1"
dbUser = "root"
dbPassword = ""
dbName = "supero_datalake2"

cusrorType = pymysql.cursors.DictCursor
connectionObject = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,db=dbName, cursorclass=cusrorType)

try:
    # Create a cursor object
    cursorObject = connectionObject.cursor()

    # SQL query string
    sqlQuery = "insert into Categories(name) values (\"smaprtphone & tablette\")"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)
    connectionObject.commit()
except Exception as e:
    print("Exeception occured:{}".format(e))

finally:
    connectionObject.close()