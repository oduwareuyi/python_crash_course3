#7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

#Pizza Toppings list
available_toppings = ['mushrooms', 'green peppers', 'extra cheese']

#Empty list for requested toppings by user
requested_toppings = []


prompt = "\nOrder your toppings: \n"
prompt += "• Menu\n\t"
prompt += "- mushrooms\n\t"
prompt += "- green peppers\n\t"
prompt += "- extra cheese"


order = True
answer = ""
topping = True

#Actions that can be carried out by user
while order:
    reply = ""
    print("Do you want to order? ")
    print('"No" to stop ordering')
    print('"Yes" to start ordering\n')
    
    answer = input()
    if answer == "No":
        order == False
        break
    elif answer == "Yes":
        print(prompt)
        print("If you are done ordering, please input 'done ordering'.\n")
        while topping:
            reply = input().lower()
            if reply == "done ordering":
                break
            if reply not in available_toppings:
                print(f"Sorry we don't have {reply}")
                continue
            else:
                requested_toppings.append(reply)
           
        if requested_toppings:
            for requested_topping in requested_toppings:
                print(f"Adding {requested_topping}.")
            print("\nFinished making your pizza!\n")
            requested_toppings = []
        else:
            print("Are you sure you want a plain pizza?\n")
            reply = input()
            if reply == "Yes":
                print("Finished making your plain pizza\n")