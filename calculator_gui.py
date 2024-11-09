import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")
        
        # Style configuration
        style = ttk.Style()
        style.configure("TButton", padding=10, font=('Helvetica', 10))
        style.configure("TLabel", padding=10, font=('Helvetica', 12))
        style.configure("TEntry", padding=10, font=('Helvetica', 12))
        
        # Variables
        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.result_var = tk.StringVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Advanced Calculator", 
                              font=('Helvetica', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # First number
        ttk.Label(main_frame, text="First Number:").grid(row=1, column=0, sticky=tk.W)
        num1_entry = ttk.Entry(main_frame, textvariable=self.num1_var)
        num1_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Second number
        ttk.Label(main_frame, text="Second Number:").grid(row=2, column=0, sticky=tk.W)
        num2_entry = ttk.Entry(main_frame, textvariable=self.num2_var)
        num2_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Operations frame
        operations_frame = ttk.LabelFrame(main_frame, text="Operations", padding="10")
        operations_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        # Operation buttons
        operations = [
            ("Add", self.add),
            ("Subtract", self.subtract),
            ("Multiply", self.multiply),
            ("Divide", self.divide),
            ("Power", self.power)
        ]
        
        for i, (text, command) in enumerate(operations):
            btn = ttk.Button(operations_frame, text=text, command=command)
            btn.grid(row=i//2, column=i%2, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        # Result
        result_frame = ttk.LabelFrame(main_frame, text="Result", padding="10")
        result_frame.grid(row=4, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        result_label = ttk.Label(result_frame, textvariable=self.result_var,
                               font=('Helvetica', 12, 'bold'))
        result_label.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Clear button
        ttk.Button(main_frame, text="Clear", command=self.clear).grid(
            row=5, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
    def get_numbers(self):
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
            return None, None
        
    def add(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            self.result_var.set(f"{num1} + {num2} = {num1 + num2}")
            
    def subtract(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            self.result_var.set(f"{num1} - {num2} = {num1 - num2}")
            
    def multiply(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            self.result_var.set(f"{num1} × {num2} = {num1 * num2}")
            
    def divide(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            try:
                result = num1 / num2
                self.result_var.set(f"{num1} ÷ {num2} = {result}")
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero!")
                
    def power(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            try:
                result = num1 ** num2
                self.result_var.set(f"{num1} ^ {num2} = {result}")
            except OverflowError:
                messagebox.showerror("Error", "Result too large!")
                
    def clear(self):
        self.num1_var.set("")
        self.num2_var.set("")
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop() 