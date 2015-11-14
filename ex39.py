stuff = {'name': 'Zed', 'age': 39, 'height': 6*12+2}
print stuff['name']
print stuff['age']
print stuff['height']
stuff['city'] = 'San Francisco'
print stuff['city']
print stuff

# create a mapping of state to Abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

#create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print out some states
print '-' * 10
print "Michigan's abbreviation is", states["Michigan"]
print "Florida's abbreviation is", states["Oregon"]

# do it by using the state then cities dict
print '-' * 10
print "Michigan has", cities[states['Michigan']]
print "Florida has", cities[states['Florida']]

# print the items
print '-' * 10
print "print the raw .items()"
print states.items()
print "print the cities"
print cities
print "print the states"
print states

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s has the abbreviation %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s is in %s." % (city, abbrev)

# now combine them
print '-' * 10
for state, abbrev in states.items():
	print "%s is in %s, which is abbreviated %s." % (cities[abbrev], state, abbrev)

# safely get an abbreviation by state that might not be there
print '-' * 10
state = states.get('Texas')
# printing state here returns None
if not state:
	print "Sorry, no Texas"

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is %s" % city


