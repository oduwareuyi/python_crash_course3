#6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

uyi = {
    'First Name' : 'Uyiosasere', 
    'Last Name' : 'Oduware', 
    'Age' :24,
    'City' : 'Benin',
}

messi = {
    "First Name" : "Lionel",
    "Last Name" : "Messi",
    "Age" : 37,
    "City" : "Miami",
}

ronaldo = {
    "First Name" : "Cristiano",
    "Last Name" : "Ronaldo",
    "Age" : 39,
    "City" : "Riyadh",
}

people = [uyi, messi, ronaldo]

for person in people:
    for key, value in person.items():
        print(f"{key} : {value}\n")