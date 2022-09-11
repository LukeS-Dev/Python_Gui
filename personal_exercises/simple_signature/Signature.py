from tkinter import *
from tkinter import ttk
from PIL import ImageGrab,Image
import time

##Requires Python Image library

def mouse_press_initial(event):
    global prev
    prev = event
    print('type : ', event.type)
    print('widget : ',event.widget)
    print('num : ',event.num)
    print('x : ', event.x)
    print('y : ', event.y)
    print('x_root', event.x_root)
    print('y_root', event.y_root)

def exportCanvas(widget):
    # x=root.winfo_rootx()+widget.winfo_x()
    # y=root.winfo_rooty()+widget.winfo_y()
    # x1=x+widget.winfo_width()
    # y1=y+widget.winfo_height()
    # ImageGrab.grab().crop((x,y,x1,y1)).save("signature.png")
    widget.update()
    widget.postscript(file="myImage.ps", colormode='color')
    psimage=Image.open('myImage.ps')
    psimage.save('myImage.png')


root = Tk()

ttk.Label(root,text="Draw your signature").pack()
canvas = Canvas(root,width =640,height = 480, background='white')
canvas.pack()

def draw(event):
    global prev
    canvas.create_line(prev.x,prev.y,event.x,event.y,width=3)
    prev = event


canvas.bind('<ButtonPress>',mouse_press_initial)
canvas.bind('<B1-Motion>',draw)

ttk.Button(root,text="Export",command=lambda:exportCanvas(canvas)).pack()

root.mainloop()