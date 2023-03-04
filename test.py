import pymysql

try :

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='test'
    )

    with connection.cursor() as cursor:
        sql = "SELECT * TABLES"
        print(cursor.execute(sql))
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

except Exception as e:
    print(f'Error\n{e}')