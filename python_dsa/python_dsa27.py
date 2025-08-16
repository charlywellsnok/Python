Bubble Sort
Can you write the bubble sort program on your own?

Create a function named bubble_sort() that takes a list as its argument.
Sort the list in ascending order within the function and return the sorted list.
Print the sorted list from outside the function.
Example
Test Input

1 15 6 8 2 5 9
Expected Output

[1, 2, 5, 6, 8, 9, 15]





# Replace ___ with your code

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

data_list = list(map(int, input().split()))

bubble_sort(data_list)
print(data_list)
