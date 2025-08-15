Average Case
The average case time complexity occurs if the element is somewhere in the middle of the array.

In this scenario, the average case

=
s
u
m
 
o
f
 
a
l
l
 
p
o
s
s
i
b
l
e
 
c
a
s
e
s
n
o
.
 
o
f
 
c
a
s
e
s
= 
no. of cases
sum of all possible cases
​
 
=
1
+
2
+
3
+
.
.
.
+
n
n
= 
n
1+2+3+...+n
​
 
=
n
⋅
(
n
+
1
)
2
n
(using the formula for the sum of first n natural numbers)
= 
n
n⋅ 
2
(n+1)
​
 
​
 (using the formula for the sum of first n natural numbers)
=
O
(
n
)
(
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
)
=O(n)(using frequency count method)
On average the algorithm performs about n/2 operations. Using frequency count method to express in Big-O notation, we drop the constants. So the time complexity becomes O(n),

Idea Emoji
Note: Average case analysis does not apply to every algorithm. In many real-world situations, it behaves similarly to the worst case.
Similar to the worst case, we can use any asymptotic notation for the average case.

Ω(n)
O(n)
Θ(n)
