Using Objects as Arguments
It's possible to use objects as arguments inside methods. Let's start with what we have already discussed.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# create an object
person1 = Person('Ana', 21)
print(person1.name)    # Ana
print(person1. age)    # 21
This program creates the person1 object of the Person class. This object has two attributes: name and age.

Now let's create a method that takes an object as an argument.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def print_person_attributes(self, person):
        print(self.name)    # Ana
        print(self.age)     # 21
        print(person.name)    # Sara
        print(person.age)    # 20


# create an object
person1 = Person('Ana', 21)

# create another object
person2 = Person('Sara', 20)


# calling print_persons_attributes() using person1 object
# person2 is used as an argument
person1.print_person_attributes(person2)
Here's how this code works:

The attributes of the person1 object is name which is equal to 'Ana' and age which is equal to 21.
The attributes of the person2 object is name which is equal to 'Sara' and age which is equal to 20.
Inside the print_persons_attributes(), self will be person1. It's because we have called this method using person1. And, the person argument takes the value of person2, which is passed as an argument.
Now, when we print self.name and self.age, we get attributes of person1. And when we print person.name and person.age, we get attributes of person2.
Let's clarify this with the help of an image.

Confused about something? Ask a question!
