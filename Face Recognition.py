from tkinter import*
from tkinter import ttk
import tkinter

from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognizer import Face_recog
from attendance import Attendance
from developer import Developer
from help import Help
from tkinter import messagebox

class Face_Recoginition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # zero is for starting position
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face-scan.ico")

        #first image 
        img = Image.open(r"Images\st.jpg") # r is used to make backward slash as forward
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        # second image 
        img1 = Image.open(r"Images\bn.jpg") # r is used to make backward slash as forward
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        s_lbl = Label(self.root,image=self.photoimg1)
        s_lbl.place(x=525,y=0,width=535,height=130)

        # third image 
        img2 = Image.open(r"Images\clg.jpg") # r is used to make backward slash as forward
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        t_lbl = Label(self.root,image=self.photoimg2)
        t_lbl.place(x=1000,y=0,width=580,height=130)
        
        # background image ---
        img3 = Image.open(r"Images\bg1.jpg") # r is used to make backward slash as forward
        img3 = img3.resize((1550,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1550,height=710)

        #label title

        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font =("Consolas",35,"bold"),bg = "light yellow",fg = "red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # student button
        img4 = Image.open(r"Images\st1.png") # r is used to make backward slash as forward
        img4 = img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2") #cursor for customization
        b1.place(x=200,y=50,width=200,height=200)
        b1_1 = Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font =("Corbel",17,"bold"),bg = "orange",fg = "black") #cursor for customization
        b1_1.place(x=200,y=250,width=200,height=40)
        

        #Face detector button
        img5 = Image.open(r"Images\ic1.png") # r is used to make backward slash as forward
        img5 = img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b2 = Button(bg_img,image=self.photoimg5,command=self.face_data,cursor="hand2") #cursor for customization
        b2.place(x=500,y=50,width=200,height=200)
        b2_1 = Button(bg_img,text="FACE DETECTOR",command=self.face_data,cursor="hand2",font =("Corbel",17,"bold"),bg = "orange",fg = "black") #cursor for customization
        b2_1.place(x=500,y=250,width=200,height=40)

        # Attendance face button -
        img6 = Image.open(r"Images\im.png") # r is used to make backward slash as forward
        img6 = img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b3 = Button(bg_img,image=self.photoimg6,command=self.attendance_data,cursor="hand2") #cursor for customization
        b3.place(x=800,y=50,width=200,height=200)
        b3_1 = Button(bg_img,text="ATTENDANCE",command=self.attendance_data,cursor="hand2",font =("Corbel",17,"bold"),bg = "orange",fg = "black") #cursor for customization
        b3_1.place(x=800,y=250,width=200,height=40)

        # help button 

        img7 = Image.open(r"Images\help.png") # r is used to make backward slash as forward
        img7 = img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b4 = Button(bg_img,image=self.photoimg7,command=self.help_data,cursor="hand2") #cursor for customization
        b4.place(x=1100,y=50,width=200,height=200)
        b4_1 = Button(bg_img,text="HELP",command=self.help_data,cursor="hand2",font =("Corbel",17,"bold"),bg = "orange",fg = "black") #cursor for customization
        b4_1.place(x=1100,y=250,width=200,height=40)

        #train button 

        img8 = Image.open(r"Images\train.png") # r is used to make backward slash as forward
        img8 = img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b5 = Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2") #cursor for customization
        b5.place(x=200,y=350,width=200,height=200)
        b5_1 = Button(bg_img,text="TRAINING DATA",command=self.train_data,cursor="hand2",font =("Corbel",17,"bold"),bg = "orange",fg = "black") #cursor for customization
        b5_1.place(x=200,y=550,width=200,height=40)

        #photos button 

        img9 = Image.open(r"Images\ph1.jpg") # r is used to make backward slash as forward
        img9 = img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b6 = Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img) #cursor for customization
        b6.place(x=500,y=350,width=200,height=200)
        b6_1 = Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font =("Corbel",17,"bold"),bg = "orange",fg = "black") #cursor for customization
        b6_1.place(x=500,y=550,width=200,height=40)

        # devloper button 
        img10 = Image.open(r"Images\pr.png") # r is used to make backward slash as forward
        img10 = img10.resize((200,200),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b7 = Button(bg_img,image=self.photoimg10,command=self.developer_data,cursor="hand2") #cursor for customization
        b7.place(x=800,y=350,width=200,height=200)
        b7_1 = Button(bg_img,text="DEVELOPER",command=self.developer_data,cursor="hand2",font =("Corbel",17,"bold"),bg = "orange",fg = "black") #cursor for customization
        b7_1.place(x=800,y=550,width=200,height=40)

        # exit button 

        img11 = Image.open(r"Images\exit.png") # r is used to make backward slash as forward
        img11 = img11.resize((200,200),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b8 = Button(bg_img,image=self.photoimg11,command=self.exit_gui,cursor="hand2") #cursor for customization
        b8.place(x=1100,y=350,width=200,height=200)
        b8_1 = Button(bg_img,text="EXIT",command=self.exit_gui,cursor="hand2",font =("Corbel",17,"bold"),bg = "orange",fg = "black") #cursor for customization
        b8_1.place(x=1100,y=550,width=200,height=40)



        #
    def open_img(self):
        os.startfile("Data")

    def exit_gui(self):     
        self.root.destroy()

        # function button 

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recog(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recoginition_System(root)
    root.mainloop()