import os
import subprocess
import tkinter as tk
import sys

class RedirectText:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)

    def flush(self):
        pass

# Define the commands and their corresponding programs
commands = {
    "open catbrowser": "browser.py",
    "open calculator": "calculator.py",
    "open game-minesweeper": "minesweeper.py",
    "open organizer": "C:/gptos/CAPOS C/capos/systemapps/fileorganizer.py"
}

def run_command(command):
    # Check if the command exists
    if command in commands:
        program = commands[command]
        script_path = os.path.join(os.path.dirname(__file__), program)
        subprocess.Popen(["python", script_path], cwd=os.path.dirname(__file__))
        success_message = f"The operation completed successfully. Executed program: {program}"
        output_area.insert(tk.END, success_message + "\n")
        return True
    elif command == "exit" or command == "quit":
        sys.exit()
    else:
        output_area.insert(tk.END, f"The command {command}\nwas not recognised as a valid prompt in CAPOS, if you think this is an error install anything related to this command, and it should work.")
        return False

def handle_command(event):
    # Get the command from the input line
    input_start = output_area.index("end-2l lineend")
    input_end = output_area.index(tk.END).strip()
    command = output_area.get(input_start, input_end).strip()

    # Clear the input line
    output_area.delete(input_start, tk.END)

    # Run the command and display the success message
    if run_command(command):
        output_area.insert(tk.END, "CAPOS C/> ")

# Create the command prompt window
window = tk.Tk()
window.title("CAPOS Prompting")
window.geometry("800x600")

# Configure font settings
font_family = "Consolas"
font_size = 12

# Create the output area
output_area = tk.Text(window, font=(font_family, font_size), bg="black", fg="white", wrap="word")
output_area.pack(fill="both", expand=True)

# Redirect standard output to the output area
original_stdout = sys.stdout
sys.stdout = RedirectText(output_area)

# Set the input prompt
output_area.insert(tk.END, "CAPOS C/> ")

# Bind Enter key to handle command
output_area.bind("<Return>", handle_command)

# Run the main event loop
window.mainloop()