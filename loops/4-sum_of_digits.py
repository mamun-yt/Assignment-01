
num = int(input("Enter a number: "))
num = abs(num)  

total = 0

while num > 0:
    last_digit = num % 10  
    total = total + last_digit
    num = num // 10       

print("Sum of digits:", total)
