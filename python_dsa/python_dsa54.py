Insertion Sort
Can you write the insertion sort program on your own?

Create a function named insertion_sort() that takes a list as its argument.
Sort the list in ascending order within the function and return the sorted list.
Print the sorted list outside the function.
Example
Test Input

1 15 6 8 2 5 9
Expected Output

[1, 2, 5, 6, 8, 9, 15]











# Replace ___ with your code

def insertion_sort(lst):
    # iterate from index 1 to last index
    for i in range(1, len(lst)):

        # key element
        key = lst[i]

        j = i - 1

        # compare the key element with elements to its left one by one
        # end the loop if the key element is larger or equal
        while j >= 0 and key < lst[j]:
            # shift the element to its right
            lst[j + 1] = lst[j]

            # decrease j to go to the next element to its left
            j = j - 1

        # insert the key element at the correct position
        lst[j + 1] = key

    return lst

# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

# call the insertion_sort() function
result = insertion_sort(data_list)

# print the sorted list
print(result)
