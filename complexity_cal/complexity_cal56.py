Python Binary Search Code
Here is how we can implement binary search in Python:

def perform_binary_search(array, target, low, high):

    # Repeat until low index and high index meet
    while low <= high:
        
        # logarithmically reduce operations 
        mid = low + (high - low)//2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    # return -1 if target not found
    return -1


array = [3, 4, 5, 6, 7, 8, 9]
target = 4

low = 0
high = len(array) - 1
result = perform_binary_search(array, target, low, high)

print(f"The index of target is {result}")
Output

The index of target is 1
Next, we will analyze the time complexity of this program.
