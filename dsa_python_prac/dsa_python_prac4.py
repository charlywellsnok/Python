Sum of Natural Numbers
We can create a program to find the sum of natural numbers using a for loop.

def calculate_sum(n):
    
    total = 0
    
    for i in range(n+1):
        total += i
    
    return total
    
result = calculate_sum(100)
print(result)    # 5050
In most cases, this program won't cause any problems.

However, what if we have to find the sum of natural numbers of an absurdly large number, let's say 10000000000?

It will take a lot of time and memory to find the sum for this number.

Next, we will solve this problem in a more optimized manner.

Confused about something? Ask a question!
