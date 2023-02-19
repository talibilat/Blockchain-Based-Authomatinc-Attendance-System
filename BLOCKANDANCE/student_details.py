from tkinter import*
from tkinter import ttk, Tk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student_Details:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1440x900+0+0")                                                                                                 
        self.root.title("Student Details - BLOCKANDANCE")   

#================================================================== V A R I A B L E S ===================================================================
        self.var_name= StringVar()
        self.var_prid= StringVar()
        self.var_registration_number= StringVar()
        self.var_department= StringVar()
        self.var_course= StringVar()
        self.var_year= StringVar()
        self.var_term= StringVar()
        self.var_gender= StringVar()
        self.var_dob= StringVar()
        self.var_email= StringVar()
        self.var_phone_number= StringVar()
        self.var_address= StringVar()
        self.var_radio1 = StringVar()

#==================================================================  U I  ===============================================================================
        # Header
        header = Image.open(r'C:\Users\talib\OneDrive\Desktop\Dissertation\21-22_CE901-SL_talib_mohammed\BLOCKANDANCE\UI_Images\background_student_details.png')       
        self.ui_image = ImageTk.PhotoImage(header)
        first_label = Label(self.root, image = self.ui_image)
        first_label.place(x=0,y=0)

        # Background Image
        background_image=Image.open(r"C:\Users\talib\OneDrive\Desktop\Dissertation\21-22_CE901-SL_talib_mohammed\BLOCKANDANCE\UI_Images\Silberrad_student_centre.jpg")
        background_image=background_image.resize((1440,670),Image.ANTIALIAS)
        self.photobackground_image=ImageTk.PhotoImage(background_image)
        background_image_label = Label(self.root,image=self.photobackground_image)
        background_image_label.place(x=0,y=226)

        # Frame over background Image
        main_frame = Frame(background_image_label, bd = 2)
        main_frame.place(x=5,y=5, width= 1430, height= 660)


        ### Right Label Frame
        right_frame = LabelFrame(main_frame, relief=RAISED , bd = 2, text = 'Search Results')
        right_frame.place(x=715,y=5,width=705, height=645)

        # Searching System in Right Label Frame 
        search_frame = LabelFrame(right_frame, bd = 2, relief = RAISED, text = "Filter", fg="black")
        search_frame.place(x=10,y=5,width=680,height=80)

        # Search
        search_label = Label(search_frame, text = "Search :", font = ("Times New Roman" , 12 , "bold"), fg="black")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()

        # Combo Box for Search 
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_searchTX, width=15, font=("Times New Roman",12,"bold"),state="readonly")
        search_combo["values"] = ("Select","Roll Number", "Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=15, sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=25,font=("Times New Roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5, pady=5, sticky=W)

        search_btn=Button(search_frame, text="Search",width=10,font=("Times New Roman",12,"bold"),fg="white",bg="black")
        search_btn.grid(row=0,column=3,padx=5, pady=10, sticky=W)

        showAll_btn=Button(search_frame,text="Show All",width=10,font=("Times New Roman",12,"bold"),fg="white",bg="black")
        showAll_btn.grid(row=0,column=4,padx=5, pady=10, sticky=W)

        ## Table Frame
        table_frame = Frame(main_frame, relief=RIDGE , bd = 2)
        table_frame.place(x=725,y=120,width=685, height=520)

        scrollbar_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        scrollbar_y = ttk.Scrollbar(table_frame, orient = VERTICAL)
        self.student_details = ttk.Treeview(table_frame, columns= ( 'Registration', 'Name', 'PRID','Department', 'Course' , 'Year', 'Term', 'Gender', 'DOB', 'Email', 'Phone', 'Address', 'Photo'),xscrollcommand= scrollbar_x.set, yscrollcommand= scrollbar_y.set)
        scrollbar_x.pack(side = BOTTOM, fill= X)
        scrollbar_x.config(command=self.student_details.xview)
        scrollbar_y.pack(side = RIGHT, fill= Y)
        scrollbar_y.config(command=self.student_details.yview)

        #Heading of the Tables
        self.student_details.heading('PRID', text = 'PRID')
        self.student_details.column('PRID', width=75)
        self.student_details.heading('Name', text = 'Name')
        self.student_details.column('Name', width=75)
        self.student_details.heading('Registration', text = 'Registration')
        self.student_details.column('Registration', width=150)        
        self.student_details.heading('Department', text = 'Department')
        self.student_details.column('Department', width=125)
        self.student_details.heading('Course', text = 'Course')
        self.student_details.column('Course', width=150)
        self.student_details.heading('Year', text = 'Year')
        self.student_details.column('Year', width=100)
        self.student_details.heading('Term', text = 'Term')
        self.student_details.column('Term', width=100)
        self.student_details.heading('Gender', text = 'Gender')
        self.student_details.column('Gender', width=100)
        self.student_details.heading('DOB', text = 'DOB')
        self.student_details.column('DOB', width=100)
        self.student_details.heading('Email', text = 'Email')
        self.student_details.column('Email', width=100)
        self.student_details.heading('Phone', text = 'Phone')
        self.student_details.column('Phone', width=100)
        self.student_details.heading('Address', text = 'Address')
        self.student_details.column('Address', width=100)
        self.student_details.heading('Photo', text = 'Photo')
        self.student_details.column('Photo', width=100)
        self.student_details['show'] = 'headings'

        self.student_details.pack(fill = BOTH, expand=1)
        self.student_details.bind('<ButtonRelease>',self.data_fill)
        self.data_fetch()
        


        

        ### Left Label Frame
        left_frame = LabelFrame(main_frame, relief=RAISED , bd = 2, text = 'Student Details')
        left_frame.place(x=5,y=5,width=705, height=645)

        # First Image in the Frame
        frame_image=Image.open(r"C:\Users\talib\OneDrive\Desktop\Dissertation\21-22_CE901-SL_talib_mohammed\BLOCKANDANCE\UI_Images\UniEssexSil.png")
        frame_image=frame_image.resize((690,100),Image.ANTIALIAS)
        self.photoframe_image=ImageTk.PhotoImage(frame_image)
        frame_image_label = Label(self.root,image=self.photoframe_image)
        frame_image_label.place(x=20,y=257)

        ## Sub-Left Frame
        sub_left_label = LabelFrame(main_frame, relief=RAISED , bd = 2, text = 'Course Details')
        sub_left_label.place(x=10,y=125,width=695, height=200)

        ## Label and Combobox in subleft frame
        # Department
        label_department = Label(sub_left_label, text = 'Department', font = ('Times New Roman', 12, 'bold'))
        label_department.grid(row=0,column=0, padx=5)

        combobox_department = ttk.Combobox(sub_left_label, textvariable= self.var_department, state='readonly')
        combobox_department['values'] = ('Select your Department', 'Computer Science', 'Psychology', 'Mathematics', 'Arts and Humanity', 'Language and Linguistics', 'History', 'Management')
        combobox_department.current(0)
        combobox_department.grid(row=0,column=1, padx=5, pady=10)

        # Course
        label_course = Label(sub_left_label, text = 'Course', font = ('Times New Roman', 12, 'bold'))
        label_course.grid(row=1,column=0, padx=5)
        combobox_course = ttk.Combobox(sub_left_label, textvariable = self.var_course , state='readonly')
        combobox_course['values'] = ('Select your Course', 'Artificial Intelligence', 'Psychology', 'Data Science', 'Arts and Humanity', 'Language and Linguistics', 'History', 'MBA')
        combobox_course.current(0)
        combobox_course.grid(row=1,column=1, padx=5, pady=10)

        # Year
        label_year = Label(sub_left_label, text = 'Course Year', font = ('Times New Roman', 12, 'bold'))
        label_year.grid(row=2,column=0, padx=5)

        combobox_year = ttk.Combobox(sub_left_label, textvariable = self.var_year, state='readonly')
        combobox_year['values'] = ('Select your Year', '2018-2019', '2019-2020', '2020-2021', '2021-2022', '2022-2023')
        combobox_year.current(0)
        combobox_year.grid(row=2,column=1, padx=5, pady=10)

        # Semester/Term
        label_term = Label(sub_left_label, text = 'Term', font = ('Times New Roman', 12, 'bold'))
        label_term.grid(row=3,column=0, padx=5)
        combobox_term = ttk.Combobox(sub_left_label, textvariable = self.var_term, state='readonly')
        combobox_term['values'] = ('Select your Term', 'First', 'Second', 'Third')
        combobox_term.current(0)
        combobox_term.grid(row=3,column=1, padx=5, pady=10)

        ## Sub Left Frame 2
        sub_left_label2 = LabelFrame(main_frame, relief=RAISED , bd = 2, text = 'Student Information')
        sub_left_label2.place(x=10,y=330,width=695, height=200)

        # PRID
        label_registration_number = Label(sub_left_label2 ,text = 'Registration Number : ', font = ('Times New Roman', 13, 'bold'))
        label_registration_number.grid(row=0,column=0, padx=15)
        registration_number = Entry(sub_left_label2, textvariable = self.var_registration_number, width = 22)
        registration_number.grid(row=0, column=1, padx = 20, pady = 10)

        # Name
        label_name = Label(sub_left_label2, text = 'Student Name : ', font = ('Times New Roman', 13, 'bold'))
        label_name.grid(row=0,column=2, padx=15)
        name = Entry(sub_left_label2, textvariable = self.var_name , width = 22)
        name.grid(row=0, column=3, padx = 20, pady = 10)

        # Registration Number
        label_prid = Label(sub_left_label2, text = 'PRID : ', font = ('Times New Roman', 13, 'bold'))
        label_prid.grid(row=1,column=0, padx=15)
        prid = Entry(sub_left_label2, textvariable = self.var_prid , width = 22)
        prid.grid(row=1, column=1, padx = 20, pady = 10)

        # Gender
        label_gender = Label(sub_left_label2, text = 'Gender : ', font = ('Times New Roman', 13, 'bold'))
        label_gender.grid(row=1,column=2, padx=15)
        combobox_gender = ttk.Combobox(sub_left_label2, textvariable= self.var_gender, state='readonly', width = 19)
        combobox_gender['values'] = ('Select your Gender', 'Male', 'Female', 'Others' )
        combobox_gender.current(0)
        combobox_gender.grid(row=1,column=3, padx=20, pady=10)

        # DOB
        label_dob = Label(sub_left_label2, text = 'DOB : ', font = ('Times New Roman', 13, 'bold'))
        label_dob.grid(row=2,column=0, padx=15)
        dob = Entry(sub_left_label2, textvariable = self.var_dob , width = 22)
        dob.grid(row=2, column=1, padx = 20, pady = 10)

        # Email Address
        label_email = Label(sub_left_label2, text = 'E-Mail : ', font = ('Times New Roman', 13, 'bold'))
        label_email.grid(row=2,column=2, padx=15)
        email = Entry(sub_left_label2, textvariable = self.var_email , width = 22)
        email.grid(row=2, column=3, padx = 20, pady = 10)

        # Phone_Number
        label_phone_number = Label(sub_left_label2 ,text = 'Phone Number : ', font = ('Times New Roman', 13, 'bold'))
        label_phone_number.grid(row=3,column=0, padx=15)
        phone_number = Entry(sub_left_label2, textvariable = self.var_phone_number,  width = 22)
        phone_number.grid(row=3, column=1, padx = 20, pady = 10)

        # Address
        label_address = Label(sub_left_label2, text = 'Address : ', font = ('Times New Roman', 13, 'bold'))
        label_address.grid(row=3,column=2, padx=15)
        address = Entry(sub_left_label2, width = 22, textvariable = self.var_address)
        address.grid(row=3, column=3, padx = 20, pady = 10)


        ## Radio Button
        radio_take_picture = ttk.Radiobutton(sub_left_label2, variable= self.var_radio1,  text= 'Take Photo Sample', value = 'Yes')
        radio_take_picture.grid(row=5,column=0)
        radio_nosample = ttk.Radiobutton(sub_left_label2, variable= self.var_radio1 , text= 'No Photo Sample', value = 'No')
        radio_nosample.grid(row=5,column=1 )  

        ## Sub Left Frame 3
        sub_left_label3 = LabelFrame(main_frame, relief=RAISED , bd = 2)
        sub_left_label3.place(x=10,y=545,width=695, height=100)      

        sub_left_label4 = LabelFrame(main_frame, relief=RAISED , bd = 2)
        sub_left_label4.place(x=10,y=595, width=695, height=50) 

        # Buttons
        button_save = Button(sub_left_label3, text = 'Save', command = self.data_entry , width = 12,  font = ('Times New Roman', 15, 'bold'), bg = 'Black', fg = 'white' )
        button_save.grid(row=0, column=0, padx = 10, pady= 5)

        button_delete = Button(sub_left_label3, text = 'Delete', command = self.data_delete, width = 12,  font = ('Times New Roman', 15, 'bold'), bg = 'Black', fg = 'white' )
        button_delete.grid(row=0, column=1, padx = 10, pady= 5)

        button_update = Button(sub_left_label3, command=self.data_update , text = 'Update', width = 12,  font = ('Times New Roman', 15, 'bold'), bg = 'Black', fg = 'white' )
        button_update.grid(row=0, column=2, padx = 10, pady= 5)

        button_reset = Button(sub_left_label3, text = 'Reset', width = 12, command = self.data_reset, font = ('Times New Roman', 15, 'bold'), bg = 'Black', fg = 'white' )
        button_reset.grid(row=0, column=3, padx = 10, pady= 5)

        button_take_picture = Button(sub_left_label4, command= self.data_with_picture, text = 'New Photo Sample', width = 20,  font = ('Times New Roman', 15, 'bold'), bg = 'Black', fg = 'white' )
        button_take_picture.grid(row=1, column=0, padx = 45, pady = 5)

        button_update_photo = Button(sub_left_label4, command= self.update_picture, text = 'Update Photo Sample', width = 20,  font = ('Times New Roman', 15, 'bold'), bg = 'Black', fg = 'white' )
        button_update_photo.grid(row=1, column=1, padx = 45, pady = 5)


