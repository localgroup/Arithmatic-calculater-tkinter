import tkinter as tk
from tkinter import messagebox, ttk


class Calculator:
    def __init__(self):
        self.result = None
        # Create the window
        self.window = tk.Tk()
        self.window.geometry("490x220+300+250")
        
        self.window.title("Arithmetic Calculator")
        self.window.config(padx=30, pady=30, bg="antique white")

        self.num1_label = tk.Label(text="Input", font=("Ariel", 12, "italic"), bg="antique white")
        self.num1_label.grid(column=0, row=0)
        self.num2_label = tk.Label(text="Input", font=("Ariel", 12, "italic"), bg="antique white")
        self.num2_label.grid(column=0, row=1)

        self.num1_input = tk.Entry(width=16, font=("Ariel", 12, "bold"), bg="gray64")
        self.num1_input.grid(column=1, row=0, columnspan=3)
        self.num1_input.focus()
        self.num1_input.insert(0, "")
        self.num2_input = tk.Entry(width=16, font=("Ariel", 12, "bold"), bg="gray64")
        self.num2_input.grid(column=1, row=1, columnspan=3)
        self.num2_input.insert(0, "")

        self.get_button = tk.Button(self.window, text="Add", command=self.add)
        self.get_button.grid(column=0, row=3, padx=(50, 10), pady=10)
        self.get_button = tk.Button(self.window, text="Subtract", command=self.sub)
        self.get_button.grid(column=1, row=3, padx=10, pady=10)
        self.get_button = tk.Button(self.window, text="Multiply", command=self.mul)
        self.get_button.grid(column=2, row=3, padx=10, pady=10)
        self.get_button = tk.Button(self.window, text="Divide", command=self.div)
        self.get_button.grid(column=3, row=3, padx=(10, 50), pady=10)
        self.get_button = tk.Button(self.window, text="Clear", command=self.clear, bg="red")
        self.get_button.grid(column=4, row=1, padx=(10, 50), pady=10)
        ttk.Button(text="Quit", command=self.window.destroy).grid(column=4, row=2)

        self.output_label = tk.Label(text="Output ", font=("Ariel", 12, "italic"), bg="antique white")
        self.output_label.grid(column=0, row=2)
        self.output = tk.Label(width=16, text=" ", font=("Ariel", 12, "italic"), bg="gray64")
        self.output.grid(column=1, row=2, columnspan=3)

    def if_string(self):
        """
        Checks if the given input is a valid number and returns a boolean.
        """
        try:
            float(self.num1_input.get())
            float(self.num2_input.get())
            return True
        except ValueError:
            messagebox.showerror("Error", "Enter valid numbers!")
            return False

    def if_empty(self):
        """
        Checks if the input fields are left empty and responds in terms of boolean.
        """
        if self.num1_input.get() == "" or self.num2_input.get() == "":
            messagebox.showerror("Error", "Fields cannot be left empty!")
            return True
        return False

    def get_float(self) -> tuple:
        """
        Returns the float equivalent of the input value, if it's a valid number.
        """
        float_value_1 = float(self.num1_input.get())
        float_value_2 = float(self.num2_input.get())
        return float_value_1, float_value_2

    def add(self):
        """
        Adds the inputs.
        """
        if not self.if_empty() and self.if_string():
            float_value_1, float_value_2 = self.get_float()
            self.result = round((float_value_1 + float_value_2), 4)
            self.output.config(text=str(self.result))
            self.next_operation()

    def sub(self):
        """
        Subtracts the inputs.
        """
        if not self.if_empty() and self.if_string():
            float_value_1, float_value_2 = self.get_float()
            self.result = round((float_value_1 - float_value_2), 4)
            self.output.config(text=str(self.result))
            self.next_operation()

    def div(self):
        """
        Divides the inputs.
        """
        if not self.if_empty() and self.if_string():
            float_value_1, float_value_2 = self.get_float()
            if float_value_2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed!")
            else:
                self.result = round((float_value_1 / float_value_2), 4)
                self.output.config(text=str(self.result))
                self.next_operation()

    def mul(self):
        """
        Multiplies the inputs.
        """
        if not self.if_empty() and self.if_string():
            float_value_1, float_value_2 = self.get_float()
            self.result = round((float_value_1 * float_value_2), 4)
            self.output.config(text=str(self.result))
            self.next_operation()

    def next_operation(self):
        """
        Prepares the input fields for the next operation by updating the input fields.
        """
        current_result = self.output.cget("text")
        self.num1_input.delete(0, tk.END)
        self.num1_input.insert(0, str(current_result))
        self.output.config(text=str(current_result))
        self.num2_input.delete(0, tk.END)

    def clear(self):
        """
        Clears the input fields.
        """
        self.num1_input.delete(0, tk.END)
        self.num1_input.focus()
        self.num2_input.delete(0, tk.END)
        self.output.config(text="")

    def run(self):
        """
        Runs the mainloop.
        """
        self.window.mainloop()


calculation = Calculator()
calculation.run()
