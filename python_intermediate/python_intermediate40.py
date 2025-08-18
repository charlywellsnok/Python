Python Inheritance
Let's see an example of Python inheritance.

Let's first create a class named Animal.

class Animal:
    def eat(self):
        print("I can eat")
Now, let's derive a class named Dog from this class.

# base class
class Animal:
    def eat(self):
        print("I can eat")


# the Dog class is derived from Animal        
class Dog(Animal):
    def bark(self):
        print("I can bark")
Here, the Dog class inherits all the attributes and methods from the Animal class. But what does that mean?

It means, objects of the Dog class can not only access methods and attributes of the Dog class, but it can also access methods and attributes of the Animal class.

Next, we will create objects of the Dog class.

Confused about something? Ask a question!
