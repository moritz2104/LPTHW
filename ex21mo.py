#_*_ coding: utf–8–*–


# def test_func(test_arg):
# 	return test_arg

# test_arg = raw_input("> ")

# print test_func(test_arg)
# print test_arg # das hier macht natürlich dasselbe.

################

# Löse folgendes Problem:
# 24 + 34 / 100 - 1023

def add(x, y):
	print "Rechne: %f + %f" % (x, y)

	return x + y

def divide(x, y):
	print "Rechne: %f / %f" % (x, y)

	return x / y

def substract(x, y):
	print "Rechne: %f - %f" % (x, y)

	return x - y

def multiply(x, y):
	print "Rechne: %f * %f" % (x, y)

	return x * y

print "Was durch was?"
x = float(raw_input("> "))
y = float(raw_input("> "))

y = divide(x, y)

print "Plus was?"
x = float(raw_input("> "))

x = add(x, y)

print "Minus was?"
y = float(raw_input("> "))

Ergebnis = substract(x, y)

print Ergebnis