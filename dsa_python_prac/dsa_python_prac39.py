Source Code: Optimized Bubble Sort
# Bubble sort in ascending order
def bubble_sort(lst):

    size = len(lst)

    for i in range(size):
        
        swapped = False
        
        for j in range(size - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        
        # This part executes if the list is sorted        
        if not swapped:
            break

    return lst

data_list = [1, 2, 4, 9, 6]

sorted_list = bubble_sort(data_list)
print(sorted_list)
If you run the visualizer, you can see that the list will be sorted after the first iteration.

Hence, during the second iteration, there will be no swapping and the program terminates early because of the break statement.

Confused about something? Ask a question!
