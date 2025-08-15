Recurrence Relation for a Dividing Function
Mathematically speaking, the master theorem provides a solution to the recurrence relation. Let's learn how we can find the recurrence relation for a dividing function.

Suppose we have a program like this.

def test(n):
    if n > 0:
        print(n)
        test(n // 2)
Given that the test() function takes T(n) time to execute,

Recurrence Relation for a Dividing Function
Figure: Recurrence Relation for a Dividing Function
From the image, we can say

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
+
1
T(n)=T( 
2
n
​
 )+1+1
=
T
(
n
2
)
+
2
T(n)
 =T( 
2
n
​
 )+2
We can simply represent the constant 2 with c.

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
c
T(n)=T( 
2
n
​
 )+c
