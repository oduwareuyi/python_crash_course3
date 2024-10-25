#/Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

favourite_number = {
    'uyi' : 7, 'blessing' : 5, 'william' : 1, 'james' : 3, 'loveth' : 9
    }
    
print(favourite_number)
    
fav_num0 = favourite_number.get('uyi', 'No such name')
fav_num1 = favourite_number.get('blessing', 'No such name')
fav_num2 = favourite_number.get('rocket', 'No such name')

print(f"Uyi's favourite number is : {fav_num0}")
print(f"Blessing's favourite number is : {fav_num1}")
print(f"Rocket's favourite number is : {fav_num2}")