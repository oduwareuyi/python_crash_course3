#6-6. Polling: Use the code in favorite_languages.py (page 96).
#• Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
#• Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

favorite_languages = {
 'jen': 'python',
'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }
 
people = ['jen', 'edward', 'uyi', 'arnold']
 
if people:
    for person in people:
        if person in favorite_languages.keys():
            print("Thank you for responding to the poll")
        else:
            print("Please take our poll")