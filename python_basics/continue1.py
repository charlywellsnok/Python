Print Odd Numbers
Write a program to display only the odd numbers between 1 and n.

Take an integer input, n.
Use a loop to iterate from 1 to n (inclusive).
In each iteration, check if the current number is even. If it is, skip the rest of the code using continue.
If the current number is odd, display the number.
Example



# Take integer input
n = int(input("Enter an integer: "))

# Write your code below
for number in range(1, n +1):
    if number % 2 == 0:
        continue


    print(number)
