from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # zero is for starting position
        self.root.title("Attendance Details")
        self.root.wm_iconbitmap("face-scan.ico")

        # variable

        self.var_atten_id = StringVar()
        self.var_name = StringVar()
        self.var_status = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()

        #first image 
        img = Image.open(r"Images\z5.jpg") # r is used to make backward slash as forward
        img = img.resize((800,200),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)
        
        # second image 
        img1 = Image.open(r"Images\z7.png") # r is used to make backward slash as forward
        img1 = img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        s_lbl = Label(self.root,image=self.photoimg1)
        s_lbl.place(x=800,y=0,width=800,height=200)

        # background image ---
        img3 = Image.open(r"Images\bg1.jpg") # r is used to make backward slash as forward
        img3 = img3.resize((1550,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1550,height=710)

        title_lbl = Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font =("Consolas",35,"bold"),bg = "light yellow",fg = "green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #  exit btn 
        b8_1 = Button(title_lbl,text="EXIT",command=self.exit_gui,cursor="hand2",font =("Corbel",9,"bold"),bd=0,relief=RIDGE,fg='white',bg='green',activebackground='black') #cursor for customization
        b8_1.place(x=1330,y=10,width=40,height=20)

        # main frame 
        main_frame = Frame(bg_img,bd = 2 )
        main_frame.place(x=10,y=55,width=1510,height=600)



        #left label frame -
        Left_frame = LabelFrame(main_frame,bd= 2 ,relief=RIDGE,text="ATTENDANCE DETAILS",font=('Consolas',12,'bold'))
        Left_frame.place(x=10,y=10,width=735,height=450)

        img_left = Image.open(r"Images\z4.png") # r is used to make backward slash as forward
        img_left = img_left.resize((720,180),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        t_lbl = Label(Left_frame,image=self.photoimg_left)
        t_lbl.place(x=5,y=0,width=720,height=180)
        
        # left inside frame
        left_inside_frame = Frame(Left_frame,bd = 2,relief=RIDGE,bg='white' )
        left_inside_frame.place(x=5,y=185,width=720,height=240)

        # Roll no 
        attendance_label = Label(left_inside_frame,text="ROLL NO",font=('Consolas',12,'bold'),bg='green')
        attendance_label.grid(row=0,column=0,padx=10,sticky=W) 
        attendance_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=('Consolas',12,'bold'))
        attendance_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W) 

        # name 
        name_label = Label(left_inside_frame,text="NAME",font=('Consolas',12,'bold'),bg='green')
        name_label.grid(row=1,column=0,padx=10,sticky=W) 
        name_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_name,font=('Consolas',12,'bold'))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

       

        # TIME
        time_label = Label(left_inside_frame,text="TIME",font=('Consolas',12,'bold'),bg='green')
        time_label.grid(row=2,column=0,padx=10,sticky=W) 
        time_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_time,font=('Consolas',12,'bold'))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # DATE
        date_label = Label(left_inside_frame,text="DATE",font=('Consolas',12,'bold'),bg='green')
        date_label.grid(row=0,column=2,padx=10,sticky=W) 
        date_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_date,font=('Consolas',12,'bold'))
        date_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

         # attendance
        attendance_label = Label(left_inside_frame,text="ATTENDANCE STATUS",font=('Consolas',12,'bold'),bg='green')
        attendance_label.grid(row=1,column=2,padx=10,sticky=W) 
        self.atten_status = ttk.Combobox(left_inside_frame,textvariable=self.var_status,font=('Consolas',12,'bold'),state="readonly",width=17) 
        self.atten_status['values'] = ('SELECT STATUS','Present','Absent')
        self.atten_status.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        self.atten_status.current(0) # select 0 index item of above tuple
        

       # button frame 
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=200,width=715,height=35)
        import_btn = Button(btn_frame,text='IMPORT DATA',command=self.fetchData,width=15,font=('Consolas',12,'bold'),bg='blue',fg='white')
        import_btn.grid(row=0,column=0)

        export_btn = Button(btn_frame,text='EXPORT CSV',command=self.export_data,width=15,font=('Consolas',12,'bold'),bg='blue',fg='white')
        export_btn.grid(row=0,column=1)

        update_btn = Button(btn_frame,text='UPDATE',command=self.update_data,width=15,font=('Consolas',12,'bold'),bg='blue',fg='white')
        update_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text='RESET',command=self.reset_data,width=15,font=('Consolas',12,'bold'),bg='blue',fg='white')
        reset_btn.grid(row=0,column=3)

        delete_btn = Button(btn_frame,text='DELETE',command=self.deleteData,width=15,font=('Consolas',12,'bold'),bg='blue',fg='white')
        delete_btn.grid(row=0,column=4)






        #right label frame -
        Right_frame = LabelFrame(main_frame,bd= 2 ,relief=RIDGE,text="STUDENT DETAILS",font=('Consolas',12,'bold'))
        Right_frame.place(x=750,y=10,width=735,height=450)

        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=5,y=5,width=720,height=400)


        #scroll bar
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.attendanceReportTable = ttk.Treeview(table_frame,column=('ROLL_NO','NAME','TIME','DATE','STATUS'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.yview)

        self.attendanceReportTable.heading('ROLL_NO',text="ROLL_NO")
        self.attendanceReportTable.heading('NAME',text="NAME")
        self.attendanceReportTable.heading('TIME',text="TIME")
        self.attendanceReportTable.heading('DATE',text="DATE")
        self.attendanceReportTable.heading('STATUS',text="STATUS")
        
        
        self.attendanceReportTable['show']='headings'
        self.attendanceReportTable.column('ROLL_NO',width=100)
        self.attendanceReportTable.column('NAME',width=100)
        self.attendanceReportTable.column('TIME',width=100)
        self.attendanceReportTable.column('DATE',width=100)
        self.attendanceReportTable.column('STATUS',width=100)
        
        
        self.attendanceReportTable.pack(fill=BOTH,expand=1)
        self.attendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

      
    # fetch data
    def fetchData(self):
        conn = mysql.connector.connect(host='localhost',username ='',password='',database='face_recognition')
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT *FROM Attendance")
        colum_nmae = [i[0] for i in my_cursor.description]
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
            for i in data:
                self.attendanceReportTable.insert('',END,values=i)
            conn.commit()
        conn.close()




    # update table
    def update_data(self):
            if self.var_atten_id.get() == "" or self.var_name.get() == "":
                messagebox.showerror("ERROR", 'All fields are required', parent=self.root)
            else:
                try:
                    Update = messagebox.askyesno("UPDATE", "Do You want to update this attendance details", parent=self.root)
                    if Update:
                        conn = mysql.connector.connect(host='localhost', username='', password='',
                                                database='face_recognition')
                        my_cursor = conn.cursor()
                        my_cursor.execute(
                        "UPDATE ATTENDANCE SET NAME=%s, TIME=%s, DATE=%s,STATUS=%s where ROLL_NO=%s",
                        (self.var_name.get(), self.var_time.get(), self.var_date.get(), self.var_status.get()
                         ,self.var_atten_id.get()))
                    else:
                        if Update == False:
                            return
                    messagebox.showinfo("Success", "Updated Successfully", parent=self.root)
                    conn.commit()
                    self.fetchData()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)


    # export data

    def export_data(self):
        # Establish a connection to the MySQL database
        conn = mysql.connector.connect(host='localhost', username='', password='',
                                                database='face_recognition')
        my_cursor = conn.cursor()
        # Execute a SELECT query to fetch the attendance data
        my_cursor.execute("SELECT * FROM attendance")
        # Get the column names
        column_names = [i[0] for i in my_cursor.description]
        # Get the data
        data = my_cursor.fetchall()
        # Close the database connection
        conn.close()
       # Check if there is any data to export
        if not data:
            messagebox.showerror("No Data", "No data found in the database.")
            return
        # Ask the user to provide a filename to save the data
        fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        # Write the data to a CSV file
        with open(fln, mode="w", newline="") as myfile:
            exp_write = csv.writer(myfile, delimiter="|")
            exp_write.writerow(column_names)
            for i in data:
                exp_write.writerow(i)

        messagebox.showinfo("Data Export", "Your data exported to " + os.path.basename(fln) + " successfully")


    # get _cursor
    def get_cursor(self,event=''):
        cursor_row=self.attendanceReportTable.focus()
        content=self.attendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_name.set(rows[1])
        
        self.var_time.set(rows[2])
        self.var_date.set(rows[3])
        self.var_status.set(rows[4])
    

    # reset function
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_name.set("")
        
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("SELECT STATUS")

    # delete function
    def deleteData(self):
        if self.var_atten_id.get()=="":
            messagebox.showerror("Error","Roll no must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Attendance Delete","Do You want to delete this student details",parent =self.root)
                if delete:
                    conn = mysql.connector.connect(host='localhost', username='', password='',
                                                database='face_recognition')
                    my_cursor = conn.cursor()
                    sql = "delete from attendance where ROLL_NO=%s"
                    val=(self.var_atten_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if delete==False:
                        return
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("Delete","Successfully Attendance Details Has Been Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    def exit_gui(self):     
        self.root.destroy()





   

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()