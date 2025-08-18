Adding Methods
As mentioned before, methods mean functions when working with classes. Let's see how we can add a method to the Student class.

class Student:


    # add a method to check pass/fail
    def check_pass_fail(self):
        if self.score >= 40:
            return True
        else:
            return False


# create objects
student1 = Student()

# add attributes
student1.name = 'Harry'
student1.score = 85
Here, we have created the check_pass_fail() method inside the Student class. Now, any object of the student class (such as student1 in the above code) can access this method.

Idea Emoji
Note: If you couldn't understand what's happening in the code, don't worry we will get back to it later. For now keep moving.
Next, we will learn to call this method.
