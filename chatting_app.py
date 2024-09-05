import tkinter as tk

class ChattingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatting")
        self.create_widgets()

    def create_widgets(self):
        self.text_area = tk.Text(self.root)
        self.text_area.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()

    def send_message(self):
        message = self.entry.get()
        self.text_area.insert(tk.END, "You: " + message + "\n")
        self.entry.delete(0, tk.END)