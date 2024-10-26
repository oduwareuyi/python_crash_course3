#7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:
#• Use a conditional test in the while statement to stop the loop.
#• Use an active variable to control how long the loop runs.
#• Use a break statement to exit the loop when the user enters a 'quit' value
prompt = "Do you want to buy anymore tickets?\n"
prompt += "Answer 'Yes' to buy more and 'No' to exit\n"

age = int(input("How old are you? "))

buy = True
while buy:
    print("\nHow many tickets do you want?")
    if age < 3:
        print("\nThe ticket is free\n")
        ticket = int(input())
        print("free")
    elif age >= 3 and age <= 12:
        print("\nOne ticket cost $10\n")
        ticket = int(input())
        print(f"${ticket * 10}")
    elif age >12:
        print("\nOne ticket cost $15\n")
        ticket = int(input())
        print(f"${ticket * 15}")
        
    print("\nTickets succesfully bought\n")
    
    customer = True
    
    while customer:
        print(f"\n{prompt}")
        answer = input().lower()
        if answer == "no":
            print("\nThanks for patronizing us")
            buy = False
            customer = False
        elif answer == "yes":
            break