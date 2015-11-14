from sys import exit

prompt = "> "

def gold_room():
	print "This room is full of gold. How much do you take?"

	choice = raw_input(prompt)
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")

def bear_room():
	print "There is a bear here."

def cthulhu_room():
  print "There is a cthulhu here."

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and a door to your left."
	print "Which one do you take?"

	choice = raw_input(prompt)

	if choice == "left":
		bear_room()
	elif choice == "right":
	  cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()

