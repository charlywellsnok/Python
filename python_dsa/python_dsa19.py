List Methods
Create a program to perform operations on a list using various list methods.

Suppose we have two lists as follows:

animals = ['Dog', 'Cat']
wild_animals = ['Tiger', 'Coyote']
Perform these operations on the animals list:

Add 'Raccoon' to the end of the animals list.
Add all the elements from wild_animals to the end of the animals list.
Remove the third element from the animals list using the pop() method.
Remove the last element from the animals list using the pop() method.
Insert 'Moose' at the third position in the animals list.
Print the animals list.
Example
Expected Output

['Dog', 'Cat', 'Moose', 'Tiger']







# Replace ___ with your code

animals = ['Dog', 'Cat']
wild_animals = ['Tiger', 'Coyote']

# perform list operations

# add Raccoon to the end using append()
animals.append('Raccoon')

# add wild_animals to animals using extend()
animals.extend(wild_animals)

# remove third elements from animals using pop(2)
animals.pop(2)

# remove last element from animals using pop()
animals.pop()

# add Moose at the third position in animals using insert()
animals.insert(2, 'Moose')

print(animals)
