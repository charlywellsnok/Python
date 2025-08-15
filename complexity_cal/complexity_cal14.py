Example: Constant Time Complexity
Let's look at the following function:

def get_squares_sum(number1, number2):
    
    # square the numbers
    number1 = number1**2
    number2 = number2**2
    
    # get the sum of squares
    result = number1 + number2

    return result

# example 
square_sum = get_squares_sum(5, 15)
print(square_sum)
Output

250
In the program above, the get_squares_sum() function takes 4 steps to execute regardless of the input size. The number of steps remains 4 regardless of the values you input for number 1 and number 2.

Hence, the time complexity of the above program is O(1).

Confused about something? Ask a question!
