from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # zero is for starting position
        self.root.title("Student Details")
        self.root.wm_iconbitmap("face-scan.ico")

        #variables--
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name=StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        

        


        #first image 
        img = Image.open(r"Images\z1.jpg") # r is used to make backward slash as forward
        img = img.resize((500,150),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=150)
        
        # second image 
        img1 = Image.open(r"Images\z2.jpg") # r is used to make backward slash as forward
        img1 = img1.resize((500,150),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        s_lbl = Label(self.root,image=self.photoimg1)
        s_lbl.place(x=500,y=0,width=570,height=150)

        # third image 
        img2 = Image.open(r"Images\man2.jpg") # r is used to make backward slash as forward
        img2 = img2.resize((500,150),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        t_lbl = Label(self.root,image=self.photoimg2)
        t_lbl.place(x=1000,y=0,width=570,height=150)

        

        # background image ---
        img3 = Image.open(r"Images\bg1.jpg") # r is used to make backward slash as forward
        img3 = img3.resize((1550,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1550,height=710)

        #label title

        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font =("Consolas",35,"bold"),bg = "light yellow",fg = "green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #exit btn
        b8_1 = Button(title_lbl,text="EXIT",command=self.exit_gui,cursor="hand2",font =("Corbel",9,"bold"),bd=0,relief=RIDGE,fg='black',bg='light yellow',activebackground='light yellow') #cursor for customization
        b8_1.place(x=1300,y=10,width=40,height=20)

        # main frame 
        main_frame = Frame(bg_img,bd = 2 )
        main_frame.place(x=10,y=45,width=1510,height=600)

        #left label frame -
        Left_frame = LabelFrame(main_frame,bd= 2 ,relief=RIDGE,text="STUDENT DETAILS",font=('Consolas',12,'bold'))
        Left_frame.place(x=10,y=1,width=735,height=580)

        img_left = Image.open(r"Images\bg3.jpg") # r is used to make backward slash as forward
        img_left = img_left.resize((720,180),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        t_lbl = Label(Left_frame,image=self.photoimg_left)
        t_lbl.place(x=5,y=0,width=720,height=180)

        # current course -
        current_co_frame = LabelFrame(Left_frame,bd= 2 ,relief=RIDGE,text="CURRENT COURSE INFORMATION",font=('Consolas',12,'bold'))
        current_co_frame.place(x=5,y=150,width=720,height=105)

        # department  -
        dep_label = Label(current_co_frame,text="DEPARTMENT",font=('Consolas',12,'bold'),bg='black',fg='white')
        dep_label.grid(row=0,column=0,padx=10,sticky=W)  
        dep_combo = ttk.Combobox(current_co_frame,textvariable=self.var_dep,font=('Consolas',12,'bold'),state="readonly") 
        dep_combo['values'] = ('SELECT DEPARTMENT','CSE','AGRICULTURE')
        dep_combo.current(0) # select 0 index item of above tuple
        dep_combo.grid(row=0,column=1,padx=2,pady=10)   

        # course -
        course_label = Label(current_co_frame,text="COURSE",font=('Consolas',12,'bold'),bg='black',fg='white')
        course_label.grid(row=0,column=2,padx=10,sticky=W)  
        course_combo = ttk.Combobox(current_co_frame,textvariable=self.var_course,font=('Consolas',12,'bold'),state="readonly") 
        course_combo['values'] = ('SELECT COURSE','SOFTWARE ENGG.','AI/DS','FOOD TECHNOLOGY')
        course_combo.current(0) # select 0 index item of above tuple
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)   

        # year 
        year_label = Label(current_co_frame,text="YEAR",font=('Consolas',12,'bold'),bg='black',fg='white')
        year_label.grid(row=1,column=0,padx=10,sticky=W)  
        year_combo = ttk.Combobox(current_co_frame,textvariable=self.var_year,font=('Consolas',12,'bold'),state="readonly") 
        year_combo['values'] = ('SELECT YEAR','2020-24','2021-25','2022-26')
        year_combo.current(0) # select 0 index item of above tuple
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)  

        # semester -
        semester_label = Label(current_co_frame,text="SEMESTER",font=('Consolas',12,'bold'),bg='black',fg='white')
        semester_label.grid(row=1,column=2,padx=10,sticky=W)  
        semester_combo = ttk.Combobox(current_co_frame,textvariable=self.var_semester,font=('Consolas',12,'bold'),state="readonly") 
        semester_combo['values'] = ('SELECT SEMESTER','1','2','3','4','5','6','7','8')
        semester_combo.current(0) # select 0 index item of above tuple
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W) 


        # class information of student -
        class_student_frame = LabelFrame(Left_frame,bd= 2 ,relief=RIDGE,text="CLASS STUDENT INFORMATION",font=('Consolas',12,'bold'))
        class_student_frame.place(x=5,y=255,width=720,height=295)
        
        # student id 
        studentid_label = Label(class_student_frame,text="STUDENT ID",font=('Consolas',12,'bold'),bg='green')
        studentid_label.grid(row=0,column=0,padx=10,sticky=W) 
        studentid_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=('Consolas',12,'bold'))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W) 

        # student name 
        studentname_label = Label(class_student_frame,text="STUDENT NAME",font=('Consolas',12,'bold'),bg='green')
        studentname_label.grid(row=1,column=0,padx=10,sticky=W) 
        studentname_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=('Consolas',12,'bold'))
        studentname_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # roll no. - 
        rollno_label = Label(class_student_frame,text="ROLL NO.",font=('Consolas',12,'bold'),bg='green')
        rollno_label.grid(row=2,column=0,padx=10,sticky=W) 
        rollno_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=('Consolas',12,'bold'))
        rollno_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # gender -
        gender_label = Label(class_student_frame,text="GENDER",font=('Consolas',12,'bold'),bg='green')
        gender_label.grid(row=3,column=0,padx=10,sticky=W) 
        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=('Consolas',12,'bold'),state="readonly",width=17) 
        gender_combo['values'] = ('SELECT GENDER','MALE','FEMALE','OTHER')
        gender_combo.current(0) # select 0 index item of above tuple
        gender_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #dob
        dob_label = Label(class_student_frame,text="D.O.B",font=('Consolas',12,'bold'),bg='green')
        dob_label.grid(row=4,column=0,padx=10,sticky=W) 
        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=('Consolas',12,'bold'))
        dob_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #email- 
        email_label = Label(class_student_frame,text="EMAIL ID",font=('Consolas',12,'bold'),bg='green')
        email_label.grid(row=0,column=2,padx=10,sticky=W) 
        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=('Consolas',12,'bold'))
        email_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # phone 
        phoneno_label = Label(class_student_frame,text="PHONE NO.",font=('Consolas',12,'bold'),bg='green')
        phoneno_label.grid(row=1,column=2,padx=10,sticky=W) 
        phoneno_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=('Consolas',12,'bold'))
        phoneno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # address - 
        address_label = Label(class_student_frame,text="ADDRESS",font=('Consolas',12,'bold'),bg='green')
        address_label.grid(row=2,column=2,padx=10,sticky=W) 
        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=('Consolas',12,'bold'))
        address_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # teacher name - 
        teacher_label = Label(class_student_frame,text="TEACHER NAME",font=('Consolas',12,'bold'),bg='green')
        teacher_label.grid(row=3,column=2,padx=10,sticky=W) 
        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=('Consolas',12,'bold'))
        teacher_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text='TAKE PHOTO SAMPLE',value='YES')
        radiobtn1.grid(row=6,column=0)
        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text='NO PHOTO SAMPLE',value='NO')
        radiobtn2.grid(row=6,column=1)

        # button frame 
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=200,width=715,height=35)
        save_btn = Button(btn_frame,text='SAVE',command=self.add_data,width=19,font=('Consolas',12,'bold'),bg='blue',fg='white')
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text='UPDATE',command=self.update_data,width=19,font=('Consolas',12,'bold'),bg='blue',fg='white')
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text='DELETE',command=self.delete_data,width=19,font=('Consolas',12,'bold'),bg='blue',fg='white')
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text='RESET',command=self.reset_data,width=19,font=('Consolas',12,'bold'),bg='blue',fg='white')
        reset_btn.grid(row=0,column=3)

        btn_frame1 = Frame(class_student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn = Button(btn_frame1,text='TAKE PHOTO SAMPLE',command=self.generate_dataset,width=80,font=('Consolas',12,'bold'),bg='blue',fg='white')
        take_photo_btn.grid(row=0,column=0)



        # right label frame
        Right_frame = LabelFrame(main_frame,bd= 2 ,relief=RIDGE,text="STUDENT DETAILS",font=('Consolas',12,'bold'))
        Right_frame.place(x=760,y=1,width=735,height=580)
        
        img_right = Image.open(r"Images\bg4.jpg") # r is used to make backward slash as forward
        img_right = img_right.resize((720,180),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        t_lbl = Label(Right_frame,image=self.photoimg_right)
        t_lbl.place(x=5,y=0,width=720,height=180)

        # searching system 
        search_frame = LabelFrame(Right_frame,bd= 2 ,relief=RIDGE,text="SEARCH SYSTEM",font=('Consolas',12,'bold'))
        search_frame.place(x=5,y=150,width=720,height=70)
        search_label = Label(search_frame,text="SEARCH BY",font=('Consolas',12,'bold'),bg='red',fg='white')
        search_label.grid(row=0,column=0,padx=10,sticky=W)
        self.search_var=StringVar()
        search_combo = ttk.Combobox(search_frame,textvariable=self.search_var,font=('Consolas',12,'bold'),state="readonly") 
        search_combo['values'] = ('SELECT','ROLL_NO','PHONE')
        search_combo.current(0) # select 0 index item of above tuple
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W) 
    
        self.txt_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.txt_search,width=15,font=('Consolas',12,'bold'))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        search_btn = Button(search_frame,command=self.search,text='SEARCH',width=12,font=('Consolas',12,'bold'),bg='blue',fg='white')
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn = Button(search_frame,command=self.fetch_data,text='SHOW ALL',width=12,font=('Consolas',12,'bold'),bg='blue',fg='white')
        showAll_btn.grid(row=0,column=4,padx=4)

        # table frame 

        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=5,y=220,width=720,height=330)

        # scroll bar -- 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame,column=('DEPARTMENT','COURSE','YEAR','SEMESTER','STUDENT_ID','NAME','ROLL_NO','GENDER','DOB','EMAIL','PHONE','ADDRESS','TEACHER','PHOTO'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('DEPARTMENT',text="DEPARTMENT")
        self.student_table.heading('COURSE',text="COURSE")
        self.student_table.heading('YEAR',text="YEAR")
        self.student_table.heading('SEMESTER',text="SEMESTER")
        self.student_table.heading('STUDENT_ID',text="STUDENT_ID")
        self.student_table.heading('NAME',text="NAME")
        self.student_table.heading('ROLL_NO',text="ROLL_NO")
        self.student_table.heading('GENDER',text="GENDER")
        self.student_table.heading('DOB',text="DOB")
        self.student_table.heading('EMAIL',text="EMAIL")
        self.student_table.heading('PHONE',text="PHONE")
        self.student_table.heading('ADDRESS',text="ADDRESS")
        self.student_table.heading('TEACHER',text="TEACHER")
        self.student_table.heading('PHOTO',text="PHOTO_SAMPLE")
        self.student_table['show']='headings'

        self.student_table.column('DEPARTMENT',width=100)
        self.student_table.column('COURSE',width=200)
        self.student_table.column('YEAR',width=100)
        self.student_table.column('SEMESTER',width=100)
        self.student_table.column('STUDENT_ID',width=100)
        self.student_table.column('NAME',width=100)
        self.student_table.column('ROLL_NO',width=100)
        self.student_table.column('GENDER',width=70)
        self.student_table.column('DOB',width=100)
        self.student_table.column('EMAIL',width=200)
        self.student_table.column('PHONE',width=90)
        self.student_table.column('ADDRESS',width=100)
        self.student_table.column('TEACHER',width=100)
        self.student_table.column('PHOTO',width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # function declaration ------

    def add_data(self):
        if self.var_dep.get()=="SELECT DEPARTMENT" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("ERROR",'All Feilds Are Required',parent=self.root)
        else:

            try:
                save = messagebox.askyesno("SAVE", "Do You want to Save this student details", parent=self.root)
                if save:   
                    conn = mysql.connector.connect(host='localhost',username ='',password='',database='face_recognition')
                    my_cursor = conn.cursor()
                    my_cursor.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        # self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),

                        ))
                else:
                    if save==False:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Student detail has been added successfully',parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f'Due to :{str(es)}',parent=self.root)
        
    # fetch data -- right window ke student table ke column me sql se data lekr show krne  ka function

    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost',username ='',password='',database='face_recognition')
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT *FROM STUDENT")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    # get cursor- entry box me sare detail aa jaye  

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content['values']
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_teacher.set(data[12]),
        self.var_radio1.set(data[13])

    # update function 
    def update_data(self):
            if self.var_dep.get() == "SELECT DEPARTMENT" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                messagebox.showerror("ERROR", 'All fields are required', parent=self.root)
            else:
                try:
                    Update = messagebox.askyesno("UPDATE", "Do You want to update this student details", parent=self.root)
                    if Update:
                        conn = mysql.connector.connect(host='localhost', username="", password='',
                                                database='face_recognition')
                        my_cursor = conn.cursor()
                        my_cursor.execute(
                        "UPDATE STUDENT SET DEPARTMENT=%s, COURSE=%s, YEAR=%s, SEMESTER=%s,NAME=%s,ROLL_NO=%s, GENDER=%s, DOB=%s, EMAIL=%s, PHONE=%s, ADDRESS=%s, TEACHER=%s, PHOTO_SAMPLE=%s where STUDENT_ID=%s",
                        (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),self.var_std_name.get(),
                        self.var_roll.get(), self.var_gender.get(),
                        self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(),
                        self.var_teacher.get(), self.var_radio1.get(),self.var_std_id.get()))
                    else:
                        if Update == False:
                            return
                    messagebox.showinfo("Success", "Updated Successfully", parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    # delete function 

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete","Do You want to delete this student details",parent =self.root)
                if delete:
                    conn = mysql.connector.connect(host='localhost', username='', password='',
                                                database='face_recognition')
                    my_cursor = conn.cursor()
                    sql = "delete from student where STUDENT_ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if delete==False:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Student Detail Has Been Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                    
    # reset function
    def reset_data(self):
        self.var_dep.set("SELECT DEPARTMENT")
        self.var_course.set("SELECT COURSE")
        self.var_year.set("SELECT YEAR")
        self.var_semester.set("SELECT SEMESTER")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_gender.set("SELECT GENDER")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")    
        self.var_radio1.set("") 
    
    
    # generate data set  take photo sample
    def generate_dataset(self):
        if self.var_dep.get() == "SELECT DEPARTMENT" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                messagebox.showerror("ERROR", 'All fields are required', parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='', password='',
                                        database='face_recognition')
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT *FROM STUDENT")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id=id+1
                my_cursor.execute(

                    "UPDATE STUDENT SET DEPARTMENT=%s, COURSE=%s, YEAR=%s, SEMESTER=%s,NAME=%s,ROLL_NO=%s, GENDER=%s, DOB=%s, EMAIL=%s, PHONE=%s, ADDRESS=%s, TEACHER=%s, PHOTO_SAMPLE=%s WHERE STUDENT_ID=%s",
                    (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),self.var_std_name.get(),
                    self.var_roll.get(), self.var_gender.get(),
                    self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(),
                    self.var_teacher.get(), self.var_radio1.get(),self.var_std_id.get()
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # load predefine data on face frontals from opencv
                face_classifier =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor = 1.3
                    # minimum neighbour = 5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id = img_id +1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==200:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Completed !!",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # search 
    def search(self):
        conn = mysql.connector.connect(host='localhost', username='', password='',
                                        database='face_recognition')
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM STUDENT where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get()) + "%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in rows:
                self.student_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    
    #exit function 
    def exit_gui(self):     
        self.root.destroy()







if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()