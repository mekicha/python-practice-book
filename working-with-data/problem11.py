#Write a function dups to find all duplicates in the list.


def dups(list):
	newlist = []
	for value in list:
		if list.count(value) > 1 and value not in newlist:
			newlist.append(value)
	return newlist
		
	
print dups([1, 2, 1, 3, 2, 5])