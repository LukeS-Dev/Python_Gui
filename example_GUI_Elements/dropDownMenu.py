from tkinter import * 
root = Tk()

root.option_add('*tearOff',False)
menubar = Menu(root)
root.config(menu=menubar)

file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)

menubar.add_cascade(menu=file,label='File')
menubar.add_cascade(menu=edit,label='Edit')
menubar.add_cascade(menu=help_,label='Help')

file.add_command(label = "New", accelerator = 'Ctrl + N',command = lambda: print("New File"))
file.add_separator()
file.add_command(label = "Open", accelerator = 'Ctrl + O', command = lambda: print("Open File"))

save = Menu(file)
file.add_cascade(menu = save, label="Save")
save.add_command(label = "Save As", command = lambda: print("Save As"))
save.add_command(label = "Save All", command = lambda: print("Save All"))

choice = IntVar()
edit.add_radiobutton(label='One',variable=choice,value=1)
edit.add_radiobutton(label='Two',variable=choice,value=2)
edit.add_radiobutton(label='Three',variable=choice,value=3)

file.post(400,300)

root.mainloop()
