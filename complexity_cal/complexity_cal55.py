Introduction to Binary Search
Binary search is a fast and efficient way to find the index of a target element in a sorted list or array.

Unlike linear search, which checks each element one by one, binary search works by repeatedly dividing the search range in half. This makes it much faster, especially for large datasets.

Idea Emoji
Note: We can use binary search only in a sorted list or array. If the list or array is not sorted, we must sort the array first.
Binary Search
Figure: Binary Search
Let's search a target value (4) using the binary search algorithm.

To find the index of this element, we will follow the following steps:

Step 1: Start with the full range

We begin with the entire array.

Set low = 0 (first index), and high = 6 (last index).

Step 2: Find the middle

Calculate the middle index:

mid = (low + high) // 2 = (0 + 6) // 2 = 3
The value at index 3 is 6.

Binary Search
Figure: Binary Search
Step 3: Compare middle value with target

We compare 6 (middle value) with the target 4.

Three possibilities:

If target == mid value (We found the target.)
If target < mid value (Search the left half (before mid).)
If target > mid value (Search the right half (after mid).)
In our case:

4 < 6 (So, the target must be in the left half.)

Update high:

high = mid - 1 = 3 - 1 = 2
Binary Search
Figure: Binary Search
Step 4: Repeat on the new range

Now we search within this smaller segment:

low = 0, high = 2

Calculate new middle:

mid = (0 + 2) // 2 = 1
The value at index 1 is 4.

Binary Search
Figure: Binary Search
Step 5: Compare again

Compare 4 (middle value) with 4 (target):

4 == 4 (We found it.)

Finally return the index of the target, that is index 1.
