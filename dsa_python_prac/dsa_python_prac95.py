Count Unique Elements in a List
Create a program to find the number of unique elements in a list.

Create a function named count_unique_elements() to count the number of unique elements in a list.
The count_unique_elements() function should accept a single argument, a list. It will return the count of unique elements.
Print the result from outside the function.
For instance, [10, 20, 10, 20, 20, 20, 30] contains three unique elements: 10, 20 and 30.

Assumption: The input list will only contain non-negative integers.

Hint: Once we create the counting list, it becomes much easier to solve this problem.

Example
Test Input

4 2 2 1 3 2 4 4 1 5
Expected Output

5
Confused about something? Ask a question








# Replace ___ with your code

# Replace ___ with your code

def count_unique_elements(lst):

    max_element = max(lst)
    counting_list = [0] * (max_element + 1)

    for num in lst:
        counting_list[num] += 1

    unique_count = 0
    
    for value in counting_list:
        if value >= 1:
            unique_count += 1
        
    return unique_count

# take integer inputs and convert it to a list
data_list = list(map(int, input().split()))

sorted_list = count_unique_elements(data_list)
print(sorted_list)




























