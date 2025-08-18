Source Code: Insertion Sort
def insertion_sort(lst):
    
    for i in range(1, len(lst)):
        key = lst[i]
        
        j = i - 1
        
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1

        lst[j + 1] = key
    
    return lst

data =  [7, 4, 1, 3, 2]

print(f"Unsorted List: {data}")
sorted_list = insertion_sort(data)
print(f"Sorted List: {sorted_list}")
Output

Unsorted List: [7, 4, 1, 3, 2]
Sorted List: [1, 2, 3, 4, 7]
Confused about something? Ask a question!
