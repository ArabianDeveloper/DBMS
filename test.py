import pymysql
# conn = pymysql.connect (user='root', password='', host='localhost')
# cursor = conn.cursor()
# databases = ("show databases")
# cursor.execute(databases)
# print(cursor.fetchall()[0][0])

def tables():
    try :
        conn = pymysql.connect(user='root', password='', host='localhost', database='test')
        with conn.cursor() as cursor:
            tables = cursor.execute("show tables")
            return cursor.fetchall()
    except pymysql.Error as r:
        print(r)

print(tables())