Computer Science Interpretation
Suppose our code has θ(n) time complexity. This means that for a sufficiently large input,

our code will complete the execution with θ(n) complexity;
it will never take 
θ
(
n
2
)
θ(n 
2
 ) complexity (because the growth of 
n
2
n 
2
  is faster than that of n);
it will never take 
θ
(
n
3
)
θ(n 
3
 ) complexity (because the growth of n3 is faster than that of n).
Essentially, the Theta notation tells us that if a program has a certain time complexity, let's say θ(log n), we can be certain that the time complexity of the program grows neither faster nor slower than θ(log n).
