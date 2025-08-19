Thought Process to Implement Linear Search
To implement linear search, we follow these steps:

1. Use a loop to traverse (access elements one-by-one) along with its corresponding index.

for index, element in enumerate(lst):
    pass
2. Compare each element with the target value.

Within the loop, we will compare list elements to the target value. If a match is found, we use the corresponding index of that value.

for index, element in enumerate(lst):
   if element == target:
        result = index
3. If the element is not found in the list, set the result to None.

for index, element in enumerate(lst):
   if element == target:
        result = index

result = None
Next, we will create a working program of linear search.

Confused about something? Ask a question!
