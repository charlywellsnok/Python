Filter List Using Comprehension
Create a program to create a list of odd numbers from a list of numbers using list comprehension.

Create a list with the following data items 12, 17, 28, 19, 11, and assign it to the numbers variable.
Create a new list and only print 17, 19, 11 (odd numbers) using list comprehension.
Print newly created list.
Example
Expected Output

[17, 19, 11]












Solution:

# Replace ___ with your code

numbers = [12, 17, 28, 19, 11]

# Use list comprehension to get only odd numbers from the numbers list
odd_numbers =[num for num in numbers if num % 2 != 0]
    

# print new list
print(odd_numbers)
