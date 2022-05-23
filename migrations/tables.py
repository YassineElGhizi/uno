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


    sqlQuery = "CREATE TABLE stores(id int primary key not null AUTO_INCREMENT, name varchar(255), link text ,updated_at timestamp )"
    cursorObject.execute(sqlQuery)


    # sqlQuery = "CREATE TABLE items(last_updated_at timestamp, id int primary key not null AUTO_INCREMENT, name_in_store varchar(255), prod_name varchar(255), link varchar(255), id_store int, category_in_store varchar(255), specification text , details text ,image_url text,current_price double, foreign key (id_store) references stores(id))"
    sqlQuery = "CREATE TABLE items(unique_id varchar(255), id int primary key not null AUTO_INCREMENT, name_in_store varchar(255), prod_name varchar(255), link varchar(255), id_store int, category_in_store varchar(255), specification text , details text ,image_url text,current_price double)"
    cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "show tables"

    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # Fetch all the rows
    rows = cursorObject.fetchall()

    for row in rows:
        print(row)

except Exception as e:
    print("Exeception occured:{}".format(e))

finally:
    connectionObject.close()