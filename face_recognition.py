from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import os
import csv
import numpy as np
from time import strftime
from datetime import datetime
from tkinter import messagebox
from firebaseconfig import db
import cv2
import threading

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.student_table = ttk.Treeview(self.root, columns=(...))
        self.root.geometry("780x600+410+140")
        self.root.title("Train Data")

        # Load the background image
        self.bg_image_path = "Assets/background_4.png"  # Path to your background image
        self.bg_img = Image.open(self.bg_image_path)
        
        # Create label to hold the background image
        self.bg_label = Label(self.root)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Call the resize function when the window size changes
        self.root.bind("<Configure>", self.resize_window)

        # Load the button image
        self.button_image_path = "Assets/detectbtn.png"
        self.button_img = Image.open(self.button_image_path).resize((150, 90))
        self.button_photo = ImageTk.PhotoImage(self.button_img)

        # Create a button with the image
        self.center_button = Button(self.root, image=self.button_photo, bd=0, highlightthickness=0, relief="flat", command=self.face_recogn)
        self.center_button.place(x=0, y=0)

        # Update the window and place button in the center after window load
        self.root.update_idletasks()
        self.place_button_in_center()

    def place_button_in_center(self):
        window_width = self.root.winfo_width()
        button_width = 150
        center_x = (window_width // 2) - (button_width // 2)
        custom_y = 360
        self.center_button.place(x=center_x, y=custom_y)

    def resize_window(self, event):
        new_width, new_height = event.width, event.height
        resized_img = self.bg_img.resize((new_width, new_height))
        self.bg_photo = ImageTk.PhotoImage(resized_img)
        self.bg_label.config(image=self.bg_photo)
        self.bg_label.image = self.bg_photo
        self.place_button_in_center()

    def mark_attendance(self, i, r, n, d):
         file_path = "Attendance.csv"

         now = datetime.now()
         d1 = now.strftime("%d/%m/%Y")
         dateString = now.strftime("%H:%M:%S")

    # Read existing data
         with open(file_path, "r", newline="\n") as f:
             reader = csv.reader(f)
             name_list = [row[0] for row in reader]

    # Append new entry if not already present
         if str(i) not in name_list:  # Ensure ID is treated as a string
             with open(file_path, "a", newline="") as f:  # Use "a" mode to append without blank lines
                 writer = csv.writer(f)
                 writer.writerow([i, r, n, d, dateString, d1, "Present"])

    def face_recogn(self):
        self.recognition_thread = threading.Thread(target=self.run_face_recognition, daemon=True)
        self.recognition_thread.start()

    def run_face_recognition(self):
        recognized_students = set()
        
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray_image = cv2.equalizeHist(gray_image) 
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)
            
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                face = gray_image[y:y+h, x:x+w]
                id, predict = clf.predict(face)
                confidence = int((100 * (1 - predict / 300)))
                                
                if confidence > 80:
                    student_ref = db.collection('Students').document(str(id))
                    student_data = student_ref.get().to_dict()
                    
                    if student_data:
                        i, n, r, d = id, student_data.get("Name"), student_data.get("RollNo"), student_data.get("Department")
                        cv2.putText(img, f"Id:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)
                        cv2.putText(img, f"RollNo:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)
                        cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)
                        cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)
                        
                        if i not in recognized_students:
                            self.mark_attendance(i, r, n, d)
                            recognized_students.add(i)
                else:
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)
        
        if not video_cap.isOpened():
            print("Error: Could not open video stream.")
            return

        while True:
            ret, img = video_cap.read()
            if ret:
                img = cv2.resize(img, (800, 600))
                img = cv2.flip(img, 1)
                img = draw_boundary(img, faceCascade, 1.1, 10, clf)
                cv2.imshow("Welcome to face recognition", img)
            else:
                print("Failed to capture image")
            
            key = cv2.waitKey(1) & 0xFF
            if key == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()