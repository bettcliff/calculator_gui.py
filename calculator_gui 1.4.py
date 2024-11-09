import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

class iPhoneCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("iPhone Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg='#000000')
        self.root.resizable(False, False)
        
        # Variables
        self.current_number = tk.StringVar(value="0")
        self.first_number = None
        self.operation = None
        self.should_reset = False
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main container
        main_frame = tk.Frame(self.root, bg='#000000', padx=10, pady=10)
        main_frame.pack(expand=True, fill='both')
        
        # Display Frame
        display_frame = tk.Frame(main_frame, bg='#000000', height=150)
        display_frame.pack(fill='x', pady=(50,20))
        display_frame.pack_propagate(False)
        
        # Result Label
        self.result_label = tk.Label(
            display_frame,
            textvariable=self.current_number,
            font=('Helvetica', 48, 'bold'),
            bg='#000000',
            fg='white',
            anchor='e',
            padx=20
        )
        self.result_label.pack(expand=True, fill='both')
        
        # Buttons Frame
        buttons_frame = tk.Frame(main_frame, bg='#000000')
        buttons_frame.pack(expand=True, fill='both')
        
        # Button layout
        buttons = [
            ('AC', '#A5A5A5', self.clear),
            ('±', '#A5A5A5', self.toggle_sign),
            ('%', '#A5A5A5', self.percentage),
            ('÷', '#FF9F0A', lambda: self.operation_clicked('/')),
            ('7', '#333333', lambda: self.number_clicked('7')),
            ('8', '#333333', lambda: self.number_clicked('8')),
            ('9', '#333333', lambda: self.number_clicked('9')),
            ('×', '#FF9F0A', lambda: self.operation_clicked('*')),
            ('4', '#333333', lambda: self.number_clicked('4')),
            ('5', '#333333', lambda: self.number_clicked('5')),
            ('6', '#333333', lambda: self.number_clicked('6')),
            ('−', '#FF9F0A', lambda: self.operation_clicked('-')),
            ('1', '#333333', lambda: self.number_clicked('1')),
            ('2', '#333333', lambda: self.number_clicked('2')),
            ('3', '#333333', lambda: self.number_clicked('3')),
            ('+', '#FF9F0A', lambda: self.operation_clicked('+')),
            ('0', '#333333', lambda: self.number_clicked('0')),
            ('.', '#333333', lambda: self.number_clicked('.')),
            ('=', '#FF9F0A', self.calculate)
        ]
        
        # Create and place buttons
        row = 0
        col = 0
        for (text, color, command) in buttons:
            button = tk.Button(
                buttons_frame,
                text=text,
                font=('Helvetica', 24),
                fg='white',
                bg=color,
                activebackground=color,
                activeforeground='white',
                relief='flat',
                command=command
            )
            
            # Make '0' button twice as wide
            if text == '0':
                button.grid(row=row, column=col, columnspan=2, pady=5, padx=5, sticky='nsew')
                col += 2
            else:
                button.grid(row=row, column=col, pady=5, padx=5, sticky='nsew')
                col += 1
            
            # Configure button to be circular
            button.configure(width=2, height=1)
            
            if col > 3:
                col = 0
                row += 1
        
        # Configure grid
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
            
    def number_clicked(self, number):
        if self.should_reset:
            self.current_number.set('0')
            self.should_reset = False
            
        current = self.current_number.get()
        if current == '0' and number != '.':
            self.current_number.set(number)
        else:
            self.current_number.set(current + number)
            
    def operation_clicked(self, op):
        self.first_number = float(self.current_number.get())
        self.operation = op
        self.should_reset = True
        
    def calculate(self):
        if self.operation and self.first_number is not None:
            second_number = float(self.current_number.get())
            try:
                if self.operation == '+':
                    result = self.first_number + second_number
                elif self.operation == '-':
                    result = self.first_number - second_number
                elif self.operation == '*':
                    result = self.first_number * second_number
                elif self.operation == '/':
                    if second_number == 0:
                        self.current_number.set('Error')
                        return
                    result = self.first_number / second_number
                    
                # Format result
                if result.is_integer():
                    self.current_number.set(int(result))
                else:
                    self.current_number.set(f"{result:.7f}".rstrip('0').rstrip('.'))
                    
            except Exception:
                self.current_number.set('Error')
                
            self.first_number = None
            self.operation = None
            self.should_reset = True
            
    def clear(self):
        self.current_number.set('0')
        self.first_number = None
        self.operation = None
        self.should_reset = False
        
    def toggle_sign(self):
        current = self.current_number.get()
        if current != '0':
            if current.startswith('-'):
                self.current_number.set(current[1:])
            else:
                self.current_number.set('-' + current)
                
    def percentage(self):
        try:
            current = float(self.current_number.get())
            result = current / 100
            if result.is_integer():
                self.current_number.set(int(result))
            else:
                self.current_number.set(str(result))
        except ValueError:
            self.current_number.set('Error')

if __name__ == "__main__":
    root = tk.Tk()
    app = iPhoneCalculator(root)
    root.mainloop()