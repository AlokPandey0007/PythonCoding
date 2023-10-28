from tkinter import *

mac=Tk()

#Sets the size of the window
mac.geometry('500x700')

#Sets the title of the window
mac.title('SimpleApplication')

#sets the color of the background
mac.config(bg='Blue')

#create frame
mailLable=Label(mac,text='Email',)
mailLable.grid(row=0,column=1)

mailEntry=Entry(mac,width=40,border=5)
mailEntry.grid(row=0,column=2)

passwordLable=Label(mac,text='Password')
passwordLable.grid(row=1,column=1)

passwordEntry=Entry(mac,width=40,border=5)
passwordEntry.grid(row=1,column=2)

signInbutton=Button(text='SignIn')
signInbutton.grid(row=3,column=1)

mac.mainloop()