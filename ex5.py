name = 'Jenner'
age = 30
eyes = 'Blue'
hair = 'Brown'
height = 74 #inches
weight = 180 #lbs
get_kg = 0.453592

print "Let's talk about %s." % name
print "He's %s years old." % age
print "He's got %s eyes and %s hair." % (eyes, hair)

print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, 
	age + weight + height)

print "He weighs %f kilograms." % (weight * get_kg)
print "%d is the nearest lower kilogram." % (weight * get_kg)

kg_weight = weight * get_kg

print "%d is also the rounded kilgram." % round(kg_weight)


