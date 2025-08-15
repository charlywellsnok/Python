Computer Science Interpretation
Let's suppose our code has Ω(n) time complexity. This means, for a sufficiently large input,

our code may complete execution with Ω(n) complexity, or
our code may complete execution with 
Ω
(
n
2
)
Ω(n 
2
 ) complexity,
however, it will never take Ω(log n) complexity (because the growth of log n is slower than that of n).
In other words, Omega notation gives a lower bound on how much time an algorithm will take — it can't be faster than that bound, but it can be slower (take more time).

For example, if a program has Ω(log n) complexity, the running time will grow at least as fast as

logn, meaning it won't be faster than logarithmic time.
