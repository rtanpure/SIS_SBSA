from tkinter import *
from tkinter import ttk
import pymysql

# pymysql , mysql.connector, sqlite3

def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()
 
 
class LoginPage:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1350x750+0+0")
        self.win.title("Sainath Bahuuddeshiya Sanstha - Student information System")

        self.title_label = Label(self.win,text="Sainath Bahuuddeshiya Sanstha - Student information System",font=("Arial",30,"bold"),bg="lightgrey",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)

        self.main_frame = Frame(self.win,bg="lightgrey",bd=6,relief=GROOVE)
        self.main_frame.place(x=250,y=150,width = 800 , height=500)

        self.login_lbl = Label(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER,font=('sans-serif',25,'bold'))
        self.login_lbl.pack(side=TOP,fill=X)

        self.entry_frame = LabelFrame(self.main_frame,text="Enter Credential's",bd=6,relief=GROOVE,bg="lightgrey",font=('sans-serif',20,'bold'))
        self.entry_frame.pack(fill=BOTH,expand=TRUE)

        self.entus_lbl = Label(self.entry_frame,text="Enter Username:",bg="lightgrey",font=('sans-serif',18))
        self.entus_lbl.grid(row=0,column=0)

        self.entps_lbl = Label(self.entry_frame,text="Enter Password:",bg="lightgrey",font=('sans-serif',18))
        self.entps_lbl.grid(row=1,column=0)

        #---------------Variables---------------#
        username = StringVar()
        password = StringVar()


        #---------------Variables end---------------#

        self.entus_ent = Entry(self.entry_frame,font=('sans-serif',18),bd=6,textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=20)

        self.entps_ent = Entry(self.entry_frame,font=('sans-serif',18),show="*",bd=6,textvariable=password)
        self.entps_ent.grid(row=1,column=1,padx=2,pady=2)


        #-----------Functions ------------------#
        
        def check_login():
            if username.get() == "Rishabh" and password.get() == "1234":
                self.register_btn.config(state="normal")
                self.fees_btn.config(state="normal")
            else:
                pass # message box


        def reset():
            username.set("")
            password.set("")
            self.register_btn.config(state="disabled")
            self.fees_btn.config(state="disabled")


        def register_sect():
            self.newWindow = Toplevel(self.win)
            self.app = Window2(self.newWindow)


        #-----------Functions end ------------------#



        #--------------Buttons------------------#

        self.button_frame = LabelFrame(self.entry_frame,bg="lightgrey",bd=7,relief=GROOVE)
        self.button_frame.place(x=470,y=0,width=300,height=130)

        self.login_btn = Button(self.button_frame,text="Login",font=("Arial",15),bd=5,width=15,command=check_login)
        self.login_btn.grid(row=0,column=0,padx=50,pady=2)

        self.reset_btn = Button(self.button_frame,text="Reset",font=("Arial",15),bd=5,width=15,command=reset)
        self.reset_btn.grid(row=1,column=0,padx=50,pady=2)


        # -------------button 2 -----------------#

        self.button_frame2 = LabelFrame(self.entry_frame,text="Options",font=("Arial",15),bg="lightgrey",bd=7,relief=GROOVE)
        self.button_frame2.place(x=0,y=150,width=775,height=200)

        
        self.register_btn = Button(self.button_frame2,text="Register",font=("Arial",15),bd=5,width=15,command=register_sect)
        self.register_btn.grid(row=0,column=0,padx=20,pady=20)
        self.register_btn.config(state="disabled")

        self.fees_btn = Button(self.button_frame2,text="Fees Records",font=("Arial",15),bd=5,width=15)
        self.fees_btn.grid(row=0,column=1,padx=20,pady=20)
        self.fees_btn.config(state="disabled")

        


        #--------------Buttons end------------------#




