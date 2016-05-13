# show content of a file in editor

# input file name and assign it to a variable
file_var = raw_input("Welche Datei willst Du oeffnen?")
# open this variable and assign it to another variable
open_var = open(file_var)
# read the second variable and print it out
print open_var.read()

