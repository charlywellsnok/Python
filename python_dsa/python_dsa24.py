Thought Process to Implement Bubble Sort
To implement bubble sort in Python:

1. Compare an element with its next element and swap them if necessary.

if lst[j] > lst[j + 1]:
    # swap elements       
    lst[j], lst[j + 1] = lst[j + 1], lst[j]
2. Repeat Step 1 for each element in the list using a loop.

Since we are comparing each element to its next element, we only need to run the loop up to the second-last element.

This is because the last element will not have a next element for comparison.

size = len(lst)

for j in range(size - 1):
    if lst[j] > lst[j + 1]:
        lst[j], lst[j + 1] = lst[j + 1], lst[j]
3. Repeat Step 2 for each element in the list.

Repeat the above steps for each position. With each iteration of the outer loop, one element will settle in its correct position, starting from the largest element.

size = len(lst)

for i in range(size):

    for j in range(size - 1):

        if lst[j] > lst[j + 1]:   
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
