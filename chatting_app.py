import tkinter as tk

class ChattingApp:
    def __init__(self, master):
        self.master = master
        master.title("Chatting")
        
        self.label = tk.Label(master, text="Welcome to the Chatting App!")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack()

    def send_message(self):
        message = self.entry.get()
        print(f"Message sent: {message}")
        self.entry.delete(0, tk.END)

root = tk.Tk()
chatting_app = ChattingApp(root)
root.mainloop()