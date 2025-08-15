Let's solve a simple problem of finding the sum of the first 1000 natural numbers:

n = 1000
total = 0 


# iterate n times
for i in range(1, n + 1):
    total = total + i

print(total)

#Output is 500500


Code in it's optimized form 

n = 1000

total = n * (n + 1) / 2
print(total)
