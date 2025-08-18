Example: Add Complex Numbers
Let's create the add() method in the Complex class.

class Complex:
    # using __init__() to create attributes
    def __init__(self, real, imag):
        self.real = real
        self.imaginary = imag

    # method to add complex numbers
    def add(self, number):
        result_real = self.real + number.real
        result_imaginary = self.imaginary + number.imaginary
        
        # create another object of Complex
        result = Complex(result_real, result_imaginary)  
        return result

n1 = Complex(5, 6)
n2 = Complex(-4, 2)

# The return value from the add() method
# is assigned to the n3 variable
n3 = n1.add(n2)

# printing n3 attributes
print('real part =', n3.real)
print('imaginary part =', n3.imaginary)
Output

real part = 1
imaginary part = 8
Here's how the add() method works.

Passing arguments and return value from a method in Python
Figure: Pass Arguments and Return a Value
In the program, we have called the add() method like this:

n3 = n1.add(n2)
In the add() method definition, self takes n1 object and number takes n2 object.

Then, the individual attributes of these two objects are added. Remember, when we add complex numbers, we must add real and imaginary parts separately.

result_real = self.real + number.real
result_imaginary = self.imaginary + number.imaginary
Then, we created a new object using these values. The real attribute of the new object will be equal to result_real, and the imaginary attribute of the object will be equal to result_imaginary.

result = Complex(result_real, result_imaginary)
Finally, this object is returned which is assigned to the n3 variable outside of the class.

Now, when we print n3.real, we get the sum of n1.real and n2.real. Similarly, when we print n3.imaginary, we get the sum of n1.imaginary and n2.imaginary.

Confused about something? Ask a question!
