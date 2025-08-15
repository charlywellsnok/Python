Analysis of 
O
(
n
)
O( 
n
​
 ) Complexity
Here's how the value k changed with respect to i in the last program.

i	k
1	1
2	1 + 1 
3	2 + 2 
4	2 + 2 + 3 
5	2 + 2 + 3 + 4
.
.	.
.
m	2 + 2 + 3 + 4 + ….. + m - 1 
The loop continues until 
k
≥
n
k≥n, based on the condition in the program.

Now, let's approximate the total value of k when the loop stops:

k
=
2
+
2
+
3
+
4
+
…
+
(
m
−
1
)
k=2+2+3+4+…+(m−1)
We approximate this to be roughly the sum of the first m natural numbers:

⇒
k
≈
m
(
m
+
1
)
2
⇒k≈ 
2
m(m+1)
​
 
Since the program stops when 
k
≥
n
k≥n, we say:

m
(
m
+
1
)
2
≥
n
2
m(m+1)
​
 ≥n
To simplify the math, we approximate again by treating this inequality as an equation and ignoring the +1 term and the division for large values of m:

⇒
m
2
≈
n
⇒m 
2
 ≈n
⇒
m
≈
n
⇒m≈ 
n
​
 
So, the loop runs for about 
n
n
​
  iterations.

Hence, the time complexity of the program is:

O
(
n
)
O( 
n
​
 )
We used approximations twice — once to simplify the sum of terms, and once to convert an inequality into an equation — so the final time complexity is close to 
O
(
n
)
O( 
n
​
 ), not exact.
