Condition in List Comprehension
List comprehensions can also have an optional if condition along with a for loop.

Suppose we have a list like this:

numbers = [12, 15, 21, 32, 14]
Now if we have to create a new list containing only the even numbers from this list. Here's how we can do it.

Let's first use list comprehension without the if condition.

numbers = [12, 15, 21, 32, 14]

even_numbers = [n for n in numbers]
print(even_numbers)    # [12, 15, 21, 32, 14]
This code iterates through the numbers list and adds each item one by one. That's why we are getting the same list.

Now to get only even numbers, we need to add condition n % 2 == 0 (if the remainder when n divided by 2 is 0, it's an even number). Let's add this condition.

numbers = [12, 15, 21, 32, 14]

even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)    # [12, 32, 14]
Notice this code if n % 2 == 0 inside the list comprehension. This code adds n to the list only if it's an even number.
