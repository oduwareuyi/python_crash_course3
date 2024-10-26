#7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:
#• Use a conditional test in the while statement to stop the loop.
#• Use an active variable to control how long the loop runs.
#• Use a break statement to exit the loop when the user enters a 'quit' value
prompt = "Do you want to buy anymore tickets?\n"
prompt += "Answer 'Yes' to buy more and 'quit' to exit\n"

active = 0; ticket = 0; cost = 0; buy = True

age = int(input("How old are you? "))

if age < 3:
        print("\nThe ticket is free\n")
        cost = 0
elif age >= 3 and age <= 12:
        print("\nOne ticket cost $10\n")
        cost = 10
elif age >12:
        print("\nOne ticket cost $15\n")
        cost = 15
        
while active < 3:
    print("\nHow many tickets do you want?")
    ticket = int(input())
    print(f"${ticket * cost}") 
    print("\nTickets succesfully bought\n")
    
    while buy:
            active += 1
            if active != 3:
                print(f"\n{prompt}")
                answer = input().lower()
                if answer == "quit":
                    print("\nThanks for patronizing us")
                    active = 3
                    break
                elif answer == "yes":
                    break
            else:
                print("Sorry you can't buy anymore tickets")
                buy = False
                break