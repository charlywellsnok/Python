Lesson
Ask Programiz
How Do Variables Actually Work?
Suppose we have a code like this below:

list1 = [1, 2, 3]

# assign list1 to list2
list2 = list1 

# append an item to list1
list1.append(4)

print(list1)
print(list2)
Can you guess the output of this program?

It's obvious that list1 will be [1, 2, 3, 4] because we have appended 4 to [1, 2, 3]. However, list2 will also be [1, 2, 3, 4].

It's because both list1 and list2 are referring to the same object because of this code list2 = list1. And, if we check the id of list1 and list2, they will be the same.

That's why we use the list's copy() method to copy one list to another if we do not want this kind of behavior.

list1 = [1, 2, 3]

# assign list1 to list2
list2 = list1.copy()

list1.append(4)

print(list1)    # [1, 2, 3, 4]
print(list2)    # [1, 2, 3]
Confused about something? Ask a question!
