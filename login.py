from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import tkinter.font as tkFont
from tkinter import messagebox
from main import Face_Recognition_System  

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("890x514+300+140")
        self.root.title("Login")

        # Load the background image
        self.bg_image_path = "Assets/login.png"  # Path to your background image
        self.bg_img = Image.open(self.bg_image_path)

        # Create label to hold the background image
        self.bg_label = Label(self.root)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Call the resize function when the window size changes
        self.root.bind("<Configure>", self.resize_window)

        self.mainframe_font = tkFont.Font(family="Poppins Bold", size=20) 
        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=410, y=0, width=480, height=514)

        login_label = Label(main_frame, text="Login", font=self.mainframe_font, fg="#060D18")
        login_label.place(x=80, y=100)

        self.subframe_font = tkFont.Font(family="Poppins Medium", size=16)

        username_label = Label(main_frame, text="Username", font=self.subframe_font)
        username_label.place(x=80, y=170)

        self.username_entry = ttk.Entry(main_frame, width=20, font=self.subframe_font)
        self.username_entry.place(x=80, y=200)

        # Create and position the Password label and text field
        password_label = Label(main_frame, text="Password", font=self.subframe_font)
        password_label.place(x=80, y=250)

        # Declare password_entry as an instance variable
        self.password_entry = ttk.Entry(main_frame, width=20, font=self.subframe_font, show="*")
        self.password_entry.place(x=80, y=280)

        button_image_path = "Assets/loginbtn.png"  # Path to your image
        button_img = Image.open(button_image_path)
        button_img = button_img.resize((120, 40))  # Resize image if needed
        self.button_photo = ImageTk.PhotoImage(button_img)

        # Create and position the Image Button
        image_button = Button(main_frame, image=self.button_photo, command=self.login, borderwidth=0, relief="flat")
        image_button.place(x=140, y=340)

        self.eye_open_path = "Assets/openeye.png"  # Path to your open eye image
        self.eye_closed_path = "Assets/closedeye.png"  # Path to your closed eye image

        # Open the eye images and resize them
        self.eye_open_img = Image.open(self.eye_open_path)
        self.eye_open_img = self.eye_open_img.resize((15, 15))
        self.eye_open_photo = ImageTk.PhotoImage(self.eye_open_img)

        self.eye_closed_img = Image.open(self.eye_closed_path)
        self.eye_closed_img = self.eye_closed_img.resize((15, 15))
        self.eye_closed_photo = ImageTk.PhotoImage(self.eye_closed_img)

        # Create and position the eye toggle button
        self.eye_button = Button(main_frame, image=self.eye_closed_photo, borderwidth=0, relief="flat", command=self.toggle_password)
        self.eye_button.place(x=300, y=287)

    def login(self):
        valid_username = "admin"
        valid_password = "123456"

        username = self.username_entry.get()
        password = self.password_entry.get()

        # Validate the username and password
        if username == valid_username and password == valid_password:
            self.open_main_window()  # Proceed to main.py window
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def open_main_window(self):
        self.root.destroy()  # Close the login window
        new_root = Tk()  # Create a new Tk instance
        face_recog_obj = Face_Recognition_System(new_root)  # Pass new_root as the root for the main window
        new_root.mainloop()  # Start the main window loop

    def toggle_password(self):
        if self.password_entry.cget('show') == "*":
            # Show password
            self.password_entry.config(show="")
            self.eye_button.config(image=self.eye_open_photo)
        else:
            # Hide password
            self.password_entry.config(show="*")
            self.eye_button.config(image=self.eye_closed_photo)

    def resize_window(self, event):
        # Adjust background image size on window resize
        new_width = event.width
        new_height = event.height

        # Resize the background image to fit the window
        resized_img = self.bg_img.resize((new_width, new_height))
        self.bg_photo = ImageTk.PhotoImage(resized_img)

        # Update the label with the new image
        self.bg_label.config(image=self.bg_photo)
        self.bg_label.image = self.bg_photo  # Prevent garbage collection


if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()
