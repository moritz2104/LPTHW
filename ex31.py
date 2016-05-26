#_*_ coding: utf–8–*–
print "\n"
name = raw_input ("Hallo Fremder, willkommen zu diesem spannenden Abenteuer-Spiel! Wie ist dein Name? \n >> ")

print "\nOk %s. Du betrittst einen dunklen Raum mit zwei Türen. Gehst du durch Tür #1 oder Tür #2? Es gilt, einem Bären zu entkommen und nicht wahnsinnig zu werden (ja, das fällt dir schwer %s).\nGewinne dieses großartige Abenteuer, indem Du Lady Madonna befreist! Sie ist von den Beatles entführst worden und Ringo Starr ist tierisch eifersüchtig!" % (name, name)

door = raw_input('\nAlso %s, bereit? Ja, ich, %s der oder die Mutige, gehe durch Tür Nr.: ' % (name, name))

if door == '1':
	print "\nWow, da sitzt ein riesiger Bär und isst Käsekuchen. Was machst du?"
	print "1: Ich schnappe mir den Käsekuchen!"
	print "2: Ich schreie den Bär an!"

	bear = raw_input('\nAlso, 1 oder 2? Entscheide dich jetzt! >> ')

	if bear == '1':
		print "Der Bär frisst dich und danach den Käsekuchen.\nGAME OVER DU PFEIFFE, geht ja gar nicht. Du bist kein Held %s!\n" % name
	elif bear == '2':
		print "Der Bär schreit zurück und frisst dich dann.\nGAME OVER DU PFEIFFE!\n"
	else:
		print "\nGute Idee %s, das mit der %s, du hast den Bären verscheucht!" % (name, bear)
		print "\nWas machst du jetzt?\n1: Ich gehe besser raus und nehme doch die andere Tür. Gefährlich hier!\n2: Ich lege mich ein bisschen auf den grünen Teppich da hinten und denke nach. %s, das ist keine gute Idee, glaube ich." % name
		almost_there = raw_input("\nAlso, %s, was machst du? >> " % name)
		if almost_there == '1':
			door = '2' # TODO 
		elif almost_there == '2':
			print "\nNachdem du da so ein bisschen nachgedacht hast kommt Lady Madonna und sagt: \"Ach %s, ich habe ja schon so lange auf dich gewartet! Endlich bist du da, oh mein %s!\". Was danach passiert kann hier nicht beschrieben werden!\n %s, Du bist ein Held!" % (name, name, name)


elif door == '2':
	print "\nDu siehst in die tiefsten Abgründe des menschlichen Wahnsinns! Alles klar, dann mal los:"
	print "Was willst du? Blaubeeeeeeren? Drückücke 1."
	print "Oder Semmelbrösel mit Ringo Starr? Bitte die 2."
	print "Erbeeren mit John und Yoko in der UDSSR? Ah, ja, drücke die 3."

	insanity = raw_input('\nNa, kannst du dich entscheiden? ')

	if insanity == "1" or insanity == '2':
		print "Du springst in den Abgrund und landest in blaubeerigen Semmelbröseln. Die Beatles singen dir ein Lied. Es heißt: %s + %s + %s = %s. Dir kommt das irgendwie bekannt vor. ABER DAS IST NICHT, WIE DU DIESES SUPER ABENTEUERSPIEL GEWINNEN KANNST %s!!!!\n GAME OVER!!!\n" % (insanity, insanity, insanity, (insanity * 3), name)
	else:
		print "\nEine dicke Brummel kommt, nimmt dich Huckepack und brummelt %s Mal mit dir um den Hintern von Lady Madonna. Ringo kriegt einen Eifersuchtsanfall. Er ruft: \"Warum hast du %s gesagt??? Und warum bist du durch Tür %s gegangen? Und warum heißt Du %s? Das geht doch nicht!\"\n Schön und gut.\n Trotzdem: GAME OVER!!!\n" % (insanity, insanity, door, name)

else:
	print "\nEin Engelschor singt ein Lied: Es geht so: \"%s Du Troooottelllll, du sollst dich zwischen eins und zwei entscheiden!\"\n\n" % name