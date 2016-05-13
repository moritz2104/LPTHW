#_*_ coding: utf–8–*–

from sys import argv # importiert argv

script, input_file = argv # definiert zwei argumente des argument vectors

# definiert eine funktion namens print_all mit dem argument f 
# (das heißt, das argument f wird gebraucht, um diese funktion auszuführen)
def print_all(f):
	# liest f und spuckt es aus (f.read(), die klammern nach read zeigen, dass read
	# seinerseits auch eine funktion ist.)
	print f.read() # !!!!! function call !!!!!

# definiert eine funktion namens rewind mit dem argument f (dem gleichen f, wie oben)
def rewind(f):
	# nimmt f und setzt den "die nadel" auf den Anfang (über man seek gibt es ne anleitung)
	f.seek(0) # !!!!! function call !!!!!

# definiert eine funktion namens print_a_line mit zwei argumenten: 
# line_count und f (dem gleichen f, wie oben)
def print_a_line(line_count, f):
	# spuckt line_count und current_file aus: 
	# line count: wird übernommen von current_line (ergibt die aktuelle zeilennummer)
	# f.readline() liest aktuelle zeile vor. (woher kommt den die? f ist doch unabhängig von current_line...)
	print line_count,"\b. Zeile: ", f.readline(), # !!!!! function call !!!!! # das komma verhindert zeilenumbrüche

# Variable current_file wird über argv mit input_file bestückt
current_file = open(input_file) # !!!!! function call !!!!!

print "First, let's print the whole file:\n"

# ruft die funktionprint_all und belegt das eine erforderliche argument mit current_file
# d.h. f wird zu current_file und über f.read() ausgelesen.
print_all(current_file) # !!!!! function call !!!!!

print "Now let's rewind, kind of like a tape. (If you remember what that is.)"

# Hier wird die Funktion rewind() aufgerufen und das args current_file übergeben.
# f wird zu current_file und zurückgespult
rewind(current_file) # !!!!! function call !!!!!

print "Now lets print three lines:"

# neue variable current_line wird auf 1 gesetzt
current_line = 1

# die funktion print_a_line wird aufgerufen und die zwei erforderlichen agrs werden übergeben:
# line_count wird mit current_line belegt
# f wird mit current_file belegt
print_a_line(current_line, current_file) # current_line = 1 # !!!!! function call !!!!!

# das ganze geschieht hier drei mal, mit jeweils einem um +1 höheres current_line.
current_line += 1
print_a_line(current_line, current_file) # current_line = current_line + 1 = 1 + 1 = 2 # !!!!! function call !!!!!

current_line += 1
print_a_line(current_line, current_file) # current_line = current_line + current_line + 1 = 1 + 1 + 1 = 3 # !!!!! function call !!!!!

# in diesem Script werden insgesamt neun Funktionen verwendet. Wow. 


