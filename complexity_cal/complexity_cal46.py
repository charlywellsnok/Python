Theta Mathematics
Now, let's dive back into the mathematical interaction of Theta.

Example

Given the following function,

f(n) = 4n + 3
let's find c1 * g(n) and c2 * g(n) based on the same conditions as before.

c
1
∗
g
(
n
)
≤
f
(
n
)
≤
c
2
∗
g
(
n
)
c1∗g(n)≤f(n)≤c2∗g(n)
n
≥
n
0
n≥n 
0
​
 
c
1
>
0
c1>0
c
2
>
0
c2>0
n
0
≥
1
n 
0
​
 ≥1
Solution

Here, the growth of the f(n) function won't be faster than the c2 * g(n) function or slower than the c1 * g(n) function after n_0 because the above conditions are satisfied:

Since c1 * g(n) always grows slower than f(n), g(n) can be any expression such as 2n, 3n, etc. However, c1 * g(n) cannot be 10n, 12n, 4n, etc. because these functions grow faster than 4n + 3.

Since c2 * g(n) always grows faster than f(n), g(n) can be any expression such as 5n, 10n, etc. However, c2 * g(n) cannot be 2n, 3n, etc. because these functions grow slower than 4n + 3.

Idea Emoji
Important: The values of c1 and c2 are different. However, the value of g(n) is the same for both of the functions.
Let's assume c1 * g(n) is 2n and c2 * g(n) is 10n. In this scenario,

c
1
∗
g
(
n
)
=
2
n
c1∗g(n)=2n
c
2
∗
g
(
n
)
=
10
n
c2∗g(n)=10n
f
(
n
)
=
4
n
+
3
f(n)=4n+3
S
i
n
c
e
,
 
f
(
n
)
 
c
a
n
n
o
t
 
g
r
o
w
 
f
a
s
t
e
r
 
t
h
a
n
 
c
2
∗
g
(
n
)
 
a
n
d
 
s
l
o
w
e
r
 
t
h
a
n
 
c
1
∗
g
(
n
)
Since, f(n) cannot grow faster than c2∗g(n) and slower than c1∗g(n)
2
n
≤
4
n
+
3
≤
10
n
 
[
f
o
r
 
a
l
l
 
n
≥
1
]
2n≤4n+3≤10n [for all n≥1]
As c1 * g(n) <= f(n) <= c2 * g(n) we can say that:

f(n) = θ(g(n))
=> f(n) = θ(n) [read as f(n) is Theta of n]
