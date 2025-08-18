Adding Methods
Now, we will add code at the end to call the check_pass_fail() method we previously created.

class Student:

    # add a method to check pass/fail
    def check_pass_fail(self):
        if self.score >= 40:
            return True
        else:
            return False

# create object
student1 = Student()

# add attributes
student1.name = 'Harry'
student1.score = 85


# call the check_pass_fail() method
# calling this method using student1 object
did_pass = student1.check_pass_fail()


print(did_pass)
Output

True
Let's see how this code works from the very beginning:

We have created the Student class. Inside this class, we have added the check_pass_fail() method.
We have created the object named student1 of the Student class using student1 = Student().
We have added two attributes to the student1 object: name and score.
Finally, we have called the check_pass_fail() method using the student1 object using student.check_pass_fail().
At this point, you might be wondering how the heck this code is working. You probably have these two obvious questions:

Our check_pass_fail() method takes one argument. However, we are calling this method without any argument. Shouldn't this give us an error?
How is self.score inside the check_pass_fail() method working? We haven't defined it.
Next, let's answer these two important questions.

Confused about something? Ask a question!
