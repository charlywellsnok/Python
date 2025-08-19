Binary Search
Program Description
Can you write the binary search program on your own?

Create a function named binary_search() that takes two arguments: lst (a list) and target (an integer) .
Use binary search to find the index of target in the lst list.
Return the index of target if the element is present in the list. If not, return None.
Print the returned value from outside the function
Note: We will use a predefined sorted list, [4, 5, 9, 12, 55, 79, 88, 99] for this practice. The target value to search for will be taken from the user input.

Example
Test Input

4
Expected Output

0
Confused about something? Ask a question!







# Replace ___ with your code

def binary_search(lst, target):

    # set low and high index
    low = 0
    high = len(lst) - 1

    # if low is greater than high,
    # the element is not found in the list
    while low <= high:

        # find middle element
        mid = (low + high) // 2

        # if target value is equal to middle element
        # return the element
        if target == lst[mid]:
            return mid

        # if target value is less than the middle element
        # update high to mid - 1
        elif target < lst[mid]:
            high = mid - 1

        # if target value is less than the middle element
        # update low to mid + 1
        else:
            low = mid + 1

    return None

lst = [4, 5, 9, 12, 55, 79, 88, 99]

target_value = int(input())

result = binary_search(lst, target_value)
print(result)
