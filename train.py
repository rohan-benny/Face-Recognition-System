from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import os
import numpy as np
from tkinter import messagebox
import cv2
import re  # Import regex for safer ID extraction


class Traindata:
    def __init__(self, root):
        self.root = root
        self.student_table = ttk.Treeview(self.root, columns=(...))
        self.root.geometry("660x504+430+140")
        self.root.title("Train Data")

        # Load background image
        self.bg_image_path = "Assets/background_3.png"
        self.bg_img = Image.open(self.bg_image_path)
        self.bg_label = Label(self.root)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.root.bind("<Configure>", self.resize_window)

        # Load button image
        self.button_image_path = "Assets/trainbtn.png"
        self.button_img = Image.open(self.button_image_path).resize((150, 90))
        self.button_photo = ImageTk.PhotoImage(self.button_img)

        # Create training button
        self.center_button = Button(self.root, image=self.button_photo, bd=0, highlightthickness=0, relief="flat",
                                    command=self.train_classifier)
        self.center_button.place(x=0, y=0)

        self.root.update_idletasks()
        self.place_button_in_center()

    def place_button_in_center(self):
        window_width = self.root.winfo_width()
        button_width = 150
        center_x = (window_width // 2) - (button_width // 2)
        custom_y = 270
        self.center_button.place(x=center_x, y=custom_y)

    def resize_window(self, event):
        new_width, new_height = event.width, event.height
        resized_img = self.bg_img.resize((new_width, new_height))
        self.bg_photo = ImageTk.PhotoImage(resized_img)
        self.bg_label.config(image=self.bg_photo)
        self.bg_label.image = self.bg_photo  # Prevent garbage collection
        self.place_button_in_center()

    def train_classifier(self):
        data_dir = "Data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data directory not found!")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('.jpg', '.png', '.jpeg'))]

        faces, ids = [], []
    
        for image_path in path:
            try:
                # Load the image and convert to grayscale
                img = Image.open(image_path).convert('L')
                img = img.resize((200, 200))  # Standardize image size
                image_np = np.array(img, 'uint8')
            
                # Extract the ID using regex
                match = re.search(r'\.(\d+)\.', os.path.basename(image_path))
                if match:
                    id = int(match.group(1))
                else:
                    print(f"Skipping {image_path} (invalid ID format)")
                    continue  # Skip images without a valid ID
            
                faces.append(image_np)
                ids.append(id)

                # Show image being processed
                cv2.imshow("Training", image_np)
                cv2.waitKey(1)

            except Exception as e:
                print(f"Error processing {image_path}: {str(e)}")
                continue

        if not faces or not ids:
            messagebox.showerror("Error", "No valid training data found.")
            return

        ids = np.array(ids)

        # Initialize and train the recognizer
        clf = cv2.face.LBPHFaceRecognizer_create()  # Use cv2.face.LBPHFaceRecognizer.create() if error occurs
        clf.train(faces, ids)
    
        # Save the trained model
        clf.write("classifier.xml")
    
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset Completed")


if __name__ == "__main__":
    root = Tk()
    obj = Traindata(root)
    root.mainloop()
