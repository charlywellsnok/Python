Time Complexity in Conditional Statements
In programs with conditional statements (if..else), the time complexity can vary depending on which blocks are executed versus skipped. Let's see how we can calculate time complexity in such cases.

Consider the following program:

def print_numbers(n):
    # if n > 100
    # print n once 
    if n > 100:
        print(n)
    else:
        # if n < 100
        # print n for n number of times
        for i in range(n):
            print(n)

num = int(input("Enter a number: "))
print_numbers(num)
Output 1

Enter a number: 105
105
Output 2

Enter a number: 3
3
3
3
Here's how this function works for different arguments.

1. If n is greater than 100

The if block is executed, printing the n only once.

This results in O(1) time complexity.

2. If n is less than or equal to 100

The loop inside the else block is executed, where the for-loop runs n times, printing n on each iteration.

This results in O(n) time complexity.

As we can see, whenever we use conditional statements, the time complexity may vary depending on the test condition of the if-statement.

Calculating Time Complexity
Figure: Calculating Time Complexity
Hence,

Best case: If n is greater than 100, the time complexity is O(1).
Worst case: If n is less than or equal to 100, the time complexity is O(n).
Since we usually take the worst case to calculate the time complexity, we can conclude that the overall time complexity of the above program is O(n).
