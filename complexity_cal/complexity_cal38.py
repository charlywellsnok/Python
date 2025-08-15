Big O Mathematics
Now, let's return to the mathematical interpretation of Big O.

Example

Given the following function,

f(n) = 4n + 3
Our goal is to find a function c * g(n) such that the following conditions are satisfied:

f
(
n
)
≤
c
∗
g
(
n
)
f(n)≤c∗g(n)
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

The growth of the f(n) function won't be exceed c * g(n) beyond 
n
0
n 
0
​
  since the above conditions are met

Because c * g(n) grows faster than f(n), it can be any expression such as 5n, 10n, 
2
n
2
2n 
2
 , etc.

However, g(n) can't be 3n, 2n, or similar functions because they grow slower than 4n + 3.

Let's assume c * g(n) is 10n. In this scenario,

c
∗
g
(
n
)
=
10
n
c∗g(n)=10n
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
∗
g
(
n
)
Since, f(n) cannot grow faster than c∗g(n)
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
4n+3≤10n [for all n≥1]
Big O Example
Figure: Big O Example
As 
c
∗
g
(
n
)
≥
f
(
n
)
c∗g(n)≥f(n), we can say that:

f(n) = O(g(n))
=> f(n) = O(n) [read as f(n) is big O of n]
Additionally, we could have chosen c * g(n) to be 
2
n
2
2n 
2
  or 
5
n
3
5n 
3
  as these functions also grow at a rate faster than 4n + 3.
