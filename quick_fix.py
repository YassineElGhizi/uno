import pymysql

#Getting All Product that have a parent
mydb = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", database="supero_api", )
mycursor = mydb.cursor()
sql = "select unique_id from products group by unique_id having count(*) > 1;"
mycursor.execute(sql, )
myresult = mycursor.fetchall()
l = []
for t in myresult:
    l.append(t[0])

for refrerance in l:
    sql = f"select id ,images from products where unique_id = '{refrerance}';"
    mycursor.execute(sql, )
    myresult = mycursor.fetchall()
    n_404 = 0
    list_ids_to_update = []
    product_with_image: str
    for images in myresult:
        if images[1] == '["https://supero.s3.eu-west-3.amazonaws.com/images/404.png"]':
            n_404 += 1
            list_ids_to_update.append(images[0])
        else:
            product_with_image = images[1]
    if n_404 != len(myresult):
        if n_404 != 0:
            print('UPDATES NEEDED', list_ids_to_update, ' len => ', len(list_ids_to_update), ' new image', product_with_image)
            for id_prod in list_ids_to_update:
                sql = 'update products set images = %s where id = %s'
                val = (product_with_image, int(id_prod))
                mycursor.execute(sql, val)
                mydb.commit()



