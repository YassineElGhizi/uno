import pymysql

def get_mapped_procuts():
    mydb = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", database="supero_datalake2", )
    mycursor = mydb.cursor()
    sql = "SELECT name FROM mapped_prod_names"
    mycursor.execute(sql,)
    return Sorting(
        simpleItems(mycursor.fetchall())
    )

def simpleItems(list_of_tuples):
    return [i[0] for i in list_of_tuples]

def Sorting(lst):
    lst.sort(key=len, reverse=True)
    return lst