enumerate()
The for loop in Python doesn't automatically use indexes.

languages = ['Python', 'Java', 'JavaScript']

for language in languages:
    print(language)
Output

Python
Java
JavaScript
However, if we need to access the index during each iteration of a for loop, we can use the enumerate() function along with the loop.

First, let's see how enumerate() works:

languages = ['Python', 'Java', 'JavaScript']

enumerate_languages = enumerate(languages)

# convert enumerate object to list
print(list(enumerate_languages))
Output

[(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]
As you can see, enumerate() adds a counter to our list and returns it.

Now, let's see how we can use it in a for loop.

languages = ['Python', 'Java', 'JavaScript']

for index, language in enumerate(languages):
    print(index, language)
Output

0 Python
1 Java
2 JavaScript
Essentially, if we need to work with indexes inside a for loop, we can utilize the enumerate() function.
