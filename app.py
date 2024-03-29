from tkinter import *
from tkinter import messagebox, filedialog, ttk
import pymysql



# Variables
PRIMARYCOLOR = '#19282F'
SECONDRYCOLOR = '#5534A5'
SUCCESSCOLOR = '#F4DFBA'
FONT = 'Tajwal'
PRBG = 'white'
SEBG = 'whitesmoke'
FONTCOLOR = 'white'
STATE = 'normal'

is_connect = False
server = ''
username = ''
password = ''
db = ''
file = ''

def Connection():
    global is_connect
    global server
    global username
    global password

    server = ent1L1F2.get()
    username = ent1L2F2.get()
    password = ent1L3F2.get()
    try :
        conn =  pymysql.connect(
                        host= server,
                        user= username,
                        password= password
                    )
        is_connect = True
        messagebox.showinfo('Database Managment System', 'server is connected')
        L1F10.configure(text=f'Server : {server}')
        L3F10.configure(text=f'Is Connect : {is_connect}')
    except pymysql.Error as r:
        is_connect = False
        messagebox.showerror('Error', r)

def ShowDB():
    global server
    global username
    global password

    try :
        conn = pymysql.connect(host=server, user= username, password=password)
        with conn.cursor() as cursor:
            databases = cursor.execute("SHOW DATABASES")
            for db in cursor:
                L1F5 = Label(F5, bg=SEBG, text=db[0])
                L1F5.pack()
        placer(F5, w=190, h=250)
    except pymysql.Error as r:
        messagebox.showerror('Error', r)

def Create_Tabel():
    try :
        conn = pymysql.connect(host=server, user= username, password=password, database=db)
        with conn.cursor() as cursor:
            sql = cursor.execute(f"CREATE TABEL {db} . {ent1L2F3.get()} ({ent1L3F3.get()} {ent1L4F3.get()}({ent1L5F3.get()}) NOT NULL);")
        tables()
    except pymysql.Error as r:
        messagebox.showerror('Error', r)


def Create_Col():
    try :
        conn = pymysql.connect(host=server, user= username, password=password, database=db)
        with conn.cursor() as cursor:
            sql = cursor.execute(f"ALTER TABLE `{ent1L2F4.get()}` ADD `{ent1L3F4.get()}` {ent1L4F4.get()}({ent1L5F4.get()}) NOT NULL {ent1L1F4.get().replace(',',' ')};")
    except pymysql.Error as r:
        messagebox.showerror('Error', r)


def CHDB():
    global db
    try : 
        conn = pymysql.connect(host=server, user= username, password=password)
        with conn.cursor() as cursor:
            cursor.execute(f'use {ent1L1F8.get()}')
            db = ent1L1F8.get()
            conn.commit()
        L2F10.configure(text=f'Database : {db}')
        L4F10.configure(text=f'Tables : {tables()}')
    except pymysql.Error as r:
        messagebox.showerror('Error', r)

def CRDB():
    try :
        conn = pymysql.connect(host=server, user= username, password=password)
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE `{ent1L2F1.get()}`;")
        ShowDB()
        
    except pymysql.Error as r:
        messagebox.showerror('Error', r)

def deldb():
    global db
    try :
        conn = pymysql.connect(host=server, user= username, password=password)
        with conn.cursor() as cursor:
            cursor.execute(f"DROP DATABASE `{ent1L1F6.get()}`;")
        ShowDB()
        L2F10.configure(text=f'Database : ')
        L4F10.configure(text=f'Tables : ')
    except pymysql.Error as r:
        messagebox.showerror('Error', r)

def deltb():
    try :
        conn = pymysql.connect(host=server, user= username, password=password, database=db)
        with conn.cursor() as cursor:
            cursor.execute(f"DROP TABLE `{db}`.`{ent1L2F6.get()}`")
        tables()
    except pymysql.Error as r:
        messagebox.showerror('Error', r)

def delcol():
    try :
        conn = pymysql.connect(host=server, user= username, password=password, database=db)
        with conn.cursor() as cursor:
            cursor.execute(f"ALTER TABLE `{ent1L1F7.get()}` DROP `{ent1L2F7.get()}`;")
    except pymysql.Error as r:
        messagebox.showerror('Error', r)

