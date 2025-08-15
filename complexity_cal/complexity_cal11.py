Introduction to Big O
Big Oh (Big O) is a mathematical notation used to represent the time complexity of an algorithm. It helps us understand how the performance of an algorithm changes with the size of the input.

Let us revisit our code from the previous chapter.

total= 0 
n = 1000

# iterate n times
for i in range(1, n + 1):
    total = total + i

print(total) # Output: 500500
The code takes n steps to execute. Instead of using just plain n for time complexity, we use the O(n) notation—read as Big Oh of n—to represent it.

Let's see a few examples of the Big O notation next to better understand how it works.
