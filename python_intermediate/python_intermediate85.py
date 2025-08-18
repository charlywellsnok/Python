Example: Calculator Using Custom Modules
Let's first create a file named calculator.py with these function:

def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
    
def divide(a, b):
    return a / b 
This calculator.py file itself is a module. Now, let's import this file from another file named main.py.

import calculator

result1 = calculator.add(2, 3)
print(result1)   # 5

result3 = calculator.multiply(10, 3)
print(result3)   # 30
After we use this statement import calculator, we can use all the functions and statements defined inside the calculator module.

Then, we have used the add() function of the calculator.py file using calculator.add().

Similarly, we have used the multiply() function of the calculator.py file using calculator.multiply().

Confused about something? Ask a question!
