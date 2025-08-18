Returning Objects From Methods
It's also possible to return an object from a method. Let's see an example.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def return_another_person(self):

        # creating an object of the Person class
        person = Person('Sara', 20)
        
        # returning the object
        return person

# create an object
person1 = Person('Ana', 21)

another_person = person1.return_another_person()
print(another_person.name)    # Sara
print(another_person.age)    # 20
Here, inside the return_another_person() method, we have created an object named person of the Person class.

# Inside return_another_person()
person = Person('Sara', 20)
The name attribute of this object is 'Sara', and the age attribute is 20.

Then, we have returned this object which is assigned to the another_person variable.

#  outside the class
another_person = person1.return_another_person()
Now, when we print another_person.name, we get 'Sara', and when we print another_person.age, we get 20.

At this point, you might be thinking how passing objects to methods and returning objects can be used in a practical program.

So in this next example, we will create a practical example involving these concepts.

Confused about something? Ask a question!
