Counting Sort in Descending Order
Can you create a counting sort program to sort elements in descending order?

Create a function named counting_sort() that takes a list of integers as its argument.
Inside the function, sort the list in descending order using counting sort.
Then, return the sorted list.
Finally, print the sorted list outside the function.
Example
Test Input

5 8 4 9 7 10 3 5 4 9
Expected Output

[10, 9, 9, 8, 7, 5, 5, 4, 4, 3]
Confused about something? Ask a question!





# Replace ___ with your code

def counting_sort(lst):

    if not lst:
        return lst

    max_element = max(lst)
    counting_list = [0] * (max_element + 1)

    for num in lst:
        counting_list[num] += 1

    sorted_output = []

    for index in range(len(counting_list) - 1, -1, -1):
        sorted_output.extend([index] * counting_list[index])

    return sorted_output

data_list = list(map(int, input().split()))

sorted_list = counting_sort(data_list)
print(sorted_list)
