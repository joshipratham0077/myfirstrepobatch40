import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_clock)  # Update every 1 second

# Create main window
root = tk.Tk()
root.title("Digital Clock")

# Clock label styling
label = tk.Label(root, font=("Arial", 80), bg="black", fg="cyan")
label.pack(anchor="center")

update_clock()  # Start the clock
root.mainloop()
