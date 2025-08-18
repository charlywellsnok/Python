Thought Process to Implement Quick Sort
Now, let's see how we can implement quick sort. We'll create a function named quick_sort() that takes a list lst as its parameter.

1. Check for base condition and determine the pivot.

We return the list if it contains one or zero elements. Else, we use the final element as the pivot.

length = len(lst)

# base condition     
if length <= 1:
    return lst
else:
    # pop() returns the last element of the list
    pivot = lst.pop() 
Note that we've removed the pivot from the list using the pop() method because we need to insert it in a different position.

2. Place the elements into the greater and lesser sublists.

# two sublists to hold elements
# greater and smaller than pivot        
right = []
left = []

# iterate through list elements    
for element in lst:
       
    # check if element is greater than pivot
    if element > pivot:

        # add element to right list
        right.append(element)
        
    else:

        # add element to left list
        left.append(element)
3. Call the function recursively to merge the two sublists.

return quick_sort(left) + [pivot] + quick_sort(right)
Here, the return statement recursively calls quick_sort(left) and quick_sort(elements greater).

As a result, the list gets broken down into smaller and smaller pieces until the list contains a single element.

Then, the return statement appends 3 lists in the following order:

the list with the smaller values
the [pivot] list consisting of only the pivot element
the list with the greater values
Thus, the lists get sorted and merged with each recursion, until a fully sorted list is returned by the function.

Next, we'll combine all these components to create the quick_sort() function.

Confused about something? Ask a question!
