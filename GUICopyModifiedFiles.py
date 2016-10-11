import shutil
import os
from tkinter import *
import tkinter.filedialog as fdialog
import sys, os.path, time, shutil
import datetime as dt

class MainClass():

    def __init__(self,master):
        self.parent=master
        self.gui()

    def gui(self):
        self.Source=StringVar()
        self.Destination=StringVar()

        MySource=Entry(myGUI, textvariable=self.Source).grid(row=9, column=1)
        browse=Button(myGUI,text="Browse",command=lambda:self.Source.set(fdialog.askdirectory())).grid(row=9, column=2)
        MyDestination=Entry(myGUI, textvariable=self.Destination).grid(row=10, column=1)
        browse1=Button(myGUI,text="Browse",command=lambda:self.Destination.set(fdialog.askdirectory())).grid(row=10, column=2)
        label1=Label(myGUI, text='Please select a source folder and the destination folder', fg='Blue').grid(row=0,column=1)
        label2=Label(myGUI, text='for recently updated files, then click copy',fg='Blue').grid(row=1,column=1)
        label3=Label(myGUI, text='Source', fg='Black').grid(row=9, column=0)
        label4=Label(myGUI, text='Destination', fg='Black').grid(row=10, column=0)
        button1=Button(myGUI, text="       Copy       ", command=self.copyy).grid(row=11, column=1)
        

    def copyy(self):
        source_file=self.Source.get()
        for root,dirs,files in os.walk(source_file):
            for file_name in files:
                now = dt.datetime.now()
                before = now - dt.timedelta(minutes=1440)
                path = os.path.join(root,file_name)
                st = os.stat(path)

                mod_time = dt.datetime.fromtimestamp(st.st_mtime)
                if mod_time > before:
                    shutil.copy(os.path.join(root, file_name),self.Destination.get()) 

if __name__ == '__main__':
    myGUI=Tk()
    app=MainClass(myGUI)
    myGUI.geometry("400x200+200+300")
    myGUI.title('Copy Modified Files')
    myGUI.mainloop()
