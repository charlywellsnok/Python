Logarithmic Complexity Analysis
Now, let's see how the program we just created works for different input sizes.

def print_numbers(n):
    i = 1
    while i < n:
        print(i)
        i = i * 2
1. Input size (n): 8

i	i = i * 2	i < n
1	1 * 2 = 2	2 < 8 is True
2	2 * 2 = 4	4 < 8 is True
4 	4 * 2 = 8 	8 < 8 is False (loop ends)
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
:
log
⁡
(
n
)
=
log
⁡
2
8
Time complexity:log(n)=log 
2
​
 8
=
3
Time complexity:log(n)
 =3
This means for input value 8, our program takes 3 steps to complete.

2. Input size (n): 10

i	i = i * 2	i < n
1	1 * 2 = 2	2 < 10 is True
2	2 * 2 = 4	4 < 10 is True
4 	4 * 2 = 8 	8 < 10 is True
8	8 * 2 = 16	16 < 10 is False (loop ends)
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
:
log
⁡
(
n
)
=
log
⁡
2
10
Time complexity:log(n)=log 
2
​
 10
=
3.32
Time complexity:log(n)
 =3.32
=
4
 
(
c
e
i
l
i
n
g
 
v
a
l
u
e
)
Time complexity:log(n)
 =4 (ceiling value)
This means for input value 10, our program takes 4 steps to complete.

Similarly, if n, = 1000, our program takes 10 steps to complete because:

log
⁡
2
1000
=
9.96
log 
2
​
 1000=9.96
=
10
(
c
e
i
l
i
n
g
 
v
a
l
u
e
)
log 
2
​
 1000
 =10(ceiling value)
