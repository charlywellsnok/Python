Python Inheritance
Can you derive a Quadrilateral class from the Polygon class in our previous example.

After you derived the Quadrilateral class, create the display_info() method inside it.
Inside this method, print "A quadrilateral is a polygon with 4 edges.".
Then, outside of the classes, create an object of Quadrilateral.
Call the display_info() method using this object.
For hints, see the code outline.

Example
Expected Output

A quadrilateral is a polygon with 4 edges.
Confused about something? Ask a question!










# Replace ___ with your code

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines.")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

# create the Quadrilateral class
class Quadrilateral(Polygon):
    def display_info(self):
        print('A quadrilateral is a polygon with 4 edges.') 

# create an object of Quadrilateral
q1 = Quadrilateral([1, 2, 3, 4])

# call the display_info() method using the object
q1.display_info()
