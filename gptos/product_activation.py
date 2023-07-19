import tkinter as tk
from tkinter import messagebox

VALID_KEYS = ["CAPOS-52-UI-HOME", "CAPOS-20-ER-HOME", "CAPOS-560-YTU-PRO", "CAPOS-562-YTI-PRO", "CAPOS-01-HJ-HOME", "CAPOS-00-XA-HOME"]

def activate_product():
    user_input = entry.get()

    if user_input in VALID_KEYS:
        with open("productkey.txt", "w") as file:
            file.write(user_input)
        messagebox.showinfo("Activation", "Product activated successfully!")
    else:
        messagebox.showerror("Invalid product key", "Invalid activation key.")

# Create the main window
window = tk.Tk()
window.title("Product Activation")
window.geometry("800x150")

# Create the label and entry for entering the activation key
label = tk.Label(window, text="Enter activation key:")
label.pack(pady=10)
entry = tk.Entry(window, show="X")
entry.pack()

# Create the activate button
activate_button = tk.Button(window, text="Activate", command=activate_product)
activate_button.pack(pady=10)

# Run the main event loop
window.mainloop()