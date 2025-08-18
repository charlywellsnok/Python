Thought Process to Implement Merge Sort
Divide the List Recursively
First, we need to divide the list into equal halves recursively until we get individual elements. Here's how we can do it:

1. Find the midpoint of the list.

merge_sort(lst):
    mid = len(lst) // 2
2. Divide the list's smaller halves recursively until individual elements are retrieved.

merge_sort(lst):

    mid = len(lst) // 2

    # end recursion if list is divided
    # into individual elements
    # i.e. when list length is 1
    if len(lst) <= 1:
        return lst


    # get the left half portion of list
    # and recursively divide it again
    left_partition = merge_sort(lst[: mid])

    # get the right half portion of list
    # and recursively divide it again
    right_partition = merge_sort(lst[mid: ])
Divide Into Sublists Recursively
Figure: Divide Into Sublists Recursively
Next, we will examine the division part of merge sort in action.

Confused about something? Ask a question!
