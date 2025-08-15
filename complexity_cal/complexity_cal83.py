Linear Space Complexity: O(n)
An algorithm has linear space complexity if the amount of memory required to execute is linearly proportional to the input size.

Let's take an example:

def find_sum(numbers):
    total = 0
    for i in numbers:
        # add i to total
        total = total + i
    return total

print(find_sum([1,2,3,4]))
Output

10
Let's find the space complexity of the find_sum() function.

Since space complexity is about memory usage in relation to the input size, we need to look at the input size to calculate space complexity.

In the above program,

Variables	Input Size
numbers	n (as the list can hold n elements)
sum	1 (sum can hold 1 element)
i	1 (sum can hold 1 element)
Space Complexity of find_sum() = n + 1 + 1
                               = n + 2
By frequency count method, we drop the constants and get:

Space complexity = O(n) 
This means, if the input size increases, the space complexity also increases linearly—just like time complexity does.
