Optimize Loop Logic
In bubble sort, each iteration of the outer loop places one element in its correct position.

However, if no swaps occur during an entire pass of the inner loop, we know that elements are already in their correct positions—the list is sorted.

No Swaps Occur in a Sorted List
Figure: No Swaps Occur in a Sorted List
Here's how we can add this logic to our code:

size = len(lst)

for i in range(size):

    # Variable to track swapping
    swapped = False
    
    for j in range(size - 1 - i):

        # Change the swapped variable to True if swapping occurs
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            swapped = True
    
    # If swapping doesn't occur, the list is sorted
    # Terminate the loop when sorted
    if not swapped:
        break
Confused about something? Ask a question!
