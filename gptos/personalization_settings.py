import tkinter as tk
from tkinter import messagebox
import os

# Color dictionary with predefined colors
COLORS = {
    "Red": "#FF0000",
    "Dark Red": "#8B0000",
    "Light Blue": "#ADD8E6",
    "Blue": "#0000FF",
    "Gray": "#808080",
    "White": "#FFFFFF",
    "Green": "#00FF00",
    "Dark Green": "#006400",
    "Lime": "#00FF00",
    "Gold": "#FFD700",
    "Pink": "#FFC0CB",
    "Purple": "#800080",
    "Dark Purple": "#483D8B",
    "Dark Blue": "#00008B"
}

def set_background_color(color):
    with open("bgcolor.txt", "w") as file:
        file.write(COLORS[color])
    messagebox.showinfo("Background Color", f"Background color set to {color}, Restart your OS to apply the changes")
    # Update the background color of the window
    window.configure(bg=COLORS[color])

def read_background_color():
    if os.path.exists("bgcolor.txt"):
        with open("bgcolor.txt", "r") as file:
            color = file.read().strip()
            return color
    return None

# Create the main window
window = tk.Tk()
window.title("Capcat OS 1.00")

# Example usage
color = read_background_color()
if color:
    window.configure(bg=color)

# Create color buttons
for color_name in COLORS:
    button = tk.Button(window, text=color_name, command=lambda c=color_name: set_background_color(c))
    button.pack(padx=10, pady=5)

# Run the main event loop
window.mainloop()