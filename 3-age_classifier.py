
# input age from user
age = int(input("Enter your age: "))

# Check age ranges
if age < 0:
    print("Invalid age. Age cannot be negative.")
elif age <= 1:
    print("You are an infant.")
elif age <= 3:
    print("You are a toddler.")
elif age <= 12:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
else:
    print("You are an adult.")
