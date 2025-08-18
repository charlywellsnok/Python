Exception Handling
As we have seen in the previous lesson, when an exception occurs, our program ends abruptly with an error message.

Most of the time, rather than showing this default error message, we may want to show a custom message that's more helpful or run a different set of code. This is known as exception handling.

Exception handling is the process of responding to exceptions in a custom way during the execution of a program.

To use exception handling in Python, we use the try...except block. Its syntax is:

try:
    # code that may cause exception
except:
    # code to run when exception occurs
Inside the try block, we put the code that may raise an exception. Now if an exception occurs, the program jumps immediately to the except block. However, if exceptions do not occur, the except block is skipped.

Next, we will see a working example of exception handling.

Confused about something? Ask a question!
