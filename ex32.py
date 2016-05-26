the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	print "Eine Frucht vom Typ: %s" % fruit

for i in change:
	print "I got %r" % i

# We can also build lists, first start with an empty one.
elements = []

# Then use the range function to do 0 to 5 counts
for i in range(1, 10):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i) # Hierdurch wird i erst der obigen elements-list hinzugefuegt.

# Now we can print these out too
for i in elements:
	print "Element was %d" % i

print "Das hier ist i: ",i

print max(elements), "Dies ist eine Funktion"
print len(elements), "Dies ist eine Funktion"
print elements.count(i), "list.count(obj)"
print elements.pop(-1), "list.pop(-1)"

elements.append(100)
print elements