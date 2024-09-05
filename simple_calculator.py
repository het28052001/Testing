import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.label1 = tk.Label(master, text="Number 1:")
        self.label1.pack()

        self.entry1 = tk.Entry(master)
        self.entry1.pack()

        self.label2 = tk.Label(master, text="Number 2:")
        self.label2.pack()

        self.entry2 = tk.Entry(master)
        self.entry2.pack()

        self.add_button = tk.Button(master, text="Add", command=self.add_numbers)
        self.add_button.pack()

    def add_numbers(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = num1 + num2
            messagebox.showinfo("Result", f"The sum is: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
calculator = SimpleCalculator(root)
root.mainloop()