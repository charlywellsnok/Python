Example: Handling Specific Exception
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator/denominator
    print(result)
    
    my_list = [1, 2, 3]
    index = int(input("Enter index: "))

    print(my_list[index])

# if ZeroDivisonError exception occurs,
# run this code
except ZeroDivisionError:
    print("Denominator cannot be 0. Try again.")

# if IndexError exception occurs, run this code
except IndexError:
    print("Index is wrong.")
Notice the exception names after the except clauses.

Output 1

If the user enters 0 as denominator, the ZeroDivisionError exception is raised and the code inside the except ZeroDivisionError: block is executed.

Enter numerator: 5
Enter denominator: 0
Denominator cannot be 0. Try again.
Output 2

If the user enters any number other than 0, 1 or 2 as index, the IndexError exception is raised and the code inside except IndexError: block is executed.

Enter numerator: 10
Enter denominator: 5
2.0
Enter index: 4
Index is wrong.
Output 3

If neither of the exceptions are raised, this will be the output.

Enter numerator: 10
Enter denominator: 5
2.0
Enter index: 2
3 
Confused about something? Ask a question!
