Thought Process to Implement Counting Sort
Now that we know how counting sort works, let's see how we can implement it in Python.

1. Find the largest element and create the counting list.

max_element = max(lst)

# create a list and initialize all its elements to 0 
counting_list = [0] * (max_element + 1)
2. Count the occurrences of the elements in the unsorted list.

for num in lst:
    counting_list[num] += 1
3. Fill out the sorted list according to the value stored in the index of counting_list.

sorted_output = []

for index, value in enumerate(counting_list):
    sorted_output.extend([index] * value)
Sort the List Based on the Index and Value in Counting List
Figure: Sort the List Based on the Index and Value in Counting List
Next, we'll integrate all these components to create a working counting sort program.

Confused about something? Ask a question!
