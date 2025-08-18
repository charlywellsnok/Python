Merge Sort in Descending Order
Write a program to sort the list items in descending order using merge sort.

Create a function named merge_sort() that takes a list as its argument.
Sort the list in descending order within the function and return the sorted list.
Print the sorted list from outside the function.
Example
Test Input

1 15 6 8 2 5 9
Expected Output

[15, 9, 8, 6, 5, 2, 1]
Confused about something? Ask a question!









# Replace ___ with your code

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_partition = merge_sort(lst[: mid])
    right_partition = merge_sort(lst[mid: ])

    return merge(left_partition, right_partition)

def merge(left, right):

    output = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        # use > for descending sort
        if left[i] > right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])
    return output

data_list = list(map(int, input().split()))

sorted_list = merge_sort(data_list)
print(sorted_list)
