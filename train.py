from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # zero is for starting position
        self.root.title("Train Data")
        self.root.wm_iconbitmap("face-scan.ico")

        #title
        title_lbl = Label(self.root,text="TRAIN DATA SET",font =("High Tower Text",35,"bold"),bg = "white",fg = "indigo")
        title_lbl.place(x=0,y=0,width=1550,height=45)

        # exit btn 
        b8_1 = Button(self.root,text="EXIT",command=self.exit_gui,cursor="hand2",font =("Corbel",9,"bold"),bd=0,relief=RIDGE,fg='white',bg='black',activebackground='black') #cursor for customization
        b8_1.place(x=1300,y=20,width=40,height=20)

        #top image 
        img_top = Image.open(r"Images\tr.jpg") # r is used to make backward slash as forward
        img_top = img_top.resize((1550,365),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1550,height=365)

        #button
        b1_1 = Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font =("High Tower Text",40,"bold"),bg = "orange",fg = "black") #cursor for customization
        b1_1.place(x=0,y=410,width=1550,height=60)


        #bottom image
        img_bot = Image.open(r"Images\tr2.jpg") # r is used to make backward slash as forward
        img_bot = img_bot.resize((1550,365),Image.ANTIALIAS)
        self.photoimg_bot = ImageTk.PhotoImage(img_bot)
        f_lbl1 = Label(self.root,image=self.photoimg_bot)
        f_lbl1.place(x=0,y=470,width=1550,height=365)

    def train_classifier(self):
        data_dir = ("Data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img = Image.open(image).convert('L') #gray scale image
            imageNP = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # train the classfier and save

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data set completed !!",parent=self.root)


        
    # exit 
    def exit_gui(self):     
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
