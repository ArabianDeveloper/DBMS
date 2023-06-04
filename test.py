# import pymysql
# # conn = pymysql.connect (user='root', password='', host='localhost')
# # cursor = conn.cursor()
# # databases = ("show databases")
# # cursor.execute(databases)
# # print(cursor.fetchall()[0][0])

# def tables():
#     try :
#         conn = pymysql.connect(user='root', password='', host='localhost', database='test')
#         with conn.cursor() as cursor:
#             tables = cursor.execute("show tables")
#             return cursor.fetchall()
#     except pymysql.Error as r:
#         print(r)

# print(tables())
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

# قائمة المنسدلة
options = ['Option 1', 'Option 2', 'Option 3']
dropdown = ttk.Combobox(root, values=options)
dropdown.pack()

# دالة التحديث لقائمة المنسدلة
def update_dropdown():
    new_options = ['New Option 1', 'New Option 2', 'New Option 3']
    dropdown['values'] = new_options