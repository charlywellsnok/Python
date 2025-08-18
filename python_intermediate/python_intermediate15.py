Adding Methods
Here, we have slightly modified the program we previously wrote and added another object, student2.

class Student:

    # add a method to check pass/fail
    def check_pass_fail(self):
        if self.score >= 40:
            return True
        else:
            return False

# create object
student1 = Student()
student1.name = 'Harry'
student1.score = 85

# calling this method using student1 object
did_pass = student1.check_pass_fail()
print(f'Did {student1.name} pass?', did_pass)


# create object
student2 = Student()
student2.name = 'Ronin'
student2.score = 35

# calling this method using student2 object
did_pass = student2.check_pass_fail()
print(f'Did {student2.name} pass?', did_pass)
Output

Did Harry pass? True
Did Ronin pass? False
Here's how did_pass = student1.check_pass_fail() works:

Calling methods using an object in Python
Figure: Calling a Method
And, here's how did_pass = student2.check_pass_fail() works.

Calling methods using an object
Figure: Calling a Method
Next, we will learn to add attributes to objects in a proper way.
