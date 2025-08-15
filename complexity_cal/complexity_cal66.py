Dividing Function
Let's first understand what a dividing function is. Then, we will learn to calculate the time complexity of dividing functions using the master theorem.

Here's an example of a dividing function:

def test(n):
    if n > 0:
        print(n)
        test(n // 2)

test(20)
Output

20
10
5
2
1
Here, test() is a recursive function because we have called the same test() function from inside it.

In each recursive call, the argument is divided by 2 using the test(n // 2) statement. Hence, test() is a dividing function.

This is also an example of the divide and conquer strategy. It is a common approach in computer science where a big problem is solved by breaking it into smaller subproblems, solving each recursively, and then combining the results.

So here, the divide part comes from cutting n in half each time, and the conquer part happens when each smaller problem is handled by a recursive call.