def comfile():
    try :
        conn = pymysql.connect(host=server, user= username, password=password, database=db)
        print(file)
        with conn.cursor() as cursor:
            cursor.execute(f"source {file}")
        messagebox.showinfo('Done', 'تم تنفيذ اوامر الملف')
    except pymysql.Error as r:
        messagebox.showerror('Error', r)

def chfi():
    global file
    file = filedialog.askopenfilename(title='Chose file to run DPMS-ARDE ')
    if len(file) > 1:
        if len(file) > 20:
            file = file.replace(file[20:], '') + '...'
            L2F9.configure(text = file)
        else :
            L2F9.configure(text = file)



def tables():
    try :
        conn = pymysql.connect(host=server, user= username, password=password, database=db)
        with conn.cursor() as cursor:
            tables = cursor.execute(f"show tables")
            return tables
    except pymysql.Error as r:
        messagebox.showerror('Error', r)

def placer(element, w, h):
    element.place(width=w, height=h)

root = Tk() # Window
root.geometry('1010x500+200+40') # settings of geometry
root.resizable(False,False) # Controls Of Resizabling
root.configure(bg=PRBG) # For Styling
root.title('Arabian Developer [Database Managment System]') # Change The Title
# root.iconbitmap('assets/icon.ico') # Change The Icon
title1 = Label(root,text='Database Managment System', fg=PRBG, bg=PRIMARYCOLOR, font=(FONT, 14))
title1.pack(fill=X)

F1 = Frame(root, bg=SEBG, bd='2', relief=GROOVE)
F1.place(x=5, y=40, width=300, height=190)
titleF1 = Label(F1,text='Database Controls', fg=FONTCOLOR, bg=SECONDRYCOLOR, font=(FONT, 12))
titleF1.pack(fill=X)

L1F1 = Label(F1, bg=SEBG, text='Databases')
L1F1.place(x=10, y=50) 
btn1L1F1 = Button(F1, cursor='hand2', text='Show', command=ShowDB, state=STATE)
btn1L1F1.place(x=100, y=50, width=125)
btn2L1F1 = Button(F1, cursor='hand2', bg=SUCCESSCOLOR, state=STATE, text='Hide', command=lambda:placer(F5, w=0, h=0))
btn2L1F1.place(x=230, y=50, width=60)

L2F1 = Label(F1, bg=SEBG, text='DB-Name')
L2F1.place(x=10, y=80)
ent1L2F1 = Entry(F1)
ent1L2F1.place(x=100,y=80, width=125)
btn1L2F1 = Button(F1, cursor='hand2', bg=SUCCESSCOLOR, state=STATE, text='Create', command=CRDB)
btn1L2F1.place(x=230, y=80, width=60)

L3F1 = Label(F1, bg=SEBG, text='Table')
L3F1.place(x=10, y=110) 
btn1L3F1 = Button(F1, cursor='hand2', text='Create Table', state=STATE, command=lambda:placer(F3, w=200, h=250))
btn1L3F1.place(x=100, y=110, width=125)
btn2L3F1 = Button(F1, cursor='hand2', bg=SUCCESSCOLOR, state=STATE, text='Hide', command=lambda:placer(F3, w=0, h=0))
btn2L3F1.place(x=230, y=110, width=60)

L4F1 = Label(F1, bg=SEBG, text='Cols')
L4F1.place(x=10, y=140)
btn1L4F1 = Button(F1, cursor='hand2', text='Create Col', state=STATE, command=lambda:placer(F4, w=200, h=250))
btn1L4F1.place(x=100, y=140, width=125)
btn2L4F1 = Button(F1, cursor='hand2', bg=SUCCESSCOLOR, state=STATE, text='Hide', command=lambda:placer(F4, w=0, h=0))
btn2L4F1.place(x=230, y=140, width=60)



F2 = Frame(root, bg=SEBG, bd='2', relief=GROOVE)
F2.place(x=310, y=40, width=300, height=190)
titleF2 = Label(F2,text='Database Connect', fg=FONTCOLOR, bg=SECONDRYCOLOR, font=(FONT, 12))
titleF2.pack(fill=X)

L1F2 = Label(F2, bg=SEBG, text='Server-Name')
L1F2.place(x=10, y=50) 
ent1L1F2 = Entry(F2)
ent1L1F2.place(x=100,y=50, width=180)

L2F2 = Label(F2, bg=SEBG, text='Username')
L2F2.place(x=10, y=80)
ent1L2F2 = Entry(F2)
ent1L2F2.place(x=100,y=80, width=180)

