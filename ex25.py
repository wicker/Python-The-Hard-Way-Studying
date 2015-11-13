# This function will break up words for us
def break_words(stuff):
	words = stuff.split(' ')
	return words

# Sorts the words
def sort_words(words):
	return sorted(words)

# Prints the first word after popping it off
def print_first_word(words):
	word = words.pop(0)
	print word
	
# Prints the last word after popping it off
def print_last_word(words):
	word = words.pop(-1)
	print word

# Takes in a full sentence and returns the sorted words
def sort_sentence(sentence):
	words = break_words(sentence)
	return sort_words(words)

# Prints the first and last words of the sentence
def print_first_and_last(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

# Sorts the words then prints the first and last one
def print_first_and_last_sorted(sentence):
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

