Adding Attributes in a Proper Way
As we have previously mentioned, adding attributes to objects is not a good practice.

Python offers a much more elegant way of defining attributes when we create objects. For that, we use the special __init__() method.

The __init__() method is a special method that is called automatically when an object is created. Let's take an example.

class Test:
    def __init__(self):
        print('Hello there')

test1 = Test()
test2 = Test()
Output

Hello there
Hello there
Here is how this code works:

When the test1 object is created, the __init__() method is called. The self argument of the __init__() method takes the value of the test1 object.
Similarly, when the test2 object is created, the __init__() method is called again. The self argument of the __init__() method takes the value of the test2 object.
Next, we will use the same __init__() method to add attributes.
