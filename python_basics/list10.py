Length of Python Lists
Write a program to find the number of items in a Python list.

The easiest way to find the number of items a list has is by using the built-in len() function.

Can you find the length of a list without using this function?

Suppose we have a list like this: [10, 20, 30, 40]
Your task is to find the length of this list programmatically.
For hints, refer to the code outline.



# Replace ___ with your code below

numbers = [10, 20, 30, 40]

length = 0

# use a loop to find the length
for number in numbers:
    length = length + 1
# print length
print(length)
