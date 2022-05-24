import pymysql

mydb = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", database="supero_datalake2", )
mycursor = mydb.cursor()
sql = "select link from items group by link having count(*) > 1 order by count(*) desc;"
mycursor.execute(sql, )
myresult = mycursor.fetchall()
l = []
for t in myresult:
    l.append(t[0])

for link in l:
    sql = f"select id from items where link = '{link}';"
    mycursor.execute(sql, )
    myresult = mycursor.fetchall()
    l2 = []
    for t in myresult:
        l2.append(t[0])
    print('=============================')
    for id in l2[1::]:
        print(id)
        sql = f"delete from items where id = {id}"
        mycursor.execute(sql, )
    print('=============================\n')
    mydb.commit()
