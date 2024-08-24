import tkinter as tk
from tkinter import messagebox
import subprocess

def set_power_plan(guid):
    try:
        subprocess.run(['powercfg', '-duplicatescheme', guid], capture_output=True, text=True)
        result = subprocess.run(['powercfg', '-setactive', guid], capture_output=True, text=True)
        # Check the return code to determine success or failure
        if result.returncode == 0:
            # If successful, display the success message
            messagebox.showinfo("Success", f"The power plan was successfully set to {guid}.")
        else:
            # If failed, display the error message with details from stderr
            messagebox.showerror("Error", f"Failed to set the power plan: {result.stderr.strip()}")
    except Exception as e:
        # Handle any other exceptions that might occur
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

def balance_mode():
    set_power_plan('381b4222-f694-41f0-9685-ff5bb260df2e')

def energy_saving_mode():
    set_power_plan('a1841308-3541-4fab-bc81-f71556f20b4a')

def high_performance_mode():
    set_power_plan('8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c')

# Create the main window
window = tk.Tk()
window.title("Power Mode Switcher")

# Create buttons for each mode
balance_button = tk.Button(window, text="Balance Mode", command=balance_mode)
balance_button.pack()

energy_saving_button = tk.Button(window, text="Energy Saving Mode", command=energy_saving_mode)
energy_saving_button.pack()

high_performance_button = tk.Button(window, text="High Performance Mode", command=high_performance_mode)
high_performance_button.pack()

# Start the GUI event loop
window.mainloop()