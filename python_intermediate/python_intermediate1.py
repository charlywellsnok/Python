List Comprehension Introduction
Before we learn about list comprehension, let's first understand why it is used.

Suppose we have to create a list of the first five powers of 2. To do this, we would typically use a for loop and append each item to the end of the list.

numbers = []

for i in range(1, 6):

    # adding 2**i to the end of the list
    numbers.append(2**i)

print(numbers)
Output

[2, 4, 8, 16, 32]
While this approach works, there is a concise way to accomplish the same result using list comprehension.

Next, let's find out how.
