Classes and Objects
Create a class

Create a class named Person.
Inside this class, create a method named greet() that takes two arguments: self and message.
Print message from inside the greet() method.
Outside of the class

Get string input from the user and assign it to the greeting variable.
Create an object named person1 of the Person class.
Call the greet() method using the person1 object with greeting as an argument.
For hints, see the code outline.

Example
Test Input

Hello
Expected Output

Hello
Confused about something? Ask a question












# Replace ___ with your code

# create the person class
class Person:
    # create the greet() method
    def greet(self, message):
        print(message)

# get user input
greeting = input()

# create object
person1 = Person()

# call the greet() method using person1
# use greeting as an argument
person1.greet(greeting)
