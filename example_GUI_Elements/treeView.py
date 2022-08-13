from tkinter import *
from tkinter import ttk
root = Tk()

treeview = ttk.Treeview(root,height=5)
treeview.pack()

treeview.insert('','0','item1',text='First')
treeview.insert('','1','item2',text='Second')
treeview.insert('','end','item3',text='Third')

logo = PhotoImage(file="/home/luke/Code/Python/Python_Gui/images/anko_logo.png").subsample(12,12)
treeview.insert('item2','end','anko',text='anko',image=logo)

#treeview.move('item2','item1','end')
treeview.item('item2',open=False)

#treeview.detach('item3')

treeview.config(columns=('version'))
treeview.column('version',width=100,anchor='center')
treeview.column('#0',width=200)
treeview.heading('#0', text = 'Main')
treeview.heading('version', text = 'Version')
treeview.set('anko','version','0.2')

#Prints current selected item.
def callback(event):
    print(treeview.selection())

treeview.bind('<<TreeviewSelect>>',callback)

root.mainloop()