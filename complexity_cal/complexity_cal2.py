Basic Time Complexity Example
Now, let's revisit the code we previously wrote.

total = 0 
n = 1000

# iterate n times
for i in range(1, n + 1):
   total = total + i

print(total)
Output

500500
How does this relate to time complexity?

Let's analyze the number of steps this code takes based on the value of n:

5: The loop runs 5 steps
2000: The loop runs 2000 steps
Thus, for any value of n, our code takes n steps to run.

This calculation is independent of the device or programming language we are using.

Takeaway: Time complexity helps us understand performance in a way that applies universally, regardless of where or how the code runs.
