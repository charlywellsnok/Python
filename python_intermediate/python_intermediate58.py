
Errors and Exceptions
We might have run into errors numerous times while programming. These errors are of two types:

1. Syntax errors

These errors are caused because of improper use of Python syntax, such as missing parentheses, wrong indentation, missing colons, etc. For example,

if 5 > 3
    print('5 is greater than 3')
Output

SyntaxError: invalid syntax
Here we are getting an error because we have missed a colon after 5 > 3. We can easily fix these errors by fixing the syntax.

2. Exceptions

The next type of error is exceptions. Even if our code is syntactically correct, we may sometimes get an error. For example, if we divide a number by 0, we get an error.

result = 5/0
print(result)
Output

ZeroDivisionError: division by zero
Here, our code is correct syntax wise, however, it's not allowed to divide a number by 0 in Python. This is an exception.

In this case, we are getting the ZeroDivisionError exception.

Next, we will learn a few different types of exceptions.

Confused about something? Ask a question!