#================================================================= F U N C T I O N S ==========================================================


#==================== S A V I N G   T H E   D A T A ====================
    def data_entry(self):
        if self.var_department.get() == 'Select Your Department' or self.var_course.get() == '' or self.var_prid.get() == '':
            messagebox.showerror("Error", 'Please fill all the fields', parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = "585786", database = 'blockandance')
                curs = conn.cursor()
                curs.execute('insert into studentdetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_registration_number.get(),
                    self.var_name.get(),
                    self.var_prid.get(),
                    self.var_department.get(),
                    self.var_course.get(),            
                    self.var_year.get(),
                    self.var_term.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone_number.get(),
                    self.var_address.get(),
                    self.var_radio1.get(),
                ))
                conn.commit()
                self.data_fetch()
                conn.close()
                messagebox.showinfo('Success', 'Details Saved', parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f'Due To :{str(es)}', parent = self.root )



#==================== F E T C H I N G   T H E   D A T A ====================
    def data_fetch(self):
        conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = "585786", database = 'blockandance')
        curs = conn.cursor()
        curs.execute('select * from studentdetails')
        data = curs.fetchall()

        if len(data) != 0:
            self.student_details.delete(*self.student_details.get_children())
            for i in data:
                self.student_details.insert('',END,values=i)
            conn.commit()
        conn.close()



