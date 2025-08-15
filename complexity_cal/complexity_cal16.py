Example: Linear Time Complexity
Let's find out the time complexity of the code below.

def print_numbers(n):
    for i in range(0, n, 3):
        print(i)

print_numbers(6)
Output

0
3
Here, the loop iterates from 0 to n, but this time, with an interval of 3. So, the loop would run for 
n
/
3
n/3 times.

If the value of

n = 6, the loop runs for 
6
3
3
6
​
  = 2 times.
n = 8, the loop runs for 
8
3
3
8
​
  = 2 times (floor value).
Let's calculate the time complexity of the code above:

Calculation of Linear Time Complexity
Figure: Calculation of Linear Time Complexity

Now, using the frequency count method, we drop the constant:

T
i
m
e
 
c
o
m
p
l
e
x
i
t
y
=
2
n
3
Time complexity= 
3
2n
​
 
=
2
3
∗
n
Time complexity
 = 
3
2
​
 ∗n
=
O
(
n
)
 
(
w
e
 
d
o
n
′
t
 
c
o
n
s
i
d
e
r
 
t
h
e
 
c
o
e
f
f
i
c
i
e
n
t
)
Time complexity
 =O(n) (we don 
′
 t consider the coefficient)
As we ignore the constant coefficient and focus on the input size, the time complexity of the print_numbers() function is O(n).
