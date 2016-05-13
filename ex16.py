from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you want that, hit RETURN."

raw_input("?")

print "Opening the file...."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()
# truncate # --> not a function, (it's a method?) neee das ist doch ne Funktion
# open # --> a function
# write # --> not a function
# raw_input # --> a function

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file!"

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print "And finally, we close the file."
target.close()

# reopen it again
print "And then, we open it again."
# show content of a file in editor

# input file name and assign it to a variable
file_var = filename
# open this variable and assign it to another variable
open_var = open(file_var)
# read the second variable and print it out
print open_var.read()