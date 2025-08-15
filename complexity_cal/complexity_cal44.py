Visualizing Theta with Graphs
Here's the same graph of the f(n) function, c1 * g(n) and c2 * g(n) we created on the last page.

Theta graph representation
Figure: Theta
Here again, we assume suppose the following conditions are met:

1. 
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

2. 
n
0
>
1
n 
0
​
 >1 and 
n
≥
n
0
n≥n 
0
​
 

3. c1 > 0 and c2 > 0

We can then say that

f(n) = θ(g(n)) (read as f(n) is Theta of g(n))
Let's visualize where the above conditions are met in the graph.

Theta graph representation
Figure: Theta
Here, the growth of f(n) is always faster than c1 * g(n) and slower than c2 * g(n) on the highlighted part of the image.

Here, Theta is called the exact bound because for all values of n in the highlighted part, the value f(n) will always be either equal to or between c1 * g(n) and c2 * g(n).
