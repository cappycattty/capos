import tkinter as tk
import subprocess

class StartMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Start Menu")
        self.geometry("300x400")  # Set the window size here

        self.create_user_button()
        self.create_icons()
        self.create_power_options()

    def create_user_button(self):
        user_button = tk.Button(self, text="User", padx=10, pady=5, command=self.open_user_menu)
        user_button.pack(side=tk.TOP, padx=10, pady=10)

    def create_icons(self):
        icon_frame = tk.Frame(self)
        icon_frame.pack(side=tk.TOP, padx=10, pady=10)

        # Create the browser icon
        browser_icon = tk.PhotoImage(file="C:\gptos\CAPOS C\capos\contents\icons/browser_icon.png")
        browser_icon_resized = browser_icon.subsample(1, 1)
        browser_button = tk.Button(icon_frame, image=browser_icon_resized, command=self.open_browser)
        browser_button.image = browser_icon_resized
        browser_button.grid(row=0, column=0, padx=10, pady=10)

        # Create the calculator icon
        calculator_icon = tk.PhotoImage(file="C:\gptos\CAPOS C\capos\contents\icons\calculator_icon.png")
        calculator_icon_resized = calculator_icon.subsample(1, 1)
        calculator_button = tk.Button(icon_frame, image=calculator_icon_resized, command=self.open_calculator)
        calculator_button.image = calculator_icon_resized
        calculator_button.grid(row=0, column=1, padx=10, pady=10)

        # Create the minesweeper icon
        minesweeper_icon = tk.PhotoImage(file="C:\gptos\CAPOS C\capos\contents\icons\minesweeper_icon.png")
        minesweeper_icon_resized = minesweeper_icon.subsample(30, 30)
        minesweeper_button = tk.Button(icon_frame, image=minesweeper_icon_resized, command=self.open_minesweeper)
        minesweeper_button.image = minesweeper_icon_resized
        minesweeper_button.grid(row=1, column=0, padx=10, pady=10)

        # Create the settings icon
        settings_icon = tk.PhotoImage(file="C:\gptos\CAPOS C\capos\contents\icons\settings_icon.png")
        settings_icon_resized = settings_icon.subsample(18, 18)
        settings_button = tk.Button(icon_frame, image=settings_icon_resized, command=self.open_settings)
        settings_button.image = settings_icon_resized
        settings_button.grid(row=1, column=1, padx=10, pady=10)

        # Create the command prompt icon
        command_prompt_icon = tk.PhotoImage(file="C:\gptos\CAPOS C\capos\contents\icons\command_prompt_icon.png")
        command_prompt_icon_resized = command_prompt_icon.zoom(1, 1)
        command_prompt_button = tk.Button(icon_frame, image=command_prompt_icon_resized, command=self.open_commandprompt)
        command_prompt_button.image = command_prompt_icon_resized
        command_prompt_button.grid(row=2, column=0, padx=10, pady=10)

    def create_power_options(self):
        power_options_frame = tk.Frame(self)
        power_options_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

        # Create the shutdown button
        shutdown_button = tk.Button(power_options_frame, text="Shutdown", padx=10, pady=5, command=self.shutdown)
        shutdown_button.pack(side=tk.LEFT, padx=5)

        # Create the restart button
        restart_button = tk.Button(power_options_frame, text="Restart", padx=10, pady=5, command=self.restart)
        restart_button.pack(side=tk.LEFT, padx=5)

    def open_user_menu(self):
        subprocess.run(["python", "user_menu.py"])

    def open_browser(self):
        subprocess.run(["python", "browser.py"])

    def open_calculator(self):
        subprocess.run(["python", "C:/gptos/CAPOS C/capos/systemapps/calculator.py"])

    def open_minesweeper(self):
        subprocess.run(["python", "minesweeper.py"])

    def open_settings(self):
        subprocess.run(["python", "settings.py"])

    def open_commandprompt(self):
        subprocess.run(["python", "C:/gptos/CAPOS C/capos/systemapps/commandprompt.py"])    

    def shutdown(self):
        # implement
        pass

    def restart(self):
        # Implement your restart logic here
        pass

if __name__ == "__main__":
    start_menu = StartMenu()
    start_menu.mainloop()