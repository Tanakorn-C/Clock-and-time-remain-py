import tkinter as tk
from tkinter import Label
import time
import datetime

# Get the target date and time
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))
hour = int(input("Enter the hour (0-23): "))
minute = int(input("Enter the minute (0-59): "))
second = int(input("Enter the second (0-59): "))

# Create the main window
window = tk.Tk()
window.title("Date Countdown Timer")

# Create a label to display the countdown
label = tk.Label(window, font=("Helvetica", 24))
label.pack()

# Update the countdown display every 1000 milliseconds (1 second)
def update_countdown():
    display_time = time.strftime("%H:%M:%S %p") #give current time
    digit_clock.config(text=display_time)
    digit_clock.after(200, present_time) #after 200 milisec run next


    # Calculate the time remaining until the target date and time
    current_time = time.time()
    target_time = time.mktime((year, month, day, hour, minute, second, 0, 0, 0))
    time_remaining = target_time - current_time

    # Convert the time remaining to a human-readable string
    days, remainder = divmod(time_remaining, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Update the label text
    label.config(text="{:.0f} days, {:.0f} hours, {:.0f} minutes, {:.0f} seconds remaining".format(days, hours, minutes, seconds))

    # Schedule the next update
    window.after(1000, update_countdown)


# Start the countdown
update_countdown()

# Run the Tkinter event loop
window.mainloop()
