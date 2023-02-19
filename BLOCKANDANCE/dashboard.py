from tkinter import*
from tkinter import Tk
from PIL import Image,ImageTk
from student_details import Student_Details
from training import Train
from face_recognition import Face_Recognitoin
 
class Dashboard:
    def __init__(self,root):
        self.dash=dash
        self.dash.geometry("1440x900+0+0")                                                                                                 
        self.dash.title("Dashboard - Blockandance")                                                                                                    


        # Background Image
        background_image = Image.open(r'C:\Users\talib\OneDrive\Desktop\Dissertation\21-22_CE901-SL_talib_mohammed\BLOCKANDANCE\UI_Images\dashboard.png')       
        background_image = background_image.resize((1440,900), Image.ANTIALIAS)
        self.dash_ui_image = ImageTk.PhotoImage(background_image)
        first_label = Label(self.dash, image = self.dash_ui_image)
        first_label.place(x=0,y=0)




#========================================================= BUTTONS ===========================================================


        button_image = Image.open(r"C:\Users\talib\OneDrive\Desktop\Dissertation\21-22_CE901-SL_talib_mohammed\BLOCKANDANCE\UI_Images\dashboard_button.png")
        self.button_detail = ImageTk.PhotoImage(button_image)

        # Details Button
        b01 = Button(self.dash,cursor='hand2',text='Student Details', command=self.details , bg='black', fg = 'white', activebackground='purple', height=2, width=33)
        b01.place(x=46,y=649)

        # Face Recognition Button
        b02 = Button(self.dash, cursor='hand2',text='Face Recognition', command=self.face_recog, bg='black', fg = 'white', activebackground='purple', height=2, width=33)
        b02.place(x=416,y=649)

        # Attendance Button
        b03 = Button(cursor='hand2',text='Attendance', bg='black', fg = 'white', activebackground='purple', height=2, width=33)
        b03.place(x=784,y=649)

        # Train Button
        b04 = Button(cursor='hand2',text='Train', bg='black', command=self.train,  fg = 'white', activebackground='purple', height=2, width=33)
        b04.place(x=1154,y=649)

#========================================================= FUNCTIONS FOR BUTTONS ===========================================================

    def details(self):
        self.new_window = Toplevel(self.dash)
        self.app = Student_Details(self.new_window)


    def train(self):
        self.new_window = Toplevel(self.dash)
        self.app = Train(self.new_window)

    def face_recog(self):
        self.new_window = Toplevel(self.dash)
        self.app = Face_Recognitoin(self.new_window)

    # def details(self):
    #     self.new_window = Toplevel(self.dash)
    #     self.app = Student_Details(self.new_window)


if __name__ == '__main__':
    dash = Tk()
    obj = Dashboard(dash)
    dash.mainloop()
    

    