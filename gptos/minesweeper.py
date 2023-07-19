import tkinter as tk
from tkinter import messagebox
import random

class Minesweeper(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Minesweeper")
        self.geometry("400x430")  # Set the window size here

        self.board_size = 10
        self.num_mines = 10

        self.create_board()
        self.place_mines()
        self.calculate_numbers()

        self.smiley_icon = tk.PhotoImage(file="C:\gptos\CAPOS C\capos\contents\icons\smiley.png").zoom(2)
        self.dead_icon = tk.PhotoImage(file="C:\gptos\CAPOS C\capos\contents\icons\dead.png").zoom(2)
        self.win_icon = tk.PhotoImage(file="C:\gptos\CAPOS C\capos\contents\icons\win.png").zoom(2)
        self.flag_icon = tk.PhotoImage(file="C:\gptos\CAPOS C\capos\contents\icons/flag.png").zoom(2, 2)
        self.bomb_icon = tk.PhotoImage(file="C:\gptos\CAPOS C\capos\contents\icons/bomb.png").zoom(2, 2)

        self.smiley_button = tk.Button(self, image=self.smiley_icon, command=self.reset_game)
        self.smiley_button.place(relx=0.5, rely=0.06, anchor="center")

        self.flags = self.num_mines
        self.flag_label = tk.Label(self, text=f"Flags: {self.flags}")
        self.flag_label.place(relx=0.15, rely=0.06, anchor="center")

        self.score = 0
        self.score_label = tk.Label(self, text=f"Score: {self.score}")
        self.score_label.place(relx=0.85, rely=0.06, anchor="center")

    def create_board(self):
        self.buttons = []
        for row in range(self.board_size):
            button_row = []
            for col in range(self.board_size):
                button = tk.Button(self, width=4, height=2, command=lambda r=row, c=col: self.handle_click(r, c))
                button.bind("<Button-3>", lambda event, r=row, c=col: self.toggle_flag(event, r, c))
                button.grid(row=row+1, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def place_mines(self):
        mines = random.sample(range(self.board_size ** 2), self.num_mines)
        for mine in mines:
            row = mine // self.board_size
            col = mine % self.board_size
            self.buttons[row][col].mine = True

    def calculate_numbers(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if not hasattr(self.buttons[row][col], "mine"):
                    count = self.count_adjacent_mines(row, col)
                    self.buttons[row][col].count = count

    def count_adjacent_mines(self, row, col):
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx = row + dx
                ny = col + dy
                if nx >= 0 and nx < self.board_size and ny >= 0 and ny < self.board_size:
                    if hasattr(self.buttons[nx][ny], "mine"):
                        count += 1
        return count

    def handle_click(self, row, col):
        button = self.buttons[row][col]
        if hasattr(button, "flag"):
            return

        if hasattr(button, "mine"):
            button.configure(image=self.bomb_icon, state="disabled", relief=tk.SUNKEN)
            self.game_over()
        else:
            count = button.count
            if count > 0:
                button.configure(text=str(count), state="disabled", relief=tk.SUNKEN)
            else:
                button.configure(state="disabled", relief=tk.SUNKEN)
                self.reveal_empty_cells(row, col)
                self.score += 1
                self.score_label.configure(text=f"Score: {self.score}")

        if self.check_win():
            self.smiley_button.configure(image=self.win_icon)

    def reveal_empty_cells(self, row, col):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx = row + dx
                ny = col + dy
                if nx >= 0 and nx < self.board_size and ny >= 0 and ny < self.board_size:
                    button = self.buttons[nx][ny]
                    if not hasattr(button, "mine") and button["state"] == tk.NORMAL:
                        self.handle_click(nx, ny)

    def game_over(self):
        self.smiley_button.configure(image=self.dead_icon)
        choice = messagebox.askquestion("Game Over", "You hit a mine! Do you want to restart?")
        if choice == "yes":
            self.reset_game()
        else:
            self.destroy()

    def check_win(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                button = self.buttons[row][col]
                if not hasattr(button, "mine") and button["state"] != tk.DISABLED:
                    return False
        return True

    def reset_game(self):
        self.smiley_button.configure(image=self.smiley_icon)
        self.flags = self.num_mines
        self.flag_label.configure(text=f"Flags: {self.flags}")
        self.score = 0
        self.score_label.configure(text=f"Score: {self.score}")
        for row in range(self.board_size):
            for col in range(self.board_size):
                button = self.buttons[row][col]
                button.configure(text="", state=tk.NORMAL, relief=tk.RAISED)
                if hasattr(button, "mine"):
                    del button.mine
                if hasattr(button, "flag"):
                    del button.flag

    def toggle_flag(self, event, row, col):
        button = self.buttons[row][col]
        if button["state"] != tk.DISABLED:
            if not hasattr(button, "flag"):
                if self.flags > 0:
                    button.configure(image=self.flag_icon)
                    button.flag = True
                    self.flags -= 1
            else:
                button.configure(image="", text="")
                del button.flag
                self.flags += 1
            self.flag_label.configure(text=f"Flags: {self.flags}")

if __name__ == "__main__":
    minesweeper = Minesweeper()
    minesweeper.mainloop()