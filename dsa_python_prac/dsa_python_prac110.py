Explanation: Binary Search Using Recursion
We call the binary_search() function recursively until low is greater than high (similar to the iterative process).

if high >= low:
    # 1. update the mid element

    # 2. if target is equal to mid, return index of mid

    # 3. update either low or high and make recursive calls
else:
    return None
If low is greater than high, it means the target element is not in the list. We return None in this case.

1. Update the mid element.

mid = (low + high) // 2
2. If the target is equal to mid, return the index of mid.

if lst[mid] == target:
    return mid
If the middle element is equal to the target, we have found the element. In this case, we return the index of the middle element, and the recursion ends.

3. Update either low or high elements and make recursive calls.

Similar to the iterative process:

If the mid element is greater than the target, we update high to mid - 1.
If the mid element is less the target, we update low to mid + 1.
Then we call the binary_search() function with these updated values.

elif lst[mid] > target:
    return binary_search(lst, target, low, mid - 1)
else:
    return binary_search(lst, target, mid + 1, high)
Confused about something? Ask a question!
