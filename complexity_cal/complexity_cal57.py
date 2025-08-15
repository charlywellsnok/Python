Calculating Time Complexity
One key thing to notice in binary search is how efficiently it cuts down the search scope. In every iteration, it cuts the array to be searched to half, reducing the number of iterations logarithmically.

In the previous example, initially, we had 7 elements to search through. In the next step, we cut the number down to 3 or 4. By the third step, the number came down to 1 or 2. Binary search repeats this process for us until we find the target or determine that it is not in the array.

Now, let's find time complexities for the following cases:

Best Case
Worst Case
