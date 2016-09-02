""" Write a function enumerate that takes a list and returns a 
list of tuples containing (index,item) for each item in the list.
"""


def enumerate(list):
	return [(x,y) for x in range(len(list)) for y in list if list[x] == y]
	
	
	
print enumerate(["a", "b", "c"])