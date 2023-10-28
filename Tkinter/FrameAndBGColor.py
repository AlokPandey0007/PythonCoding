from tkinter import *

mac=Tk()

#Sets the size of the window
mac.geometry('500x700')

#Sets the title of the window
mac.title('SimpleApplication')

#sets the color of the background
mac.config(bg='Blue')

#create frame
frame1=Frame(mac,bg="red",width=300,height=300,cursor='dot')
frame1.pack(side='top') #to display on window

frame2=Frame(mac,bg='green',width=300,height=300,cursor='dotbox')
frame2.pack(side='bottom')

button1=Button(frame1,fg="Blue",text='Button1')
button2=Button(frame2,fg="Blue",text='Button2')

inp=Label(mac,text='hello world')
inp.pack()

button1.pack()
button2.pack()

mac.mainloop()