Calculate Factorial of a Number
Write a program to find the factorial of an integer entered by the user.

The factorial of a positive integer n is defined as:

factorial = 1 * 2 * 3 * .... n
To solve this problem:

Get an integer input from the user and assign it to the variable n. We'll assume the user will always enter a positive integer.
Using a for loop to compute the factorial.
Print the factorial outside the loop.
Hint: This problem is similar to the sum of natural numbers problem we wrote earlier. Refer to the code outline for more guidance.




# Replace ___ with your code below

# Take integer input
number = int(input("Enter a number: "))
total = 1
# Iterate from 1 to n: range(1, n+1)
for i in range(1,number+1):
   
# Multiply each number by total
    total = total * i 
print(total)
