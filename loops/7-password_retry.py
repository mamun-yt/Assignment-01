password = "Mamun123"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter password: ")

    if user_input == password:
        print("Login successful!")
        break
    else:
        attempts = attempts + 1
        print("Wrong password. Attempts left:", max_attempts - attempts)

if attempts == max_attempts:
    print("Account locked")
