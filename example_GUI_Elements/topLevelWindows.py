from tkinter import * 
from tkinter import ttk

root = Tk()
root.title("Main Window")
root.geometry("300x300")

window = Toplevel(root)
window.title("New window")
window.state('withdrawn')


def windowPopup():
    if Toplevel.winfo_exists(window) != 1:
        print(":(")
    window.state('normal')

def closeWindow():
    window.state('withdrawn')


ttk.Button(text="Pop up", command = windowPopup).pack()
ttk.Button(text="Close", command = closeWindow).pack()

#define maximum size and minium size of the window
window.maxsize(600,500)
window.minsize(200,200)

root.mainloop()