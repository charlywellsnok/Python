Constant Time Complexity
An algorithm has a constant time complexity if its execution time remains constant regardless of the input size.

If you were to plot this relationship on a graph, it would appear as a flat horizontal line — showing that the time stays the same, no matter how much the input grows.

Graph for Constant Time Complexity
Figure: Graph for Constant Time Complexity
Let's see an example:

lst = [22, 23, 24, 25, 11]
print(lst[3]) # Output: 25
Calculation of Constant Time Complexity
Figure: Calculation of Constant Time Complexity
The code above always takes a fixed amount of time – 2 units – to execute no matter how large the list is. Therefore, one would expect the time complexity of the above code to be O(2).

However, it is a common practice to use O(1) to denote constant time complexity whenever the code takes any fixed number of steps – 2, 3, 4 or 100.

Let's look at another example next.
