from tkinter import*
from tkinter import Tk, messagebox
from PIL import Image,ImageTk
import cv2
import mysql.connector
from time import strftime
import datetime
import smtplib
import ssl
from email.message import EmailMessage


class Face_Recognitoin:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1440x900+0+0")                                                                                                 
        self.root.title("Dashboard - Blockandance")  


        self.var_name= StringVar()
        self.var_prid= StringVar()
        self.var_registration_number= StringVar()
        self.var_department= StringVar()
        self.var_course= StringVar()
        self.var_year= StringVar()
        self.var_term= StringVar()
        self.var_email= StringVar()

# =======================================================  U I  ============================================================

        header = Image.open(r'C:\Users\talib\OneDrive\Desktop\Dissertation\21-22_CE901-SL_talib_mohammed\BLOCKANDANCE\UI_Images\background_student_details.png')       
        self.ui_image = ImageTk.PhotoImage(header)
        first_label = Label(self.root, image = self.ui_image)
        first_label.place(x=0,y=0)

        footer = Image.open(r'C:\Users\talib\OneDrive\Desktop\Dissertation\21-22_CE901-SL_talib_mohammed\BLOCKANDANCE\UI_Images\randomtech.jpg')       
        self.ui_image2 = ImageTk.PhotoImage(footer)
        second_label = Label(self.root, image = self.ui_image2)
        second_label.place(x=0,y=150)

        label = Label(second_label,text="Mark your Attendance Below",font=("verdana",30,"bold"),bg="white",fg="navyblue") 
        label.place(x=0,y=0,width=1440,height=45)

# ====================================================  B U T T O N  ============================================================


        std_img_btn=Image.open(r"C:\Users\talib\OneDrive\Desktop\Dissertation\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\f_det.jpg") 
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn) 
        std_b1 = Button(second_label,command=self.recognise_face,image=self.std_img1,cursor="hand2") 
        std_b1.place(x=650,y=270,width=180,height=180) 
        std_b1_1 = Button(second_label,command=self.recognise_face,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue") 
        std_b1_1.place(x=650,y=450,width=180,height=45)


# ====================================================  F U N C T I O N S  ========================================================



    def attendance(self,name,fata,department,prid):
                with open(r'C:\Users\talib\OneDrive\Desktop\Dissertation\21-22_CE901-SL_talib_mohammed\BLOCKANDANCE\maked_attendance.csv','r+',newline='\n') as file:
                    data = file.readlines()
                    list_name = []
                    for line in data:
                        i = line.split((','))
                        list_name.append(i[0])
                    if (str(fata) not in list_name): 
                        dt = datetime.datetime.now()
                        date = dt.strftime('%d/%m/%Y')
                        time = dt.strftime('%H:%M:%S')
                        present = 'Present'
                        file.writelines(f'\n{fata},{name},{prid},{department},{time},{date},{present}')

                        email_sender = 'talibilat2019@gmail.com'
                        email_password = 'fuumlsvsmgicuaau'
                        email_receiver = self.var_email

                        subject = 'Attendance'
                        body = 'Your attendance has been marked University of Essex'

                        em = EmailMessage()
                        em['From'] = email_sender
                        em['To'] = email_receiver
                        em['Subject'] = subject
                        em.set_content(body)

                        context = ssl.create_default_context()

                        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                            smtp.login(email_sender, email_password)
                            smtp.sendmail(email_sender,email_receiver,em.as_string())
                        try:
                            conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = "585786", database = 'blockandance')
                            curs = conn.cursor()
                            curs.execute('insert into attendance values(%s,%s,%s,%s,%s,%s,%s)',(
                                fata,
                                name,
                                prid,
                                department,
                                time,            
                                date,
                                present
                            ))
                            conn.commit()
                            self.data_fetch()
                            conn.close()
                            messagebox.showinfo('Success', 'Details Saved', parent = self.root)
                        except Exception as es:
                            messagebox.showerror("Error", f'Due To :{str(es)}', parent = self.root )





    def recognise_face(self):
        def square(image, classifier, scale, Neighbour, color,text, clf):
            grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(grey_image, scale, Neighbour)

            coordinates = []

            for (a,b,c,d) in features:
                cv2.rectangle(image,(a,b),(a+c,b+d),(0,0,255),5)
                id,predict = clf.predict(grey_image[b:b+d, a:a+c])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = "585786", database = 'blockandance')
                curs = conn.cursor()
                curs.execute('select Name from studentdetails where Registration ='+ str(id))
                self.var_name = curs.fetchone()[0]

                curs.execute('select Registration from studentdetails where Registration ='+str(id))
                self.var_registration_number = curs.fetchone()[0]

                curs.execute('select Department from studentdetails where Registration ='+str(id))
                self.var_department = curs.fetchone()[0]

                curs.execute('select PRID from studentdetails where Registration ='+str(id))
                self.var_prid = curs.fetchone()[0]

                curs.execute('select Email from studentdetails where Registration ='+str(id))
                self.var_email = curs.fetchone()[0]

                if confidence > 75:
                    cv2.putText(image, f'Name:{self.var_name}',(a,b-30),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(128,128,128),thickness=1)
                    self.attendance(self.var_name,self.var_registration_number,self.var_department,self.var_prid)

                else:
                    cv2.rectangle(image, (a,b),(a+c,b+d),(0,0,255),5)                
                    cv2.putText(image, f'Unknown Face',(a,b-55),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(128,128,128),thickness=1)
                coordinates = [a,b,c,d]

            return coordinates
        




        def recognition(image,clf,face_cascade):
            coordination = square(image,face_cascade,1.1,10,(255,25,255),'Face',clf)
            return image
        
        face_cascade = cv2.CascadeClassifier(r"C:\Users\talib\anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r'C:\Users\talib\OneDrive\Desktop\Dissertation\21-22_CE901-SL_talib_mohammed\BLOCKANDANCE\clf.xml')

        cideo_cap = cv2.VideoCapture(0)

        while True:
           
            ret,image = cideo_cap.read()
            # cv2.imwrite('temp.png',image)
            # img=cv2.imread('data//2_1.png')
            image = recognition(image,clf,face_cascade)
            cv2.imshow('Welcome',image)

            if cv2.waitKey(1)==13:
                break
        cideo_cap.release()
        cv2.destroyAllWindows()


                    

#   img=cv2.imread(r'C:\Users\talib\OneDrive\Desktop\Screenshot 2022-11-16 183036.png')
#         print(img.shape)

#         image = recognition(img,clf,face_cascade)
#         print(image.shape)
#         cv2.imshow('Welcome',image)
#         cv2.waitKey(0)


if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognitoin(root)
    root.mainloop()