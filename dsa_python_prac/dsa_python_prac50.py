Selection Sort in Descending Order
Write a program to sort the list items in descending order using selection sort.

Create a function named selection_sort() that takes a list as its argument.
Sort the list in descending order within the function and return the sorted list.
Print the sorted list from outside the function.
Tip: In this case, you need to find the largest element and make swaps.

Example
Test Input

1 15 6 8 2 5 9
Expected Output

[15, 9, 8, 6, 5, 2, 1]
Confused about something? Ask a question!













# Replace ___ with your code

def selection_sort(lst):

    for i in range(len(lst)):

        min_index = i

        for j in range(i + 1, len(lst)):

            # to find the largest element, change < to >
            if lst[j] > lst[min_index]:
                min_index = j

        lst[min_index], lst[i] = lst[i], lst[min_index]

    return lst


# take inputs and convert it to a list
data_list = list(map(int, input().split()))

result = selection_sort(data_list)

print(result)
