Time Complexity - 
O
(
n
)
O( 
n
​
 )
Let's calculate the time complexity for the following code:

def print_numbers(n):
    i = 1
    k = 1
    
    while k < n:
        print(k)
 
        # add i to the value of k 
        k = k + i

        i = i + 1

n = 10
print_numbers(n)
Output

1
2
4
7
The time complexity of the above program will be around 
O
(
n
)
O( 
n
​
 ) and not exactly 
O
(
n
)
O( 
n
​
 ). We elaborate on this distinction later on in this course..

For the moment, just keep in mind that algorithms may have time complexities other than O(n), 
O
(
n
2
)
O(n 
2
 ), O(logn), and O(1) too.

Idea Emoji
Tip: Try running the above program with different values of n.
The time complexity calculation of this program may be slightly difficult to grasp initially, but as the next step, we will break it down in more detail.
