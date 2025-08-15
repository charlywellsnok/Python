Example: Quadratic Time Complexity
Let's look at a simple code example to see quadratic time complexity in action.

def print_numbers(n):
    for i in range(0, n):
        for j in range(0, n):
            print(j)

print_numbers(2)
Output

0
1
0
1
Calculation of Quadratic time complexity
Figure: Calculation of Quadratic time complexity
In the code above, we have two nested loops, each iterating n times. This means that for every iteration of the outer loop, the inner loop runs n times as well. Therefore, the execution time increases quadratically with respect to the input size, which results in a time complexity of O(n²).
