from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog
import mysql.connector

# Declating a global variable for CSV files
mydata=[]


class Attendance:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1440x900+0+0")
        self.root.title("BLOCKANDANCE - Attendance")


# ========================================== D E C L A R I N G    T H E    V A R I A B L E S ==========================================


        self.var_registration_number=StringVar()
        self.var_prid=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance=StringVar()



# ====================================================  U S E R   I N T E R F A C E ====================================================



        # FIRST TOP LABEL
        label_image=Image.open(r"UI_Images\background_student_details.png")
        # label_image=label_image.resize((1440,130),Image.ANTIALIAS)
        self.label_image=ImageTk.PhotoImage(label_image)
        first_label = Label(self.root,image=self.label_image)
        first_label.place(x=0,y=0,width=1440,height=215)

        # BACKGROUND IMAGE
        background_image=Image.open(r"UI_Images\randomtech.jpg")
        background_image=background_image.resize((1440,768),Image.ANTIALIAS)
        self.background_image=ImageTk.PhotoImage(background_image)
        background_image = Label(self.root,image=self.background_image)
        background_image.place(x=0,y=130,width=1440,height=768)
        
        # TITLE
        label_title = Label(background_image,text="Welcome to Attendance Pannel",font=("verdana",30,"bold"),bg="white",fg="#002B53")
        label_title.place(x=0,y=0,width=1440,height=45)


        # C R E A T I N G     T W O     D I F F E R E N T    S E C T I O N S


        # MAIN FRAME
        main_frame = Frame(background_image,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=55,width=1420,height=690)

        # LEFT FRAME 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",11,"bold"),fg="#002B53")
        left_frame.place(x=10,y=10,width=700,height=670)

        # RIGHT FRAME
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance",font=("verdana",11,"bold"),fg="#002B53")
        right_frame.place(x=720,y=10,width=700,height=670)        

        
        # C R E A T I N G    E N T R Y    F I E L D S   F O R   L E F T


        # REGISTRATION NUMBER
        label_registration_number = Label(left_frame,text="Registration Number:",font=("verdana",11,"bold"),fg="#002B53",bg="white")
        label_registration_number.grid(row=0,column=0,padx=5,pady=10,sticky=W)
        entry_registration_number = ttk.Entry(left_frame,textvariable=self.var_registration_number,width=16,font=("verdana",11,"bold"))
        entry_registration_number.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        # PRID
        label_prid = Label(left_frame,text="PRID:",font=("verdana",11,"bold"),fg="#002B53",bg="white")
        label_prid.grid(row=0,column=2,padx=5,pady=15,sticky=W)
        entry_prid = ttk.Entry(left_frame,textvariable=self.var_prid,width=16,font=("verdana",11,"bold"))
        entry_prid.grid(row=0,column=3,padx=5,pady=15,sticky=W)

        # STUDENT NAME
        label_name = Label(left_frame,text="Name:",font=("verdana",11,"bold"),fg="#002B53",bg="white")
        label_name.grid(row=1,column=0,padx=5,pady=15,sticky=W)
        entry_name = ttk.Entry(left_frame,textvariable=self.var_name,width=16,font=("verdana",11,"bold"))
        entry_name.grid(row=1,column=1,padx=5,pady=15,sticky=W)

        # TIME
        label_time = Label(left_frame,text="Time:",font=("verdana",11,"bold"),fg="#002B53",bg="white")
        label_time.grid(row=1,column=2,padx=5,pady=15,sticky=W)
        entry_time = ttk.Entry(left_frame,textvariable=self.var_time,width=16,font=("verdana",11,"bold"))
        entry_time.grid(row=1,column=3,padx=5,pady=15,sticky=W)

        # DATE 
        label_date = Label(left_frame,text="Date:",font=("verdana",11,"bold"),fg="#002B53",bg="white")
        label_date.grid(row=2,column=0,padx=5,pady=15,sticky=W)
        entry_date = ttk.Entry(left_frame,textvariable=self.var_date,width=16,font=("verdana",11,"bold"))
        entry_date.grid(row=2,column=1,padx=5,pady=15,sticky=W)

        # ATTENDANCE
        label_attendance = Label(left_frame,text="Status:",font=("verdana",11,"bold"),fg="#002B53",bg="white")
        label_attendance.grid(row=2,column=2,padx=5,pady=15,sticky=W)
        combobox_attendance=ttk.Combobox(left_frame,textvariable=self.var_attendance,width=14,font=("verdana",11,"bold"),state="readonly")
        combobox_attendance["values"]=("Status","Present","Absent")
        combobox_attendance.current(0)
        combobox_attendance.grid(row=2,column=3,padx=5,pady=15,sticky=W)


        # C R E A T I N G   T A B L E   F O R   D A T A   V I E W


        # FRAME FOR TABLE
        table_frame_left = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        table_frame_left.place(x=10,y=180,width=680,height=410)
        # SCROLLBAR FOR TABLE
        scroll_x = ttk.Scrollbar(table_frame_left,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame_left,orient=VERTICAL)

        # TABLE
        self.table_attendance = ttk.Treeview(table_frame_left,column=('Registration','PRID',"Name","Time","Date",'Attendance'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.table_attendance.xview)
        scroll_y.config(command=self.table_attendance.yview)

        # SETTING UP HEADINGS AND COLUMNS OF THE TABLE
        self.table_attendance.heading('Registration',text="Registration No.")
        self.table_attendance.column('Registration',width=100)
        self.table_attendance.heading('PRID',text="PRID")
        self.table_attendance.column('PRID',width=100)
        self.table_attendance.heading("Name",text="Name")
        self.table_attendance.column("Name",width=100)
        self.table_attendance.heading("Time",text="Time")
        self.table_attendance.column("Time",width=100)
        self.table_attendance.heading("Date",text="Date")
        self.table_attendance.column("Date",width=100)
        self.table_attendance.heading('Attendance',text="Attendance Status")
        self.table_attendance.column('Attendance',width=100)
        self.table_attendance["show"]="headings"
        self.table_attendance.pack(fill=BOTH,expand=1)        
        # self.table_attendance.bind("<ButtonRelease>",self.get_cursor_left)
    

        # B U T T O N S


        # Button Frame
        frame_button = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        frame_button.place(x=10,y=589,width=680,height=50)

        # IMPORT BUTTON
        button_import=Button(frame_button,command=self.import_csv,text="Import CSV",width=14,font=("verdana",10,"bold"),fg="white",bg="#002B53")
        button_import.grid(row=0,column=0,padx=14,pady=8 ,sticky=W)

        # EXPORT BUTTON
        button_export=Button(frame_button,command=self.exportCsv,text="Export CSV",width=14,font=("verdana",10,"bold"),fg="white",bg="#002B53")
        button_export.grid(row=0,column=1,padx=14,pady=8 ,sticky=W)

        # UPDATE BUTTON
        button_update=Button(frame_button,command = self.data_update,text="Update",width=14,font=("verdana",10,"bold"),fg="white",bg="#002B53")
        button_update.grid(row=0,column=2,padx=14,pady=8 ,sticky=W)

        # RESET BUTTON
        button_reset=Button(frame_button,text="Reset",command=self.data_reset,width=14,font=("verdana",10,"bold"),fg="white",bg="#002B53")
        button_reset.grid(row=0,column=3,padx=14,pady=8 ,sticky=W)


        # C R E A T I N G    E N T R Y    F I E L D S   F O R   L E F T


        # TABLE FRAME 
        table_frame_right = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame_right.place(x=10,y=90,width=685,height=530)
        
        # SCROLL BAR
        scroll_x = ttk.Scrollbar(table_frame_right,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame_right,orient=VERTICAL)

        # CREATING TABLE 
        self.attendanceReport = ttk.Treeview(table_frame_right,column=('Registration','PRID',"Name","Time","Date",'Attendance'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        # HEADINGS AND COLUMNS
        self.attendanceReport.heading('Registration',text="Registration Number")
        self.attendanceReport.column('Registration',width=100)        
        self.attendanceReport.heading('PRID',text="PRID")
        self.attendanceReport.column('PRID',width=100)
        self.attendanceReport.heading("Name",text="Name")
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.heading('Attendance',text="Attendance Status")
        self.attendanceReport.column('Attendance',width=100)
        self.attendanceReport["show"]="headings"


        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor_right)
        self.data_fetch()
    # =================================update for mysql button================
    # Update button
        del_btn=Button(right_frame,command=self.data_update,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="#002B53")
        del_btn.grid(row=0,column=1,padx=6,pady=10,sticky=W)
    #Update button
        del_btn=Button(right_frame,command=self.data_delete,text="Delete",width=12,font=("verdana",12,"bold"),fg="white",bg="#002B53")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)




# ========================================== D E C L A R I N G    T H E    F U N C T I O N S ==========================================
    
    
    def data_fetch(self):
        conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = "585786", database = 'blockandance')
        mycursor = conn.cursor()

        mycursor.execute("select * from attendance")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("",END,values=i)
            conn.commit()
        conn.close()

    


    
    def data_update(self):
        if self.var_registration_number.get()=="" or self.var_prid.get=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attendance.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update?",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host = 'localhost', user = 'root', password = "585786", database = 'blockandance')
                    mycursor = conn.cursor()
                    mycursor.execute("update attendance set registration=%s, prid=%s, name=%s, time=%s, date=%s, attendance=%s where registration=%s",( 
                    self.var_registration_number.get(),
                    self.var_prid.get(),
                    self.var_name.get(),
                    self.var_time.get(),
                    self.var_date.get(),
                    self.var_attendance.get(),
                    self.var_registration_number.get()  
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.data_fetch()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    
    def data_delete(self):
        if self.var_registration_number.get()=="":
            messagebox.showerror("Error","Registration Number Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Are you sure you want to delete the entry?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = "585786", database = 'blockandance')
                    mycursor = conn.cursor() 
                    mycursor.execute("delete from attendance where std_id=%s",(self.var_registration_number.get(),))
                else:
                    if not delete:
                        return
                conn.commit()
                self.data_fetch()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  

    def data_reset(self):
        self.var_registration_number.set("")
        self.var_prid.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("Status")

    def data_fetch_for_import(self,rows):
        global mydata
        mydata = rows
        self.attendanceReport.delete(*self.attendanceReport.get_children())
        for i in rows:
            self.attendanceReport.insert("",END,values=i)
            print(i)
        

    def import_csv(self):
        mydata.clear()
        file_location=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(file_location) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.data_fetch_for_import(mydata)
            

    #==================Experot CSV=============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            file_location=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(file_location,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    #=============Cursur Function for CSV========================

    def get_cursor_left(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_registration_number.set(data[0]),
        self.var_prid.set(data[1]),
        self.var_name.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attendance.set(data[5])  

     #=============Cursur Function for mysql========================

    def get_cursor_right(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_registration_number.set(data[0]),
        self.var_prid.set(data[1]),
        self.var_name.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attendance.set(data[5])    
    #=========================================Update CSV============================

    # export upadte
    def action(self):
        if self.var_registration_number.get()=="" or self.var_prid.get=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attendance.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = "585786", database = 'blockandance')
                mycursor = conn.cursor()
                mycursor.execute("insert into attendance values(%s,%s,%s,%s,%s,%s)",(
                self.var_registration_number.get(),
                self.var_prid.get(),
                self.var_name.get(),
                self.var_time.get(),
                self.var_date.get(),
                self.var_attendance.get()
                ))

                conn.commit()
                self.data_fetch()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved in Database!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)







if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()