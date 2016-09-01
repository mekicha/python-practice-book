""" Write a function group(list, size) that take a list and 
splits into smaller lists of given size."""


def group(list, size):
	newlist = []
	while list:
		newlist.append(list[:size])
		list = list[size:]
	return newlist
	
	
print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
