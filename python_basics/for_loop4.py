2. Generate numbers from 1 to n: Use range(1, n+1) to generate integers from 1 to n (n+1 because the last number is exclusive).

3. Initialize the total variable to 0: Before adding up the numbers, initialize the total variable to 0 outside the loop.





n = int(input("Enter an integer"))

total = 0


for i in range(1,n+1):
    print(i)
    total = total + i

print(f"Total = {total}")
