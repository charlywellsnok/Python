Time Complexity of Two For Loops
Let's calculate the time complexity for the following code:

def print_numbers(n):
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j)

print_numbers(5)
Here,

The first loop runs n times.
The second loop also runs n times.
Let's visualize this program with the help of an image.

Calculating Time Complexity
Figure: Calculating Time Complexity
Here, the time complexity of this program is O(n) because the two loops are independent of each other and not nested.

If one loop was nested inside the other, the time complexity would have been 
O
(
n
2
)
O(n 
2
 ). The inner loop would run n times for every iteration of the outer loop.
