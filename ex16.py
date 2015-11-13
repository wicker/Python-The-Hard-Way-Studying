from sys import argv

script, filename = argv

print "We're going to erase %s." % filename
print "If you don't want to do that, hit CTRL-C (^C)."
print "If you do want to do that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'a')

#print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")


print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

print "But we'll open it again because we want to read it."
target = open(filename, 'r')

print target.read()
target.close()
