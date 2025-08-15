Example: Quadratic Time Complexity
Let's take a different example to better understand quadratic time complexity.

def print_numbers(n):

    for i in range(n):
        for j in range(i):
            print(j)

print_numbers(3)
Output

0
0
1
Calculation of Quadratic Time Complexity
Figure: Calculation of Quadratic Time Complexity
In this example,

The outer loop runs n times, where n is the input.
The inner loop runs i times in each iteration of the outer loop, where i varies from 0 to (n-1).
Thus, the inner loop executes a total of 0 + 1 + 2 + ... + (n-2) operations, which can be expressed as (n-1)(n-1+1)/2 = n(n-1)/2 operations.

Although the execution time is not exactly 
n
2
n 
2
 , the time complexity is proportional to the square of the input size.

Therefore, the time complexity of this print_numbers() function is 
O
(
n
2
)
O(n 
2
 ), representing quadratic time complexity.
