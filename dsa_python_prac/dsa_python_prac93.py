Counting Sort
Can you create a counting sort program to sort elements in ascending order on your own?

Create a function named counting_sort() that takes a list of integers as its argument.
Inside the function, sort the list using counting sort.
Then, return the sorted list.
Finally, print the sorted list outside the function.
Example
Test Input

5 8 4 9 7 10 3 5 4 9
Expected Output

[3, 4, 4, 5, 5, 7, 8, 9, 9, 10]
Confused about something? Ask a question!





def counting_sort(lst):

   # if list is empty or has one element, return itself
    if len(lst) <= 1:
        return lst

    # find the largest element
    # and create the counting list
    max_element = max(lst)
    counting_list = [0] * (max_element + 1)

    # fill the counting list with frequency of each number
    for num in lst:
        counting_list[num] += 1

    # create the sorted output list
    sorted_output = []
    for index, value in enumerate(counting_list):
        sorted_output.extend([index] * value)

    return sorted_output

data_list = list(map(int, input().split()))

sorted_list = counting_sort(data_list)
print(sorted_list)
