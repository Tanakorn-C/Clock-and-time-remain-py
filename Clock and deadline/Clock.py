from tkinter import *
import tkinter as tk
from tkcalendar import DateEntry
import datetime
import time

root = Tk()  #create window
root.config(background="#d3ffdc")
root.title("Clock and Deadline")
root.geometry('920x390')

def my_update():
    my_label2.config(text=calendar.get_date())

    now = datetime.datetime.now()
    date = str(calendar.get_date())
    cal_get = datetime.datetime.strptime(date, '%Y-%m-%d')

    tomorrow = cal_get - now
    delta = tomorrow

    cal_get_edit = str(cal_get)
    cal_get_edited = cal_get_edit[:-8:]

    delta_edit = str(delta)
    delta_edited = delta_edit[:-7:].replace("-", "")

    #delta_fix = datetime.datetime.strftime(date, '%Y-%m-%d')
    if delta.days < 0:

        my_label3.config(text='Ship has sailed')
    else:
        my_label3.config(text=f'Take your time. There are ' + delta_edited + ' left until ' + str(cal_get_edited))
        my_label3.after(5000, my_update)

#create calendar 
calendar = DateEntry(root, selectmode='day')
calendar.place(x=330, y=340)
button1 = tk.Button(root, text='Set', height=1, width=3, command=lambda:my_update())
button1.place(x=440, y=340)

#selected date
my_label2 = Label(root, bg="lemonchiffon")
#my_label2.place(x=820, y=340)
#time left
my_label3 = Label(root, bg="lemonchiffon")
my_label3.place(x=490,  y=340)

# present clock
def present_time():
    display_time = time.strftime("%H:%M:%S %p") #give current time
    digit_clock.config(text=display_time)
    digit_clock.after(1000, present_time) #after 1000 milisec run next
    my_label.config(text=(time.strftime("%Z" + " " + "%A" + "\n" + "%x")))

digit_clock = Label(root, font=("Century Gothic", 120), bg="#93E9BE", fg="black")
digit_clock.pack() #come in

my_label = Label(root, text="", font=("Garamond", 35))
my_label.pack(pady=15)

present_time()

root.mainloop()