Approach 2: Reducing Time Complexity
Now, let's approach the same problem with reduced time complexity.

def two_sum(num_list, target_value):
    
    dictionary = {}

    for index, value in enumerate(num_list): 
        # add items of num_list to dictionary
        # value as key and index as value
        dictionary[value] = index
    
    for i in range(len(num_list)):
        complement = target_value - num_list[i]
        
        # check if item's complement is present in dictionary
        if complement in dictionary and dictionary[complement] != i:
            
            # return element index and complement's index
            return [i, dictionary[complement]]
    
num_list = [2, 7, 11, 15]
target_value = 9

result = two_sum(num_list, target_value)
print(result)    
Output

[0, 1]
Complexity Calculation of two_sum() function
Figure: Complexity Calculation of two_sum() function
Here, the code works similarly to our code on the last page. However, the time complexity of the code is O(n).
