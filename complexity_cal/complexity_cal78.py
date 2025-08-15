Solving Recurrence Relation with Master Theorem
To solve an equation using recurrence relation for a decreasing function, the function must be in the following format:

T
(
n
)
=
a
T
(
n
−
b
)
+
f
(
n
)
T(n)=aT(n−b)+f(n)
w
h
e
r
e
,
where,
f
(
n
)
=
O
(
n
k
)
,
f(n)=O(n 
k
 ),
a
>
0
,
 
b
>
0
,
a>0, b>0,
k
≥
0
k≥0
Now, let's observe the equation for three different cases:

Case 1: a = 1

T
(
n
)
=
O
(
n
k
+
1
)
T(n)=O(n 
k+1
 )
Case 2: a > 1

T
(
n
)
=
O
(
n
k
a
n
b
)
T(n)=O(n 
k
 a 
b
n
​
 
 )
Case 3: a < 1

T
(
n
)
=
O
(
n
k
)
T(n)=O(n 
k
 )
Let's see some examples of the calculating time complexity of decreasing function.
