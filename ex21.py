def add(a, b):
	print "Adding %d + %d" % (a, b)
	return a + b

def substract(a, b):
	print "Substracting %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "Multiplying %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "Dividing %d / %d" % (a, b)
	return a / b

print "Let's do some math with just funnctions!"

a = input("What is a? > ")
b = input("What is b? > ")

age = add(a, b)
height = substract(a, b)
weight = multiply(a, b)
iq = divide(a, b)

# age = add(30, 4)
# height = substract(240, 60)
# weight = multiply(3, 25)
# iq = divide(1000, 5)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle.....
print "Here is a puzzle."

what = add(age, substract(height, multiply(weight, divide(iq, 2))))
#what = 

print "That becomes:", what, "Can you do it by hand?"

# a = int(raw_input("What is a? > "))
# b = int(raw_input("What is b? > "))

# add(a, b)
# substract(a, b)
# multiply(a, b)
# divide(a, b)