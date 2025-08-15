Introduction to Linear Time Complexity
An algorithm has linear time complexity if its execution time grows directly in proportion to the size of the input. In other words, if the input size doubles, the time it takes to run the algorithm roughly doubles as well.

If you were to plot this relationship on a graph, it would form a straight line — showing that the time increases at a constant rate as input grows.

Graph of Linear time complexity
Figure: Graph of Linear time complexity
Let's understand linear time complexity with the help of an example:

def print_hello(n):
    for i in range(n):
        print("Hello")

print_hello(5)
Output

Hello
Hello
Hello
Hello
Hello
Calculation of Linear time complexity
Figure: Calculation of Linear time complexity
The print_hello() function executes 2n statements.

That is,

If n = 5, the function will execute 2 * 5 = 10 statements
If n = 88, the function will execute 2 * 88 = 176 statements
If n = 100000, the function will execute 2 * 100,000 = 200,000 statements
As we can see, the execution time of our code is directly proportional to the size of the input, hence, its time complexity is linear.

Linear time complexity is denoted by O(n).
