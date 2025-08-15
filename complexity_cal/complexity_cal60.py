ime Complexity: O(nlogn)
Let's now time to put our knowledge so far to application, and calculate the time complexity for the following code:

def print_numbers(n):
    i = 0
    j = 1
    while i < n:
        while j < n:
            print(j)

            # j is doubled in each iteration
            # logarithmically reducing operations
            j = j * 2
        
        i = i+1

print_numbers(20)
Output

1
2
4
8
16
Here,

The outer loop (while i < n) runs n times.
The inner loop starts with j = 1 and doubles j each time (j = j * 2) until the condition j < n is false.
Since j is not reset inside the outer loop, the inner loop only runs once — during the first iteration. After that, j has become equal to or greater than n, so j < n immediately fails, and the inner loop is skipped.
Let's visualize with the following image:

Calculating Time Complexity
Figure: Calculating Time Complexity
Hence,

T
i
m
e
 
c
o
m
p
l
e
x
i
t
y
=
3
n
l
o
g
n
+
2
n
Time complexity=3nlogn+2n
=
n
l
o
g
n
 
[
h
i
g
h
e
s
t
 
t
e
r
m
]
Time complexity
 =nlogn [highest term]
=
O
(
n
l
o
g
n
)
Time complexity
 =O(nlogn)
Note:If j were reset during each outer loop iteration, the inner loop would run log n times in every iteration of the outer loop, giving a total of n log n steps. In that case, the time complexity would be O(n log n).

But in our code, since j keeps growing and isn't reset, the inner loop only runs once, and so the full program runs in O(n) time overall.
