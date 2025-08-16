Thought Process to Implement Insertion Sort
3. Repeat Step 1 and Step 2 until all elements are sorted.

Now, we will add an outer loop to repeat step 1 and step 2 for all elements.

# iterate from index 1 to last index
for i in range(1, len(lst)):

    # key element 
    key = lst[i] 

    j = i - 1

    # compare the key element with elements to its left one by one
    # end the loop if the key element is larger or equal         
    while j >= 0 and key < lst[j]:
        # shift the element to its right
        lst[j + 1] = lst[j]
  
        # decrease j to go to the next element to its left
        j = j - 1

    # insert the key element at the correct position
    lst[j + 1] = key
Next, we will write a working program to implement insertion sort.
