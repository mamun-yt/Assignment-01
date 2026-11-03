num = int(input("Enter a number: "))

digits = str(num)
power = len(digits)

total = 0

for d in digits:
    total = total + int(d) ** power

if total == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