#==================== F I L L I N G   B A C K   T H E   D A T A ====================
    def data_fill(self, i = ''):
        cursor_focus = self.student_details.focus()
        content = self.student_details.item(cursor_focus)
        data = content["values"]

        self.var_registration_number.set(data[0]),
        self.var_name.set(data[1]),
        self.var_prid.set(data[2]),        
        self.var_department.set(data[3]),
        self.var_course.set(data[4]),
        self.var_year.set(data[5]),
        self.var_term.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone_number.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radio1.set(data[12])


#========================== U P D A T I N G  T H E   D A T A =================================

    def data_update(self):
        if self.var_department.get() == 'Select Your Department' or self.var_course.get() == '' or self.var_prid.get() == '':
            messagebox.showerror("Error", 'Please fill all the fields', parent = self.root)
        else:
            try:
                update = messagebox.askyesno('Update', ' Are you sure? ', parent = self.root)
                if update > 0:
                    conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = "585786", database = 'blockandance')
                    curs = conn.cursor()
                    curs.execute("update studentdetails set  Name=%s, PRID=%s, Department=%s,Course=%s,Year=%s,Term=%s,Gender=%s,DOB=%s,Phone=%s,Email=%s,Address=%s,Photo=%s where Registration=%s",( 
                    self.var_name.get(),
                    self.var_prid.get(),
                    self.var_department.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_term.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_phone_number.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_radio1.get(),
                    self.var_registration_number.get()   
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo('Success', 'Details successfully updated', parent = self.root)
                conn.commit()
                self.data_fetch()
                conn.close()
            except Exception as es:
                print( self.root)
                messagebox.showerror("Error", f'Due To :{str()}', parent = self.root )



#=============================== D E L E T E   D A T A   F R O M   D A T A B A S E ========================================
    def data_delete(self):
        if self.var_prid.get()=="":
            messagebox.showerror("Error","Please enter the PRID!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Are you sure?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='585786',host='localhost',database='blockandance')
                    curr = conn.cursor() 
                    query="delete from studentdetails where PRID=%s"
                    val=(self.var_prid.get(),)
                    curr.execute(query,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.data_fetch()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

#=============================== R E S E T   D A T A ========================================

    def data_reset(self):
        self.var_prid.set(""),
        self.var_name.set(""),
        self.var_department.set("Select Your Department"),
        self.var_course.set("Select "),
        self.var_year.set("Select your Year"),
        self.var_term.set("Select your Semester"),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_phone_number.set(""),
        self.var_address.set(""),
        self.var_registration_number.set(""),
        self.var_email.set(""),
        self.var_radio1.set("")
    
#=============================== T A K I N G    P H O T O   S A M P L E ==========================

    def update_picture(self):
        if self.var_department.get() == 'Select Your Department' or self.var_course.get() == '' or self.var_prid.get() == '':
            messagebox.showerror("Error", 'Please fill all the fields', parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = "585786", database = 'blockandance')
                curs = conn.cursor()
                curs.execute('select * from studentdetails')
                result = curs.fetchall()
                pk = 0
                for i in result:
                    pk = i[0]
                curs.execute("update studentdetails set  Name=%s, PRID=%s, Department=%s,Course=%s,Year=%s,Term=%s,Gender=%s,DOB=%s,Phone=%s,Email=%s,Address=%s,Photo=%s where Registration=%s",( 
                    self.var_name.get(),
                    self.var_prid.get(),
                    self.var_department.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_term.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_phone_number.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_radio1.get(),
                    self.var_registration_number.get()   
                    ))
                conn.commit()
                self.data_fetch()
                self.data_reset()
                conn.close()
                


                face_model = cv2.CascadeClassifier(r'C:\Users\talib\OneDrive\Desktop\Dissertation\21-22_CE901-SL_talib_mohammed\BLOCKANDANCE\haarcascade_frontalface_default.xml')

                def crop_face(image):
                    
                    # Comverting the image to Greyscale
                    grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                    face = face_model.detectMultiScale(grey,1.3,5)
                    for (x,y,w,h) in face:
                        cropped_image=image[y:y+h,x:x+w]
                        return cropped_image
                capture=cv2.VideoCapture(0)
                image_id = 0
                while True:
                    back,image_frame=capture.read()
                    if crop_face(image_frame) is not None:
                        image_id+=1
                        face=cv2.resize(crop_face(image_frame),(400,400))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        data_image ="BLOCKANDANCE//data//" + str(pk) + "_" + str(image_id) + ".png"
                        # plt.imsave(data_image,face)
                        cv2.imwrite(data_image, face)
                        cv2.putText(face,str(image_id),(50,50),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(image_id)==50:
                        break
                capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    def data_with_picture(self):
        if self.var_department.get() == 'Select Your Department' or self.var_course.get() == '' or self.var_prid.get() == '':
            messagebox.showerror("Error", 'Please fill all the fields', parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = "585786", database = 'blockandance')
                curs = conn.cursor()
                curs.execute('insert into studentdetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_registration_number.get(),
                    self.var_name.get(),
                    self.var_prid.get(),
                    self.var_department.get(),
                    self.var_course.get(),            
                    self.var_year.get(),
                    self.var_term.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone_number.get(),
                    self.var_address.get(),
                    self.var_radio1.get(),
                ))
                conn.commit()
                self.data_fetch()
                conn.close()

                face_model = cv2.CascadeClassifier(r'C:\Users\talib\OneDrive\Desktop\Dissertation\21-22_CE901-SL_talib_mohammed\BLOCKANDANCE\haarcascade_frontalface_default.xml')

                def crop_face(image):
                    
                    # Comverting the image to Greyscale
                    grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                    face = face_model.detectMultiScale(grey,1.3,5)
                    for (x,y,w,h) in face:
                        cropped_image=image[y:y+h,x:x+w]
                        return cropped_image
                capture=cv2.VideoCapture(0)
                image_id = 0
                while True:
                    back,image_frame=capture.read()
                    if crop_face(image_frame) is not None:
                        image_id+=1
                        face=cv2.resize(crop_face(image_frame),(400,400))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        data_image ="BLOCKANDANCE//data//" + str(self.var_registration_number.get()) + "_" + str(image_id) + ".png"
                        # plt.imsave(data_image,face)
                        cv2.imwrite(data_image, face)
                        cv2.putText(face,str(image_id),(50,50),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(image_id)==50:
                        break
                capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

if __name__ == '__main__':
    root = Tk()
    obj = Student_Details(root)
    root.mainloop()