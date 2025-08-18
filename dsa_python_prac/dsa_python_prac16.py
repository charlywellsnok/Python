List append() and extend()
The append() method

The append() method adds an element to the end of the list.

currencies = ['Dollar', 'Euro', 'Pound']

# append 'Yen' to the list
currencies.append('Yen')

print(currencies)
Output

['Dollar', 'Euro', 'Pound', 'Yen']
Idea Emoji
Note: The append() method does not return any value; it only modifies the original list.
The extend() method

The extend() method adds all the elements of an iterable (a list, tuple, string, etc.) to the end of the list.

languages = ['French', 'English']
languages1 = ['Spanish', 'Portuguese']

# append language1 elements to languages
languages.extend(languages1)

print(languages)
Output

['French', 'English', 'Spanish', 'Portuguese']
Idea Emoji
Note: The extend() method also does not return any value; it only modifies the original list.
By the way, we can also use the + operator to extend a list in Python. For example,

languages = ['French', 'English']
languages1 = ['Spanish', 'Portuguese']

# append language1 elements to languages
languages = languages + languages1

print(languages)
Output

['French', 'English', 'Spanish', 'Portuguese']
Confused about something? Ask a question!
