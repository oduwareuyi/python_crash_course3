#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    'Paris' : {
    'Country' : 'France',
    'Population' : 'Approximately 2.1 million',
    'Fact' : 'Known as the "City of Light" and home to the Eiffel Tower.'
    },
    'Tokyo' : {
    'Country' : 'Japan',
    'Population' : 'Approximately 14 million',
    'Fact' : 'The most populous metropolitan area in the world, Tokyo has hosted the Olympics twice.',
    },
    'Nairobi' : {
    'Country' : 'kenya',
    'Population' : 'Approximately 4.4 million',
    'Fact' : 'Known as the "Safari Capital of the World" due to its proximity to wildlife reserves.',
    },
}

if cities:
    for key, value in cities.items():
        print(f"{key}:")
        for key, value in value.items():
            print(f"\n\t{key} : {value}")