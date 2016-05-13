name = 'Moritz Juedes'
age = 34 # jojoo
height = 180.0 # cm
weight = 76 # kg
eyes = 'Brown'
teeth = 'White'
hair = 'Blond'
cm_to_inches = 0.393701
cm_to_foot = 0.0328084


print "Let's talk about %r." % name
print "He's %d cm tall." % height
print "That's exactly %f inches." % (height * cm_to_inches)
print "That's exactly %f foot." % (height * cm_to_foot)
print "Again, that's exactly", height * cm_to_foot, "foot." # this works, too.
print "He's %d kg heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, I will try to get it exactly right. 
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)