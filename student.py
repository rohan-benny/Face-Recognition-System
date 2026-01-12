from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from tkinter import messagebox
from firebaseconfig import db
import cv2
import os
import re


class Student:
    def __init__(self, root):
        self.root = root
        self.student_table = ttk.Treeview(self.root, columns=(...))
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")
        self.fetch_data()

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        # Load the background image
        self.bg_image_path = "Assets/background_2.png"  # Path to your background image
        self.bg_img = Image.open(self.bg_image_path)

        # Create label to hold the background image
        self.bg_label = Label(self.root)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Call the resize function when the window size changes
        self.root.bind("<Configure>", self.resize_background)

        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=5,y=210,width=1880,height=620)

        # Left Frame
        self.leftframe_font = tkFont.Font(family="Poppins SemiBold", size=14) 
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=self.leftframe_font,labelanchor='n')
        left_frame.place(x=5,y=0,width=720,height=586)
        
        # Current course
        self.leftframe_font1 = tkFont.Font(family="Poppins SemiBold", size=12)
        current_course=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=self.leftframe_font1,labelanchor='n')
        current_course.place(x=5,y=5,width=700,height=150)
        
        # Department
        dep_label=Label(current_course,text="Department",font=self.leftframe_font1)
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course,textvariable=self.var_dep,font=self.leftframe_font1,width=20,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","Commerce","Management","Humanities")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course
        course_label=Label(current_course,text="Course",font=self.leftframe_font1)
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course,textvariable=self.var_course,font=self.leftframe_font1,width=20,state="readonly")
        course_combo["values"]=("Select Course","BCA","Bcom","BBA","MCA","Msc.Cs","Msc.Ds")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        Year_label=Label(current_course,text="Year",font=self.leftframe_font1)
        Year_label.grid(row=1,column=0,padx=10,sticky=W)

        Year_combo=ttk.Combobox(current_course,textvariable=self.var_year,font=self.leftframe_font1,width=20,state="readonly")
        Year_combo["values"]=("Select Year","2022-23","2023-24","2024-25","2025-26")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        semester_label=Label(current_course,text="Semester",font=self.leftframe_font1)
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course,textvariable=self.var_semester,font=self.leftframe_font1,width=20,state="readonly")
        semester_combo["values"]=("Select Semester","Sem-1","sem-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class student information
        class_student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=self.leftframe_font1,labelanchor='n')
        class_student_frame.place(x=5,y=160,width=700,height=380)

        student_id_label=Label(class_student_frame,text="Student ID",font=self.leftframe_font1)
        student_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        StudentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=self.leftframe_font1)
        StudentId_entry.grid(row=0,column=1,padx=7,pady=5,sticky=W)


        studentName_label=Label(class_student_frame,text="Student Name",font=self.leftframe_font1)
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        StudentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=self.leftframe_font1)
        StudentName_entry.grid(row=0,column=3,padx=7,pady=5,sticky=W)


        class_div_label=Label(class_student_frame,text="Section",font=self.leftframe_font1)
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=self.leftframe_font1)
        class_div_entry.grid(row=1,column=1,padx=7,pady=5,sticky=W)


        rollno_label=Label(class_student_frame,text="Roll No",font=self.leftframe_font1)
        rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=self.leftframe_font1)
        rollno_entry.grid(row=1,column=3,padx=7,pady=5,sticky=W)


        gender_label=Label(class_student_frame,text="Gender",font=self.leftframe_font1)
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=self.leftframe_font1,width=17,state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)


        dob_label=Label(class_student_frame,text="DOB",font=self.leftframe_font1)
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=self.leftframe_font1)
        dob_entry.grid(row=2,column=3,padx=7,pady=5,sticky=W)

        email_label=Label(class_student_frame,text="Email",font=self.leftframe_font1)
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=self.leftframe_font1)
        email_entry.grid(row=3,column=1,padx=7,pady=5,sticky=W)

        phoneno_label=Label(class_student_frame,text="Mobile No",font=self.leftframe_font1)
        phoneno_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phoneno_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=self.leftframe_font1,validate="key", validatecommand=(self.root.register(self.validate_mobile_number), "%P"))
        phoneno_entry.grid(row=3,column=3,padx=7,pady=5,sticky=W)

        address_label=Label(class_student_frame,text="Address",font=self.leftframe_font1)
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=self.leftframe_font1)
        address_entry.grid(row=4,column=1,padx=7,pady=5,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo",value="yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo",value="no")
        radiobtn2.grid(row=6,column=1)

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=260,width=696,height=40)
        take_photo_btn=Button(btn_frame,text="Take Photo",command=self.generate_dataset,font=self.leftframe_font1,bg="#060D18",fg="#F8BA41",width=36)
        take_photo_btn.grid(row=0,column=0)
        update_photo_btn=Button(btn_frame,text="Update Photo",font=self.leftframe_font1,bg="#060D18",fg="#F8BA41",width=36)
        update_photo_btn.grid(row=0,column=1,padx=2)
        

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=298,width=696,height=40)
        save_btn=Button(btn_frame1,text="Save",command=self.add_data,font=self.leftframe_font1,bg="#060D18",fg="#F8BA41",width=17)
        save_btn.grid(row=0,column=0)
        update_btn=Button(btn_frame1,text="Update",command=self.update_data,font=self.leftframe_font1,bg="#060D18",fg="#F8BA41",width=17)
        update_btn.grid(row=0,column=1,padx=1)
        delete_btn=Button(btn_frame1,text="Delete",command=self.delete_data,font=self.leftframe_font1,bg="#060D18",fg="#F8BA41",width=17)
        delete_btn.grid(row=0,column=2,padx=1)
        reset_btn=Button(btn_frame1,text="Reset",command=self.reset_data,font=self.leftframe_font1,bg="#060D18",fg="#F8BA41",width=17)
        reset_btn.grid(row=0,column=3,padx=1)
 

        # Right Frame 
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=self.leftframe_font,labelanchor='n')
        right_frame.place(x=740,y=0,width=766,height=586)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=2,y=2,width=756,height=485)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","section","rollno","gender","dob","email","address","mobile no","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("section",text="Section")
        self.student_table.heading("rollno",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("mobile no",text="Mobile No")
        self.student_table.heading("photo",text="Photo Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("section",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("mobile no",width=100)
        self.student_table.column("photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()




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

    def validate_mobile_number(self, P):
        # Allow only digits and limit input to 10 characters
        if P.isdigit() and len(P) <= 10:
            return True
        return False

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            # Mobile number validation: Ensure it has exactly 10 digits
            mobile_number = self.var_phone.get()
            if len(mobile_number) != 10:
                messagebox.showerror("Error", "Invalid mobile number. It should be exactly 10 digits.", parent=self.root)
                return
        
            # Email validation: Basic format check (e.g., example@domain.com)
            email = self.var_email.get()
            if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                messagebox.showerror("Error", "Invalid email address.", parent=self.root)
                return

            try:
                # Data to be saved into Firestore
                student_data = {
                    "Department": self.var_dep.get(),
                    "Course": self.var_course.get(),
                    "Year": self.var_year.get(),
                    "Semester": self.var_semester.get(),
                    "StudentID": int(self.var_std_id.get()),
                    "Name": self.var_std_name.get(),
                    "Section": self.var_div.get(),
                    "RollNo": self.var_roll.get(),
                    "Gender": self.var_gender.get(),
                    "DOB": self.var_dob.get(),
                    "Email": self.var_email.get(),
                    "MobileNo": self.var_phone.get(),
                    "Address": self.var_address.get(),
                    "PhotoStatus": self.var_radio1.get() 
                }

                # Save the data to Firestore under a "Students" collection
                db.collection('Students').document(self.var_std_id.get()).set(student_data)
                self.fetch_data()

                # Confirmation message
                messagebox.showinfo("Success", "Student details saved successfully", parent=self.root)

            except Exception as e:
                messagebox.showerror("Error", f"Failed to save data: {str(e)}", parent=self.root)


    def fetch_data(self):
        try:

            for item in self.student_table.get_children():
                self.student_table.delete(item)
            # Fetch data from Firestore
            students_ref = db.collection('Students')
            students = students_ref.stream()

            # Populate the table with the fetched data
            for student in students:
                data = student.to_dict()  # Convert Firestore document to a dictionary
                self.student_table.insert('', 'end', values=(
                data.get('Department'),
                data.get('Course'),
                data.get('Year'),
                data.get('Semester'),
                data.get('StudentID'),
                data.get('Name'),
                data.get('Section'),
                data.get('RollNo'),
                data.get('Gender'),
                data.get('DOB'),
                data.get('Email'),
                data.get('Address'),
                data.get('MobileNo'),
                data.get('PhotoStatus')
            ))

            #messagebox.showinfo("Success", "Data fetched successfully", parent=self.root)

        except Exception as e:
            print(f"Failed to fetch data: {str(e)}")


    def get_cursor(self,evebt=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]    

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_address.set(data[11]),
        self.var_phone.set(data[12]),
        self.var_radio1.set(data[13])

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            # Mobile number validation: Ensure it has exactly 10 digits
            mobile_number = self.var_phone.get()
            if not re.match(r'^[0-9]{10}$', mobile_number):
                messagebox.showerror("Error", "Invalid mobile number. It should be exactly 10 digits.", parent=self.root)
                return
        
            # Email validation: Basic format check (e.g., example@domain.com)
            email = self.var_email.get()
            if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
                messagebox.showerror("Error", "Invalid email address.", parent=self.root)
                return

            try:
                update=messagebox.askyesno("Update","Do you want to update",parent=self.root)
                if(update>0):
                    student_ref = db.collection('Students').document(self.var_std_id.get())

                # Update the document with new values
                student_ref.update({
                    'Department': self.var_dep.get(),
                    'Course': self.var_course.get(),
                    'Year': self.var_year.get(),
                    'Semester': self.var_semester.get(),
                    'StudentID': int(self.var_std_id.get()),
                    'Name': self.var_std_name.get(),
                    'Section': self.var_div.get(),
                    'RollNo': self.var_roll.get(),
                    'Gender': self.var_gender.get(),
                    'DOB': self.var_dob.get(),
                    'Email': self.var_email.get(),
                    'Address': self.var_address.get(),
                    'MobileNo': self.var_phone.get(),
                    'PhotoStatus': self.var_radio1.get()  # Assuming radio button for photo status
                })

                # Show success message
                messagebox.showinfo("Success", "Student record updated successfully", parent=self.root)
                self.fetch_data()

            except Exception as e:
                messagebox.showerror("Error", f"Failed to update data: {str(e)}", parent=self.root)

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be present", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete", "Do you want to delete this student?", parent=self.root)
                if delete > 0:
                    # Get the reference to the student document by student ID
                    student_ref = db.collection('Students').document(self.var_std_id.get())
                
                    # Delete the student document
                    student_ref.delete()

                    # Show success message
                    messagebox.showinfo("Success", "Student record deleted successfully", parent=self.root)


                    # Refresh the table after deletion
                    self.fetch_data()

                else:
                    if not delete:
                        return

            except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete data: {str(e)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_address.set(""),
        self.var_phone.set(""),
        self.var_radio1.set("")


    def generate_dataset(self):
        # Check if required fields are empty
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                # Reference to the student document in Firestore using the student ID
                student_ref = db.collection('Students').document(self.var_std_id.get())

                # Check if the student already exists in the Firestore database
                student_data = student_ref.get()
                if not student_data.exists:
                    # If the student document doesn't exist, create a new one
                    student_ref.set({
                        'Department': self.var_dep.get(),
                        'Course': self.var_course.get(),
                        'Year': self.var_year.get(),
                        'Semester': self.var_semester.get(),
                        'StudentID': int(self.var_std_id.get()),
                        'Name': self.var_std_name.get(),
                        'Section': self.var_div.get(),
                        'RollNo': self.var_roll.get(),
                        'Gender': self.var_gender.get(),
                        'DOB': self.var_dob.get(),
                        'Email': self.var_email.get(),
                        'Address': self.var_address.get(),
                        'MobileNo': self.var_phone.get(),
                        'PhotoStatus': self.var_radio1.get()  # Assuming radio button for photo status
                    })
                else:
                    # If the student document already exists, update it
                    student_ref.update({
                        'Department': self.var_dep.get(),
                        'Course': self.var_course.get(),
                        'Year': self.var_year.get(),
                        'Semester': self.var_semester.get(),
                        'StudentID': self.var_std_id.get(),
                        'Name': self.var_std_name.get(),
                        'Section': self.var_div.get(),
                        'RollNo': self.var_roll.get(),
                        'Gender': self.var_gender.get(),
                        'DOB': self.var_dob.get(),
                        'Email': self.var_email.get(),
                        'Address': self.var_address.get(),
                        'MobileNo': self.var_phone.get(),
                        'PhotoStatus': self.var_radio1.get()  
                    })

                

                # Face detection and image capture logic
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    if len(faces) == 0:
                        return None

                    for (x, y, w, h) in faces:
                        return img[y:y+h, x:x+w]

                # Start capturing video
                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, my_frame = cap.read()
                    if not ret:
                        messagebox.showerror("Error", "Failed to open the camera", parent=self.root)
                        break

                    # Perform face cropping
                    cropped_face = face_cropped(my_frame)
                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)  # Grayscale conversion

                        # Save the image
                        file_name_path = f"data/user.{self.var_std_id.get()}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)

                        # Show the image with the count on it
                        cv2.putText(face,f'{img_id}', (30, 30), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)  # Converted img_id to string
                        cv2.imshow("Cropped Face", face)

                    # Stop after 100 images or pressing Enter (keycode 13)
                    if cv2.waitKey(1) == 13 or img_id == 150:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating Dataset Completed")

            except Exception as e:
                # Show error message if something goes wrong
                messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)
    








    

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
