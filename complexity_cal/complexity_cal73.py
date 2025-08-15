Example 1
Remember the following function we discussed earlier:

def test(n):
    if n > 0:
        print(n)
        test(n // 2)
Its time complexity follows the recurrence:

T
(
n
)
=
T
(
n
2
)
+
1
T(n)=T( 
2
n
​
 )+1
Let's calculate its time complexity using the master theorem.

Step 1: Compare the recurrence relation to the general form.

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
)
T(n)=aT( 
b
n
​
 )+Ө(n 
k
 (logn) 
p
 ))
Step 2: Rewrite the recurrence relation to match the general form.

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
2
)
+
Ө
(
n
0
(
log
⁡
n
)
0
)
T(n)=1∗T( 
2
n
​
 )+Ө(n 
0
 (logn) 
0
 )
Step 3: Identify a, b, k and p and check the conditions for the master theorem.

a = 1
b = 2
k = 0
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
1
=
0
log 
b
​
 a=log 
2
​
 1=0
k
=
0
k=0
Since 
log
⁡
b
a
=
k
log 
b
​
 a=k and p > -1, let's apply the formula to find time complexity for this scenario.

T
(
n
)
=
Ө
(
n
k
log
⁡
p
+
1
n
)
T(n)=Ө(n 
k
 log 
p+1
 n)
=
Ө
(
n
0
log
⁡
0
+
1
n
)
T(n)
 =Ө(n 
0
 log 
0+1
 n)
=
Ө
(
1
∗
log
⁡
1
n
)
T(n)
 =Ө(1∗log 
1
 n)
=
Ө
(
log
⁡
n
)
T(n)
 =Ө(logn)
