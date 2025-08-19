Thought Process: Binary Search
Suppose we have the following sorted list, and we have to find the index of element 4 (the target value).

A Sorted list
Figure: A Sorted list
This is how binary search works:

1. Set the first index as low and the last index as high.

# set low and high index
low = 0
high = len(lst) - 1
Set Low and High
Figure: Set Low and High
2. Find the middle element.

mid = (low + high) // 2
Find the mid Element
Figure: Find the mid Element
3. Check for three possibilities.

Possibility 1: If the target value is equal to the middle element, we have found the element.

if target_value == lst[mid]:
    result_index = mid
Since our target_value is 4 and the current middle element is 6, this condition has not been met yet.

Possibility 2: If the target value is greater than the middle element, update the low index to mid + 1.

if target_value > lst[mid]
    low = mid + 1
This condition has not been met yet.

Possibility 3: If the target value is less than the middle element, update the high index to mid - 1.

if target_value < lst[mid]
    high = mid - 1
Update the high Index
Figure: Update the high Index
Basically, we are updating the low and high indexes such that they are closer to both the mid value and the target element.

4. We update the mid element again and repeat step 3.

We will repeat the process until low is greater than high. If low is greater than high, our target value is not in the list.

# if low is greater than high,
# the element is not found in the list 
while low <= high:

    # update middle point in each iteration
    mid = (low + high) // 2

    # condition for target value found
    if target_value == lst[mid]:
        return mid

    # update either low or high
    elif target_value < lst[mid]:
        high = mid - 1
    else:
        low = mid + 1
Basically, in each iteration, we are updating either the low or high index to bring it closer to the position of the target element.

In our case, the target element is found in the second iteration.

Found the Target Element
Figure: Found the Target Element
With this knowledge, we will create a working program for binary search next.

Confused about something? Ask a question!
