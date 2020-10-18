from tkinter import *

window = Tk() #line to create the main Window
window.title("Converter")
window.resizable(0,0)


# All the widgets of the GUI goes in between these
def kg_to():
        try :
            input = float(e1_value.get())
        except ValueError:
            change_message("Invalid Input Try Again!!")
        else:
            change_message("")
            grams  = float(e1_value.get()) * 1000
            t1.delete("1.0",END)
            t1.insert(END , grams)
            pounds  = float(e1_value.get()) * 2.20
            t2.delete("1.0",END)
            t2.insert(END , pounds)
            ounces  = float(e1_value.get()) * 35.274
            t3.delete("1.0",END)
            t3.insert(END , ounces)


##Input Label : KG

Input_Kg = Label(window , text = "Kg")
Input_Kg.grid(row = 0 , column = 0)

##Widget for inoput value
e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value )
e1.grid(row =0 , column = 1 )


b1 = Button(master = window, text = "Convert" ,command= kg_to)
b1.grid (row = 0 , column = 2 )

#Outputs Labels
Output_g = Label(window , text = "grams")
Output_g.grid(row = 1 , column = 0)


Output_pounds = Label(window , text = "pounds")
Output_pounds.grid(row = 1 , column = 1)


Output_ounces = Label(window , text = "ounces")
Output_ounces.grid(row = 1 , column = 2)


#Outputs Values
t1 = Text(window , height = 1, width = 20)
t1.grid(row = 2, column = 0)

t2 = Text(window , height = 1, width = 20)
t2.grid(row = 2, column = 1)

t3 = Text(window , height = 1, width = 20)
t3.grid(row = 2, column = 2)

#Message
##Message text value
message_text = StringVar()
def change_message(message):
    message_text.set(message)



Message = Label(window ,textvariable= message_text)
Message.grid(row = 3 , column = 1)






window.mainloop()
