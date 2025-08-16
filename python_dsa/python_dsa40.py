Thought Process to Implement Selection Sort
Consider the list we introduced in the previous section.

Unsorted List
Figure: Unsorted List
First, let's see how we can find the smallest element and swap it with the element in the first position.

1. Find the index of the smallest element in the list.

lst = [18, 10, 8, 14, 1]

min_index = 0

# iterate from second element to last
for j in range(1, len(lst)):
    
    # get the index of the smallest element
    if lst[j] < lst[min_index]:
        min_index = j

print(min_index)  # 4
Here's how this code works to find the smallest element:

Find the Smallest Element
Figure: Find the Smallest Element
2. Swap the smallest element with the first element.

# swap the smallest element with the first element
lst[min_index], lst[0] = lst[0], lst[min_index]
Now, the smallest element is placed in the first position.

We need to continue these steps for each position.

Next, we will add an outer loop to this code (with some adjustments) so that this process is repeated for all positions.
