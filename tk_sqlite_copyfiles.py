import shutil
import os
from tkinter import *
import tkinter.filedialog as fdialog
import sys, os.path, time, shutil
import datetime as dt
import sqlite3
import time
from datetime import datetime
import string

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
        label1=Label(myGUI, text='Please select a source folder & destination folder', fg='Blue').grid(row=0,column=1)
        label2=Label(myGUI, text='for recently updated files, then click copy',fg='Blue').grid(row=1,column=1)
        label3=Label(myGUI, text='Source', fg='Black').grid(row=9, column=0)
        label4=Label(myGUI, text='Destination', fg='Black').grid(row=10, column=0)
        button1=Button(myGUI, text="       Copy       ", command=self.copyy).grid(row=12, column=1)
         
    def copyy(self):
    #create & connect to db   
        conn = sqlite3.connect('TimeLogs4.db')
        c = conn.cursor()
        t = datetime.now()
        t1 = t.timetuple()
        t2 = (time.mktime(t1))
    #Create table 
        conn.execute("CREATE TABLE if not exists Tracker(CheckFolder TEXT, datestamp TEXT );")    
        date = str(dt.datetime.fromtimestamp(int(time.time())).strftime('%Y-%M-%D %H:%M:%S'))
        source_file=self.Source.get()
        
        #src = str(source_file)
        #num = 1
        c.execute("INSERT INTO Tracker(CheckFolder, datestamp) VALUES(?,?)", (source_file, t2))
        conn.commit()
        c.execute("SELECT count(CheckFolder) FROM Tracker WHERE CheckFolder=? ",([source_file]))
        ct1 = c.fetchone()
        ct2 = ''.join(map(str,(ct1)))
        ct3 = int(ct2)
        print (ct3)
        if ct3 < 2:
            mystring1 =str("0.0")
        else:    
            c.execute("SELECT datestamp FROM Tracker WHERE CheckFolder=? ORDER BY datestamp DESC LIMIT 1 OFFSET 1 ",([source_file])) 
            beforepull = c.fetchone()
            mystring = ''.join(map(str,(beforepull)))
            mystring1 = str(mystring)
        for root,dirs,files in os.walk(source_file):
            for file_name in files:
                now = dt.datetime.now()
                path = os.path.join(root,file_name)
                st = os.stat(path)
                mod_time = (dt.datetime.fromtimestamp(st.st_mtime))
                mt1 = mod_time.timetuple()
                mt2 = str(time.mktime(mt1))                              
                if mt2 > mystring1:
                    shutil.copy(os.path.join(root, file_name),self.Destination.get())
                    print('Updated and created files have been copied to their destinations')                    
                else:
                    print(('%s last modified %s'%(path,mod_time)))
if __name__ == '__main__':
    myGUI=Tk()
    app=MainClass(myGUI)
    myGUI.geometry("400x200+200+300")
    myGUI.title('Copy Modified Files')
    myGUI.mainloop()
