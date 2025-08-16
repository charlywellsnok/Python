uThought Process to Implement Selection Sort
3. Repeat step 2 for each element in the list.

for i in range(len(lst)):
    min_index = i

    for j in range(i + 1, len(lst)):
        if lst[j] < lst[min_index]:
            min_index = j
Here, we have added an outer loop to ensure that each element in the list is considered, not just the first element.

1st iteration

In the first iteration of the outer loop, we identify the smallest element in the entire list (the entire list is unsorted). Then, this element is swapped with the first element.

2nd iteration

After the first iteration, the smallest element is placed in the first position. The unsorted position of the list will be from the second to the last position.

In the second iteration, we identify the smallest element in the unsorted position of the list (second-smallest element). Then, this element is swapped with the second element.

This process continues until the end of the list is reached. By the final iteration, the list will be fully sorted.
