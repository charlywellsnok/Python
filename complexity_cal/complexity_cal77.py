Recurrence Relation for Decreasing Function
Mathematically speaking, the master theorem provides a solution to the recurrence relation. Let's learn how we can find the recurrence relation for a decreasing function.

Consider the following program:

def test(n):
    if n > 0:
        for i in range(1, n+1):
            print(n)
        test(n-1)
If the test() function takes T(n) time to execute,

Recurrence Relation for decreasing Function
Figure: Recurrence Relation for decreasing Function
From the image, we can say,

T
(
n
)
=
T
(
n
−
1
)
+
n
+
n
+
1
T(n)=T(n−1)+n+n+1
=
T
(
n
)
=
T
(
n
−
1
)
+
(
2
n
+
1
)
T(n)
 =T(n)=T(n−1)+(2n+1)
=
T
(
n
)
=
T
(
n
−
1
)
+
n
 
[
u
s
i
n
g
 
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
 
f
o
r
 
2
n
+
1
]
T(n)
 =T(n)=T(n−1)+n [using frequency count method for 2n+1]
