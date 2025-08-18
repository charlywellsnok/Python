Working of Quick Sort
Suppose we have the following unsorted list.

Unsorted List
Figure: Unsorted List
1. Select the pivot element.

There are several variations of quick sort depending on what element is selected as the pivot.

It is important to pick a good pivot element for the fast implementation of quick sort. A pivot can be:

The first element
The last element
The middle element
Any random element from the list
We'll use the last element as our pivot element:

Select the Last Element as the Pivot
Figure: Select the Last Element as the Pivot
2. Rearrange the list.

Now, the elements that are smaller than the pivot are put on the left, and the elements larger than the pivot are put on the right.

Rearrange the List
Figure: Rearrange the List
3. Divide the sublists.

We choose pivot elements again for the left and right sublists separately, and then we repeat step 2.

Divide 
Figure: Divide the Sublists
4. Sort and merge the sublists.

First, we sort and merge the divided elements left to the initial pivot. Then, we do the same to the divided elements to the right of the pivot.

This leaves us with two sorted sublists.

Finally, we merge the left sublist, the pivot, and the right sublist to get the final sorted list.

Merge the Sorted Sublists
Figure: Merge the Sorted Sublists
Confused about something? Ask a question!
