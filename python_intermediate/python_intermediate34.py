Lesson
Ask Programiz
The dir() Function
The dir() function lists out all the attributes and methods of the given object. For example,

number = 1
print(dir(number))
Output

['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', ......]
This means, an integer (which is an object) can access all these methods and attributes.

Let's try to use this __add__() method in our code.

number = 5

result = number.__add__(100)
print(result)
Output

105
As we can see, the __add__() method can be used for addition.

In fact, the + operator internally calls this __add__() method for addition. The above code is equivalent to:

number = 5

result = number + 100
print(result)
At the surface, it may look like the + operator is working like how it works in mathematics, but internally it's calling the __add__() method for addition.

Confused about something? Ask a question!
