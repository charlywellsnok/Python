Exception Handling
Create a program to print an item of a list based on user input (index). If the index doesn't exist in a list, print a custom message.

Assign a list, [10, 20, 30], to the numbers variable.
Take an integer input and assign it to the index variable.
Print the item at that given index.
However, if the index is not in the list, print a custom message 'Index is wrong'.
Use exception handling to solve this problem.

Example
Test Input

5
Expected Output

Index is wrong
Confused about something? Ask a question!














# Replace ___ with your code

# create a try block
try:
    numbers = [10, 20, 30]

    # take integer input
    index = int(input())

    # print the item from the number list
    print(numbers[index])

# create the except block
except:
    print('Index is wrong')
