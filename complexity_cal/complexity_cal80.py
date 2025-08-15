Example 2
Suppose we are given the following recurrence relation:

T
(
n
)
=
2
T
(
n
−
1
)
+
1
T(n)=2T(n−1)+1
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
2
∗
T
(
n
−
1
)
+
O
(
n
0
)
T(n)=2∗T(n−1)+O(n 
0
 )
Step 3: Find a, b, and k check the conditions for the master theorem.

a = 2
b = 1
k = 0
Since a > 0, b > 0, and 
k
≥
0
k≥0, the master theorem is possible.

Step 4: Compare a and 1 and apply the matching rule.

Here,

a = 2
k = 0
Since a > 1, let's apply the formula to find the time complexity for this scenario.

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
=
O
(
n
0
a
n
1
)
T(n)
 =O(n 
0
 a 
1
n
​
 
 )
=
O
(
1
∗
2
n
)
T(n)
 =O(1∗2 
n
 )
=
O
(
2
n
)
T(n)
 =O(2 
n
 )
Next, let's consider a slightly different recurrence.
