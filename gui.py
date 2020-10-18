from tkinter import *

window = Tk() #line to create the main Window

# All the widgets of the GUI goes in between these



b1 = Button(master = window, text = "Execute")
b1.grid (row = 0 , column = 0 )
b2 = Button(master = window, text = "Cancel")
b2.grid(row = 0, column = 2)



e1 = Entry(window)
e1.grid(row =0 , column = 1 )



t1 = Text(window , height = 1, width = 20)
t1.grid(row = 1, column = 1)
window.mainloop()
