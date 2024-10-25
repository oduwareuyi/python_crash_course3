#6-10. Favorite Numbers: Modify your program from Exercise 6 (page 98) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers

favourite_numbers = {
    'uyi' : [7, 5, 1],
    'blessing' : [5, 2], 
    'william' : [1, 8, 0], 
    'james' :[3,9,1],
    'loveth' : [9],
    }
    
for key, value in favourite_numbers.items():
    if len(value) == 1:
        print(f"{key} favorite number is:")
    else:
        print(f"{key} favorite numbers are:")
    
    for number in value:    
        print(f"{number}")

print() #Adding newline for visibility after each person's fav number(s)