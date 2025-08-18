Using super()
It's possible to call the base class methods from derived classes. For that, we use super().

In this example, let's see how we can call the display_info() method of the Polygon class from the Triangle class using super().

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


        # call the display_info() method of Polygon
        super().display_info()


# create an object of Triangle
t1 = Triangle([5, 6, 7])

# call get_perimeter using t1
perimeter = t1.get_perimeter()
print("Perimeter:", perimeter)

# call display_info() using t1
t1.display_info()
Output

Perimeter: 18
A triangle is a polygon with 3 edges.
A polygon is a two dimensional shape with straight lines.
Notice, this code super().display_info() inside the display_info() method of the Triangle class. This code calls the display_info() method of Polygon.

Next, we will see an image to understand this.

Confused about something? Ask a question!
