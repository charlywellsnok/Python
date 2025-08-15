Example 3
Consider the following recurrence relation.

T
(
n
)
=
2
T
(
n
2
)
+
n
2
T(n)=2T( 
2
n
​
 )+n 
2
 
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
b
)
+
Ө
(
n
k
(
log
⁡
n
)
p
)
T(n)=aT( 
b
n
​
 )+Ө(n 
k
 (logn) 
p
 )
Step 2: Rewrite the recurrence relation to match the general form.

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
2
)
+
Ө
(
n
2
(
log
⁡
n
)
0
)
T(n)=2∗T( 
2
n
​
 )+Ө(n 
2
 (logn) 
0
 )
Step 3: Identify a, b, k, and p and check the conditions for the master theorem.

a = 2
b = 2
k = 2
p = 0
Since 
a
≥
1
a≥1, b > 1, 
k
≥
0
k≥0, and p is a real number, the master theorem is possible.

Step 4: Compare 
log
⁡
b
a
log 
b
​
 a and k and apply the matching rule.

Here,

log
⁡
b
a
=
log
⁡
2
2
=
1
log 
b
​
 a=log 
2
​
 2=1
k
=
2
k=2
Since 
log
⁡
b
a
log 
b
​
 a and 
p
≥
0
p≥0, let's apply the formula to find the time complexity for this scenario.

T
(
n
)
=
Ө
(
n
k
(
log
⁡
n
)
p
)
T(n)=Ө(n 
k
 (logn) 
p
 )
=
Ө
(
n
2
(
log
⁡
n
)
0
)
T(n)
 =Ө(n 
2
 (logn) 
0
 )
=
Ө
(
n
2
∗
1
)
T(n)
 =Ө(n 
2
 ∗1)
=
Ө
(
n
2
)
T(n)
 =Ө(n 
2
 )
Next, let's look at another example.
