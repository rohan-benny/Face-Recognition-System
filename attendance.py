from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from tkinter import messagebox
from firebaseconfig import db
import cv2
import os
import csv
from tkinter import filedialog

myData=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.student_table = ttk.Treeview(self.root, columns=(...))
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student Attendance")

        self.var_attend_id=StringVar()
        self.var_attend_rollno=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()

        # Load the background image
        self.bg_image_path = "Assets/background_5.png"  # Path to your background image
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
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance",font=self.leftframe_font,labelanchor='n')
        left_frame.place(x=5,y=0,width=730,height=586)

        self.leftframe_font1 = tkFont.Font(family="Poppins SemiBold", size=12)
        left_inside_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,font=self.leftframe_font,labelanchor='n')
        left_inside_frame.place(x=5,y=5,width=720,height=450)

        Attendance_id_label=Label(left_inside_frame,text="Attendance ID :",font=self.leftframe_font1)
        Attendance_id_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        AttendanceId_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_id,width=16,font=self.leftframe_font)
        AttendanceId_entry.grid(row=0,column=1,padx=7,pady=15,sticky=W)

        roll_id_label=Label(left_inside_frame,text="Roll No :",font=self.leftframe_font1)
        roll_id_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)
        Attendroll_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_rollno,width=16,font=self.leftframe_font)
        Attendroll_entry.grid(row=0,column=3,pady=8)

        name_label=Label(left_inside_frame,text="Name :",font=self.leftframe_font1)
        name_label.grid(row=1,column=0)
        name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_name,width=16,font=self.leftframe_font)
        name_entry.grid(row=1,column=1,pady=8)

        dep_label=Label(left_inside_frame,text="Department :",font=self.leftframe_font1)
        dep_label.grid(row=1,column=2)
        dep_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_dep,width=16,font=self.leftframe_font)
        dep_entry.grid(row=1,column=3,pady=8)

        time_label=Label(left_inside_frame,text="Time :",font=self.leftframe_font1)
        time_label.grid(row=2,column=2)
        time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_time,width=16,font=self.leftframe_font)
        time_entry.grid(row=2,column=3,pady=8)

        date_label=Label(left_inside_frame,text="Date :",font=self.leftframe_font1)
        date_label.grid(row=2,column=0)
        date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_date,width=16,font=self.leftframe_font)
        date_entry.grid(row=2,column=1,pady=8)

        attendanceLabel=Label(left_inside_frame,text="Attendance Status :",font=self.leftframe_font1)
        attendanceLabel.grid(row=3,column=0)

        self.attend_status=ttk.Combobox(left_inside_frame,textvariable=self.var_attend_attendance,width=14,font=self.leftframe_font1,state="readonly")
        self.attend_status["values"]=("Status","Present","Absent")
        self.attend_status.grid(row=3,column=1,pady=8)
        self.attend_status.current(0)

        btn_frame1=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=8,y=390,width=700,height=40)
        imprt_btn=Button(btn_frame1,text="Import csv",command=self.importCsv,font=self.leftframe_font1,bg="#060D18",fg="#F8BA41",width=17)
        imprt_btn.grid(row=0,column=0)
        export_btn=Button(btn_frame1,text="Export csv",command=self.exportCsv,font=self.leftframe_font1,bg="#060D18",fg="#F8BA41",width=17)
        export_btn.grid(row=0,column=1,padx=1)
        update_btn=Button(btn_frame1,text="Update",command=self.update_data,font=self.leftframe_font1,bg="#060D18",fg="#F8BA41",width=17)
        update_btn.grid(row=0,column=2,padx=1)
        reset_btn=Button(btn_frame1,text="Reset",command=self.reset_data,font=self.leftframe_font1,bg="#060D18",fg="#F8BA41",width=17)
        reset_btn.grid(row=0,column=3,padx=1)

        # Right Frame 
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=self.leftframe_font,labelanchor='n')
        right_frame.place(x=740,y=0,width=766,height=586)
        
        tableframe1=Frame(right_frame,bd=2,relief=RIDGE)
        tableframe1.place(x=8,y=5,width=750,height=450)

        scroll_x=ttk.Scrollbar(tableframe1,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tableframe1,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(tableframe1,column=("id","rollno","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance Id")
        self.AttendanceReportTable.heading("rollno",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=150)
        self.AttendanceReportTable.column("rollno",width=150)
        self.AttendanceReportTable.column("name",width=150)
        self.AttendanceReportTable.column("department",width=150)
        self.AttendanceReportTable.column("time",width=150)
        self.AttendanceReportTable.column("date",width=150)
        self.AttendanceReportTable.column("attendance",width=150)
                
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for row in rows:
            if len(row) == 7:  # Ensure each row has 7 columns (id, rollno, name, department, time, date, attendance)
                self.AttendanceReportTable.insert("", END, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            else:
                messagebox.showwarning("Warning", "Some rows are missing data.")


    def importCsv(self):
        global myData
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV file","*.csv"),("ALL File","*.*")),parent=self.root)
        if not fln:  # If no file is selected
            return
        myData.clear()
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)

    def exportCsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","No Data Found",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV file","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to " + os.path.basename(fln) + " successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
            
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_attend_id.set(rows[0])
        self.var_attend_rollno.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_rollno.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")

    def update_data(self):
        # Find the row in myData that matches the current Attendance ID
        found = False
        for i in range(len(myData)):
            if myData[i][0] == self.var_attend_id.get():  # Compare with Attendance ID
                # Update the row with new values from entry fields
                myData[i] = [
                    self.var_attend_id.get(),
                    self.var_attend_rollno.get(),
                    self.var_attend_name.get(),
                    self.var_attend_dep.get(),
                    self.var_attend_time.get(),
                    self.var_attend_date.get(),
                    self.var_attend_attendance.get()
                ]
                found = True
                break

        if found:
            # Save updated data back to the CSV file
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save Updated CSV", filetypes=(("CSV file", "*.csv"), ("All files", "*.*")), parent=self.root)
            if fln:
                with open(fln, mode="w", newline="") as myfile:
                    csv_writer = csv.writer(myfile, delimiter=",")
                    for row in myData:
                        csv_writer.writerow(row)
                messagebox.showinfo("Success", "Data updated successfully!", parent=self.root)
        else:
            messagebox.showerror("Error", "Attendance ID not found", parent=self.root)








    def resize_background(self, event):
        # Get the new size of the window
        new_width = event.width
        new_height = event.height

        # Resize the background image to fit the window
        resized_img = self.bg_img.resize((new_width, new_height))
        self.bg_photo = ImageTk.PhotoImage(resized_img)

        # Update the label with the new image
        self.bg_label.config(image=self.bg_photo)
        self.bg_label.image = self.bg_photo

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()