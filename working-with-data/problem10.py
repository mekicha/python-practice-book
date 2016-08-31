#Write a function unique to find all the unique elements of a list.

def unique(list):
	newlist = []
	for value in list:
		if value in newlist:
			continue
		newlist.append(value)
	return newlist
	
print unique([1, 2, 1, 3, 2, 5])
	