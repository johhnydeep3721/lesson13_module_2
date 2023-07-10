import tkinter
from tkinter.ttk import *
from tkinter.scrolledtext import *
import mysql.connector

def getConnection():
    connection = mysql.connector.connect(host='localhost', 
                                        user='root', 
                                        passwd='root',
                                        database='Quan_ly_hoc_vien'
    )
    return connection

giaodien = tkinter.Tk()

giaodien.title("Quan Ly Hoc Vien") 
giaodien.geometry("500x530") # kich thuoc giao dien
heading = tkinter.Label(giaodien,text="Chuong Trinh Quan Ly Hoc Vien",fg="black")
heading.grid(column=1,row=0,padx=100)

def label():
    # tieu de ten
    label1 = tkinter.Label(giaodien,text="Name",fg="black")
    label1.grid(column=0,row=1)

    label2 = tkinter.Label(giaodien,text="Age",fg="black")
    label2.grid(column=0,row=2)

    label3 = tkinter.Label(giaodien,text="Country",fg="black")
    label3.grid(column=0,row=3)

    label4 = tkinter.Label(giaodien,text="Sex",fg="black")
    label4.grid(column=0,row=4)

    label5 = tkinter.Label(giaodien,text="information",fg="black")
    label5.grid(column=0,row=5)

    label6 = tkinter.Label(giaodien,text="English",fg="black")
    label6.grid(column=0,row=6)
label()

 # phan nhap thong tin
value1 = tkinter.StringVar()
textbox1 = tkinter.Entry(giaodien,width=20,textvariable=value1)
textbox1.grid(column=1,row=1)

value2 = tkinter.StringVar()
textbox2 = tkinter.Entry(giaodien,width=20, textvariable=value2)
textbox2.grid(column=1,row=2)

value3 = tkinter.StringVar()
textbox3 = tkinter.Entry(giaodien,width=20, textvariable=value3)
textbox3.grid(column=1,row=3)


combobox = Combobox(giaodien)
combobox['values'] =('male','female')
combobox.grid(column=1,row=4)

value5 = tkinter.IntVar()
textbox5 = tkinter.Entry(giaodien,width=20, textvariable=value5)
textbox5.grid(column=1,row=5)



value6 = tkinter.IntVar()
textbox6 = tkinter.Entry(giaodien,width=20, textvariable=value6)
textbox6.grid(column=1,row=6)

# Phan xu ly
def Them_hoc_vien():
    connection = getConnection()
    cursor = connection.cursor()

    name = textbox1.get()
    age = int(textbox2.get())
    country = textbox3.get()
    sex = combobox.get()
    information = int(textbox5.get())
    english = int(textbox6.get())

    insert = '''
        INSERT INTO hoc_vien (name, age, country, sex, information, english)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''
    values = (name,age,country,sex,information,english)
    cursor.execute(insert,values)
    connection.commit()
    cursor.close()
    connection.close()
def Hien_thi_hoc_vien():

    pass
def Xoa_hoc_vien():
    pass
def Sua_hoc_vien():
    pass

def Ket_noi():
    pass


Button_Them_hoc_vien = tkinter.Button(giaodien,text="Them hoc vien",bg="white",fg="black")
Button_Them_hoc_vien.grid(column=0,row=7)

Button_Hien_thi_hoc_vien = tkinter.Button(giaodien,text="Hien Thi Hoc Vien",bg="white",fg="black")
Button_Hien_thi_hoc_vien.grid(column=1,row=7)

Button_Xoa_Hoc_Vien = tkinter.Button(giaodien,text="Xoa Hoc Vien",bg="white",fg="black")
Button_Xoa_Hoc_Vien.grid(column=0,row=8)

Button_Sua_Hoc_Vien = tkinter.Button(giaodien,text="Sua Hoc Vien",bg="white",fg="black")
Button_Sua_Hoc_Vien.grid(column=1,row=8)


scrolled = ScrolledText(giaodien,width=30, height=10)
scrolled.grid(column=1,row=9,pady=10)

Button_Ket_noi = tkinter.Button(giaodien,text="Ket Noi",bg="white",fg="black")
Button_Ket_noi.grid(column=1,row=10)

giaodien.mainloop()
