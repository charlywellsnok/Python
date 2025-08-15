#Finding factorial using funtion
def compute_factorial(n):
    factorial = 1
    
    # Compute factorial
    for i in range(1, n+1):
        factorial = factorial * i 
    
    # Return the factorial
    return factorial

# Get user input
number = int(input("Enter a positive integer: "))
total = compute_factorial(number)

print(total)

