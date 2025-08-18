Merge Sort
Can you write the merge sort program on your own?

Create a function named merge_sort() that takes a list of numbers as its argument.
Sort the list using merge sort and return it.
Outside the function, print the returned list.
Example
Test Input

1 15 6 8 2 5 9
Expected Output

[1, 2, 5, 6, 8, 9, 15]
Confused about something? Ask a question!










# Replace ___ with your code

def merge_sort(lst):

    # base condition:
    # recursion ends if the length of the list is 1 or less
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    # get the left half of the list
    # and further divide it using recursion
    left_partition = merge_sort(lst[: mid])

    # get the right half of the list
    # and further divide it using recursion
    right_partition = merge_sort(lst[mid:])

    # call the merge() function
    # combine list recursively
    return merge(left_partition, right_partition)

# function to sort and merge sublists (conquer phase)
def merge(left, right):

    output = []

    i = 0
    j = 0

    # merge elements in a sorted manner
    # from left and right portions
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    # append the remaining element
    output.extend(left[i:])
    output.extend(right[j:])

    return output

# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = merge_sort(data_list)

print(sorted_list)
