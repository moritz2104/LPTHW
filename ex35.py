#_*_ coding: utf–8–*–
from sys import exit

def gold_room():
	print "Dieser Raum ist voll mit Gold. Wieviel Kilogramm nimmst Du davon mit? Nimm bloß nicht zu viel!"

	choice = raw_input('>> ')
	if choice.isdigit():
		how_much = int(choice)
	else:
		dead("Ey, Du musst eine Zahl eintippen!")

	if how_much <= 7:
		print "Na schön, du hast nicht zu viel mitgenommen. Gewonnen!"
		exit(0)
	else:
		dead("Du hast zu viel mitgenommen! GAME OVER!")


def bear_room():
	print "Da sitzt ein dicker Bär!"
	print "Der Bär hat einen Topf voll Honig."
	print "Er sitzt vor einer Tür."
	print "Wie willst du ihn verscheuchen?"
	bear_moved = False

	while True:
		choice = raw_input('>> ')

		if "Honig" in choice :
			dead("Der Bär wird sauer und frisst Dich auf.")
		elif "schrei" in choice and not bear_moved:
			print "Der Bär fängt an zu weinen und läuft zu seiner Mama. Die Tür ist frei. Was machst Du jetzt?"
			bear_moved = True
		elif not "öffne" in choice and bear_moved:
			dead("Der Bär kommt zurück und frisst dich auf. Du hättest vielleicht erstmal die Tür öffnen sollen.")
		elif "öffne" in choice and bear_moved:
			gold_room()
		else:
			print "Ich habe keine Ahnung, was das heißen soll."


def madonna_room():
	print "Hier sitzt die schöne Lady Madonna."
	print "Rennst du um dein Leben oder bleibst du hier?"

	choice = raw_input('>> ')

	if "renne" in choice:
		start()
	elif "hier" in choice or "bleibe" in choice:
		dead ("Lady Madonna verwandelt sich in einen Bären und frisst dich auf. GAME OVER! :-( ")
	elif "Wunsch" in choice:
		gold_room()
	else:
		madonna_room()


def dead(why):
	print why, "Game over Du Pfeiffe."
	print "Was willst Du jetzt machen?"
	print "Weiterspielen oder raus hier?"
	choice = raw_input('>> ')
	if "weiter" in choice:
		start()
	elif "raus" in choice:
		exit(0)
	else:
		dead("Du sollst Dich entscheiden, Mann!")


def start():
	print "Du bist in einem großen weißen Raum."
	print "Es gibt da eine Tür zu deiner rechten und eine zu deiner linken."
	print "Welche Tür nimmst du?"

	choice = raw_input('>> ')

	if "recht" in choice:
		bear_room()
	elif "link" in choice:
		madonna_room()
	else:
		dead("Du hättest dich besser für eine der Türen entschieden. Jetzt kommt ein Bär und frisst dich auf.")


start()










