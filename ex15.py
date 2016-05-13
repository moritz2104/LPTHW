# Importiert ein Modul namens argument vector (argv) aus der sys Library (oder sys Package). 
# Die sys Library enthaelt systemspezifische Parameter und Funktionen
from sys import argv

# Weisst argv die Variablen script und filename zu.
script, filename = argv

# Oeffnet das File (und macht damit erstmal nichts.) Stimmt nicht. File wird der Variablen txt angehaengt.
var = open(filename)

# Printet einen String und holt sich die Variable filename.
# Die wurde im ersten Schritt im Terminal angegeben.
print "Here is your file %r %r:" % (filename, filename)

# Haengt der Variablen txt die Funktion read an. Das passiert ueber den Punkt.
print var.read()

# Hier wie oben. Nur, dass jetzt der Filename nicht ueber argv kommt, sondern ueber raw_input.
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()