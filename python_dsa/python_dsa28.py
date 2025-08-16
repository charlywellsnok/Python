Bubble Sort in Descending Order
Write a program to sort the list items in descending order using bubble sort.

Create a function named bubble_sort() that takes a list as its argument.
Sort the list in descending order within the function and return the sorted list.
Print the sorted list from outside the function.
Tip: In this case, you need to swap elements if the current element is smaller than the next element.

Example
Test Input

1 15 6 8 2 5 9
Expected Output

[15, 9, 8, 6, 5, 2, 1]




# Replace ___ with your code

def bubble_sort(lst):

    size = len(lst)

    # outer loop to access each list element
    for i in range(size):

        # inner loop to compare list elements
        for j in range(size - 1):

            # swap if the element is less than the next element
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst

data_list = list(map(int, input().split()))

sorted_list = bubble_sort(data_list)
print(sorted_list)
