from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from Login_Page import Login_page

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1440x900+0+0")

# ===================================================== V A R I A B L E S ==============================================
        self.var_first_name=StringVar()
        self.var_last_name=StringVar()
        self.var_contact_number=StringVar()
        self.var_username=StringVar()
        self.var_password=StringVar()
        self.var_confirm_password=StringVar()

# ============================================================ U I =====================================================

        #======== BACKGROUND =============
        self.background=ImageTk.PhotoImage(file=r"UI_Images\regui.jpg")
        label_background=Label(self.root,image=self.background)
        label_background.place(x=0,y=0, relwidth=1,relheight=1)

        #====== REGISTRATION FRAME ===========
        frame= Frame(self.root,bg="white")
        frame.place(x=320,y=80,width=900,height=580)
        
        label_registration = Label(frame,text="Registration",font=("times new roman",30,"bold"),bg='white')
        label_registration.place(x=325,y=130)

        #====== FIRST NAME ===========
        first_name = Label(frame,text="First Name:",font=("times new roman",15,"bold"),bg='white')
        first_name.place(x=100,y=200)
        self.fname=ttk.Entry(frame,textvariable=self.var_first_name ,font=("times new roman",15,"bold"))
        self.fname.place(x=103,y=225,width=270)


        #====== LAST NAME ===========
        last_name = Label(frame,text="Last Name:",font=("times new roman",15,"bold"),bg='white')
        last_name.place(x=100,y=270)
        self.lname=ttk.Entry(frame,textvariable=self.var_last_name,font=("times new roman",15,"bold"))
        self.lname.place(x=103,y=295,width=270)


        #====== CONTACT NUMBER ===========
        contact_number = Label(frame,text="Contact No:",font=("times new roman",15,"bold"),bg='white')
        contact_number.place(x=530,y=200)
        self.cnumber=ttk.Entry(frame,textvariable=self.var_contact_number,font=("times new roman",15,"bold"))
        self.cnumber.place(x=533,y=225,width=270)


        #====== USERNAME ===========
        username = Label(frame,text="Username:",font=("times new roman",15,"bold"),bg='white')
        username.place(x=530,y=270)
        self.text_username=ttk.Entry(frame,textvariable=self.var_username,font=("times new roman",15,"bold"))
        self.text_username.place(x=533,y=295,width=270)


        #====== PASSWORD ===========
        password = Label(frame,text="Password:",font=("times new roman",15,"bold"),bg='white')
        password.place(x=100,y=350)
        self.text_password=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15,"bold"))
        self.text_password.place(x=103,y=375,width=270)


        #====== CONFIRM PASSWORD ===========
        confirm_password = Label(frame,text=" Confirm Password:",font=("times new roman",15,"bold"),bg='white')
        confirm_password.place(x=530,y=350)
        self.text_confirm_password=ttk.Entry(frame,textvariable=self.var_confirm_password,font=("times new roman",15,"bold"))
        self.text_confirm_password.place(x=533,y=375,width=270)

        #====== REGISTER BUTTON ===========
        burron_register=Button(frame,command=self.registration,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,bg='#002B53', fg='white',activeforeground="white",activebackground="#007ACC")
        burron_register.place(x=300,y=450,width=270,height=35)

        button_login=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,bg='#002B53', fg='#fff',activeforeground="white",activebackground="#007ACC")
        button_login.place(x=300,y=490,width=270,height=35)



    def registration(self):
        if (self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_contact_number.get()=="" or self.var_username.get()=="" or self.var_password.get()=="" or self.var_confirm_password.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.var_password.get() != self.var_confirm_password.get()):
            messagebox.showerror("Error","Please make sure your paswords in the above fields are same")
        else:
            try:
                conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = "585786", database = 'blockandance')
                curs = conn.cursor()
                curs.execute("select * from users where username=%s",(self.var_username.get(),))
                row=curs.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another username")
                else:
                    curs.execute("insert into users values(%s,%s,%s,%s,%s)",(
                    self.var_first_name.get(),
                    self.var_last_name.get(),
                    self.var_contact_number.get(),
                    self.var_username.get(),
                    self.var_password.get()
                    ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    def login(self):
        self.new_window = Toplevel(self.root)
        self.app = Login_page(self.new_window)

if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()