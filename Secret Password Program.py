password =str(input("Enter your password: "))
character_count = len(password)
if len(password) < 5:
    print(f"Your password must be at least 5 characters long,current length is {len(password)}")

if password.isdigit(): print("Your password is digits only")
elif password.isalpha(): print("Your password is alphabetical only")
elif password.isalnum(): print("Your password is Alphanumeric")

if password == "secret123":
        print('Access Granted')
else:
        print('Access denied, Wrong password')