L3F2 = Label(F2, bg=SEBG, text='Password')
L3F2.place(x=10, y=110) 
ent1L3F2 = Entry(F2)
ent1L3F2.place(x=100,y=110, width=180)

btn1F2 = Button(F2, state='normal', cursor='hand2', text='Connect', bg=SUCCESSCOLOR, command=Connection)
btn1F2.place(x=100, y=140, width=180)



F3 = Frame(root, bg=SEBG, bd='2', relief=GROOVE)
F3.place(x=5, y=240, width=200, height=250)
titleF3 = Label(F3,text='Create Table', fg=FONTCOLOR, bg=SECONDRYCOLOR, font=(FONT, 12))
titleF3.pack(fill=X)

L1F3 = Label(F3, bg=SEBG, text='Col-Props')
L1F3.place(x=6,y=170)
ent1L1F3 = Entry(F3)
ent1L1F3.place(x=86,y=170, width=100)

L2F3 = Label(F3, bg=SEBG, text='Table-Name')
L2F3.place(x=6,y=50)
ent1L2F3 = Entry(F3)
ent1L2F3.place(x=86,y=50, width=100)

L3F3 = Label(F3, bg=SEBG, text='Col-Name')
L3F3.place(x=6,y=80)
ent1L3F3 = Entry(F3)
ent1L3F3.place(x=86,y=80, width=100)

L4F3 = Label(F3, bg=SEBG, text='Col-Type')
L4F3.place(x=6,y=110)
choices = ['int', 'varchar', 'text', 'date']
ent1L4F3 = ttk.Combobox(F3, values = choices)
ent1L4F3.place(x=86,y=110, width=100)

L5F3 = Label(F3, bg=SEBG, text='Col-Length')
L5F3.place(x=6,y=140)
ent1L5F3 = Entry(F3)
ent1L5F3.place(x=86,y=140, width=100)

btn1F3 = Button(F3, cursor='hand2', text='Create', bg=SUCCESSCOLOR, state=STATE, command=Create_Tabel)
btn1F3.place(x=6, y=205, width=180)



F4 = Frame(root, bg=SEBG, bd='2', relief=GROOVE)
F4.place(x=213, y=240, width=200, height=250)
titleF4 = Label(F4,text='Create Column', fg=FONTCOLOR, bg=SECONDRYCOLOR, font=(FONT, 12))
titleF4.pack(fill=X)

L1F4 = Label(F4, bg=SEBG, text='Col-Props')
L1F4.place(x=6,y=170)
ent1L1F4 = Entry(F4)
ent1L1F4.place(x=86,y=170, width=100)

L2F4 = Label(F4, bg=SEBG, text='Table-Name')
L2F4.place(x=6,y=50)
ent1L2F4 = Entry(F4)
ent1L2F4.place(x=86,y=50, width=100)

L3F4 = Label(F4, bg=SEBG, text='Col-Name')
L3F4.place(x=6,y=80)
ent1L3F4 = Entry(F4)
ent1L3F4.place(x=86,y=80, width=100)

L4F4 = Label(F4, bg=SEBG, text='Col-Type')
L4F4.place(x=6,y=110)
choices = ['int', 'varchar', 'text', 'date']
ent1L4F4 = ttk.Combobox(F4, values = choices)
ent1L4F4.place(x=86,y=110, width=100)

L5F4 = Label(F4, bg=SEBG, text='Col-Length')
L5F4.place(x=6,y=140)
ent1L5F4 = Entry(F4)
ent1L5F4.place(x=86,y=140, width=100)

btn1F4 = Button(F4, cursor='hand2', text='Create', bg=SUCCESSCOLOR, state=STATE, command=Create_Col)
btn1F4.place(x=6, y=205, width=180)



F5 = Frame(root, bg=SEBG, bd='2', relief=GROOVE)
F5.place(x=420, y=240, width=0, height=0)
titleF5 = Label(F5,text='Databases', fg='white', bg=SECONDRYCOLOR, font=(FONT, 12))
titleF5.pack(fill=X)


F6 = Frame(root, bg=SEBG, bd='2', relief=GROOVE)
F6.place(x=615, y=40, width=200, height=120)
titleF6 = Label(F6,text='Delete', fg=FONTCOLOR, bg=SECONDRYCOLOR, font=(FONT, 12))
titleF6.pack(fill=X)

