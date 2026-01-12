from tkinter import *




class Sample:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

if __name__=="__main__":
    root = Tk()
    obj = Sample(root)
    root.mainloop()