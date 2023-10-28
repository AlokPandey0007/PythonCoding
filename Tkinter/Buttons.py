from tkinter import *

mac=Tk()

#Sets the size of the window
mac.geometry('500x700')

#Sets the title of the window
mac.title('SimpleApplication')


#method
def click_msg():
    print("Hello World")
button=Button(mac,text="Login", command=click_msg(),bg="black",fg="red",activebackground="yellow",activeforeground="black",font=("bold",15))
button.pack()


mainloop()  