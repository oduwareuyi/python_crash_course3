#Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
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
    
    while True:
        print(f"\n{prompt}")
        answer = input().lower()
        if answer == "no":
            print("\nThanks for patronizing us")
            buy = False
            break
        elif answer == "yes":
            break