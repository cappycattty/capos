import tkinter as tk
from tkinter import messagebox
import os

def activate_product_key():
    if os.path.isfile("user_details.txt"):
        try:
            with open("productkey.txt", "r") as file:
                product_key = file.read()
            messagebox.showinfo("Activation", f"Product key:\n{product_key}")
        except FileNotFoundError:
            messagebox.showerror("Could not find details", "Couldn't find details for product key. Did you forget to activate CapOS?")
    else:
        messagebox.showerror("No User Details", "Product key could not be loaded because no username is set.")

def set_username():
    username = username_entry.get().strip()
    if username:
        # Create the user folder
        folder_path = os.path.join("C:/gptos/CAPOS C/capos/users", username)
        os.makedirs(folder_path, exist_ok=True)
        
        # Create subfolders
        subfolders = ["Programs", "Downloads", "Pictures", "Media"]
        for subfolder in subfolders:
            subfolder_path = os.path.join(folder_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)
        
        with open("user_details.txt", "w") as file:
            file.write(username)
        
        messagebox.showinfo("Username Set", f"Username '{username}' has been set.")
    else:
        messagebox.showerror("Invalid Username", "Please enter a valid username.")

# Create the user account window
window = tk.Tk()
window.title("User Account")
window.geometry("300x200")  # Set the window size here

# Create the username label and entry
username_label = tk.Label(window, text="Username:")
username_label.pack()

username_entry = tk.Entry(window)
username_entry.pack()

# Create the set username button
set_username_button = tk.Button(window, text="Set Username", command=set_username)
set_username_button.pack()

# Create the activation button
activate_button = tk.Button(window, text="Activate Product Key", command=activate_product_key)
activate_button.pack()

# Run the main event loop
window.mainloop()