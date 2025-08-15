Introduction to Theta
The Theta notation represents the exact (tight) bound of the running time of an algorithm.

Let's understand the meaning of the statement with the help of a graph.

Graph of function
Figure: Graph of function
Here, the function f(n) is represented on the graph.

Next, we will plot two more functions on the graph, c1 * g(n) and c2 * g(n) that will intersect f(n) at the 
n
0
n 
0
​
  point.

Theta graph representation
Figure: Theta
Here,

c1 and c2 are positive constants.
the function f(n) will always be equal to or between the function c1*g(n) and c2*g(n) after the 
n
0
n 
0
​
  point.
In this case, c1*g(n) and c2*g(n) are called the exact bounds of f(n) because the f(n) function will never grow faster than c2*g(n) and slower than c1 * g(n).
