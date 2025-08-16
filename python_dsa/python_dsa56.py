Partial Insertion Sort
Write a program that sorts only the first n elements of a list using the insertion sort algorithm.

Create the function perform_partial_sort() to sort the first n elements in ascending order.
This function takes two arguments: a list and the number of elements to sort.
Within the function, use insertion sort to arrange the elements.
Return the sorted portion and print it.
For example, if the number of elements to sort is 3, only first three elements are sorted and printed.

Example
Test Input

5 6 2 9 1 3 
3
Expected Output

[2, 5, 6]




















# Replace ___ with your code

def perform_partial_sort(lst, n):

    # iterate only till the n-th element
    for step in range(1, n):
        key = lst[step]
        j = step - 1

        # compare the key element with elements to its left one by one
        # end the loop if the key element is larger or equal
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1

        lst[j + 1] = key

    return lst[:n]


data = list(map(int, input().split()))
n = int(input())

sorted_partial_list = perform_partial_sort(data, n)
print(sorted_partial_list)
