#7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.
users_poll = {}

active_poll = True

while active_poll:
    name = input("What's your name? ")
    dream_vacation = input('Where would you like to go for your' ' dream vacation:\n')
    users_poll[name] = dream_vacation
    response = input("\nWould you like to fill for another user? (yes/ no)")
    
    if response == 'no':
        active_poll = False
        print("\nThank you for your response 🙏")
        print("------Dream vacation------")
        
for name, location in users_poll.items():
    print(f"{name.title()} would like to go to {location.title()} for dream vaction")
    
