from tkinter import*
from tkinter import ttk, Tk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
from tkinter import messagebox


face_model = cv2.CascadeClassifier(r'C:\Users\talib\OneDrive\Desktop\Dissertation\21-22_CE901-SL_talib_mohammed\BLOCKANDANCE\haarcascade_frontalface_default.xml')
def crop_face(image):
    # Comverting the image to Greyscale
    grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    face = face_model.detectMultiScale(grey,1.3,5)
    for (x,y,w,h) in face:
        cropped_image=image[y:y+h,x:x+w]
        return cropped_image

registration_number = input('Registration number')
capture=cv2.VideoCapture(0)
image_id = 0
while True:
    back,image_frame=capture.read()
    print(image_frame)
    if crop_face(image_frame) is not None:
        image_id+=1
        face=cv2.resize(crop_face(image_frame),(400,400))
        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        data_image ="BLOCKANDANCE//Ev//" + str(registration_number) + "_" + str(image_id) + ".png"
        cv2.imwrite(data_image, face)
        cv2.putText(face,str(image_id),(50,50),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)        
        cv2.imshow("Capture Images",face)

    if cv2.waitKey(1)==13 or int(image_id)==50:
        break
capture.release()
cv2.destroyAllWindows()
