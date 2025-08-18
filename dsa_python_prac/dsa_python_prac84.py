Quick Sort in Descending Order
Write a program to sort the list items in descending order using quick sort.

Create a function named quick_sort() that takes a list as its argument.
Sort the list in descending order within the function and return the sorted list.
Print the sorted list from outside the function.
Example
Test Input

1 15 6 8 2 5 9
Expected Output

[15, 9, 8, 6, 5, 2, 1]
Confused about something? Ask a question!




# Replace ___ with your code

def quick_sort(lst):
    length = len(lst)

    if length <= 1:
        return lst
    else:
        pivot = lst.pop()

    right = []
    left = []

    for element in lst:

        if element > pivot:
            right.append(element)
        else:
            left.append(element)

    # this part is changed
    return quick_sort(right) + [pivot] + quick_sort(left)

# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = quick_sort(data_list)
print(sorted_list)
