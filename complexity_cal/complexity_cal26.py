Example 1: Logarithmic Time Complexity
Let's find out the time complexity of the code below.

def print_numbers(n):
    i = 1
    
    # iterate until i < n
    while i < n:
        print(i)
        # double the value of i each iteration
        i = i * 2

print_numbers(5)
Output

1
2
4
Inside the loop, we start with i = 1, and in each iteration, we double the value of i. The loop continues as long as i is less than n and terminates once i is equal to or greater than n.

Let's see how the print_numbers() function works:

Iteration	Value of i
1st	i * 2 = 2 = 21 
2nd	i * 2 = 4 = 22
3rd	i * 2 = 8 = 23
...	...
kth	i * 2 = 2 k-1 * 2 = 2k 
Suppose the loop condition i < n becomes false after the kth iteration. This means:

2
k
≥
n
(
w
h
e
r
e
 
2
k
 
i
s
 
t
h
e
 
v
a
l
u
e
 
o
f
 
i
)
 
,
 
w
h
e
r
e
 
k
 
i
s
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
t
i
m
e
s
 
t
h
e
 
l
o
o
p
 
i
t
e
r
a
t
e
s
2 
k
 ≥n(where 2 
k
  is the value of i) , where k is the number of times the loop iterates
Solving for k,

2
k
≥
n
2 
k
 ≥n
2
k
=
n
(
f
o
r
 
s
i
m
p
l
i
c
i
t
y
)
2 
k
 =n(for simplicity)
k
=
log
⁡
2
(
n
)
k=log 
2
​
 (n)
k
=
log
⁡
(
n
)
 
(
s
t
e
p
s
)
k=log(n) (steps)
Thus, the above code runs 
log
⁡
(
n
)
log(n) times for n input size and exhibits time complexity is 
O
(
log
⁡
n
)
O(logn).