L1F6 = Label(F6, bg=SEBG, text='Database')
L1F6.place(x=0, y=50) 
ent1L1F6 = Entry(F6)
ent1L1F6.place(x=55,y=50, width=90)
btn2L1F6 = Button(F6, cursor='hand2', bg=SUCCESSCOLOR, state=STATE, text='DEL', command=deldb)
btn2L1F6.place(x=150, y=50, width=40)

L2F6 = Label(F6, bg=SEBG, text='Tabel')
L2F6.place(x=0, y=80)
ent1L2F6 = Entry(F6)
ent1L2F6.place(x=55,y=80, width=90)
btn1L2F6 = Button(F6, cursor='hand2', bg=SUCCESSCOLOR, state=STATE, text='DEL', command=deltb)
btn1L2F6.place(x=150, y=80, width=40)


F7 = Frame(root, bg=SEBG, bd='2', relief=GROOVE)
F7.place(x=615, y=170, width=200, height=150)
titleF7 = Label(F7,text='Delete Column', fg=FONTCOLOR, bg=SECONDRYCOLOR, font=(FONT, 12))
titleF7.pack(fill=X)

L1F7 = Label(F7, bg=SEBG, text='Table')
L1F7.place(x=5, y=50) 
ent1L1F7 = Entry(F7)
ent1L1F7.place(x=70,y=50, width=115)

L2F7 = Label(F7, bg=SEBG, text='Column')
L2F7.place(x=5, y=80)
ent1L2F7 = Entry(F7)
ent1L2F7.place(x=70,y=80, width=115)

btn1F7 = Button(F7, cursor='hand2', text='Delete', bg=SUCCESSCOLOR, state=STATE, command=delcol)
btn1F7.place(x=5, y=110, width=180)


F8 = Frame(root, bg=SEBG, bd='2', relief=GROOVE)
F8.place(x=820, y=40, width=185, height=120)
titleF8 = Label(F8,text='Switch Database', fg=FONTCOLOR, bg=SECONDRYCOLOR, font=(FONT, 12))
titleF8.pack(fill=X)

L1F8 = Label(F8, bg=SEBG, text='Database')
L1F8.place(x=5, y=50) 
ent1L1F8 = Entry(F8)
ent1L1F8.place(x=65,y=50, width=105)

btn1F8 = Button(F8, cursor='hand2', text='Switch', bg=SUCCESSCOLOR, state=STATE, command=CHDB)
btn1F8.place(x=5, y=80, width=170)


F9 = Frame(root, bg=SEBG, bd='2', relief=GROOVE)
F9.place(x=820, y=170, width=185, height=150)
titleF9 = Label(F9,text='Command File', fg=FONTCOLOR, bg=SECONDRYCOLOR, font=(FONT, 12))
titleF9.pack(fill=X)

L1F9 = Label(F9, bg=SEBG, text='File')
L1F9.place(x=5, y=50) 
btn1L1F9 = Button(F9, text='Chose File', command=chfi, bg=SUCCESSCOLOR).place(x=105,y=50, width=70)

L2F9 = Label(F9, bg=SEBG, text='لم يتم اختيار ملف')
L2F9.place(x=5, y=80)

btn1F9 = Button(F9, cursor='hand2', text='Run', bg=SUCCESSCOLOR, state=STATE, command=comfile)
btn1F9.place(x=5, y=110, width=170)


F10 = Frame(root, bg=SEBG, bd='2', relief=GROOVE)
F10.place(x=615, y=330, width=390, height=160)
titleF10 = Label(F10,text='STATUS', fg=FONTCOLOR, bg=SECONDRYCOLOR, font=(FONT, 12))
titleF10.pack(fill=X)

L1F10 = Label(F10, bg=SEBG, text=f'Server : ')
L1F10.place(x=25, y=50)

L2F10 = Label(F10, bg=SEBG, text=f'Database : ')
L2F10.place(x=25, y=80)

L3F10 = Label(F10, bg=SEBG, text=f'Is Connect : {is_connect}')
L3F10.place(x=220, y=50)

L4F10 = Label(F10, bg=SEBG, text=f'Tables : ')
L4F10.place(x=220, y=80)

L5F10 = Label(F10, bg=SEBG, text='DEVELOPED BY : ARABIAN DEVELOPER ')
L5F10.place(x=85, y=130)
root.mainloop()