from tkinter import *  #Tkinter is needed to give me the tools to create my GUI.
from tkinter import messagebox

root = Tk()
root.title("Calculator")
root.geometry("300x500")   #This will give it a title and dimensions.

display = Label(root, text="")
display.grid(row=0, column=0, columnspan=4) #This creates the actual space for all the allignment below.


Button(root, text="7", width=5, height=2).grid(row=1, column=0)
Button(root, text="8", width=5, height=2).grid(row=1, column=1)
Button(root, text="9", width=5, height=2).grid(row=1, column=2)
Button(root, text="/", width=5, height=2).grid(row=1, column=3)

Button(root, text="4", width=5, height=2).grid(row=2, column=0)
Button(root, text="5", width=5, height=2).grid(row=2, column=1)
Button(root, text="6", width=5, height=2).grid(row=2, column=2)
Button(root, text="*", width=5, height=2).grid(row=2, column=3)

Button(root, text="1", width=5, height=2).grid(row=3, column=0)
Button(root, text="2", width=5, height=2).grid(row=3, column=1)
Button(root, text="3", width=5, height=2).grid(row=3, column=2)
Button(root, text="-", width=5, height=2).grid(row=3, column=3)

Button(root, text="0", width=5, height=2).grid(row=4, column=0)
Button(root, text="=", width=5, height=2).grid(row=4, column=1)
Button(root, text="+", width=5, height=2).grid(row=4, column=3)

#Basically what all of those are doing is alligning the numbers and operations(remembered the word finally). I did have to look up how to allign them properly, but once I got one, the rest were pretty easy to do.The first GUI lab we did was helpful for this part.
root.mainloop()
