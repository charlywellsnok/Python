Inheritance Introduction
Inheritance is an important concept of object-oriented programming. Let's create a scenario to understand what inheritance is and what problem it solves.

Why Inheritance?
Suppose we need to create a racing game with cars and motorcycles as vehicles.

To solve this problem, we can create two separate classes to handle each of their functionalities.

However, both cars and motorcycles are vehicles, and they will share some common attributes and methods.

So instead of creating two independent classes, we can create the Vehicle class that shares the common features of both cars and motorcycles. Then, we can derive the Car class from this Vehicle class.

In doing so, the Car class inherits all the attributes and methods of the Vehicle class. And, we can add car-specific features in the Car class.

Similarly, we can derive the Motorcycle class that inherits from the Vehicle class. Again, this Motorcycle class gets all vehicle-specific attributes and methods from the Vehicle class.

Python Inheritance
Figure: Python Inheritance
This is the basic concept of inheritance. Inheritance allows a class (child or derived class) to inherit attributes and methods from another class (parent or base class).

In our example, Vehicle is the parent or base class and Car and Motorcycle are child or derived classes.

Next, we will learn to implement inheritance in Python.

Confused about something? Ask a question!
