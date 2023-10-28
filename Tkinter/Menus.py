from tkinter import *

window=Tk()

#Sets the size of the window
window.geometry('500x700')

#Sets the title of the window
window.title('SimpleApplication')


menuO=Menu(window)

file=Menu(menuO,tearoff=0)

file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save As")

#adds line seprator
file.add_separator()
file.add_command(label="Exit")

menuO.add_cascade(label="Menu",menu=file)

window.config(menu=menuO)


mainloop()