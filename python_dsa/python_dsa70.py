Nth Smallest Element of Two Sorted Lists
Write a program to find the nth smallest element after merging and sorting two sorted lists.

Create a function named find_smallest_number() that takes three arguments: two lists and an integer n.
Assumption: The input lists will always be in ascending order.
Inside the function, merge two lists in ascending order.
Then, find the nth element from the list and return it.
Print the nth smallest element from outside the function.
For example,

For lists [4, 9, 11] and [3, 5, 7]. It's 4th smallest element is 7.

It's because if we merge these lists in ascending order, we will get [3, 4, 5, 7, 9, 11]. Hence, the 4th smallest element is 7.

Tip: Use the logic of the merge() function we previously created to merge lists in ascending order. Then, find the nth element.

Example
Test Input

5 6 7
3 5 9
2
Expected Output

5








# Replace ___ with your code

def find_smallest_number(nums1, nums2, n):

    output = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        # since both lists are in ascending order
        # compare their corresponding items
        # and append the smaller item list to output
        if nums1[i] < nums2[j]:
            output.append(nums1[i])
            i += 1
        else:
            output.append(nums2[j])
            j += 1
    output.extend(nums1[i:])
    output.extend(nums2[j:])

    return output[n - 1]

# take integer inputs and convert it to a list
nums1 = list(map(int, input().split()))

# take integer inputs and convert it to a list
nums2 = list(map(int, input().split()))

# take an integer input
n = int(input())

result = find_smallest_number(nums1, nums2, n)
print(result)
