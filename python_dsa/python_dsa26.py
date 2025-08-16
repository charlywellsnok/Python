Visualize Bubble Sort
Click on the "Visualize this code" button below to see bubble sort in action.

def bubble_sort(lst):

    size = len(lst)

    # outer loop to access each list element
    for i in range(size):

        # inner loop to compare list elements
        for j in range(size - 1):

            # swap elements if necessary
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst       

data_list = [15, 16, 6, 8, 5]
print(f"Unsorted List: {data_list}")

sorted_list = bubble_sort(data_list)

print(f"Sorted List: {sorted_list}")
