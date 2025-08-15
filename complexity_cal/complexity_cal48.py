Analogy of Asymptotic Notation
Let's see an analogy to better understand asymptotic notations.

Imagine you want to buy a laptop and you have a budget of $100 for it.

You don't know how much it costs but you have three possibilities to consider:

P
r
i
c
e
≤
$
100
Price≤$100

The laptop may cost you $100, $80, or $1. However, it is certain that the price of the laptop will not be more than $100. Hence, you can buy the laptop without any problem.

This possibility would be exactly like the Big O. If a program takes O(n) time to execute, it means that the program can take n, logn, or even less time to execute. We can tell that the rate of growth of our algorithm will never be more than O(n) for a sufficiently large value of n.

P
r
i
c
e
≥
$
100
Price≥$100

The laptop may cost you $100, $101, or $1000. The price will certainly be $100 or more, with no upper limit. In this case, buying the laptop would not be possible.

This possibility would resemble the Omega scenario. If the time complexity of our program is Ω(n), it means that the program can take n, 
n
2
n 
2
 , or 
n
3
n 
3
 time to execute.

This is not particularly useful because it does not tell us how fast the time complexity of our algorithm will grow for large values of n.

P
r
i
c
e
=
$
100
Price=$100

The laptop can cost you exactly $100. In this case, you can buy the laptop without any problem.

This possibility would be exactly like Theta. If the time complexity of our program is ፀ(n), it means it will take ፀ(n) time to execute. This is useful information as the rate of growth of our algorithm will be the same as ፀ(n) even for a sufficiently large values of n.

This analogy helps illustrate how each notation gives a different kind of information:

Big O tells us how slow an algorithm could be (at most).
Omega tells us how fast it could be (at best).
Theta tells us how fast it always is, within a narrow range.
In practice, Big O is the most commonly used, especially when analyzing performance for large inputs. It helps us understand how an algorithm might behave in the most demanding scenarios.
