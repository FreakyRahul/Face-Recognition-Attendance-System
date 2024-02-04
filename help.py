from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # zero is for starting position
        self.root.title("Help")
        self.root.wm_iconbitmap("face-scan.ico")

        
        title_lbl = Label(self.root,text="HELP WINDOW",font =("High Tower Text",35,"bold"),bg = "black",fg = "indigo")
        title_lbl.place(x=0,y=0,width=1550,height=45)

        img_top = Image.open(r"Images\help2.png") # r is used to make backward slash as forward
        img_top = img_top.resize((1300,650),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=110,y=45,width=1300,height=650)

        help_label = Label(self.root,text="contact us :  rs7267389@gmail.com , xxxxxxxxxx",font=('Consolas',20,'bold'),fg='black')
        help_label.place(x=100,y=700)

        b8_1 = Button(self.root,text="EXIT",command=self.exit_gui,cursor="hand2",font =("Corbel",9,"bold"),bd=0,relief=RIDGE,fg='white',bg='black',activebackground='black') #cursor for customization
        b8_1.place(x=1300,y=20,width=40,height=20)

    def exit_gui(self):     
        self.root.destroy()
        
if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()