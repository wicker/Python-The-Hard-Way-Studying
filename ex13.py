# sys is a library or module
from sys import argv
from sys import path
from sys import maxint

# unpack whatever is in argv and
# assign it to all of these variables in order
script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third

print "The path is: ", path[0]
print "The max int is: ", maxint
