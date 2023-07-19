import tkinter as tk
import subprocess

def open_user_account():
    print("Opening User Account settings...")

def open_personalization():
    subprocess.run(["python", "personalization_settings.py"])

def open_system_settings():
    print("Opening System settings...")

def open_languages():
    print("Opening Languages settings...")

def open_storage():
    print("Opening Storage settings...")

def open_gpt_os_updater():
    print("Opening GPT OS Updater...")

# Create the main window
window = tk.Tk()
window.title("GPT OS Simulator")
window.geometry("600x600")  # Set window size to 800x800

# Create buttons for each setting
user_account_button = tk.Button(window, text="User Account", command=open_user_account)
user_account_button.pack()

personalization_button = tk.Button(window, text="Personalization", command=open_personalization)
personalization_button.pack()

system_settings_button = tk.Button(window, text="System Settings", command=open_system_settings)
system_settings_button.pack()

languages_button = tk.Button(window, text="Languages", command=open_languages)
languages_button.pack()

storage_button = tk.Button(window, text="Storage", command=open_storage)
storage_button.pack()

gpt_os_updater_button = tk.Button(window, text="GPT OS Updater", command=open_gpt_os_updater)
gpt_os_updater_button.pack()

# Start the Tkinter event loop
window.mainloop()