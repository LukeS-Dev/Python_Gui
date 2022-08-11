from tkinter import *
from tkinter import ttk
import time
import threading

#Create global thread stopping method. Ideally this should be a threading
#handler method which throws an exception but since this example won't 
#be used elsewhere I think this should be okay. But bad practice otherwise.
stopThreads = False

def thread_monitorScale(value,label):
    update_frequency = 0.025
    while True:
        label.config(text="Current Value : " + "%.1f"%value.get())
        global stopThreads
        if stopThreads == True:
            break
        time.sleep(update_frequency)

def thread_updatePercent(progressbar,percent):
    totalDownloadTime = 5
    stepIntervalDownloadTime = totalDownloadTime/1000

    for i in range(1000):
        completion = i * 0.1
        completion_str = "%.1f"%completion + " Complete"
        progressbar.config(value = completion)
        percentage.config(text = completion_str)
        time.sleep(stepIntervalDownloadTime)
        
        global stopThreads
        if stopThreads == True:
            break

    percentage.config(text = "100% Complete")

def closeThreads(threads,window):
    global stopThreads
    stopThreads = True
    for thread in threads: 
        print(thread)

    time.sleep(0.2)
    window.destroy()
    

window = Tk()
window.geometry("400x300")

#Create Dummy loading text - indeterminate
ttk.Label(window,padding=30,text="Downloading").pack()

progressbar = ttk.Progressbar(window,orient = HORIZONTAL,length = 150,mode = 'indeterminate')
progressbar.pack()
progressbar.start()

#Create download percentage. using fake update
ttk.Label(window,padding=30,text="Downloading more").pack()

progressbar_percent = ttk.Progressbar(window,orient = HORIZONTAL,length = 150,mode = 'determinate',maximum=100.0,value=0)
progressbar_percent.pack()

percentage = ttk.Label(window,text = "0% Complete")
percentage.pack()

#Create scaling input
label_currValue = ttk.Label(window,text = "Current Value : 0")
label_currValue.pack()

value = DoubleVar()
scale = ttk.Scale(window, orient=HORIZONTAL, length = 150, variable = value,from_ = 0.0, to = 100.0)
scale.pack()

#Thread management
t_updatePercentage  = threading.Thread(target=thread_updatePercent,args=[progressbar_percent,percentage]).start()
t_monitorScale      = threading.Thread(target=thread_monitorScale,args=[value,label_currValue]).start()
threads = [t_updatePercentage,t_monitorScale]

for threads in threads:
    thread.join()

window.protocol("WM_DELETE_WINDOW",lambda: closeThreads(threads,window))
window.mainloop()