Example: Python Inheritance
Let's create an object of the Dog class.

# base class
class Animal:
    def eat(self):
        print("I can eat")

# the Dog class is derived from Animal
# notice Animal inside ()        
class Dog(Animal):
    def bark(self):
        print("I can bark")


# object of the dog class
dog1 = Dog()

# call the bark() method (of Dog)
dog1.bark()

# call the eat() method (of Animal)
dog1.eat()
Output

I can bark
I can eat
Here, dog1 is the object of the Dog class. Hence,

dog1.bark() calls the bark() method of the Dog class.
dog1.eat() calls the eat() method of the Animal class. It's possible because Dog is derived from Animal, so the Dog class inherits all the methods and attributes of Animal.
Inherit a derived class from a base class
Figure: Python Inheritance
Idea Emoji
Note: Objects of Animal can only access methods and attributes of Animal. It's because Dog is derived from Animal and not the other way around.
Confused about something? Ask a question!
