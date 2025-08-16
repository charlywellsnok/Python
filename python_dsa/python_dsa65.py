Visualize: merge() Function
The merge() function takes two sorted lists and merges them into one sorted list.

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

merge([4, 5], [2, 3, 7, 9])
Idea Emoji
Note: For this function to work, left and right must already be sorted.
Next, we will combine the divide part and the merge part in the same code to create our merge sort program.
