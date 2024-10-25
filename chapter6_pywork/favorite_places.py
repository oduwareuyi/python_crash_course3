#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places = {
    "uyi" : ["italy","paris","dubai"], 
    "baldwin" : ["paris","south korea","spain"],
    "authur" : ["japan", "china", "russia"],
}

for key, value in favorite_places.items():
    if len(value) == 1:
        print(f"{key} favorite place is:")
    else:
        print(f"{key} favorite places are:")
        
    for places in value:
        print(f"\t{places}")
    print() #adds a new line after each person's favorite places