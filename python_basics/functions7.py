Product of Two Numbers using Functions
Write a program to find the product of two numbers.

Step 1

Define a function named get_product() that accepts two parameters: number1 and number2.
Inside the function, multiply number1 by number2 and return the result.
Step 2

Outside of the function:

Get two integer inputs from the user and store them in n1 and n2.
Call the get_product() function with arguments n1 and n2 and store the return value in the total variable.
Print the total variable.
Example


# Replace ___ with your code below
# Replace ___ with your code below

# Define the get_product() function
def get_product(number1,number2):
    result = number1 * number2
    return result

# Get integer inputs from the user
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

# Call the function with arguments: n1 and n2
# Print the total
total = get_product(n1,n2)
print(total)

