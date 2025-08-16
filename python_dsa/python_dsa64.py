Thought Process: The merge() Function
Suppose we have two sorted lists: left and right.

left = [5]
right = [4]
Our goal is to get this sorted list, [4, 5], by merging them.

The merge() function should also work for lists with more than one element.

Suppose we have two sorted lists: left and right.

left = [4, 5]
right = [2, 3, 7]
Our goal is to get this sorted list, [2, 3, 4, 5, 7], by merging them.

Here's how we can implement this functionality inside the merge() function.

1. Compare the elements of left and right and add the smaller element to the output list.

# empty list to store the merged result
output = []

# index for the left sublist
i = 0

# index for the right sublist
j = 0

# if element of left list is smaller
# add that element to the output list
if left[i] < right[j]:
    output.append(left[i])

# else, add the element of right list
else:
    output.append(right[j])
Append Smallest Element to Output
Figure: Append Smallest Element to Output
2. Repeat Step 1 for all elements in both lists until we reach the end of one of the lists.

Using a loop, we need to compare elements of left with the element elements of right in the manner shown below:

Merge Sublists in Sorted Manner
Figure: Merge Sublists in Sorted Manner
This allows us to extract the smallest elements one by one.

output = [ ]

i = 0
j = 0

# loop through both the lists
while i < len(left) and j < len(right):

    if left[i] < right[j]:
        output.append(left[i])
        i += 1;    # increment i
    else:
        output.append(right[j])
        j += 1;    # increment j
The loop terminates once one of the lists exceeds its bounds.

3. Outside the loop, append the remaining elements and return the output list.

def merge(left, right):
    output = [ ]

    i = 0
    j = 0

    while i < len(left) and j < len(right): 

        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j]) 
            j += 1



    # copy the remaining elements to output
    output.extend(left[i:])
    output.extend(right[j:])



    return output
Append remaining elements to output
Figure: Append remaining elements to output
Next, let's visualize how the merge() function works.
