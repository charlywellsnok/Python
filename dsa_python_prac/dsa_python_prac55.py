Working of Insertion Sort
3. Compare the key with the elements of the sorted sublist (moving from right to left) and insert it into its correct position.

We'll compare the key element with the element to its left. If the key is smaller:

Shift the sorted element, 7, to the right.
Insert the key element, 4, in its position.
Insertion in the First Iteration
Figure: Insertion in the First Iteration
Here, we have inserted the key element, 4, into its correct position instead of simply swapping it. This is why it's known as insertion sort.

4. Repeat Step 3 for all the elements of the unsorted part.

Now, the key element is 1.

We'll compare the key element with the elements to its left one by one.

Insertion in the Second Iteration
Figure: Insertion in the Second Iteration
Here's how to interpret this image:

The key element, 1, is compared to 7. Since the key element is smaller, 7 is shifted to the right.
Again, the key element, 1, is compared to 4. Since the key element is smaller, 4 is shifted to the right.
Finally, 1 is inserted at the first position.
Idea Emoji
Note: If the key is larger than or equal to the element to its left, we stop the comparison because the element is already in the correct position.
Confused about something? Ask a question!
