import tkinter as tk
import subprocess

def open_browser():
    subprocess.run(["python", "browser.py"])

def open_calculator():
    subprocess.run(["python", "C:/gptos/CAPOS C/capos/systemapps/calculator.py"])

def open_minesweeper():
    subprocess.run(["python", "minesweeper.py"])

def open_settings():
    subprocess.run(["python", "settings.py"])

# Create the main window
window = tk.Tk()
window.title("Programs")
window.geometry("150x155")  # Set the window size here

# Create a frame to hold the program buttons
frame = tk.Frame(window)
frame.pack(padx=10, pady=10)

# Create the program buttons
browser_button = tk.Button(frame, text="Catpty Browser", width=15, command=open_browser)
browser_button.pack(pady=5)

calculator_button = tk.Button(frame, text="Calculator", width=15, command=open_calculator)
calculator_button.pack(pady=5)

minesweeper_button = tk.Button(frame, text="Minesweeper", width=15, command=open_minesweeper)
minesweeper_button.pack(pady=5)

settings_button = tk.Button(frame, text="OS Settings", width=15, command=open_settings)
settings_button.pack(pady=5)

# Run the main event loop
window.mainloop()