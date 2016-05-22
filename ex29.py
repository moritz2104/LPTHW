people = 20
cats = 3
dogs = 15

if people < cats: # if this is TRUE, do what comes indented.
	print "Es gibt zu viele Katzen!"

if people > cats:
	print "Nicht zu viele Katzen, die Welt ist gerettet."

if people < dogs:
	print "Es gibt weniger Hunde als Menschen."

if people > dogs:
	print "Juchuuuu, mehr Menschen als Hunde."

print "\n"
dogs += 5

if people >= dogs:
	print "Gleich viele oder mehr Menschen wie Hunde."

if people <= dogs:
	print "Gleich viele oder weniger Menschen wie Hunde."

if people == dogs:
	print "Gleichstand zwischen Hunden und Menschen."

print "##########\n"

if people == dogs:
	if cats < people:
		print "1. Gleichstand zwischen Hunden und Menschen. Und ausserdem weniger Katzen als Menschen."

if people == dogs and cats < people:
	print "2. Gleichstand zwischen Hunden und Menschen. Und ausserdem weniger Katzen als Menschen."

if people == dogs and not cats > people:
	print "3. Gleichstand zwischen Hunden und Menschen. Und ausserdem weniger Katzen als Menschen."