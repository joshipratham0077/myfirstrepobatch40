alaram feature

import tkinter as tk
import time
import threading
from tkinter import messagebox
import winsound  # For Windows sound alarm. Cross-platform alternative shown below.

# -----------------------------
# ALARM FUNCTION
# -----------------------------
def check_alarm():
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time.get():
            # Play sound (Windows)
            try:
                winsound.Beep(1000, 1500)  # frequency, duration
            except:
                pass

            # Show popup
            messagebox.showinfo("Alarm", "⏰ Alarm Time! Wake up!")
            break
        time.sleep(1)


# -----------------------------
# CLOCK UPDATE FUNCTION
# -----------------------------
def update_clock():
    current = time.strftime("%H:%M:%S")
    clock_label.config(text=current)
    clock_label.after(1000, update_clock)


# -----------------------------
# SET ALARM
# -----------------------------
def set_alarm():
    alarm = alarm_time.get()
    if alarm == "":
        messagebox.showerror("Error", "Please enter time in HH:MM format")
        return

    # Start alarm thread
    t = threading.Thread(target=check_alarm)
    t.start()

    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm}")


# -----------------------------
# GUI SETUP
# -----------------------------
root = tk.Tk()
root.title("Clock with Alarm")

clock_label = tk.Label(root, font=("Arial", 70), bg="black", fg="cyan")
clock_label.pack(pady=20)

alarm_frame = tk.Frame(root)
al