class Window2:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1750x950+0+0")
        self.win.title("Sainath Bahuuddeshiya Sanstha - Student information System")

        self.title_label = Label(self.win,text="Sainath Bahuuddeshiya Sanstha - Student Management System",font=("Arial",30,"bold"),border=12,relief=GROOVE,bg="lightgrey")
        self.title_label.pack(side=TOP,fill=X)

        self.detail_frame = LabelFrame(self.win,text="Enter Details",font=("Arial",25),border=12,relief=GROOVE)
        self.detail_frame.place(x=20,y=90,width=500,height=870)

        self.data_frame = LabelFrame(self.win,bg="lightgrey",relief=GROOVE)
        self.data_frame.place(x=550,y=90,width=1220,height=870)


        #---------------function---------------#
        
        def fetch_data():
            conn = pymysql.connect(host="localhost", user="root", password="",database="sbsa_sis_db")
            curr = conn.cursor()
            curr.execute("SELECT * FROM student_db")
            rows = curr.fetchall()
            if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("",END,values=row)
                conn.commit()
            conn.close()

            

        def fetch_specific():
            conn = pymysql.connect(host="localhost", user="root", password="", database="sbsa_sis_db")
            curr = conn.cursor()
            sql_query = "SELECT * FROM student_db WHERE {} = %s".format(searchin.get())
            curr.execute(sql_query, (searchby.get(),))
            rows = curr.fetchall()  # Changed from fetchmany() to fetchall() to retrieve all matching rows
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", END, values=row)
                conn.commit()
            conn.close()
            

        def add_func():
            conn = pymysql.connect(host="localhost", user="root", password="",database="sbsa_sis_db")
            curr = conn.cursor()
            curr.execute("INSERT INTO student_db VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Register_number.get(),Full_Name.get(),Mobile_Number.get(),Date_Of_Birth.get(),Gender.get(),Email.get(),Address.get(),Course_name.get(),Batch.get(),Enrollment_number.get()))
            conn.commit()
            conn.close()
            fetch_data()

        def get_cursor(event):
            cursor_row = self.student_table.focus()
            content = self.student_table.item(cursor_row)
            row = content['values']
            Register_number.set(row[0])
            Full_Name.set(row[1])
            Mobile_Number.set(row[2])
            Date_Of_Birth.set(row[3])
            Gender.set(row[4])
            Email.set(row[5])
            Address.set(row[6])
            Course_name.set(row[7])
            Batch.set(row[8])
            Enrollment_number.set(row[9])


        def update_func():
            conn = pymysql.connect(host="localhost", user="root", password="",database="sbsa_sis_db")
            curr = conn.cursor()
            curr.execute("UPDATE student_db set Full_Name=%s, Mobile_Number=%s, Date_Of_Birth=%s, Gender=%s, Email=%s, Address=%s, Course_name=%s, Batch=%s, Enrollment_number=%s WHERE Register_number=%s",(Full_Name.get(),Mobile_Number.get(),Date_Of_Birth.get(),Gender.get(),Email.get(),Address.get(),Course_name.get(),Batch.get(),Enrollment_number.get(),Register_number.get()) )
            conn.commit()
            conn.close()
            fetch_data()
            clear()


        def clear():
            Register_number.set("")
            Full_Name.set("")
            Mobile_Number.set("")
            Date_Of_Birth.set("")
            Gender.set("")
            Email.set("")
            Address.set("")
            Course_name.set("")
            Batch.set("")
            Enrollment_number.set("")

        def delete_func():
            conn = pymysql.connect(host="localhost", user="root", password="",database="sbsa_sis_db")
            curr = conn.cursor()
            curr.execute("DELETE FROM student_db WHERE Register_number=%s",(Register_number.get()) )
            conn.commit()
            conn.close()
            fetch_data()
            clear()




        #-------------Variables----------#

        # "Register number","Full Name","Mobile Number","Date Of Birth","Gender","Email","Address","Course name","Batch","Enrollment number"

        Register_number =StringVar()
        Full_Name=StringVar()
        Mobile_Number=StringVar()
        Date_Of_Birth=StringVar()
        Gender=StringVar()
        Email=StringVar()
        Address=StringVar()
        Course_name=StringVar()
        Batch=StringVar()
        Enrollment_number=StringVar()

        searchby = StringVar()
        searchin = StringVar()



        # ------------Entry ------------#

        self.std_name_lbl = Label(self.detail_frame,text="Full Name",font=('Arial',17),bg="lightgrey")
        self.std_name_lbl.grid(row=0,column=0,padx=2,pady=2)
        self.std_name_ent = Entry(self.detail_frame,bd=7,font=('Arial',17),textvariable=Full_Name)
        self.std_name_ent.grid(row=0,column=1,padx=2,pady=2)

        self.std_mob_lbl = Label(self.detail_frame,text="Mobile Number",font=('Arial',17),bg="lightgrey")
        self.std_mob_lbl.grid(row=1,column=0,padx=2,pady=2)
        self.std_mob_ent = Entry(self.detail_frame,bd=7,font=('Arial',17),textvariable=Mobile_Number)
        self.std_mob_ent.grid(row=1,column=1,padx=2,pady=2)

        self.std_dob_lbl = Label(self.detail_frame,text="Date Of Birth",font=('Arial',17),bg="lightgrey")
        self.std_dob_lbl.grid(row=2,column=0,padx=2,pady=2)
        self.std_dob_ent = Entry(self.detail_frame,bd=7,font=('Arial',17),textvariable=Date_Of_Birth)
        self.std_dob_ent.grid(row=2,column=1,padx=2,pady=2)

        self.std_gender_lbl = Label(self.detail_frame,text="Gender",font=('Arial',17),bg="lightgrey")
        self.std_gender_lbl.grid(row=3,column=0,padx=2,pady=2)
        self.std_gender_ent = ttk.Combobox(self.detail_frame,font=('Arial',17),state="readonly",textvariable=Gender)
        self.std_gender_ent['values'] = ("Male" , "Female" , "Others")
        self.std_gender_ent.grid(row=3,column=1,padx=2,pady=2)

        

        self.std_email_lbl = Label(self.detail_frame,text="Email",font=('Arial',17),bg="lightgrey")
        self.std_email_lbl.grid(row=4,column=0,padx=2,pady=2)
        self.std_email_ent = Entry(self.detail_frame,bd=7,font=('Arial',17),textvariable=Email)
        self.std_email_ent.grid(row=4,column=1,padx=2,pady=2)

        self.std_address_lbl = Label(self.detail_frame,text="Address",font=('Arial',17),bg="lightgrey")
        self.std_address_lbl.grid(row=5,column=0,padx=2,pady=2)
        self.std_address_ent = Entry(self.detail_frame,bd=7,font=('Arial',17),textvariable=Address)
        self.std_address_ent.grid(row=5,column=1,padx=2,pady=2)

        self.std_course_lbl = Label(self.detail_frame,text="Course name",font=('Arial',17),bg="lightgrey")
        self.std_course_lbl.grid(row=6,column=0,padx=2,pady=2)
        self.std_course_ent = Entry(self.detail_frame,bd=7,font=('Arial',17),textvariable=Course_name)
        self.std_course_ent.grid(row=6,column=1,padx=2,pady=2)

        self.std_batch_lbl = Label(self.detail_frame,text="Batch",font=('Arial',17),bg="lightgrey",anchor="e")
        self.std_batch_lbl.grid(row=7,column=0,padx=2,pady=2)
        self.std_batch_ent = Entry(self.detail_frame,bd=7,font=('Arial',17),textvariable=Batch)
        self.std_batch_ent.grid(row=7,column=1,padx=2,pady=2)

        self.std_enn_lbl = Label(self.detail_frame,text="Enrollment number",font=('Arial',17),bg="lightgrey",anchor="e")
        self.std_enn_lbl.grid(row=8,column=0,padx=2,pady=2)
        self.std_enn_ent = Entry(self.detail_frame,bd=7,font=('Arial',17),textvariable=Enrollment_number)
        self.std_enn_ent.grid(row=8,column=1,padx=2,pady=2)

        self.std_reg_lbl = Label(self.detail_frame,text="Register number",font=('Arial',17),bg="lightgrey")
        self.std_reg_lbl.grid(row=9,column=0,padx=2,pady=2)
        self.std_reg_ent = Entry(self.detail_frame,bd=7,font=('Arial',17),textvariable=Register_number)
        self.std_reg_ent.grid(row=9,column=1,padx=2,pady=2)


        # ------------Entry end ------------#

        #---------------Buttons1_____________#

        self.btn_frame1 = LabelFrame(self.detail_frame,font=("Arial",15),bg="lightgrey",bd=7,relief=GROOVE)
        self.btn_frame1.place(x=20,y=450,width=450,height=140)

        self.add_btn = Button(self.btn_frame1,bg="lightgrey",font=("Arial",17),text="Add",bd=7,width=15,command=add_func)
        self.add_btn.grid(row=0,column=0,padx=2,pady=2)

        self.update_btn = Button(self.btn_frame1,bg="lightgrey",font=("Arial",17),text="Update",bd=7,width=15,command=update_func)
        self.update_btn.grid(row=0,column=1,padx=2,pady=2)

        self.delete_btn = Button(self.btn_frame1,bg="lightgrey",font=("Arial",17),text="Delete",bd=7,width=15,command=delete_func)
        self.delete_btn.grid(row=1,column=0,padx=2,pady=2)

        self.clear_btn = Button(self.btn_frame1,bg="lightgrey",font=("Arial",17),text="Clear",bd=7,width=15,command=clear)
        self.clear_btn.grid(row=1,column=1,padx=2,pady=2)


        


        #---------------Serach Frame and buttons_____________#

        self.search_frame = LabelFrame(self.data_frame,font=("Arial",15),bg="lightgrey",bd=7,relief=GROOVE)
        self.search_frame.place(x=0,y=0,width=1200,height=70)

        self.searchby_ent = Entry(self.search_frame,bd=7,font=('Arial',17),textvariable=searchby)
        self.searchby_ent.grid(row=0,column=0,padx=2,pady=2)

        self.search_in = ttk.Combobox(self.search_frame,font=("Arial",15),state="readonly",textvariable=searchin)
        self.search_in['values'] = ("Full_Name","Mobile_Number","Enrollment_number","Register_number","Batch","Course_name")
        self.search_in.grid(row=0,column=1,padx=2,pady=2)

        self.search_btn = Button(self.search_frame,bg="lightgrey",font=("Arial",17),text="Search",bd=7,width=15,command=fetch_specific)
        self.search_btn.grid(row=0,column=2,padx=2,pady=2)

        self.showall_btn = Button(self.search_frame,bg="lightgrey",font=("Arial",17),text="Show all",bd=7,width=15,command=fetch_data)
        self.showall_btn.grid(row=0,column=3,padx=2,pady=2)


        #---------------Serach results frame_____________#
        self.main_frame = LabelFrame(self.data_frame,bg="lightgrey",bd=11,relief=GROOVE)
        self.main_frame.place(x=0,y=80,width=1200,height=790)

        y_scroll = Scrollbar(self.main_frame,orient=VERTICAL)
        x_scroll = Scrollbar(self.main_frame,orient=HORIZONTAL)

        self.student_table = ttk.Treeview(self.main_frame,columns=("Register number","Full Name","Mobile Number","Date Of Birth","Gender","Email","Address","Course name","Batch","Enrollment number"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
        self.student_table.pack(fill=BOTH,expand=TRUE)

        y_scroll.config(command=self.student_table.yview)
        x_scroll.config(command=self.student_table.xview)

        y_scroll.pack(side=RIGHT,fill=Y)
        x_scroll.pack(side=BOTTOM,fill=X)

        self.student_table.heading("Register number",text="Register number")
        self.student_table.heading("Full Name",text="Full Name")
        self.student_table.heading("Mobile Number",text="Mobile Number")
        self.student_table.heading("Date Of Birth",text="Date Of Birth")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Course name",text="Course name")
        self.student_table.heading("Batch",text="Batch")
        self.student_table.heading("Enrollment number",text="Enrollment number")

        self.student_table['show'] = 'headings'

        self.student_table.column("Register number",width=100)
        self.student_table.column("Full Name",width=100)
        self.student_table.column("Mobile Number",width=100)
        self.student_table.column("Date Of Birth",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Course name",width=100)
        self.student_table.column("Batch",width=100)
        self.student_table.column("Enrollment number",width=100)

        fetch_data()

        self.student_table.bind("<ButtonRelease-1>",get_cursor)






if __name__ == "__main__":
    main()