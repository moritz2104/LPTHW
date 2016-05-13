# this part defines the function "cheese_and_crackers"
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"

# hier wird cheese_count die zahl 20 und boxes_of_crackers die zahl 30 zugewiesen.
# then the function is being called
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# hier gibt es zwei neue Variablen, die dann anstelle der Argumente eingesetzt werden.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# here the funtion is being called
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside, too:"
cheese_and_crackers(10 + 20, 5 + 6)

# holt sich die oben festegelegten Variablen und addiert einen Betrag.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)