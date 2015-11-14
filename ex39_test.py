import ex39_hashmap

# create a mapping of state to abbreviation
states = ex39_hashmap.new()
ex39_hashmap.set(states, 'Oregon', 'OR')
ex39_hashmap.set(states, 'Florida', 'FL')
ex39_hashmap.set(states, 'California', 'CA')
ex39_hashmap.set(states, 'New York', 'NY')
ex39_hashmap.set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
cities = ex39_hashmap.new()
ex39_hashmap.set(cities, 'CA', 'San Francisco')
ex39_hashmap.set(cities, 'MI', 'Detroit')
ex39_hashmap.set(cities, 'FL', 'Jacksonville')

# add some more cities
ex39_hashmap.set(cities, 'NY', 'New York')
ex39_hashmap.set(cities, 'OR', 'Portland')


# print out some cities
print '-' * 10
print "NY State has: %s" % ex39_hashmap.get(cities, 'NY')
print "OR State has: %s" % ex39_hashmap.get(cities, 'OR')

# print some states
print '-' * 10
print "Michigan's abbreviation is: %s" % ex39_hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % ex39_hashmap.get(states, 'Florida')

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: %s" % ex39_hashmap.get(cities, ex39_hashmap.get(states, 'Michigan'))
print "Florida has: %s" % ex39_hashmap.get(cities, ex39_hashmap.get(states, 'Florida'))

# print every state abbreviation
print '-' * 10
ex39_hashmap.list(states)

# print every city in state
print '-' * 10
ex39_hashmap.list(cities)

print '-' * 10
state = ex39_hashmap.get(states, 'Texas')

if not state:
  print "Sorry, no Texas."

# default values using ||= with the nil result
# can you do this on one line?
city = ex39_hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
