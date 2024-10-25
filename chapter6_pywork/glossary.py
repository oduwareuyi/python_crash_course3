#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
#• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {
    'print' : 'Display output', 'Tuples' : 'Holds any fixed values', 'List' : 'Holds values that can be changed', 'if statements' : 'evaluates if a condition is true or false and whatever follows it next', 'list comprehension' : 'can be used to create a list with few lines'
}

print(f"print:\n\t{glossary['print']}")

print(f"\nTuples:\n\t{glossary['Tuples']}")

print(f"\nList:\n\t{glossary['List']}")

print(f"\nif statements:\n\t{glossary['if statements']}")

print(f"\nlist comprehension:\n\t{glossary['list comprehension']}")