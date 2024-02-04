from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # zero is for starting position
        self.root.title("Dveeloper Details")
        self.root.wm_iconbitmap("face-scan.ico")

        title_lbl = Label(self.root,text="DEVELOPER ZONE",font =("High Tower Text",35,"bold"),bg = "white",fg = "black")
        title_lbl.place(x=0,y=0,width=1550,height=45)

        img_top = Image.open(r"Images\dev1.jpg") # r is used to make backward slash as forward
        img_top = img_top.resize((1550,740),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1550,height=740)

        main_frame1 = Frame(f_lbl,bd = 2 ,bg='white')
        main_frame1.place(x=837,y=263,width=200,height=222)


        img = Image.open(r"Images\pr.png") # r is used to make backward slash as forward
        img = img.resize((200,200),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lbl1 = Label(main_frame1,image=self.photoimg)
        f_lbl1.place(x=0,y=0,width=200,height=220)

        main_frame2 = Frame(f_lbl,bd = 2 ,bg='white')
        main_frame2.place(x=510,y=263,width=325,height=222)


        abt = Label(main_frame2,text='''
Hello, I am Rahul Sharma a
passionate
software developers with expertise.
I developed this face recognition 
attendance system using Python 
Tkinter to make attendance tracking 
easier and more accurate.
Our contact details:
rs7267389@gmail.com
        ''',
        font=('Courier','11','bold'))
        abt.place(x=0,y=0,width=325,height=222)




        b8_1 = Button(self.root,text="EXIT",command=self.exit_gui,cursor="hand2",font =("Corbel",9,"bold"),bd=0,relief=RIDGE,fg='white',bg='black',activebackground='black') #cursor for customization
        b8_1.place(x=1300,y=20,width=40,height=20)

    def exit_gui(self):     
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()