Frequency Count Method
We use the frequency count method to calculate the time complexity of an algorithm. The method involves counting the number of steps our program takes to execute, similar to what we did in our earlier example.

Let's take a look at the code that calculates the sum of the first n natural numbers.

def find_sum(n):
    # Initialize total to zero
    total = 0
    # Iterate n times
    for i in range(1, n + 1):
        # Add the current number to total
        total = total + i

    # Return the final sum
    return total

result = find_sum(10)
print(result)
Output

55
Here's how many times each line inside the find_sum() runs :

At the beginning of the loop, the line total = 0 runs once.
The for i in range(1, n+1) line runs n times because the loop iterates from 1 to n. Each iteration checks the loop condition and proceeds, so this counts as a step each time.
Inside the loop, total = total + i runs n times, once for each iteration.
return total runs once at the end.
Let's say every step inside the function takes 1 unit of time. Then, the units of time spent are:

Frequency count method
Figure: Frequency count method
So, the total steps inside the function can be expressed as:

Total steps = 1 + n + n + 1 = 2n + 2
Or, in terms of a polynomial function:

f(n)=2n+2
This means the function takes roughly 2n + 2 steps to execute.

Next, we will explore the degree of a polynomial function, which helps simplify and better understand the time complexity of any function f(n).
