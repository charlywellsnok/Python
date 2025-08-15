Omega Mathematics
Now, let's see a mathematical example of Omega.

Example:

Given the following function,

f(n) = 4n + 3
let's find c * g(n) based on the same conditions as before.

f
(
n
)
≥
c
∗
g
(
n
)
f(n)≥c∗g(n)
n
≥
n
0
n≥n 
0
​
 
c
>
0
c>0
n
0
≥
1
n 
0
​
 ≥1
Solution

Here,

The growth of the c * g(n) function won't be faster than the f(n) function after 
n
0
n 
0
​
  because the above conditions are satisfied:

Since c * g(n) never grows faster than f(n) does, g(n) can be any expression such as 2n, 3n, etc. However, c * g(n) cannot be 5n, 10n, etc., because these functions grow faster than 4n + 3.

Let's assume c * g(n) is 2 * n. In this scenario,

c
∗
g
(
n
)
=
2
∗
n
c∗g(n)=2∗n
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
 
c
∗
g
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
 
f
(
n
)
Since, c∗g(n) cannot grow faster than f(n)
4
n
+
3
≥
2
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
4n+3≥2n [for all n≥1]
Omega Example
Figure: Omega Example
As c * g(n) <= f(n) we can say that:

f(n) = Ω(g(n))
=> f(n) = Ω(n) [read as f(n) is Omega of n]
Additionally, we could have chosen c * g(n) to be 3n or logn as well, because these functions also don't grow faster than 4n + 3.
