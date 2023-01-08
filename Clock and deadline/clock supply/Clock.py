from tkinter import Tk #create windoe
from tkinter import Label #write in Tk
import time
import datetime

root = Tk()
root.title("Clock and Deadline")
root.geometry('920x450')

def present_time():
    display_time = time.strftime("%H:%M:%S %p") #give current time
    digit_clock.config(text=display_time)
    digit_clock.after(200, present_time) #after 200 milisec run next

digit_clock = Label(root, font=("arial", 120), bg="gray", fg="black")
digit_clock.pack() #come in

present_time()

root.mainloop()
