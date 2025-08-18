Adding Attributes
First, let's see how to add attributes manually to objects.

class Student:
    pass

# create objects
student1 = Student()

# add attributes
student1.name = 'Harry'
student1.score = 85

# print attributes of student1
print(student1.name)
print(student1.score)
Output

Harry
85
Here, student1.name = 'Harry' adds the name attribute to the student1 object. Similarly, student1.score adds the score attribute to the object.

Idea Emoji
Note: This is not a proper way to use attributes; we put attributes inside the class itself. We are writing code in this way to make things simple for the moment. We will come back to this topic later in this lesson and see the right way to add attributes.
Next, we will learn to define methods inside a class.
