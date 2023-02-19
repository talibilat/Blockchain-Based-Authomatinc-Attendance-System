from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import numpy as np
from tkinter import messagebox
import cv2
import os

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1440x980+0+0")                                                                                                  
        self.root.title("Training the data  - BLOCKANDANCE")       


        ui_image = Image.open(r'C:\Users\talib\OneDrive\Desktop\Dissertation\21-22_CE901-SL_talib_mohammed\BLOCKANDANCE\UI_Images\train.jpg')       
        ui_image = ui_image.resize((1440,980), Image.ANTIALIAS)
        self.ui_image = ImageTk.PhotoImage(ui_image)
        first_label = Label(self.root, image = self.ui_image)
        first_label.place(x=0,y=0)                                                                                              


        std_img_btn=Image.open(r"C:\Users\talib\OneDrive\Desktop\Dissertation\Python-FYP-Face-Recognition-Attendence-System-master\Images_GUI\t_btn1.png")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(image=self.std_img1,command=self.train_classifier,cursor="hand2")
        std_b1.place(x=630,y=217,width=180,height=180)

        std_b1_1 = Button(text="Train Dataset",command=self.train_classifier,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=630,y=400,width=180,height=45)


    def train_classifier(self):
        data_dir=(r"C:\Users\talib\OneDrive\Desktop\Dissertation\21-22_CE901-SL_talib_mohammed\BLOCKANDANCE\data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('_')[0])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("BLOCKANDANCE//clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Success","Training Dataset Complated!",parent=self.root)



if __name__ == '__main__':
    root = Tk()
    obj = Train(root)
    root.mainloop()