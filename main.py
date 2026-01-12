from tkinter import *
from PIL import Image, ImageTk
from student import Student 
import os
from train import Traindata
from face_recognition import FaceRecognition
from attendance import Attendance
import sys

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # Load the background image
        self.bg_image_path = "Assets/background_image.png"  # Path to your background image
        self.bg_img = Image.open(self.bg_image_path)

        # Create label to hold the background image
        self.bg_label = Label(self.root)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Call the resize function when the window size changes
        self.root.bind("<Configure>", self.resize_background)

        # Load button images
        self.button_images = []
        for i in range(6):
            img_path = f"Assets/button_{i+1}.png"  # Replace with your button image paths
            img = Image.open(img_path)
            resized_img = img.resize((270, 160))  # Adjust button size as needed
            self.button_images.append(ImageTk.PhotoImage(resized_img))

        # Create and place buttons in a grid layout (2 rows, 3 buttons per row)
        self.buttons = []
        for i in range(6):
            if i == 0:
                command = self.student_details  # First button for student details
            elif i==1:
                command=self.face_recog
            elif i==2:
                command=self.attendance
            elif i==3:
                command=self.train_data
            elif i == 4:
                command = self.open_image  
            elif i==5:
                command=self.logout
            else:
                command = None 

            button = Button(self.root, image=self.button_images[i], bd=0, highlightthickness=0, relief="flat", command=command)
            button.place(x=300 + (i % 3) * 330, y=370 + (i // 3) * 200)  # Adjust positions accordingly
            
            # Set the background color to match the window's background color or any specific color
            button.config(bg="#DCDCDC")  # Set this to the desired background color, e.g., light gray
            button.config(cursor="hand2")
            self.buttons.append(button)


    def resize_background(self, event):
        # Get the new size of the window
        new_width = event.width
        new_height = event.height

        # Resize the background image to fit the window
        resized_img = self.bg_img.resize((new_width, new_height))
        self.bg_photo = ImageTk.PhotoImage(resized_img)

        # Update the label with the new image
        self.bg_label.config(image=self.bg_photo)
        self.bg_label.image = self.bg_photo  # Prevent garbage collection
    
    def open_image(self):
        os.startfile("Data")


    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Traindata(self.new_window)

    def face_recog(self):
        self.new_window=Toplevel(self.root)
        self.app=FaceRecognition(self.new_window)
    
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def logout(self):
        self.root.destroy()
        from login import Login
        login_window = Tk()
        login_obj = Login(login_window)
        login_window.mainloop()
        sys.exit() 
        


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
