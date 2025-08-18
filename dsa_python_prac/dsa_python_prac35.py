Optimize Inner Loop
This is the bubble sort algorithm we've been using so far:

def bubble_sort(lst):

    size = len(lst)

    for i in range(size):

        for j in range(size - 1):           
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
If we look at the inner loop, we can notice it always iterates up to the second-last element, size - 1, and compares it with the last element.

# Inner loop always runs up to the second-last element
for j in range(size - 1):
    if lst[j] < lst[j + 1]:
       ... .. ...       
However, our program already places

The largest element in the last position after the first iteration
The second-largest element in the second-last position after the second iteration
And so on...
Sorted Elements in Each Iteration
Figure: Sorted Elements in Each Iteration
Since each outer loop iteration places an element in its final position (from right to left), we can optimize our code by reducing the number of inner loop comparisons.

# Outer loop controls number of passes
for i in range(size):
    # Reduces comparison range by i in each pass
    # Before: range(size - 1)
    for j in range(size - 1 - i):
       ... .. ...
Next, let's write the complete program of the optimized bubble sort.

Confused about something? Ask a question!
