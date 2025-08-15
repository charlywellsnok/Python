Constant Space Complexity – O(1)
An algorithm has a constant space complexity when the memory it uses doesn't depend on the change in its input size.

In other words, even if the input size grows, the memory required to execute the program remains the same.

Let's take an example.

def find_sum(n1, n2, n3):
    result = n1 + n2 + n3
    print(result)

find_sum(1,2,3)
Output

6 
Let's find the space complexity of the find_sum() function.

Let's look at variables and their sizes again to understand memory usage.

In the above program,

Variables	Input Size
n1	1
n2	1
n3	1 
result	1
S
p
a
c
e
 
C
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
1
+
1
+
1
+
1
Space Complexity=1+1+1+1
=
4
Space Complexity
 =4
=
4
∗
n
0
 
(
B
e
c
a
u
s
e
 
n
0
=
1
)
Space Complexity
 =4∗n 
0
  (Because n 
0
 =1)
=
n
0
(
B
y
 
f
r
e
q
u
e
n
c
y
 
c
o
u
n
t
 
m
e
t
h
o
d
)
Space Complexity
 =n 
0
 (By frequency count method)
By the frequency count method, constants are dropped.

=
1
Space Complexity
 =1
=
O
(
1
)
Space Complexity
 =O(1)
O(1) thus means that, even if the input size increases, the space complexity doesn't change—just like in the case of time complexity.
