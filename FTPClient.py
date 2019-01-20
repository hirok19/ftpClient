#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 20:27:18 2019

@author: supaul
"""


"""
1. Change the positioning of buttons.
2. Add other fields as required.
3. Convert to .exe 
4. Upload on Git
5. Test on another computer's file system.
6. Download a FTP client: try to mimic as many functionalities as possible
7. Make the UI richer
8. Append a read me
9. Add to Resume
"""

from ftplib import FTP
try:
    
    #ftp.retrbinary('RETR README', open('README', 'wb').write)
    import tkinter
    top = tkinter.Tk()
    top.title('My FTP Client')
    top.geometry("300x300") #You want the size of the app to be 500x500
    top.resizable(0, 0) #Don't allow resizing in the x or y direction
    from tkinter import *
    L1 = Label(top, text="File Location")
    L1.pack( side = LEFT)
    E1 = Entry(top, bd =5)
    E1.pack(side = RIGHT)
    #top.mainloop()
    def helloCallBack():
        try:
            #get the text of the concerned text box and just call
            ftp = FTP('ftp.nluug.nl')
            ftp.login("anonymous", "ftplib-example-1")
            data = []
            ftp.dir(data.append)
            for line in data:
                print(line)
            ftp.cwd('/pub/')         # change directory to /pub/
            # reading from a text box 
            fileLocation= E1.get()
            print(fileLocation)
            ftp.retrbinary("RETR " + fileLocation,open(fileLocation, 'wb').write)
            print("File download succesful")
            ftp.quit()
        except Exception as caughtException:
            print("This is an exception")
            print(caughtException)
    But = tkinter.Button(top, text ="Download", command = helloCallBack,height=5,width=5)
    But.pack()
    top.mainloop()
    top.destroy()
except ConnectionRefusedError:
    print("Connection refused")
except AttributeError:
    print("File Not there")
    