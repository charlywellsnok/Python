Visualizing Big O with Graphs
Let's revisit the graph of the functions f(n) and c * g(n) we created in the previous page.

Big O graph representation
Figure: Big O
In this graph, we assume that the following conditions are met:

1. 
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
 

3. c > 0

Under the conditions, we can conclude that:

f(n) = O(g(n)) (read as f(n) is Big Oh of g(n))
Let's visualize where the above conditions are met in the above graph.

Big O graph representation
Figure: Big O
Here, the growth of c * g(n) is always faster than O(g(n)) for values n0 and above, as illustrated on the highlighted part of the image.

Here, c * g(n) is called the upper bound because for all values of n in the highlighted part, the value of c * g(n) is always equal to or greater than O(g(n)).

Idea Emoji
Lingo: f(n) grows no faster than g(n).
Next, we will relate this mathematical interpretation to time complexity.
