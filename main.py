import tkinter as tk
from datetime import datetime

def calculate_remaining_time(current_time_str, target_time_str):
    current_time = datetime.strptime(current_time_str, "%Y-%m-%d %H:%M:%S")
    target_time = datetime.strptime(target_time_str, "%Y-%m-%d %H:%M:%S")

    remaining_time = target_time - current_time
    remaining_days = remaining_time.days
    remaining_hours = remaining_time.seconds // 3600

    output_text.set(f"{remaining_days} days left and {remaining_hours} hours left")

# Create the main window
root = tk.Tk()
root.title("Countdown Widget")

# Input fields
tk.Label(root, text="Current Date and Time").pack()
current_time_entry = tk.Entry(root)
current_time_entry.pack()

tk.Label(root, text="Target Date and Time").pack()
target_time_entry = tk.Entry(root)
target_time_entry.pack()

# Output field
output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text)
output_label.pack()

# Button to calculate remaining time
calculate_button = tk.Button(root, text="Calculate", command=lambda: calculate_remaining_time(current_time_entry.get(), target_time_entry.get()))
calculate_button.pack()

# Run the GUI
root.mainloop()