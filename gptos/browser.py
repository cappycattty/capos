import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrolledtext
import webbrowser

class GPTBrowser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cat Browser")
        self.geometry("800x600")  # Set the window size here

        self.url_entry = ttk.Entry(self)
        self.url_entry.pack(side=tk.TOP, fill=tk.X)

        self.go_button = ttk.Button(self, text="Go", command=self.load_page)
        self.go_button.pack(side=tk.TOP, pady=5)

        self.web_view = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.web_view.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def load_page(self):
        url = self.url_entry.get()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url

        try:
            response = webbrowser.open(url)
            if not response:
                self.web_view.insert(tk.END, "Failed to load the page.")
        except webbrowser.Error:
            self.web_view.insert(tk.END, "An error occurred while loading the page.")

if __name__ == "__main__":
    browser = GPTBrowser()
    browser.mainloop()