#6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    'print' : 'Display output',
    'Tuples' : 'Holds any fixed values',
    'List' : 'Holds values that can be changed',
    'if statements' : 'evaluates if a condition is true or false and whatever follows it next',
    'list comprehension' : 'can be used to create a list with few lines', 
    'keys()' : 'A method that can be used with a for loop to access keys in a dictionary',
    'items()' : 'used with for loop to print out key : value pairs', 
    'values()' : 'used with a for loop to print out values in a dictionary', 
    'set' : 'used to store non-ordered and unique values', 'in' : 'used to check if a value is in a list or tuple or dictionary',
}

for key, value in glossary.items():
    print(f"{key}:\n\t{value}")