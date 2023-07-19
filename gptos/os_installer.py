import tkinter as tk
import os
import sys

def install_os():
    # Close the confirmation window
    window.destroy()

    # Run the os_installation.py script
    os.system(sys.executable + " os_installation.py")

def close_window():
    # Close the confirmation window
    window.destroy()

# Create the confirmation window
window = tk.Tk()
window.title("CapOS Installation Confirmation")
window.geometry("480x200")  # Set the window size here

# Create a label for the welcome message
welcome_label = tk.Label(window, text="Welcome to CapOS", font=("Consolas", 16))
welcome_label.pack(pady=20)

# Create a label for the installation version
version_label = tk.Label(window, text="You are installing Version 1.00 which is the latest.", font=("Consolas", 12))
version_label.pack(pady=10)

# Create the install button
install_button = tk.Button(window, text="Install", width=10, height=2, font=("Consolas", 12), command=install_os)
install_button.pack(pady=10, side=tk.LEFT)

# Create the no button
no_button = tk.Button(window, text="No", width=10, height=2, font=("Consolas", 12), command=close_window)
no_button.pack(pady=10, side=tk.RIGHT)

# Run the main event loop
window.mainloop()