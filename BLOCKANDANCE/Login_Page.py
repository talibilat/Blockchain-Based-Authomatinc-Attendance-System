from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
from dashboard import Dashboard
import mysql.connector


class Login_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1440x980+0+0")                                                                                                  
        self.root.title("BLOCKANDANCE")    


        self.username_text=StringVar()
        self.password_text=StringVar()

        # University Logo
        img_unilogo = Image.open(r'C:\Users\talib\OneDrive\Desktop\Dissertation\21-22_CE901-SL_talib_mohammed\BLOCKANDANCE\UI_Images\background.png')       
        img_unilogo = img_unilogo.resize((1440,900), Image.ANTIALIAS)
        self.ui_image = ImageTk.PhotoImage(img_unilogo)
        first_label = Label(self.root, image = self.ui_image)
        first_label.place(x=0,y=0)

        # Login Label
        login_label = Label(text="Login",font=("Aksara Bali Galang",20),fg="#002B53",bg="#689099")
        login_label.place(x=669,y=494)

        # Username Label and Text Box
        username_label = Label(text="Username",font=("Aksara Bali Galang",15),fg="#002B53",bg="#689099")
        username_label.place(x=475,y=551)
        self.username_text=ttk.Entry(textvariable=StringVar(),font=("Aksara Bali Galang",15,"bold"))
        self.username_text.place(x=475,y=582,width=524,height=67)

        # Password Label and Text Box
        password_label = Label(text="Password",font=("Aksara Bali Galang",15),fg="#002B53",bg="#689099")
        password_label.place(x=475,y=652.92)
        self.password_text=ttk.Entry(textvariable=StringVar(),show='*',font=("Aksara Bali Galang",15,"bold"))
        self.password_text.place(x=475,y=685,width=524,height=67)

        # Login Button
        login_button=Button(self.root, text="Login",font=("Aksara Bali Galang",15,"bold"),bd=0,command=self.login,relief=RIDGE,fg="#002B53",bg="white",activeforeground="white",activebackground="black")
        login_button.place(x=475,y=788,width=524,height=67)



    # def login(self):
    #     self.dashboard=Toplevel(self.root)
    #     self.app=Dashboard(self.dashboard)


    def login(self):
        if (self.username_text.get()=="" or self.password_text.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.username_text.get()=="admin" and self.password_text.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = "585786", database = 'blockandance')
            mycursor = conn.cursor()
            mycursor.execute("select * from users where username=%s and password=%s",(
                self.username_text.get(),
                self.password_text.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("YesNo","Access only Admin")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Dashboard(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()


if __name__ == '__main__':
    root = Tk()
    obj = Login_page(root)
    root.mainloop()