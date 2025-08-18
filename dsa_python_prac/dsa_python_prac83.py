Quick Sort
Can you write the quick sort program on your own to sort elements in ascending order?

Create a function named quick_sort() that takes a list as its argument.
Inside the function, sort the list using quick sort.
Return the sorted list.
Print the sorted list outside the function.
Example
Test Input

1 15 6 8 2 5 9
Expected Output

[1, 2, 5, 6, 8, 9, 15]
Confused about something? Ask a question!





# Replace ___ with your code

def quick_sort(lst):
    length = len(lst)

    if length <= 1:
        return lst
    else:
        # pop() returns the last element of the list
        pivot = lst.pop()

    right = []
    left = []

    # iterate through list elements
    for element in lst:

        # check if element is greater than pivot
        if element > pivot:

            # add element to right list
            right.append(element)
        else:

            # add element to left list
            left.append(element)

    return quick_sort(left) + [pivot] + quick_sort(right)

# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = quick_sort(data_list)
print(sorted_list)
