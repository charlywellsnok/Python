Adding Methods
Let's start with the first question.

1. Our method takes one argument but we are calling it without any argument. How is it working?

class Student:
    def check_pass_fail(self):
        ... .. ...

student1 = Student()
... .. ...
# calling the method
did_pass = student1.check_pass_fail()
When we define methods, we must use self as the first argument. It's because we are calling the method using the object, student1.check_pass_fail(). This student1 object is automatically passed to the check_pass_fail() method and the self argument will be this object.

Idea Emoji
Remember: We must always use self as the first argument in the function definition. This self takes the value of the object calling it.
2. Second question was, how is self.score working inside the check_pass_fail() method?

Since self inside the check_pass_fail() method takes the value of the student1 object, self.score is equal to student1.score, which was 85 in our example. That's why we are not getting any errors.

We know it sounds confusing. So let's try to visualize what's happening next.

Confused about something? Ask a question!
