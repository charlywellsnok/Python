Big O Complexity Chart
Now that we have discussed different types of complexities, our next step is to explore which time complexity is the most optimal.

If we plot a graph of Input Size Vs. Time for different algorithms, it would look something like this.

Big O Complexity Chart
Figure: Big O Complexity Chart
From the graph, we can see that O(1) and 
O
(
log
⁡
n
)
O(logn) time complexities are better as they grow much slower than O(n) and 
O
(
n
2
)
O(n 
2
 ) complexities.

O
(
n
2
)
O(n 
2
 ) time complexity increases exponentially with input size, making them nearly unworkable with. Hence, we should try to avoid writing programs with 
O
(
n
2
)
O(n 
2
 ).

In many scenarios, we can optimize such programs with 
O
(
n
2
)
O(n 
2
 ) to O(n) or O(log n) complexity. We can even optimize programs with O(n) complexity to O(log n).

Next, we will convert a program with 
O
(
n
2
)
O(n 
2
 ) time complexity to O(n).
