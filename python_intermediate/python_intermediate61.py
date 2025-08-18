Example: Exception Handling
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator/denominator

    print(result)
except:
    print("Denominator cannot be 0. Try again.")
Here, the exception occurs if the denominator is 0. Let's see how this program works for different values of denominator.

Output when denominator is not 0

Enter numerator: 4
Enter denominator: 2
2.0
In this case, exceptions do not occur. Hence, the except block is skipped.

Output when denominator is 0

Enter numerator: 4
Enter denominator: 0
Denominator cannot be 0. Try again.
In this case, an exception is raised because of this code result = numerator/denominator. When the exception occurs, code after it is ignored and the except block is executed.

Idea Emoji
Note: In this program, we have used the print() function inside the except block for simplicity. We can put whatever code we want inside the except block.
Confused about something? Ask a question!
