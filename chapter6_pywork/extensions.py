#6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.

cities = {
    '•Paris' : {
    'Country' : 'France',
    'Population' : 'Approximately 2.1 million',
    'Fact' : 'Known as the "City of Light" and home to the Eiffel Tower.'
    },
    '•Tokyo' : {
    'Country' : 'Japan',
    'Population' : 'Approximately 14 million',
    'Fact' : 'The most populous metropolitan area in the world, Tokyo has hosted the Olympics twice.',
    },
    '•Nairobi' : {
    'Country' : 'kenya',
    'Population' : 'Approximately 4.4 million',
    'Fact' : 'Known as the "Safari Capital of the World" due to its proximity to wildlife reserves.',
    },
}

# Adding "famous_food" to each city's dictionary
cities['•Paris']['Famous Food'] = 'Croissants and baguettes'
cities['•Tokyo']['Famous Food'] = 'Sushi and ramen'
cities['•Nairobi']['Famous Food'] = 'Nyama choma and ugali'

if cities:
    for key, value in cities.items():
        print(f"{key}:")
        for key, value in value.items():
            print(f"\n\t{key} : {value}")