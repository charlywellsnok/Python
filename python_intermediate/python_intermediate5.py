Dictionary Comprehension
Just like list comprehension, dictionary comprehension is a concise way of creating dictionaries. Let's explore it with an example.

Suppose we have the following list:

numbers = [1, 2, 3, 4]
Now, suppose we have to create the following dictionary from the list:

{1: 1, 2: 4, 3: 9, 4: 16}
Here,

The keys of the dictionary are the items of the list
Their corresponding values are the squares of the items.
Let's first see how we can accomplish this task without dictionary comprehension.

numbers = [1, 2, 3, 4]

# creating an empty dictionary
square_numbers = {}

# using a loop to add items to dictionary
for number in numbers:
    square_numbers[number] = number**2

print(square_numbers)
Output

{1: 1, 2: 4, 3: 9, 4: 16}
Next, we will create the same dictionary using dictionary comprehension.
















