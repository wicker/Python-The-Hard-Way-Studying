# -*- coding: utf-8 -*-
# this is a python program to perform divination 
# using the system of your choice. call a text file 
# with a list of the possible cards, runes, animals,
# or other symbols.  

from sys import argv
import random

script, filename = argv

location = ['The Present','The Obstacle','The Past','The Future','Above','Below','Advice','External Influences','Hopes and Fears', 'Outcome']

# auto generate list of minor arcana
def generate_list_of_minor_arcana():
	suits = ['Wands','Swords','Cups','Pentacles']
	num_of = ['1','2','3','4','5','6','7','8','9','10','Page','Knight','Queen','King']

	for n in suits:
		for m in num_of:
			print "%s of %s" % (m, n)

# print the name of a card
def print_a_card():
	return random.choice(card)

# load the card names 
with open(filename) as f:
	card = [x.strip('\n') for x in f.readlines()]

# prompt the user 
print('There are three kinds of readings:')
print('1. Single Card')
print('2. Triple Card')
print('3. Celtic Cross')

reading_type = input('What kind of reading do you want?\n')

if reading_type is 1:
	# readi a single card
	print "Your single card is: %s" % print_a_card()
elif reading_type is 2:
	# read three card
	print "You have chosen three cards: %s, %s, and %s."\
	% (print_a_card(), print_a_card(), print_a_card())
elif reading_type is 3:
	# read the cards of the cross:
	for a in range(1,10,1):
		print a,location[a]
		print " ",print_a_card()


