Decreasing Function
In this lesson, we will first understand what a decreasing function is. Then, we will learn to calculate the time complexity of decreasing functions using the master theorem.

Here's an example of a decreasing function:

def test(n):
    if n > 0:
        for i in range(1, n+1):
            print(n)
        test(n-1)

test(2)
Output

2
2
1
Here, test() is a recursive function because it calls itself (test()) from within. Each time it runs, the argument is reduced by 1 using the test(n - 1) statement. Hence, test() is a decreasing function, also known as the subtract-and-conquer approach.
