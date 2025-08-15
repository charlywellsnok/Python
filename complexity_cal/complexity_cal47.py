Choosing Asymptotic Notation
In the previous section, we discussed the following different asymptotic notations:

Big Oh notation (O)

Big Oh describes how fast the running time of an algorithm can grow as the input gets larger. It gives us an upper limit on that growth. This doesn't mean it tells us the actual maximum time the algorithm will take. Instead, it shows how the time could increase in the most demanding scenarios as the input grows.

Omega notation (Ω)

Omega describes the slowest possible rate at which the running time can grow. In other words, it gives us the best-case growth. This doesn't mean the algorithm will always be that fast, but it won't be any faster than this bound.

Theta notation (θ)

Theta describes situations where the running time grows at the same rate in both the best and worst cases. It shows that the algorithm's growth is tightly bound on both sides.

So, using phrases like "maximum time" or "minimum time" can be misleading. These notations are not about exact durations. Instead, they describe how the performance of an algorithm behaves as the input size becomes very large.

To make these concepts easier to understand, let's look at a simple analogy in the next section.
