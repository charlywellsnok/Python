Lesson
Ask Programiz
The type() Function
To verify everything is an object in Python, we can use the built-in type() function. For example,

number = 10
print(type(number))
Output

<class 'int'>
If we look at the output, we can see <class 'int'>. It means 10 is an object created from the int class.

Let's try a few more examples,

numbers = [1, 4, 9, 16]
print(type(numbers))   # <class 'list'>   

flag = True
print(type(True))   # <class 'bool'>

def my_function():
    pass

print(type(my_function))    # <class 'function'>
As we can see, all these entities are created from a class, which means they are objects.

Confused about something? Ask a question!
