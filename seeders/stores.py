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
    sqlQuery = "insert into stores(name, link) values (%s , %s)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery , ("uno","https://uno.ma"))


    # SQL query string
    sqlQuery = "insert into stores(name, link) values (%s ,%s)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery , ("jumia","https://www.jumia.ma"))

    # SQL query string
    sqlQuery = "insert into stores(name, link) values (%s ,%s)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery , ("electroplanet","https://www.electroplanet.ma/"))

    # SQL query string
    sqlQuery = "insert into stores(name, link) values (%s ,%s)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery , ("kitea","https://www.electroplanet.ma/"))

    # SQL query string
    sqlQuery = "insert into stores(name, link) values (%s ,%s)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery , ("bricoma","https://www.electroplanet.ma/"))

    # SQL query string
    sqlQuery = "insert into stores(name, link) values (%s ,%s)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery , ("decathlon","https://www.electroplanet.ma/"))

    # SQL query string
    sqlQuery = "insert into stores(name, link) values (%s ,%s)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery , ("ikea","https://www.electroplanet.ma/"))

    # SQL query string
    sqlQuery = "insert into stores(name, link) values (%s ,%s)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery , ("consomeelectro","https://www.electroplanet.ma/"))

    # SQL query string
    sqlQuery = "insert into stores(name, link) values (%s ,%s)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery , ("megalife","https://www.electroplanet.ma/"))

    # SQL query string
    sqlQuery = "insert into stores(name, link) values (%s ,%s)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery , ("beautysuccess","https://www.electroplanet.ma/"))

    # SQL query string
    sqlQuery = "insert into stores(name, link) values (%s ,%s)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery , ("prixmaroc","https://www.electroplanet.ma/"))

    # SQL query string
    sqlQuery = "insert into stores(name, link) values (%s ,%s)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery , ("iris","https://www.electroplanet.ma/"))


    connectionObject.commit()
except Exception as e:
    print("Exeception occured:{}".format(e))

finally:
    connectionObject.close()