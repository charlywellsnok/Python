Finding Time Complexity from Polynomials
The time complexity of a function is determined by the term with the highest degree in the polynomial, but we ignore its coefficient (the constant that multiplies the variable).

Example 1

Consider the function of the steps required to find the sum of the first n natural numbers:

f(n) = 2n + 2
Here, the term with the highest degree is 2n. Since we don't include the coefficient in time complexity, its time complexity is n.

Idea Emoji
Note: We typically denote time complexity as O(n) instead of just n. We will cover O(n) (the Big O notation) for time complexity in the next chapter.
This means our program takes n steps to complete.

Example 2

Let's take another example.

f
(
n
)
=
5
n
3
+
2
n
2
+
10
n
f(n)=5n 
3
 +2n 
2
 +10n
Here, the degree of the polynomial is 3 and the term with the highest degree is 
5
n
3
5n 
3
 . Hence, its time complexity is 
O
(
n
3
)
O(n 
3
 ).

Thus, a program with 
O
(
n
3
)
O(n 
3
 ) time complexity takes 
n
3
n 
3
  steps to complete.
