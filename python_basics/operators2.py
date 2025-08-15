# % - remainder
# / - division with decilmal point
# //-division to achieve whole number only


#Divide Pens to Students
#Write a program to divide pens among students.

#Imagine you have to divide 14 pens among 3 students equally. Your task is to find out:

#How many pens each student would get when divided equally?
#The number of pens left over (if any).
#To solve this problem:

#Create a variable named pen_number and assign it the value of 14.
#Create another variable named student_number and assign it the value of 3.
#Compute the number of pens each student will get and print the result.
#Compute the number of pens remaining and print the remainder.






# Replace ___ with your code below

# Create pen_number and student_number variables
pen_number = 14

# Compute the number of pens each student will get and print it
# Hint: find the quotient
student_number = 3

# Compute and print the number of remaining pens
# Hint: find the remainder
total = pen_number // student_number
print(f"Pens for each student: {total}")

remainder = pen_number % student_number
print(f"Remaining pens: {remainder}")
