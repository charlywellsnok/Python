Lesson
Ask Programiz
Optimized: Sum of Natural Numbers
We can find the sum of natural numbers using a simple formula:

S
u
m
 
o
f
 
n
a
t
u
r
a
l
 
n
u
m
b
e
r
s
=
n
∗
(
n
+
1
)
2
Sum of natural numbers= 
2
n∗(n+1)
​
 
Let's use this formula to find the sum of natural numbers.

def calculate_sum(n):
    return n * (n + 1) // 2
    
result = calculate_sum(100)
print(result)    # 5050
This program runs in a fraction of a second, even for very large numbers. It's because we solved this problem with a single instruction, regardless of the size of the input.

Confused about something? Ask a question!
