Arithmetic Using Lambda
Create a program to find the sum of the square root of two numbers using a lambda function.

Create the lambda function and assign it to a variable named compute.
The function should take two arguments and return the sum of the square roots of the arguments.
Take two integer inputs and assign them to n1 and n2 respectively.
Call the lambda function with n1 and n2 as arguments and print the result.
Hint: n**0.5 gives the square root of n

Example
Test Input

4
9
Expected Output

5.0











# Replace ___ with your

# create the function
compute = lambda n1, n2: (n1**0.5) + (n2**0.5)

# take two integer inputs
n1 = int(input())
n2 = int(input())

# call the function and print the result
print(compute(n1,n2))
