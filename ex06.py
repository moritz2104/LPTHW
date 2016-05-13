# hier werden Variablen festgelegt.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
yeah = "Yeah!"
y = "Those who know %s and those, who %s. %s" % (binary, do_not, yeah)

# hier werden die Variablen x und y ausgegeben.
print x
print y # string inside string 1 and 2

# hier werden die Variablen x und y innerhalb eines Strings ausgegeben.
print "I said: %r." % x # string inside string 3
print "I also said: '%s'." % y # string inside string 4, 5 und 6

hilarious = False # Variable mit dem Wert "False"
joke_evaluation = "Isn't that joke so funny?! %r" # Variable mit einem String und einem format string

print joke_evaluation % hilarious # prints joke and puts evaluation inside, umgekehrt sozusagen

w = "This is the left side of...."
e = " a string with a right side."
dieses = "dieses hier"	
was = "%s" % dieses
v = "Allright. Fuege mal %s ein" % was

print w + e + v
print v