Counting Swaps
Write a program to count the number of swaps made during the selection sort process.

Create a function named count_swaps() that takes a list of integers as its input.
The function should return the number of swaps needed to sort the list.
Print the number of swaps required from outside the function.
For example, the list [3, 1, 7, 5, 6] requires 3 swaps.

After the first swap, the list is converted to [1, 3, 7, 5, 6].

After the second swap, the list is converted to [1, 3, 5, 7, 6].

After the third swap, the list is converted to [1, 3, 5, 6, 7].

Refer to the code outline for hints.

Example
Test Input

3 1 7 5
Expected Output

2
Confused about something? Ask a question!



















# Replace ___ with your code

def count_swaps(lst):

    # set swaps to 0
    swaps = 0

    for i in range(len(lst)):
        min_index = i

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        # swap only if lst[i] and lst[min_index] are not equal
        if lst[i] != lst[min_index]:
            lst[i], lst[min_index] = lst[min_index], lst[i]
            swaps += 1

    return swaps

# take integer inputs and convert it to a list
data = list(map(int, input().split()))

result = count_swaps(data)

print(result)
