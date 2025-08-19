Find the Occurrence of a Number
Create a program to find the occurrence of a given number in a list.

Create a function named count_occurrences() that takes two arguments: lst (a list) and n (an integer whose occurrences we need to find).
Find the count of occurrences of n in lst and return this count.
Print the result from outside the function.
Note: We will use a predefined list, [3, 3, 4, 5, 6, 6, 6, 2], for this problem. The element whose occurrence we need to determine will be taken from the user input.

Example
Test Input

6
Expected Output

3
Reason: The occurrence of the value 6 in this list is 3 because it is present in 3 places.












# Replace ___ with your code

def count_occurrences(lst, n):

    count = 0

    for element in lst:
        if element == n:
            # increment count if a match is found
            count += 1
    return count

lst = [3, 3, 4, 5, 6, 6, 6, 2]

# take integer input
n = int(input())

count = count_occurrences(lst, n)

print(count)
