# -*- coding: utf-8 -*-
# this is a python program to perform divination 
# using the system of your choice. call a text file 
# with a list of the possible cards, runes, animals,
# or other symbols.  

from sys import argv
import random

script, filename = argv

location = ['The Present','The Obstacle','The Past','The Future','Above','Below','Advice','External Influences','Hopes and Fears', 'Outcome']

# print the name of a rune
def print_a_rune():
	return random.choice(rune)

# load the rune names 
with open(filename) as f:
	rune = [x.strip('\n') for x in f.readlines()]

# prompt the user 
print('There are three kinds of readings:')
print('1. Single Rune')
print('2. Triple Rune')
print('3. Celtic Cross')

reading_type = input('What kind of reading do you want?\n')

if reading_type is 1:
	print "Your single rune is: %s" % print_a_rune()
elif reading_type is 2:
	print "You have chosen three runes: %s, %s, and %s."\
	% (print_a_rune(), print_a_rune(), print_a_rune())
elif reading_type is 3:
	for a in range(1,10,1):
		print a,location[a]
		print " ",print_a_rune()


