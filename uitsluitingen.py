from tkinter import *

root = Tk()

input = Entry()
input.get()


#maakt label widget aan
essentLbl = Label (root, text="Essent uitsluitingen")
#maakt button aan
createBtn = Button(root, text="create", padx=50)

# plaats het op het scherm
essentLbl.grid(row=0,column=0)
input.grid(row=0, column=1)
createBtn.grid(row=1, column=1)

root.mainloop()