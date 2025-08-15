Example 3
Consider the following recurrence relation:

T
(
n
)
=
1
2
T
(
n
−
1
)
+
n
2
T(n)= 
2
1
​
 T(n−1)+n 
2
 
Now let's calculate its time complexity using the master theorem.

Step 1: Compare the recurrence relation with the general form.

The general form of T(n) is:

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
O
(
n
k
)
T(n)=aT(n−b)+O(n 
k
 )
Step 2: Modify recurrence relation to match the general form.

T
(
n
)
=
1
2
∗
T
(
n
−
1
)
+
n
2
T(n)= 
2
1
​
 ∗T(n−1)+n 
2
 
Step 3: Find a, b, and k check the conditions for the master theorem.

a
=
1
2
a= 
2
1
​
 
b
=
1
b=1
k
=
2
k=2
Since a > 0, b > 0, and 
k
≥
0
k≥0, the master theorem is possible.

Step 4: Compare a and 1 and applying the matching rule.

Here,

a
=
1
2
a= 
2
1
​
 
k
=
2
k=2
Since a < 1, let's apply the formula to find the time complexity for this scenario.

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
=
O
(
n
2
)
T(n)
 =O(n 
2
 )
