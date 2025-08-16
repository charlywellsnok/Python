Visualize Merge Sort
Click the "Visualize this code" button to see how the full merge sort and focus on where the divide and merge process occurs.

def merge_sort(lst):

    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    left_partition = merge_sort(lst[: mid])

    right_partition = merge_sort(lst[mid:])

    # start merging
    return merge(left_partition, right_partition)

def merge(left, right):

    output = []

    i = 0   
    j = 0 

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    # append the remaining element
    output.extend(left[i:])
    output.extend(right[j:])
        
    return output
        
data_list = [6, 8, 1, 4, 5, 3, 7]
print(f"Unsorted: {data_list}")

result = merge_sort(data_list)

print(f"Sorted: {result}")
We might think that merge sort divides the whole list first. Then, it starts merging. But it doesn't work like that.

Instead, we divide one side of the list first, merge it, and then divide and merge the other side. This process keeps going until the entire list is sorted.

See the source code of merge sort in the next page and try with different lists.
