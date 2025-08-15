Approach 1: Solving with 
O
(
n
2
)
O(n 
2
 ) complexity
The problem can be solved simply by using a nested loop.

def two_sum(num_list, target_value):
    # iterate over each number in the list
    for i in range(len(num_list)):
        # iterate over subsequent numbers in the list
        for j in range(i + 1, len(num_list)):
            # check if their sum equals the target value
            if num_list[i] + num_list[j] == target_value:
                # return the indices of the two numbers
                return [i, j]

num_list = [2, 7, 11, 15]
target_value = 9

result = two_sum(num_list, target_value)

# print the result
print(result)
Output

[0, 1]
The complexity of this code is 
O
(
n
2
)
O(n 
2
 ) because

Complexity Calculation of two_sum() function
Figure: Complexity Calculation of two_sum() function
While the above code gives us the correct output, it is not the most efficient solution for large input sizes. It is possible to solve the same problem with reduced time complexity, which we will attempt next.
