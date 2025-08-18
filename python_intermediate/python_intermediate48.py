Example: Python Inheritance
Let's create an object of the Triangle class and call the get_perimeter() method and the display_info() method.

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
Here, this code t1 = Triangle([5, 6, 7]) creates an object of the Triangle class. Since the Triangle class doesn't have the __init__() method, the __init__() method of the Polygon class is called.

This code t1.get_perimeter() calls the get_perimeter() method. Since get_perimeter() is not defined in Triangle, the get_perimeter() of the Polygon class is called.

This code t1.display_info() class the display_info() method. However, both Polygon and Triangle have this method. In such cases, the display_info() method of the derived class Triangle is called and the method of the base class Polygon is ignored. This is called method overriding.

If the same method is defined in both the base and the derived class, then the method of the derived class overrides the method of the base class.

Next, we will see an image to understand this concept better.

Confused about something? Ask a question!
