Worst Case
Consider the following scenarios where the target value is:

not present in the list,
he first element, or
the last element,
In these scenarios, the loop continues several iterations and continues dividing the list to half until the condition of the while loop low <= high is False.

Therefore,

Time complexity = O(log n)
This is considered the worst case because, unlike the best case—where the target is found in the first comparison—the algorithm must continue searching through all possible divisions until the search space is exhausted.
