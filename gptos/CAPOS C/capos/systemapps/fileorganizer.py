import os
import tkinter as tk
from tkinter import ttk

def browse_directory(directory, parent=""):
    if parent:
        file_tree.delete(*file_tree.get_children(parent))
    else:
        file_tree.delete(*file_tree.get_children())
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            item_id = file_tree.insert(parent, "end", text=item, values=("Folder", item_path))
            file_tree.insert(item_id, "end")  # Placeholder for sub-items
        else:
            item_type = "File"
            item_name, item_ext = os.path.splitext(item)
            if item_ext == ".py":
                item_name += ".exe"  # Append fake .exe extension for Python scripts
            item_path = item_path.replace(".py", ".exe")  # Replace .py with .exe in path for display purposes
            file_tree.insert(parent, "end", text=item_name, values=(item_type, item_path))

def toggle_item(event):
    item_id = file_tree.focus()
    if file_tree.item(item_id, "open"):
        file_tree.item(item_id, open=False)
    else:
        item_type = file_tree.item(item_id, "values")[0]
        if item_type == "Folder":
            item_path = file_tree.item(item_id, "values")[1]
            browse_directory(item_path, parent=item_id)

# Create the file explorer window
window = tk.Tk()
window.title("File Explorer")
window.geometry("800x600")

# Define the directory to browse
directory = "C:/gptos/CAPOS C"

# Create the file tree
file_tree = ttk.Treeview(window, columns=("Type", "Path"), show="tree")
file_tree.heading("#0", text="Name")
file_tree.heading("Type", text="Type")
file_tree.heading("Path", text="Path")
file_tree.pack(fill="both", expand=True)

# Bind double-click event to toggle item expansion
file_tree.bind("<Double-1>", toggle_item)

# Browse the directory initially
browse_directory(directory)

# Run the main event loop
window.mainloop()