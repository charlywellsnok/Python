Optimized Bubble Sort
Write a program to sort the list items in descending order using optimized bubble sort.

Create a function named bubble_sort() that takes a list as an argument.
Inside the function, sort the list in descending order using optimized bubble sort.
Print the sorted list outside the function.
Example
Test Input

1 15 6 8 2 5 9
Expected Output

[15, 9, 8, 6, 5, 2, 1]
Confused about something? Ask a question!









# Replace ___ with your code

def bubble_sort(lst):
    size = len(lst)

    # initialize a variable as False
    # to indicate that no swaps have taken place
    for i in range(size - 1):
        flag = False

        for j in range(size - i - 1):
            # to sort in descending order
            # check if item less than next item
            if lst[j] < lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

                # if any element is swapped,
                # set swapped to True.
                flag = True

        if not flag:
            break

    return lst

# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = bubble_sort(data_list)
print(sorted_list)
