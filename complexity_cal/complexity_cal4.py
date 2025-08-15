Analysis of Algorithms
When analyzing an algorithm, we consider three possible scenarios:

Best Case: The algorithm performs with the least possible number of steps.
Average Case: The algorithm performs with the average number of steps.
Worst Case: The algorithm performs with the maximum possible number of steps.
Consider the following list/array:

numbers = [9, 11, 12, 18, 15]
Best case

Suppose we need to search for 9 in the numbers list.

We would find 9 in the first search.
Even if the list grows, we would still be able to find it in our first search.

This is the best-case analysis—the algorithm performs at its best with the least number of steps.

Worst case

Now, suppose we need to search for 19 in the numbers list.

The number 19 isn't in the list, so we would have to search through the entire list (5 steps).
This is the worst-case analysis as it needs us to check every element before concluding that 19 is not present in the list.

Average case

We may need to search for an element that falls somewhere in between the first and last elements.

If the element is present in the first position, it would take 1 search.
If the element is present in the third position, it would take 3 searches.
Similarly, if the element is present in the nth index, it would take n searches. '
The average case analysis is calculated by taking the sum of all possible cases and dividing by the total number of cases:

A
v
e
r
a
g
e
 
C
a
s
e
=
s
u
m
 
o
f
 
a
l
l
 
p
o
s
s
i
b
l
e
 
c
a
s
e
s
n
Average Case= 
n
sum of all possible cases
​
 
Therefore, the average case analysis to search for an element in the numbers list is:

A
v
e
r
a
g
e
 
C
a
s
e
=
1
+
2
+
3
+
4
+
5
5
=
3
Average Case= 
5
1+2+3+4+5
​
 =3
In other words, it takes 3 steps to search for an element in the list.
