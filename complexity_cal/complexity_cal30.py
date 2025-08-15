Convert 
O
(
n
2
)
O(n 
2
 ) to O(n) Complexity
Let's see an example of how we can rewrite a program and improve its time complexity. As we do so, we will achieve the same result, but drastically improve the performance.

Problem

Given a list of integers, num_list, and an integer, target_value, let's find the indices of the two numbers such that they add up to the target_value. Our goal is to implement this solution efficiently, reducing its time complexity from O(n²) to O(n).

Suppose:
num_list = [2, 7, 11, 15]
target_value = 9

The output should be:
[0, 1]

Reason:
2 plus 7 is 9.
The index of 2 and 7 is 0 and 1 respectively.
Let's take another example.

Suppose:
num_list = [2, 7, 11, 15]
target_value = 22

The output should be:
[1, 3]

Reason:
7 plus 15 is 22.
The index of 7 and 15 is 1 and 3 respectively.
Next, we will solve this problem with different complexities.

Confused about something? Ask a question!
