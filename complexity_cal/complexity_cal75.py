Example 4
Before we move ahead, let's consider one final example:

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
Ө
(
n
2
log
⁡
2
n
)
T(n)=2T( 
2
n
​
 )+Ө(n 
2
 log 
2
 n)
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
2
)
T(n)=2T( 
2
n
​
 )+Ө(n 
2
 (logn) 
2
 )
Step 3: Identify a, b, k, and p and check the conditions for the master theorem.

a = 2
b = 2
k = 2
p = 2
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
<
k
log 
b
​
 a<k and 
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
2
)
T(n)
 =Ө(n 
2
 (logn) 
2
 )
=
Ө
(
n
2
log
⁡
2
n
)
T(n)
 =Ө(n 
2
 log 
2
 n)
