"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View']}}

"""
locations = {
    'North America':
        { 'USA' : ['Mountain View', 'Atlanta']
        },
    'Asia':
        { 'India' : ['Bangalore'],
          'China' : ['Shanghai', 'Beijing']
        },
    'Africa':
        { 'Egypt' : ['Cairo']
        }
    
    }
"""

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai', 'Beijing']
locations['Africa'] = {'Egypt': ['Cairo']}

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""

print(1)
usa_city = sorted(locations['North America']['USA'])
print(usa_city)

print(2)
asia_city = []
for countries, cities in locations['Asia'].iteritems():
    for city in cities:
        asia_city.append(city + " - " + countries)

print(asia_city)


