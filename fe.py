from tkinter import*  # tkinker is used for GUI
from tkinter import ttk
from PIL import Image,ImageTk #pillow is used for uploading images


class FRAMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition System")
    
        #to upload images
        img=Image.open(r"D:\Images\background.jpg")
        img=img.resize((1920,1080)) #herw ANTIALIAS converts high level imhae into low level
        self.photoimg=ImageTk.PhotoImage(img)
        # ^^ now imgae is set
        
        # now to set background image into window
        bg_img=Label(self.root,image=self.photoimg)
        #now to show this image in window
        bg_img.place(x=0,y=0,width=1920,height=1080)

        title_lbl=Label(bg_img,text="Face Recognition Attendance System",font=("times new roman",35,"bold"),background="white",foreground="red")
        title_lbl.place(x=0,y=0,width=1920,height=60)

 # student button
        std=Image.open(r"D:\Images\student1.jpg")
        std=std.resize((220,220))
        self.photostd=ImageTk.PhotoImage(std)

        #first student button
        b1=Button(bg_img,image=self.photostd,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

    #   b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("time new roman",15,"bold"),bg="White",foreground="red")
    #   b1_1.place(x=200,y=300,width=218,height=22)

# Face Detaction
        img2=Image.open(r"D:\Images\face_detection2.jpg")
        img2=img2.resize((220,220))
        self.photoimg2=ImageTk.PhotoImage(img2)

        #Second Face Detaction Button
        b2=Button(bg_img,image=self.photoimg2,cursor="hand2")
        b2.place(x=500,y=100,width=220,height=220)

    #   b2_1=Label(bg_img,text="Face Detection",cursor="hand2",font=("time new roman",15,"bold"),bg="white",foreground="red")
    #   b2_1.place(x=500,y=299,width=218,height=22)

# Attendance
        img3=Image.open(r"D:\Images\attendance.jpg")
        img3=img3.resize((220,220))
        self.photoimg3=ImageTk.PhotoImage(img3)

        #Second Attendance Button
        b3=Button(bg_img,image=self.photoimg3,cursor="hand2")
        b3.place(x=200,y=400,width=220,height=220)

    #   b3_1=Label(bg_img,text="Attendance",cursor="hand2",font=("time new roman",15,"bold"),bg="white",foreground="red")
    #   b3_1.place(x=200,y=400,width=218,height=22)

# Admin
        img4=Image.open(r"D:\Images\admin.jpg")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)

        #Second Attendance Button
        b4=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b4.place(x=200,y=400,width=220,height=220)

    #   b3_1=Label(bg_img,text="Attendance",cursor="hand2",font=("time new roman",15,"bold"),bg="white",foreground="red")
    #   b3_1.place(x=200,y=400,width=218,height=22)

















if __name__ == "__main__" :
    root=Tk()
    obj=FRAMS(root)
    root.mainloop()

