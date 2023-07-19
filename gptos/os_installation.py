import tkinter as tk
from tkinter import messagebox
import time

def simulate_os_installation():
    # Define the list of tips
    tips = [
        "Tip: You can only see your background change once you restart the OS.",
        "Tip: The minesweeper game is coded in Python, which doesn't use Pygame.",
        "Tip: Most of the icons in minesweeper are 16 by 16 which means they're small. That's why!",
        "Tip: The taskbar icons are 24 by 24 and resized using Python.",
        "Tip: Most of the OS requires Python and a whole lot of libraries.",
        "Tip: You can get product keys for free, but these are not actual real product keys. It's for the OS simulation!"
    ]

    # Create the installation window
    window = tk.Tk()
    window.title("OS Installation")
    window.geometry("600x400")  # Set the window size here

    # Create a label to display the installation progress
    progress_label = tk.Label(window, text="Installing Cap OS...")
    progress_label.pack(pady=20)

    # Create a label for displaying the tips
    tip_label = tk.Label(window, text="")
    tip_label.pack()

    # Create a label for the loading animation
    loading_label = tk.Label(window, text="")
    loading_label.pack()

    # Define the animation characters
    animation_chars = [".", "..", "..."]

    # Simulate installation process
    for i in range(41):
        # Update the installation progress
        progress_label.configure(text=f"Installing Cap OS ({i+1}/41)")

        # Display the tip every 6 seconds
        if i % 6 == 0:
            tip_index = i // 6  # Calculate the index of the tip to display
            tip_label.configure(text=tips[tip_index])

        # Update the loading animation
        loading_label.configure(text=animation_chars[i % len(animation_chars)])

        # Update the window
        window.update()

        # Simulate installation delay
        time.sleep(0.4)

    # Show installation complete message
    messagebox.showinfo("Installation Complete", "Cap OS installation is complete!")

    # Close the installation window
    window.destroy()

# Entry point for the installation script
if __name__ == "__main__":
    simulate_os_installation()