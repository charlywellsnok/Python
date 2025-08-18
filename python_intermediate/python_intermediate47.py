Inheriting the Triangle Class
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines.")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges.")
Here, we have inherited the Triangle class from Polygon. We have also removed the code of creating objects.

If you have noticed, both the Polygon class and the Triangle class have the same display_info() method.

Next, we will create an object of the derived class Triangle.

Confused about something? Ask a question!


