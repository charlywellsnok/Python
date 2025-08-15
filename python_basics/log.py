#and	True if both expressions are true.	(total > 100) and (is_member == "yes")
#or	True if any one of the expressions is true.	(credit_score > 700) or (stable_income == "yes")
#not 	True if the expression is false.	(not is_logged_in)



# User input
credit_score = int(input("Credit score? "))
stable_income = input("Stable income (yes/no)? ")

# Check eligibility
if (credit_score >= 700) and (stable_income == "yes"):
    print("You are eligible for a loan.")
else:
    print("You are not eligible for a loan."
