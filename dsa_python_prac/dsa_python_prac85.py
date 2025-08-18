Pick Middle Element as Pivot
Write a quick sort program that sorts elements in ascending order. However, choose the middle element as the pivot.

Create a function

Create a function named quick_sort() that takes a list as its argument.
Implement the quick sort algorithm with the middle element as the pivot.
Return the sorted list.
Print the returned list outside the function.
Example
Test Input

7 2 1 6 8 5 3 4
Expected Output

[1, 2, 3, 4, 5, 6, 7, 8]
Confused about something? Ask a question!





# Replace ___ with your code

def quick_sort(lst):
    length = len(lst)
    if length <= 1:
        return lst
    else:
        # choose the middle element as pivot
        pivot = lst.pop(length // 2)

    right = []
    left = []

    for element in lst:

        if element > pivot:
            right.append(element)
        else:
            left.append(element)

    return quick_sort(left) + [pivot] + quick_sort(right)

data_list = list(map(int, input().split()))

sorted_list = quick_sort(data_list)
print(sorted_list)
