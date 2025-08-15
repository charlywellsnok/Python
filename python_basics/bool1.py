#>	var > 10	Is var greater than 10?
#>=	var >= 10	Is var greater than or equal to 10?
#<	var < 10	Is var less than 10?
#<=	var <= 10	Is var less than or equal to 10?
#==	var == 10	Is var equal to 10?
#!=	var != 10	Is var not equal to 10?

#Compare Two Numbers
#Write a program to perform comparisons between two variables.

#Get two integer inputs from the user and store them in var1 and var2, respectively.
#Compare var1 and var2 using the comparison operators <, >, and != respectively.
#Print the results in the format shown in the Expected Output section.




# Replace ___ with your code below

# Get two integer inputs
var1 = int(input())
var2 = int(input())

# Compare variables and print them in the given format
result1 = var1 < var2
result2 = var1 > var2
result3 = var1 != var2

print(f"var1 < var2: {result1}")
print(f"var1 > var2: {result2}")
print(f"var1 != var2: {result3}")

