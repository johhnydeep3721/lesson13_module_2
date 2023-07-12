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

label_them_xoa_sua = tkinter.Label(giaodien,text="")
label_them_xoa_sua.grid(column=1, row=9)

label_ketnoi = tkinter.Label(giaodien,text="")
label_ketnoi.grid(column=1, row=12)

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
    age = textbox2.get()
    country = textbox3.get()
    sex = combobox.get()
    information = int(textbox5.get())
    english = int(textbox6.get())

    insert = '''
        INSERT INTO Hocvien (name, age, country, sex, information, english)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''
    values = (name,age,country,sex,information,english)
    cursor.execute(insert,values)
    connection.commit() # chức năng kết nối vào sql không được quên :))
    cursor.close()
    connection.close()

    scrolled.insert(tkinter.END, "")

    textbox1.delete(0, tkinter.END) # xoa chu trong text
    textbox2.delete(0, tkinter.END)
    textbox3.delete(0, tkinter.END)
    combobox.delete(0, tkinter.END)
    textbox5.delete(0, tkinter.END)
    textbox6.delete(0, tkinter.END)

    try:    # hien thi them
        connection = getConnection()
        if connection.is_connected():
            label_them_xoa_sua.config(text="Da Them", fg="black")
            connection.close()
    except mysql.connector.errors as error:
        label_them_xoa_sua.config(text="Loi", fg="red")

def Hien_thi_hoc_vien():
    connection = getConnection()
    cursor = connection.cursor()
    select_query = 'SELECT * FROM Hocvien'
    cursor.execute(select_query)
    result = cursor.fetchall()

    scrolled.delete('1.0', tkinter.END) #xoa noi dung co trong scrolled
    for row in result:
        scrolled.insert(tkinter.END, f"ID: {row[0]} ")
        scrolled.insert(tkinter.END, f"Name: {row[1]} ")
        scrolled.insert(tkinter.END, f"Age: {row[2]} ")
        scrolled.insert(tkinter.END, f"Country: {row[3]} ")
        scrolled.insert(tkinter.END, f"Sex: {row[4]} ")
        scrolled.insert(tkinter.END, f"Information: {row[5]} ")
        scrolled.insert(tkinter.END, f"English: {row[6]} ")
        scrolled.insert(tkinter.END, "-"*20 +"\n")
        
        connection.commit()
def Xoa_hoc_vien():
    connection = getConnection()
    cursor = connection.cursor()
    delete_query = "DELETE FROM Hocvien where id = %s"
    id_to_delete = 1
    cursor.execute(delete_query, (id_to_delete,))
    connection.close()
    cursor.close()
    connection.commit()
    scrolled.insert(tkinter.END, "XOA THANH CONG \n")

    textbox1.delete(0, tkinter.END) 
    textbox2.delete(0, tkinter.END)
    textbox3.delete(0, tkinter.END)
    combobox.delete(0, tkinter.END)
    textbox5.delete(0, tkinter.END)
    textbox6.delete(0, tkinter.END)

    try: 
        connection = getConnection()
        if connection.is_connected():
            label_them_xoa_sua.config(text="Da Xoa", fg="black")
            connection.close()
    except mysql.connector.errors as error:
        label_them_xoa_sua.config(text="Loi", fg="red")


def Sua_hoc_vien():
    connection = getConnection()
    cursor = connection.cursor()
    update = "UPDATE Hocvien SET name = %s, age = %s, sex = %s, information = %s, engllish = %s WHERE id = %s"
    new_name = textbox1.get()
    new_age = int(textbox2.get())
    new_county = textbox3.get()
    new_sex = combobox.get()
    new_information = int(textbox5.get())
    new_english = int(textbox6.get())
    id_update =1
    cursor.execute(update, new_name,new_age,new_county,new_sex,new_information,new_english,id_update)

    connection.commit()
    scrolled.insert(tkinter.END, "SUA THANH CONG \n")

    textbox1.delete(0, tkinter.END)
    textbox2.delete(0, tkinter.END)
    textbox3.delete(0, tkinter.END)
    combobox.delete(0, tkinter.END)
    textbox5.delete(0, tkinter.END)
    textbox6.delete(0, tkinter.END)
    try: 
        connection = getConnection()
        if connection.is_connected():
            label_them_xoa_sua.config(text="Da Sua", fg="black")
            connection.close()
    except mysql.connector.errors as error:
        label_them_xoa_sua.config(text="Loi", fg="red")


def Ket_noi():
    connection = getConnection()
    cursor = connection.cursor()
    connection.commit()
    scrolled.insert(tkinter.END, "KET NOI THANH CONG \n")
    try: 
        connection = getConnection()
        if connection.is_connected():
            label_ketnoi.config(text="Da Ket Noi", fg="black")
            connection.close()
    except mysql.connector.errors as error:
        label_ketnoi.config(text="Loi", fg="red")



Button_Them_hoc_vien = tkinter.Button(giaodien,text="Them hoc vien",bg="white",fg="black",command=Them_hoc_vien)
Button_Them_hoc_vien.grid(column=0,row=7)

Button_Hien_thi_hoc_vien = tkinter.Button(giaodien,text="Hien Thi Hoc Vien",bg="white",fg="black",command=Hien_thi_hoc_vien)
Button_Hien_thi_hoc_vien.grid(column=1,row=7)

Button_Xoa_Hoc_Vien = tkinter.Button(giaodien,text="Xoa Hoc Vien",bg="white",fg="black",command=Xoa_hoc_vien)
Button_Xoa_Hoc_Vien.grid(column=0,row=8)

Button_Sua_Hoc_Vien = tkinter.Button(giaodien,text="Sua Hoc Vien",bg="white",fg="black",command=Sua_hoc_vien)
Button_Sua_Hoc_Vien.grid(column=1,row=8)


scrolled = ScrolledText(giaodien,width=30, height=10)
scrolled.grid(column=1,row=10,padx=10)

Button_Ket_noi = tkinter.Button(giaodien,text="Ket Noi",bg="white",fg="black",command=Ket_noi)
Button_Ket_noi.grid(column=1,row=11)

giaodien.mainloop()
