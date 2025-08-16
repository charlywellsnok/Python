Visualize Dividing the List Recursively
Click the "Visualize this code" button to see how the list is divided step by step.

def merge_sort(lst):

    if len(lst) <= 1:
        return lst
        
    print(f'lst: {lst}')

    mid = len(lst) // 2

    print(f'mid: {lst[mid]}')

    left = merge_sort(lst[: mid])
    print(f'Left partition: {left}')

    right = merge_sort(lst[mid: ])
    print(f'Right partition: {right}')

    return '---'

data_list = [5, 4, 7, 3, 2]
merge_sort(data_list)
As you can see, we keep splitting the list into left and right halves, until we can't split anymore.

In the program, the merge_sort() function is returning '---'.

However, to perform conquer and combine, we will call another function merge() from the return statement. This function will combine individual elements in a sorted manner, which we will explore next.
