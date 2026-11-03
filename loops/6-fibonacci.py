
n = int(input("How many terms? "))

a = 0
b = 1

if n <= 0:
    print("Please enter a positive number.")
else:
    for i in range(n):
        print(a, end=" ")
        next_term = a + b
        a = b
        b = next_term
    print()
