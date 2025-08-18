Working of Counting Sort
3. Count the occurrence of each element and put the count in the respective index of the counting list.

For example, element 5 occurs twice in the unsorted list. So, we add the number 2 in index 5 of the counting list.

Similarly, element 8 occurs once in the unsorted list. So, we insert 1 in index 8 of the counting list, and so on.

Count of Each Element 
Figure: Count of Each Element
Basically, in a counting list:

index - represents the value in our original list
value - represents the occurrence
4. Add the indexes of the counting list to the new sorted list.

Now, go through the counting list sequentially and append each of its indexes to a new list based on the value in that index.

The indices 0, 1, and 2 all have the values 0. So, we insert them 0 times in a new sorting list. Meaning we don't insert these elements in our new list.

Next,

the index 3 has the value 1, so we insert 3 once.
the index 4 has the value 2, so we insert 4 twice,
and so on.
Sort the List Based on the Index
Figure: Sort the List Based on the Index
As you can see, we've sorted all the elements.

Idea Emoji
Note: Since counting sort uses the indexes of a list for sorting, it cannot be used for floating-point numbers.
Confused about something? Ask a question!
