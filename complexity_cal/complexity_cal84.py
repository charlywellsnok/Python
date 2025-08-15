Quadratic Space Complexity: 
O
(
n
2
)
O(n 
2
 )
An algorithm has quadratic space complexity if the amount of memory it takes to execute is proportional to the square of the input size.

This means as the input size grows, the memory required to execute the program also grows quadratically (think of linear but squared).

Let's take an example.

def print_list_items(nested_list):

    for single_list in nested_list:
        for item in single_list:
            print(item)

print_list_items([[1, 2], [4, 5]])
Output

1
2
4
5
Here, nested_list is a square matrix. Since space complexity is about memory usage in relation to the input size, we need to look at the input size to calculate space complexity.

In the above program,

Variables	Input Size
nested_list	n * n (square matrix)
single_list	n
item	1 
S
p
a
c
e
 
C
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
n
∗
n
+
1
+
1
Space Complexity=n∗n+1+1
=
n
2
+
2
Space Complexity
 =n 
2
 +2
Hence,

S
p
a
c
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
O
(
n
2
)
 
[
b
y
 
f
r
e
q
u
e
n
c
y
 
c
o
u
n
t
 
m
e
t
h
o
d
]
Space complexity=O(n 
2
 ) [by frequency count method]
This means, as the input size grows, the space complexity also grows quadratically—just like time complexity.
