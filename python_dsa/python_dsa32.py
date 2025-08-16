Visualize Bubble Sort for Sorted List
Our optimized bubble sort completed in fewer steps than the unoptimized one. However, our program still iterates even when the list is already sorted.

For example, our bubble sort algorithm iterates five times for this already sorted list [1, 2, 5, 7, 9] because the list has five elements. You can test it out by running the visualizer below.

# Bubble sort in ascending order
def bubble_sort(lst):

    size = len(lst)
    
    for i in range(size):

        for j in range(size - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

data_list = [1, 2, 5, 7, 9]

sorted_list = bubble_sort(data_list)
print(sorted_list)
