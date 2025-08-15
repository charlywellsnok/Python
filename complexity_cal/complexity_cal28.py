Example 2: Logarithmic Time Complexity
Let's look at another example to understand logarithmic time better.

def countdown(n):
    while n > 0:
        print(n)
        n = n // 2

countdown(16)
Here's what happens, when we call the function:

Step	Value of n	Calculation for next n	Condition n > 0
1	16	16 // 2 = 8	16 > 0 is True
2	8	8 // 2 = 4	8 > 0 is True
3	4	4 // 2 = 2	4 > 0 is True
4	2	2 // 2 = 1	2 > 0 is True
5	1	1 // 2 = 0	1 > 0 is True
As you can see, even though we start with 16, it only takes 5 prints (steps) to finish. The value of n halves each time, so the total steps grow very slowly — that's logarithmic time!
