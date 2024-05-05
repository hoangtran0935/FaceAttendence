from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

#from train import Train
from FaceAttendance import facerecognitionsystem
from attendance import Attendance
from developer import Developer
import os
from tkinter import filedialog as fd
from helpsupport import Helpsupport
from student import Student
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:/Users/Dell.MM/hoang/face_recognition_attendance_system/FRAS/Images_GUI/banner.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"C:/Users/Dell.MM/hoang/face_recognition_attendance_system/FRAS/Images_GUI/bg3.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Face Recognition based Attendance System",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"C:/Users/Dell.MM/hoang/face_recognition_attendance_system/FRAS/Images_GUI/std1.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=150,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Add Students",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=150,y=380,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"C:/Users/Dell.MM/hoang/face_recognition_attendance_system/FRAS/Images_GUI/det1.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=360,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.face_rec,text="Mark Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=360,y=380,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"C:/Users/Dell.MM/hoang/face_recognition_attendance_system/FRAS/Images_GUI/att.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.atndd,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=780,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.atndd,text="Show Atnd",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=780,y=380,width=180,height=45)

        dev_img_btn=Image.open(r"C:/Users/Dell.MM/hoang/face_recognition_attendance_system/FRAS/Images_GUI/dev.jpg")
        dev_img_btn=dev_img_btn.resize((180,180),Image.ANTIALIAS)
        self.dev_img1=ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(bg_img,command=self.developr,image=self.dev_img1,cursor="hand2",)
        dev_b1.place(x=570,y=200,width=180,height=180)

        dev_b1_1 = Button(bg_img,command=self.developr,text="Developers",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        dev_b1_1.place(x=570,y=380,width=180,height=45)

        # exit   button 8
        exi_img_btn=Image.open(r"C:/Users/Dell.MM/hoang/face_recognition_attendance_system/FRAS/Images_GUI/exi.jpg")
        exi_img_btn=exi_img_btn.resize((180,180),Image.ANTIALIAS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.Close,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=990,y=200,width=180,height=180)

        exi_b1_1 = Button(bg_img,command=self.Close,text="Exit",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=990,y=380,width=180,height=45)

# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data_img")
# ==================Functions Buttons=====================
    def atndd(self):
        os.startfile("C:/Users/Dell.MM/hoang/face_recognition_attendance_system/FRAS/Attendance")
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=facerecognitionsystem(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def helpSupport(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)

    def Close(self):
        root.destroy()
    
    





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
