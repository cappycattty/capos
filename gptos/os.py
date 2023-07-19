import tkinter as tk
import subprocess
import os
from PIL import Image, ImageTk

def open_browser():
    subprocess.run(["python", "browser.py"])

def open_calculator():
    subprocess.run(["python", "C:/gptos/CAPOS C/capos/systemapps/calculator.py"])

def open_file_explorer():
    subprocess.run(["python", "CAPOS C\capos\systemapps/fileorganizer.py"])

# Create the main window
window = tk.Tk()
window.title("Capcat OS 1.00")

# Create the OS simulator frame
os_simulator = tk.Frame(window)
os_simulator.pack(fill="both", expand=True)

def read_background_color():
    try:
        with open("bgcolor.txt", "r") as file:
            color = file.read().strip()
        return color
    except FileNotFoundError:
        return None

# Create the desktop frame
desktop = tk.Frame(os_simulator, bg=read_background_color() or "blue")
desktop.pack(fill="both", expand=True)

# Load the background image
background_image = tk.PhotoImage(file="C:/gptos/CAPOS C/capos/contents/icons/systemicons/osicon.png")

# Create a label widget for the background image
background_label = tk.Label(window, image=background_image, bg=read_background_color() or "blue")
background_label.place(x=0.7, y=0.9, relwidth=1, relheight=1)

# Create a label widget for the desktop text
text_label = tk.Label(window, text="CAP Os 1.00", font=("Arial", 48), fg="white", bg=read_background_color() or "blue")
text_label.place(relx=0.7, rely=0.9, anchor="center")

# Configure the window size
window.geometry("800x600")

# Create the taskbar frame
taskbar = tk.Frame(window, bg="black", height=40)
taskbar.pack(fill="x", side="bottom")

# Create the Start button in the taskbar
start_button = tk.Button(taskbar, text="Start", padx=10)
start_button.pack(side="left", padx=10, pady=5)

# Create the Programs button in the taskbar
programs_button = tk.Button(taskbar, text="Programs", padx=7)
programs_button.pack(side="left", padx=7, pady=5)

def open_start_menu():
    subprocess.run(["python", "start_menu.py"])

def open_programs_menu():
    subprocess.run(["python", "programs_menu.py"])

# Configure the Start button to open the Start menu
start_button.config(command=open_start_menu)

# Configure the Programs button to open the Programs menu
programs_button.config(command=open_programs_menu)

# Load the browser icon
browser_icon = tk.PhotoImage(file="C:\gptos\CAPOS C\capos\contents\icons/browser_icon.png")
browser_icon_resized = browser_icon.zoom(1, 1)  # Adjust the subsample factors to resize the icon

# Create the Browser button in the taskbar with the resized icon
browser_button = tk.Button(taskbar, image=browser_icon_resized, bg="black", borderwidth=0, command=open_browser)
browser_button.image = browser_icon_resized
browser_button.place(relx=0.2, rely=0.5, anchor="w")

# Load the calculator icon
calculator_icon = tk.PhotoImage(file="C:\gptos\CAPOS C\capos\contents\icons/calculator_icon.png")
calculator_icon_resized = calculator_icon.zoom(1, 1)

# Create the Calculator button in the taskbar with the resized icon
calculator_button = tk.Button(taskbar, image=calculator_icon_resized, bg="black", borderwidth=0, command=open_calculator)
calculator_button.image = calculator_icon_resized
calculator_button.place(relx=0.26, rely=0.5, anchor="w")

# Load the file explorer icon
file_explorer_icon = tk.PhotoImage(file="C:\gptos\CAPOS C\capos\contents\icons/file_explorer_icon.png")
file_explorer_icon_resized = file_explorer_icon.zoom(1, 1)

# Create the File Explorer button in the taskbar with the resized icon
file_explorer_button = tk.Button(taskbar, image=file_explorer_icon_resized, bg="black", borderwidth=0, command=open_file_explorer)
file_explorer_button.image = file_explorer_icon_resized
file_explorer_button.place(relx=0.32, rely=0.5, anchor="w")

# Load the desktop icon images and resize them
icon_browser_desktop = tk.PhotoImage(file="C:\gptos\CAPOS C\capos\contents\icons/browser_icon_desktop.png").subsample(8, 8)
icon_calculator_desktop = tk.PhotoImage(file="C:\gptos\CAPOS C\capos\contents\icons\calculator_icon_desktop.png").subsample(8, 8)

# Create the desktop icons
icon_browser_desktop_button = tk.Button(desktop, image=icon_browser_desktop, bg="blue", borderwidth=0, command=open_browser)
icon_browser_desktop_button.place(x=50, y=50)

icon_calculator_desktop_button = tk.Button(desktop, image=icon_calculator_desktop, bg="blue", borderwidth=0, command=open_calculator)
icon_calculator_desktop_button.place(x=45, y=130)

# Run the main event loop
window.mainloop()