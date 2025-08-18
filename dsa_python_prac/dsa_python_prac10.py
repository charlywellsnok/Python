List Slicing Examples
numbers = [10, 20, 30, 40, 50, 60]

# items from index 0 to 3
print(numbers[0: 4])    # [10, 20, 30, 40]

# items from index 3 to 4
print(numbers[3: 5])   # [40, 50]

# using negative index in slicing

# items from the fourth item (3rd index)
# to the second-last item

print(numbers[3: -1])   # [40, 50]
Here, numbers[3: -1] returns a list with items from index 3 to index -2 (because the last index -1 is exclusive and not included in the list).

Confused about something? Ask a question!
