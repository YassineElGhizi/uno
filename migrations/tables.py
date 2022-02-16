import pymysql

# Create a connection object
dbServerName = "127.0.0.1"
dbUser = "root"
dbPassword = ""
dbName = "supero_datalake"

cusrorType = pymysql.cursors.DictCursor
connectionObject = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,db=dbName, cursorclass=cusrorType)

try:
    # Create a cursor object
    cursorObject = connectionObject.cursor()

    # # SQL query string
    # sqlQuery = "CREATE TABLE Categories(id int primary key not null AUTO_INCREMENT, name varchar(255))"
    # # Execute the sqlQuery
    # cursorObject.execute(sqlQuery)

    # # SQL query string
    # sqlQuery = "CREATE TABLE Subcategories(id int primary key not null AUTO_INCREMENT, name varchar(255), id_cat int, foreign key (id_cat) references categories(id))"
    # # Execute the sqlQuery
    # cursorObject.execute(sqlQuery)

    # SQL query string
    sqlQuery = "CREATE TABLE Stores(id int primary key not null AUTO_INCREMENT, name varchar(255), link text ,updated_at timestamp )"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)

    # SQL query string
    # sqlQuery = "CREATE TABLE Items(last_updated_at timestamp, id int primary key not null AUTO_INCREMENT, name varchar(255), slug varchar(255), link varchar(255), id_store int, id_category int, color varchar(255),stockage varchar(255) , details text ,image_url text,current_price double, foreign key (id_store) references stores(id),foreign key (id_category) references categories(id))"
    # sqlQuery = "CREATE TABLE Items(last_updated_at timestamp, id int primary key not null AUTO_INCREMENT, name varchar(255), slug varchar(255), link varchar(255), id_store int, id_subcategory int, specification text , details text ,image_url text,current_price double, foreign key (id_store) references stores(id),foreign key (id_subcategory) references subcategories(id))"
    sqlQuery = "CREATE TABLE Items(last_updated_at timestamp, id int primary key not null AUTO_INCREMENT, name_in_store varchar(255), prod_name varchar(255), link varchar(255), id_store int, category_in_store varchar(255), specification text , details text ,image_url text,current_price double, foreign key (id_store) references stores(id))"
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)


    # SQL query string
    sqlQuery = "CREATE TABLE Prices(id_item int , price double, created_at timestamp, foreign key (id_item) references items(id))"
    # Execute the sqlQuery
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