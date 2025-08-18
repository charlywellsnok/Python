Taking a deeper look at class
Here's the class we previously created.

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
If you look at this code, the class itself doesn't store any data. However, this class has two attributes: name and score.

Now, if we create an object (with two arguments), the __init__() method is called automatically and that object will have two attributes: name and score with the given values.

We can create as many objects as we want from this class and each object will have name and score attributes and can use the check_pass_fail() method.

Creating two objects from a class
Figure: Creating objects from a class
Confused about something? Ask a question!
