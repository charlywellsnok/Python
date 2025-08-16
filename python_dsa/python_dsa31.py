Optimizing Inner Loop
The output of this optimized bubble sort implementation is the same as the unoptimized one. However, this program doesn't compare the already sorted elements.

When you check the steps in visualizer, you can see this code now executes in fewer steps.

# Bubble sort in ascending order
def bubble_sort(lst):

    size = len(lst)
    
    for i in range(size):

        for j in range(size - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

data_list = [9, 6, 1, 4, 2]

sorted_list = bubble_sort(data_list)
print(sorted_list)

