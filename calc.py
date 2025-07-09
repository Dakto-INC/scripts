import time
import math
import webbrowser
import tkinter as tk
from fractions import Fraction

# Welcome message
print("Welcome to Dakto INC Calculator")
time.sleep(1)
print("\n---------------------------------------------------------------\n")

# Memory
memory = None
history = []

# CLI
class Calculator:
    def add(self, x, y):
        return x + y 

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x - y

    def divide(self, x, y):
        if y == 0:
            return "Can't divide by zero"
        return x / y
    
    def power(self, x, y):
        return math.pow(x, y)
    
    def sqrt(self, x):
        return math.sqrt(x)
    
    def sin(self, x):
        return math.sin(math.radians(x))
    
    def cos(self, x):
        return math.cos(math.radians(x))
    
    def tan(self, x):
        return math.tan(math.radians(x))
    
    def log(self, x):
        return math.log(x)
    
    def ln(self, x):
        return math.log(x)
    
    def factorial(self, x):
        return math.factorial(int(x))
    
    def dec2frac(self, x):
        return Fraction(str(x)).limit_denominator()

def run_cli():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    time.sleep(0.1)

    print("\n---------------------------------------------------------------")
    print("\nCalculating equations...")
    time.sleep(2)

    calc = Calculator()
    print("\nAnswers:")
    print("Addition:", calc.add(num1, num2))
    print("Subtraction:", calc.subtract(num1, num2))
    print("Multiplication:", calc.multiply(num1, num2))
    print("Division:", calc.divide(num1, num2))

    # CLI Exit Message
    print("\n---------------------------------------------------------------")
    print("\nThank you for using Dakto INC Calculator")

def run_cli_scientific():
    calc = Calculator()
    print("\nScientific Answers: ")
    print("1. Power (x^y)\n2. Square Root\n3. Sin\n4. Cos\n5. Tan\n6. Log\n7. Ln\n8. Factorial\n9. Fraction Addition")
    science = input("Choose an operation [1-9]: ").strip()
    
    try:
        if science == '1':
            x = float(input("Enter base: "))
            y = float(input("Enter exponent: "))
            print("Result: ", calc.power(x, y))
        elif science == '2':
            x = float(input("Enter number: "))
            print("Result: ", calc.sqrt(x))
        elif science == '3':
            x = float(input("Enter angle in degrees: "))
            print("Result:", calc.sin(x))
        elif science == '4':
            x = float(input("Enter angle in degrees: "))
            print("Result: ", calc.cos(x))
        elif science == '5':
            x = float(input("Enter angle in degrees: "))
            print("Result: ", calc.tan(x))
        elif science == '6':
            x = float(input("Enter number: "))
            print("Result: ", calc.log(x))
        elif science == '7':
            x = float(input("Enter number: "))
            print("Result: ", calc.ln(x))
        elif science == '8':
            x = float(input("Enter interger: "))
            print("Result: ", calc.factorial(x))
        elif science == '9':
            x = float(input("Enter decimal number: "))
            print("Fraction: ", calc.dec2frac(x))
        else:
            print("Invalid choice")
    except Exception as e:
        print("Error:", e)



# GUI

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        allowed_names = {**vars(math), "Fraction": Fraction}
        result = eval(expr, {"__builtins__": None}, allowed_names)
        display.set(str(result))
        history.append(f"{expr} = {result}")
        expr = str(result)
    except Exception as e:
        display.set("An error occurred")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

def dec_to_frac():
    global expr
    try:
        if not expr:
            display.set("Nothing to convert")
            return
        allowed_names = {**vars(math), "Fraction": Fraction}
        value = eval(expr, {"__builtins__": None}, allowed_names)
        fraction = Fraction(str(value)).limit_denominator()
        display.set(str(fraction))
        expr = str(fraction)
    except Exception as e:
        display.set("An error occurred")
        expr = ""

def memory_save():
    global memory, expr
    try:
        memory = eval(expr, {"__builtins__": None}, {**vars(math), "Fraction": Fraction})
        display.set("Saved")
        expr = ""
    except:
        display.set("Error")
        expr = ""

def memory_recall():
    global expr
    if memory is not None:
        expr += str(memory)
        display.set(expr)
    else:
        display.set("Empty")

def memory_clear():
    global memory
    memory = None
    display.set("Memory Cleared")

def show_history():
    if history:
        display.set("\n".join(history))
    else:
        display.set("No history")

def open_website(event=None):
    webbrowser.open_new("https://www.daktoinc.co.uk")

def run_gui():
    global display
    root = tk.Tk()
    root.configure(bg="black")
    root.title("Dakto INC Calculator")
    root.geometry("430x570")

    display = tk.StringVar()
    entry = tk.Entry(root, textvariable=display, font=('Arial', 14))
    entry.grid(columnspan=4, ipadx=70, ipady=10, pady=10)

    # Button rows
    button = [
        ('7',2,0), ('8',2,1), ('9',2,2), ('/',2,3),
        ('4',3,0), ('5',3,1), ('6',3,2), ('*',3,3),
        ('1',4,0), ('2',4,1), ('3',4,2), ('-',4,3),
        ('0',5,0), ('.',5,1), ('=',5,2), ('+',5,3),
        ('sin',6,0), ('cos',6,1), ('tan',6,2), ('sqrt(',6,3),
        ('log10(',7,0), ('ln',7,1), ('^',7,2), ('C',7,3),
        ('Fraction(',8,0), ('π',8,1), ('e',8,2), ('(',8,3),
        (')',9,0), ('Frac-Dec',9,1), ('M+',9,2), ('MR',9,3),
        ('MC',10,0), ('History',10,1)
    ]

    for (text, row, col) in button:
        if text == '=':
            action = equal
        elif text == 'C':
            action = clear
        elif text == 'Frac-Dec':
            action = dec_to_frac
        elif text == 'M+':
            action = memory_save
        elif text == 'MR':
            action = memory_recall
        elif text == 'MC':
            action = memory_clear
        elif text == 'History':
            action = show_history
        elif text == '^':
            action = lambda: press('**')
        elif text == 'Fraction':
            action = lambda: press('Fraction(')
        else:
            action = lambda t=text: press(t)

        Button = tk.Button(root, text=text, command=action, height=2, width=9).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")

    for i in range(7):
        root.grid_rowconfigure(i, weight=1)
    for i in range(6):
        root.grid_columnconfigure(i, weight=1)

    # DKI Hyperlink
    link = tk.Label(root, text="Dakto INC", fg="blue", cursor="hand2", bg="black", font=("Arial", 9, "underline"))
    link.grid(row=99, column=5, sticky="e", padx=10, pady=5)
    link.bind("<Button-1>", open_website)
    
    root.mainloop()

# CLI or GUI?
question = input("Would you like to use CLI, CLI-Scientific (CLIS) or GUI? ").strip().upper()

if question == "CLI":
    run_cli()
elif question == "CLIS":
    run_cli_scientific()
elif question == "GUI":
    run_gui()
else:
    print("Choice is invalid. Script will now exit.")
