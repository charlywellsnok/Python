Example: Add Complex Numbers
In this example, we will add two complex numbers by creating classes and objects.

If you do not know, a complex number has real and imaginary parts.

Complex number representation using an object
Figure: Complex Numbers
When we add two complex numbers, we need to add real and imaginary parts separately.

Let's first create a class that represents complex numbers.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imaginary = imag

n1 = Complex(5, 6)
n2 = Complex(-4, 2)
Here, we have created objects n1 and n2 of the Complex class with attributes real and imaginary.

Next, we will create a method named add() to add these two objects.

Confused about something? Ask a question!
