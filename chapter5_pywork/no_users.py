user_names = []

if user_names:
    for user in user_names:
        if user.lower() == "admin":
            print(f"Hello {user.lower()} would you like to see a status report")
        else:
            print(f"\nHello {user.lower()} thank you for logging in again")
else:
    print("We need to find some users!")