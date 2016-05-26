# i = 0
# numbers = []

# print '\n',i
# print numbers

# while i < 5:
# 	print "\nAt the top of the loop i is %d" % i
# 	numbers.append(i)

# 	print "Now i = i + 1 is being done."
# 	i += 1

# 	print "At the bottom of the loop i is %d" % i
# 	print "Numbers now: ", numbers

# print "\nThe numbers: "

# for num in numbers:
# 	print num


# def counter_one():
# 	von = int(raw_input('von >> '))
# 	bis = int(raw_input('bis >> '))
# 	abstand = int(raw_input('abstand >> '))
# 	zahlen = []

# 	while von < bis:
# 		print "\nWir starten bei %d" % von
# 		zahlen.append(von)

# 		von = von + abstand

# 		print "Wir landen in diesem Durchgang bei %d" % von
# 		print "Die Liste enthaelt folgende Zahlen: ", zahlen

# counter_one()

def counter_two(start, stop, step):
	for i in range(start, stop, step):
		print i

x = int(raw_input("Wo soll ich starten? >> "))
y = int(raw_input("Bis wo soll ich zaehlen? >> "))
z = int(raw_input("Und mit welchem Abstand? >> "))

counter_two(x, y, z)

# def sag_was(variante):
# 	if variante == 1:
# 		print "Was willst du sagen?"
# 		gesagt = raw_input("Ich will sagen, dass ")
# 		print "Ok, du sagst, dass", gesagt
# 	elif variante == 2:
# 		print "Was willst Du machen?"
# 		gemacht = raw_input("Ich will ")
# 		print "Alles klar. Du willst", gemacht, ". Ok, klingt gut. Mach mal!"
			
# wahl = int(raw_input("Nimmst Du eins oder zwei? "))
# sag_was(wahl)