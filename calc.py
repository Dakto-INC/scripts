import time
import math
import tkinter as tk

# Welcome message
print("Welcome to Dakto INC Calculator")
time.sleep(1)
print("\n---------------------------------------------------------------\n")

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
    print("\Scientific Answers: ")
    print("1. Power (x^y)\n2. Square Root\n3. Sin\n4. Cos\n5. Tan\n6. Log\n7. Ln\n8. Factorial")
    science = input("Choose an operation [1-8]: ").strip()

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
    else:
        print("Invalid choice")

# GUI
expr = ""

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr, {"__builtins__": None}, vars(math)))
        display.set(result)
        expr = ""
    except:
        display.set("An error occured.")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

def run_gui():
    global display
    root = tk.Tk()
    root.configure(bg="red")
    root.title("Dakto INC Calculator")
    root.geometry("270x150")

    display = tk.StringVar()
    entry = tk.Entry(root, textvariable=display)
    entry.grid(columnspan=4, ipadx=70)

    # GUI Buttons
    Button = tk.Button(root, text='1', command=lambda: press(1), height=1, width=7).grid(row=2, column=0)
    Button = tk.Button(root, text='2', command=lambda: press(2), height=1, width=7).grid(row=2, column=1)
    Button = tk.Button(root, text='3', command=lambda: press(3), height=1, width=7).grid(row=2, column=2)
    Button = tk.Button(root, text='4', command=lambda: press(4), height=1, width=7).grid(row=3, column=0)
    Button = tk.Button(root, text='5', command=lambda: press(5), height=1, width=7).grid(row=3, column=1)
    Button = tk.Button(root, text='6', command=lambda: press(6), height=1, width=7).grid(row=3, column=2)
    Button = tk.Button(root, text='7', command=lambda: press(7), height=1, width=7).grid(row=4, column=0)
    Button = tk.Button(root, text='8', command=lambda: press(8), height=1, width=7).grid(row=4, column=1)
    Button = tk.Button(root, text='9', command=lambda: press(9), height=1, width=7).grid(row=4, column=2)
    Button = tk.Button(root, text='0', command=lambda: press(0), height=1, width=7).grid(row=5, column=0)

    Button = tk.Button(root, text='+', command=lambda: press('+'), height=1, width=7).grid(row=5, column=1)
    Button = tk.Button(root, text='-', command=lambda: press('-'), height=1, width=7).grid(row=5, column=2)
    Button = tk.Button(root, text='*', command=lambda: press('*'), height=1, width=7).grid(row=6, column=0)
    Button = tk.Button(root, text='/', command=lambda: press('/'), height=1, width=7).grid(row=6, column=1)
    Button = tk.Button(root, text='=', command=equal, height=1, width=7).grid(row=6, column=2)
    Button = tk.Button(root, text='C', command=clear, height=1, width=7).grid(row=7, column=1)

    # GUI Science Buttons
    
    Button = tk.Button(root, text='sin', command=lambda: press('sin('), height=1, width=7).grid(row=8, column=0)
    Button = tk.Button(root, text='cos', command=lambda: press('cos('), height=1, width=7).grid(row=8, column=1)
    Button = tk.Button(root, text='tan', command=lambda: press('tan('), height=1, width=7).grid(row=8, column=2)
    Button = tk.Button(root, text='ln', command=lambda: press('log10'), height=1, width=7).grid(row=9, column=0)
    Button = tk.Button(root, text='log', command=lambda: press('log'), height=1, width=7).grid(row=9, column=1)
    Button = tk.Button(root, text='√', command=lambda: press('sqrt'), height=1, width=7).grid(row=9, column=2)
    Button = tk.Button(root, text='^', command=lambda: press('**'), height=1, width=7).grid(row=10, column=0)
    Button = tk.Button(root, text='π', command=lambda: press('pi'), height=1, width=7).grid(row=10, column=1)
    Button = tk.Button(root, text='e', command=lambda: press('e'), height=1, width=7).grid(row=10, column=2)
    
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



