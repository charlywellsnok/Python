Computer Science Interpretation
Let's start this analysis with a graph of different time complexities.

Big O graph 
Figure: Big O
Suppose our code has O(n) time complexity. This means, for a sufficiently large input,

our code may complete execution with O(log n) complexity, or
our code may complete execution with O(n) complexity.
however, it will never take 
O
(
n
2
)
O(n 
2
 ) complexity (because the growth of 
n
2
n 
2
  is faster than that of n).
Essentially, the Big O notation tells us how time complexity grows with input size. The growth can be logarithmical O(log n), linear O(n), quadratical 
O
(
n
2
)
O(n 
2
 ), and so on.

Further, if a program has a certain time complexity, let's take O(log n) for an example, we can be sure that its time complexity will never grow faster than log(n).
