Lesson
Ask Programiz
Revision: Classes and Objects
Methods and the self Parameter
We use objects to call methods. Here, t1.call_me() calls the call_me() method using the t1 object.

The self parameter represents the object calling it. In the program below, self will be object t1.

# creating the Test class
class Test:
   def call_me(self):
      pass

# object t1 of the Test class
t1 = Test()

# calling call_me() using the t1 object
t1.call_me()
The __init__() method
The __init__() method is automatically called when an object is created. We usually use the __init__() method to define attributes of the object.

# creating the Test class
class Test:
   def __init__(self, a):
       self.attr1 = a
       self.attr2 = 100    

# object t1 of the Test class
t1 = Test(1)
t2 = Test(10)
Here, objects t1 and t2 have two attributes attr1 and attr2.

For object t1,

attr1 is 1 and attr2 is 100
For object t2,

attr1 is 10 and attr2 is 100
Confused about something? Ask a question!
