Thought Process to Implement Insertion Sort
This is how we implement insertion sort in Python:

1. Divide the array into sorted and unsorted sublists by finding the key element.

The key will always be the first element of the unsorted part.

Sorted and Unsorted Parts
Figure: Sorted and Unsorted Parts
Let i be the index of the key. Then,

key = lst[i]
This will help us virtually divide our list into two parts. All indexes less than i now belong to the sorted part.

Idea Emoji
Note: Initially, the sorted part contains only one element, 7. A list with a single element is always considered sorted.
2. Compare the key with the sorted elements one by one (from right to left) until the key element is either equal to or smaller.

If the sorted element to the left is larger than the key, we

Shift that element one position to the right.
Keep repeating this process until the sorted element is smaller than the key.
Finally, insert key at the correct position.
Here's how we can do it.

key = lst[i]

j = i - 1

# compare the key element with elements to its left one by one
# end the loop if the key element is larger or equal  
while key <= lst[j] and j >= 0:

    # shift the element to its right
    lst[j + 1] = lst[j]
  
    # decrease j to go to the next element to its left
    j = j - 1

# insert the key element at the correct position
lst[j + 1] = key
Next, we will use a loop to repeat this process for all the elements in the list.
