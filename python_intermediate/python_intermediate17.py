Adding Attributes in a Proper Way
Let's add the __init__() method to the Student class we previously created.

class Student:


    # adding the __init__() method
    def __init__(self, name, score):
       self.name = name
       self.score = score


    # add a method to check pass/fail
    def check_pass_fail(self):
        if self.score >= 40:
            return True
        else:
            return False

# create object
student1 = Student('Harry', 85)

# calling this method using student1
did_pass = student1.check_pass_fail()
print(f'Did {student1.name} pass?', did_pass)
Output

Did Harry pass? True
Here, we have created an object like this:

student1 = Student('Harry', 85)
When this object is created, the __init__() method is automatically called. Inside this method,

self takes the value of object student1
the name argument will be 'Harry'
the score argument will be 85
Then, name is assigned to self.name. Since name represents student1 in this case, the name argument of student1 will be 'Harry'.

Similarly, the score argument of student1 will be 85.

Passing Arguments to Methods in Python
Figure: Passing Arguments to a Method
Now, imagine if we need to check if a student passed or failed for another student, we just need to create an object from the Students class and use the check_pass_fail() method.

student2 = Student('Ronin', 35)

did_pass = student2.check_pass_fail()
print(f'Did {student2.name} pass?', did_pass)
When the student2 object is created, the same __init__() method is called. However, the value of self will be the student2 object and its name and score attributes will be 'Ronin' and 35.

And, when student2.check_pass_fail() is called, self takes the value of student2. The value of self.score will be 35.

Confused about something? Ask a question!
