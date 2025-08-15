Example 1
Remember the following program we discussed earlier:

def test(n):
    if n > 0:
        for i in range(1, n+1):
            print(n)
        test(n-1)
If the test(n) function takes T(n) time to execute, then its recurrence relation is:

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
T(n)=T(n−1)+n
Let's calculate its time complexity using the master theorem.

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
1
)
T(n)=1∗T(n−1)+O(n 
1
 )
Step 3: Find a, b, and k check the conditions for the master theorem.

a = 1
b = 1
k = 1
Since a > 0, b > 0, and 
k
≥
0
k≥0, the master theorem is possible.

Step 4: Compare a and 1 and apply: the matching rule.

Here,

a = 1
k = 1
Since a = 1, let's apply the formula to find the time complexity for this scenario.

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
=
O
(
n
1
+
1
)
T(n)
 =O(n 
1+1
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
Next, let's consider a slightly different recurrence.
