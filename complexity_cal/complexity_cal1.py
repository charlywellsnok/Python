How to Analyze Algorithms?
Various factors can be considered while analyzing an algorithm. Among them, two factors are particularly important:

Time Complexity: How long an algorithm takes to run with respect to the input size.
Space Complexity: How much space an algorithm takes to run with respect to the input size.
In the next chapter, we will dive deeper into time complexity.


Introduction to Time Complexity
Time complexity is the measure of how an algorithm's runtime grows as the input size increases. It's one of the most important concepts in Data Structures and Algorithms (DSA).

But how do we actually calculate the time complexity of an algorithm?

At first, you might think we could just track the execution time. For example, if a program takes 16 minutes to run, does that mean its time complexity is 16 minutes?

Not quite! Execution time depends on factors like:

The device running the program,
The programming languages used,
Network speed, and more.
For this reason, execution time is not a reliable measure. Instead, we calculate time complexity based on the number of steps required for a given input. For example,

If an algorithm has the time complexity of O(n),

It takes 5 steps for an input of 5
It takes 10 steps for an input of 10
We will cover what O(n) means in detail later in this course, but for now, remember:

Time complexity is about the number of steps required, and not execution time on a specific device!
