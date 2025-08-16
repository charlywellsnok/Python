Omit Start and End Index in Slicing
It is possible to omit the start or end index while slicing.

Omit the Start Index

If we omit the start index, the slicing starts from the first item.

numbers = [10, 20, 30, 40, 50, 60]

# items from first item to third index
print(numbers[: 4])    # [10, 20, 30, 40]
Omit the End Index

If we omit the end index, the slicing goes up to the last item.

numbers = [10, 20, 30, 40, 50, 60]

# items from 3rd index to last item
print(numbers[3: ])   # [40, 50, 60]
What if we omit both the start and end indexes?

If we omit both the start and end indexes, we get a new list that contains all the items from the original list (from the first item to the last item).

numbers = [10, 20, 30, 40, 50, 60]

# omitting both the start and end indexes
# items from first to last
print(numbers[:])   # [10, 20, 30, 40, 50, 60]
