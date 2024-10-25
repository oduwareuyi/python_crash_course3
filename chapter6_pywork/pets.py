#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. 
#Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.


# Step 1: Create dictionaries for different pets
pet1 = {"kind": "dog", "owner": "Alice"}
pet2 = {"kind": "cat", "owner": "Bob"}
pet3 = {"kind": "parrot", "owner": "Charlie"}

# Step 2: Store the dictionaries in a list
pets = [pet1, pet2, pet3]

# Step 3: Loop through the list and print details about each pet using items()
for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print()  # Adds a newline for better readability between pets