Understanding Linear Time Complexity
Let's take the same example from our last page to understand linear time complexity better.

def print_numbers(n):
    for i in range(0, n, 3):
        print(i)

print_numbers(6)
Output

0
3
In this example, the function executes a for loop that iterates from 0 to n, with a step of 3. Its execution is complete in 
2
n
3
3
2n
​
  steps.

The total number of iterations, thus, (and thus the steps executed) is directly proportional to n.

Scenarios:

If n = 6, the code executes 
2
3
∗
6
3
2
​
 ∗6 = 4 statements
If n = 87, the code executes 
2
3
∗
87
3
2
​
 ∗87 = 58 statements
If n = 10002, the code executes 
2
3
∗
10002
3
2
​
 ∗10002 = 6668 statements
Notice that the number of steps required to run our code is not equal to the input but directly proportional to the input size.

As long as the number of steps needed to execute the code is directly proportional to the input size, the function's time complexity is linear—O(n).
