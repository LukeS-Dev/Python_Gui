from tkinter import *
from tkinter import ttk

def mouse_press(event):
    global prev
    prev = event
    print('type : ', event.type)
    print('widget : ',event.widget)
    print('num : ',event.num)
    print('x : ', event.x)
    print('y : ', event.y)
    print('x_root', event.x_root)
    print('y_root', event.y_root)

    pos_x = event.x
    pos_y = event.y


#This is a function that binds to specific mouse events.
root = Tk()

canvas = Canvas(root,width =640,height = 480, background='white')
canvas.pack()

def draw(event):
    global prev
    canvas.create_line(prev.x,prev.y,event.x,event.y,width=3)
    prev = event

canvas.bind('<ButtonPress>',mouse_press)
canvas.bind('<B1-Motion>',draw)

#1 - Left button, 2 Mid button, 3 Right click. 
#<Button>, <ButtonPress> -- ANy
#<1> <2> <3> //Bind to specific mouseclick
#<ButtonRelease-1> //Release
#<Double-Button-1> //Double click
#<Enter> <Leave> //Hover or leave
#<Motion> <B1-Motion> //Mouse was moved 

root.mainloop()