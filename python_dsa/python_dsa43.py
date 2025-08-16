uSelection Sort
Can you write the selection sort program on your own?

Create a function named selection_sort() that takes a list as its argument.
Sort the list in ascending order within the function and return the sorted list.
Print the sorted list outside the function.
Example
Test Input

1 15 6 8 2 5 9
Expected Output

[1, 2, 5, 6, 8, 9, 15]













# Replace ___ with your code

def selection_sort(lst):

    for i in range(len(lst)):

        # assume the first unsorted element is the minimum
        min_index = i

        # iterate over unsorted elements
        for j in range(i + 1, len(lst)):

            # find index of the smallest element
            # in the unsorted part of the list
            if lst[j] < lst[min_index]:
                min_index = j

        # swap the smallest element with the first element
        # of the unsorted part
        lst[min_index], lst[i] = lst[i], lst[min_index]

    return lst

# take inputs and convert it to a list
data_list = list(map(int, input().split()))

result = selection_sort(data_list)

print(result)
