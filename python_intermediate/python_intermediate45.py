Example: Python Inheritance
Let's first create the Polygon class.

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines.")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

p1 = Polygon([3, 4, 5])
p1.display_info()
perimeter = p1.get_perimeter()
print(f'Perimeter: {perimeter}')
Output

A polygon is a two dimensional shape with straight lines
Perimeter: 12
Here,

When the p1 object is created, the __init__() method is called. And, the sides attribute of the p1 object will be [3, 4, 5].
Then, the get_perimeter() method is called using the p1 object which returns the perimeter.
Next, we will inherit the Triangle class from Polygon.

Confused about something? Ask a question!
