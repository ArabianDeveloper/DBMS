import pymysql
conn = pymysql.connect (user='root', password='', host='localhost')
cursor = conn.cursor()
databases = ("show databases")
cursor.execute(databases)
print(cursor.fetchall()[0][0])