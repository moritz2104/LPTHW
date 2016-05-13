# this one is like your scripts with argv
def print_two(*args): # *args takes all arguments to the function
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	print arg1, arg2 # Aha! Das geht auch!
	print arg1 + (" ") + arg2 # Aha! Und das geht auch!

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this takes no arguments
def print_none():
	print "I got no argmuments."

print_two("Moritz", "Juedes")
print_two_again("Moritz", "Juedes")
print_one("One_Argument_yeah")
print_none()