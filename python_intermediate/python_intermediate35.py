Lesson
Ask Programiz
The id() Function
In Python, every object has an id for identity. The id of an object is always unique and constant for this object during its lifetime.

We can check the id of an object by using the id() function. For example,

number1 = 5
print(id(number1))   # 9789120

number2 = 10
print(id(number2))   # 9789280
As we can see, the id of number1 and number2 are different. It means they are two different objects.

Now, let's see what will happen if we assign one variable to another.

number1 = 5
print(id(number1))   # 9789120

number2 = number1
print(id(number2))   # 9789120
Here, we can see that the id of number1 and number2 is the same. It means these two variables are referring to the same object. Python does this for memory optimization.

Confused about something? Ask a question!
