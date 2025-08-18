Example: Person class
In this example,

We will create a Person class.
The object of this class will have name and age attributes. We will take input from the user and assign values to these attributes.
Then, we will create another method display_info to print these attributes.
Source Code
class Person:
    def __init__(self):
        self.name = input('Enter name: ')
        self.age = int(input('Enter age: '))
    
    def display_info(self):
        print(f'name: {self.name}')
        print(f'age: {self.age}')

person1 = Person()
person1.display_info()

person2 = Person()
person2.display_info()
Output

Enter name: Jack
Enter age: 21
name: Jack
age: 21
Enter name: Daniels
Enter age: 22
name: Daniels
age: 22
Here, when an object of Person is created, the __init__() method is called, and the user is asked to enter person_name and person_age. We have assigned these values to self.name and self.age respectively. That means, the objects of Person will have two attributes: name and age.

Now, when we call display_info() using person1, the name and the age attributes of the person1 object are printed.

Similarly, when we call display_info() using person2, the name and age attributes of the person2 object are printed.

Confused about something? Ask a question!
