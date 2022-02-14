import pymysql

# Create a connection object
dbServerName = "127.0.0.1"
dbUser = "root"
dbPassword = ""
dbName = "datalake"

cusrorType = pymysql.cursors.DictCursor
connectionObject = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,db=dbName, cursorclass=cusrorType)

try:
    # Create a cursor object
    cursorObject = connectionObject.cursor()

    # SQL query string
    sqlQuery = "insert into SubCategories(name , id_cat) values (\"iphone\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"ipad\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"mac\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"watch\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"ecouteurs\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"tv\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"accessoires\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"electromenager\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"coiffure\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"chauffage\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"climatiseur\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"appareil photo\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"laptop\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"android_phones\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"tablette android\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"tablette android\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"telephone domistique\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"accessoires telephone\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"equipement informatique\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "insert into Subcategories(name , id_cat) values (\"console\" , 1)"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    connectionObject.commit()
except Exception as e:
    print("Exeception occured:{}".format(e))

finally:
    connectionObject.close()