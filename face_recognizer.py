from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime





class Face_recog:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # zero is for starting position
        self.root.title("Face Recognition")
        self.root.wm_iconbitmap("face-scan.ico")

        title_lbl = Label(self.root,text="FACE RECOGNITION",font =("High Tower Text",35,"bold"),fg = "cyan",bg='black')
        title_lbl.place(x=0,y=0,width=1550,height=45)
        
        #exit btn
        b8_1 = Button(self.root,text="EXIT",command=self.exit_gui,cursor="hand2",font =("Corbel",9,"bold"),bd=0,relief=RIDGE,fg='white',bg='black',activebackground='black') #cursor for customization
        b8_1.place(x=1300,y=20,width=40,height=20)

        img_right = Image.open(r"Images\face6.jpg") # r is used to make backward slash as forward
        img_right = img_right.resize((1550,790),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        r_lbl = Label(self.root,image=self.photoimg_right)
        r_lbl.place(x=0,y=45,width=1550,height=790)

        b1_1 = Button(r_lbl,text='''FACE RECOGNITION''',command=self.face_recogn,cursor="spider",font =("Elephant",11,"bold"),bg = "light blue",fg = "black") #cursor for customization
        b1_1.place(x=743,y=462,width=100,height=100)

    # attendance

    def mark_att(self,r,n):
        conn = mysql.connector.connect(host='localhost',username ='',password='',database='face_recognition')
        my_cursor = conn.cursor()
        # Check if the name is already present in the database
        sql = "SELECT name FROM attendance WHERE name IN (%s, %s)"
        val = (r, n)
        my_cursor.execute(sql, val)
        result = my_cursor.fetchall()
        name_list = [x[0] for x in result]
        if r not in name_list and n not in name_list:
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
            present = "Present" 
         
       
            sql = "INSERT INTO attendance (ROLL_NO,NAME,TIME,DATE,STATUS) VALUES (%s, %s, %s, %s, %s)"
            val = (r, n, dtString, d1, present)
            my_cursor.execute(sql, val)
            conn.commit()
            conn.close()

        #face recognition

    def face_recogn(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord =[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host='localhost', username='', password='',
                                                database='face_recognition')
                my_cursor = conn.cursor()
                my_cursor.execute("select NAME from student where STUDENT_ID="+str(id))
                n=my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select ROLL_NO from student where STUDENT_ID="+str(id))
                r=my_cursor.fetchone()
                r = "+".join(r)



                if confidence>77:                    
                    cv2.putText(img,f'NAME : {n}',(x,y-70),cv2.FONT_ITALIC,0.8,(0,0,255 ),3)
                    cv2.putText(img,f'ROLL NO : {r}',(x,y-40),cv2.FONT_ITALIC,0.8,(0,0,255),3)
                    # self.mark_attendance(r,n)
                    self.mark_att(r,n)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"UNKNOWN FACE",(x,y-55),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),3)
                coord=[x,y,w,h]
            return coord
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img 
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Press Enter key to Exit",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

        
    # exit function
    def exit_gui(self):     
        self.root.destroy()
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_recog(root)
    root.mainloop()
