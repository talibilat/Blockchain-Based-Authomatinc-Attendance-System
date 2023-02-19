BLOCKENDACNE
============================================================================================
Folder BLOCKENDANCE <br>


1. UI_Images - It contains the images of the UI.

2. attendance.py - it takes the csv file and update the attendance on on the database and displays on the UI as well.

3. clf.xml - trained classifier file

4. collectdata.py - file for collecting the data only

5. dashboard.py - It is a dashboard the user get after logging in.

6. databaseTest.py - Helps to test the connection with the database.

7. evaluation.ipynb - evaluation of LBPH classifier

8. face_recognition.py - file resposible for face detection and fetching the data from database and storing in a .csv file as well as in the database

9. haarcascade_frontalface_default.xml - Used by HAAR cascade to detect face

10. Login_Page.py - Login page for admins.

11. marked_attendance.csv - attendance is stored in this file

12. register.py- Registeration page for Admins

13. student_details.py - file responsible for taking photo samples and details of the student.

14. training.py - File responsible for the data training.

Folder Node - This file consist of web3 server which will integrate the application with the blockchain.

Folder SmartContract - This contains the smartcontract which will later deploy on the blockchain

=====================================================================================================

Flow of the Blockendance Applicataion

register.py > Login_page.py > dashboard.py > student_details.py > training.py > face_recognition.py > attendance.py > Node > SmartContract