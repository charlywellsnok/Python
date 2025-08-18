Slicing a List
We can access a portion of a list using the slicing notation :.

Suppose we have a list like this:

numbers = [10, 20, 30, 40, 50, 60 ]
We can create a sublist with the items [30, 40, 50] from numbers using the slicing notation as follows:

numbers = [10, 20, 30, 40, 50, 60]

# start: 2
# end: 5
new_numbers = numbers[2: 5]
print(new_numbers)    # [30, 40, 50]
Here, numbers[2: 5] means that the new list's

first item should be the item at the 2nd index (of the numbers list)
last item should be the item at the 4th index
One crucial thing we need to remember about slicing is that the start index is inclusive, but the end index is exclusive.

Hence, numbers[2: 5] means create a new list with items present at index 2 up to 4 (and not 5).

Confused about something? Ask a question!
