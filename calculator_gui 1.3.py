import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from tkinter import font

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Futuristic Calculator")
        self.root.geometry("500x650")
        self.root.configure(bg='#1a1a1a')
        
        # Make window non-resizable
        self.root.resizable(False, False)
        
        # Variables
        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.result_var = tk.StringVar()
        
        # Custom Styles
        self.style = ttk.Style()
        self.style.configure('Modern.TFrame', background='#1a1a1a')
        self.style.configure('Modern.TButton',
                           font=('Helvetica', 12, 'bold'),
                           padding=15,
                           background='#2d2d2d',
                           foreground='#ffffff')
        self.style.configure('Title.TLabel',
                           font=('Helvetica', 24, 'bold'),
                           background='#1a1a1a',
                           foreground='#00ff9d')
        self.style.configure('Modern.TLabel',
                           font=('Helvetica', 12),
                           background='#1a1a1a',
                           foreground='#ffffff')
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main container
        main_frame = tk.Frame(self.root, bg='#1a1a1a', padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')
        
        # Result frame moved to top
        result_frame = tk.Frame(main_frame, bg='#2d2d2d', pady=10)
        result_frame.pack(fill='x', pady=(0, 20))  # Reduced top padding, added bottom margin
        
        # Create a calculator display-like result box
        result_display = tk.Frame(result_frame, 
                                bg='#232323',
                                highlightbackground='#00ff9d',
                                highlightthickness=2,
                                bd=0)
        result_display.pack(fill='x', padx=20)
        
        # Add inner frame for additional styling
        inner_display = tk.Frame(result_display,
                               bg='#1a1a1a',
                               padx=15,
                               pady=15)
        inner_display.pack(fill='x', padx=2, pady=2)
        
        result_label = tk.Label(inner_display,
                              textvariable=self.result_var,
                              font=('Consolas', 16, 'bold'),
                              bg='#1a1a1a',
                              fg='#00ff9d',
                              justify='right',
                              anchor='e',
                              width=30,
                              height=2)
        result_label.pack(expand=True)

        # Add a subtle "screen reflection" effect
        reflection = tk.Frame(result_display,
                            height=2,
                            bg='#00ff9d')
        reflection.pack(fill='x', padx=20)
        
        # Title with gradient effect - moved below result
        title_frame = tk.Frame(main_frame, bg='#1a1a1a')
        title_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(title_frame,
                             text="QUANTUM CALCULATOR",
                             font=('Helvetica', 24, 'bold'),
                             bg='#1a1a1a',
                             fg='#00ff9d')
        title_label.pack()
        
        # Subtitle
        subtitle_label = tk.Label(title_frame,
                                text="Advanced Computing Interface",
                                font=('Helvetica', 10),
                                bg='#1a1a1a',
                                fg='#00ff9d')
        subtitle_label.pack()
        
        # Input fields with modern styling
        input_frame = tk.Frame(main_frame, bg='#1a1a1a')
        input_frame.pack(fill='x', pady=20)
        
        # Custom Entry style
        entry_style = {
            'font': ('Helvetica', 14),
            'bg': '#2d2d2d',
            'fg': '#ffffff',
            'insertbackground': '#00ff9d',
            'relief': 'flat',
            'bd': 0
        }
        
        # First number
        tk.Label(input_frame,
                text="FIRST VALUE",
                font=('Helvetica', 10, 'bold'),
                bg='#1a1a1a',
                fg='#00ff9d').pack(anchor='w')
        
        entry1 = tk.Entry(input_frame,
                         textvariable=self.num1_var,
                         **entry_style)
        entry1.pack(fill='x', pady=(5, 15))
        
        # Second number
        tk.Label(input_frame,
                text="SECOND VALUE",
                font=('Helvetica', 10, 'bold'),
                bg='#1a1a1a',
                fg='#00ff9d').pack(anchor='w')
        
        entry2 = tk.Entry(input_frame,
                         textvariable=self.num2_var,
                         **entry_style)
        entry2.pack(fill='x', pady=5)
        
        # Operations frame
        operations_frame = tk.Frame(main_frame, bg='#1a1a1a')
        operations_frame.pack(fill='x', pady=20)
        
        # Operation buttons
        operations = [
            ("ADD", self.add, '#4CAF50'),
            ("SUBTRACT", self.subtract, '#2196F3'),
            ("MULTIPLY", self.multiply, '#9C27B0'),
            ("DIVIDE", self.divide, '#FF9800'),
            ("POWER", self.power, '#E91E63')
        ]
        
        # Create two rows of buttons
        for i, (text, command, color) in enumerate(operations):
            btn = tk.Button(operations_frame,
                          text=text,
                          command=command,
                          font=('Helvetica', 12, 'bold'),
                          bg=color,
                          fg='white',
                          relief='flat',
                          padx=20,
                          pady=15,
                          cursor='hand2')
            btn.grid(row=i//2, column=i%2, padx=5, pady=5, sticky='ew')
        
        operations_frame.grid_columnconfigure(0, weight=1)
        operations_frame.grid_columnconfigure(1, weight=1)
        
        # Clear button
        clear_btn = tk.Button(main_frame,
                            text="CLEAR",
                            command=self.clear,
                            font=('Helvetica', 12, 'bold'),
                            bg='#FF5252',
                            fg='white',
                            relief='flat',
                            padx=20,
                            pady=15,
                            cursor='hand2')
        clear_btn.pack(fill='x', pady=20)
        
        # Add hover effects
        self.add_button_hover_effects(clear_btn)
        for child in operations_frame.winfo_children():
            self.add_button_hover_effects(child)
            
    def add_button_hover_effects(self, button):
        original_color = button.cget('background')
        
        def on_enter(e):
            button['background'] = self.adjust_color(original_color, 1.1)
            
        def on_leave(e):
            button['background'] = original_color
            
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
        
    def adjust_color(self, color, factor):
        # Convert color to RGB
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        
        # Adjust colors
        r = min(255, int(r * factor))
        g = min(255, int(g * factor))
        b = min(255, int(b * factor))
        
        return f'#{r:02x}{g:02x}{b:02x}'

    # Your existing calculation methods remain the same
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
            result = num1 + num2
            self.result_var.set(f"{num1:g} + {num2:g} = {result:g}")
            
    def subtract(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            result = num1 - num2
            self.result_var.set(f"{num1:g} - {num2:g} = {result:g}")
            
    def multiply(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            result = num1 * num2
            self.result_var.set(f"{num1:g} × {num2:g} = {result:g}")
            
    def divide(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            try:
                result = num1 / num2
                self.result_var.set(f"{num1:g} ÷ {num2:g} = {result:g}")
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero!")
                
    def power(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            try:
                result = num1 ** num2
                self.result_var.set(f"{num1:g} ^ {num2:g} = {result:g}")
            except OverflowError:
                messagebox.showerror("Error", "Result too large!")
                
    def clear(self):
        self.num1_var.set("")
        self.num2_var.set("")
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernCalculator(root)
    root.mainloop() 