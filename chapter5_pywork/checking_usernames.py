current_users =["Thanos", "Dark side", "messi", "ronaldo", "adele", "admin"]

new_users = ["The Bishop", "Dark side", "Thanos", "Kratos", "Brainiac" ]

copy_current_users = [current.lower() for current in current_users]
    
for user in new_users:
    if user.lower() in copy_current_users:
        print("Try another username")
    else:
        print("Username is available")