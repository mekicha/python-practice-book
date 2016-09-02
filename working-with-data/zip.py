"""Provide an implementation for zip function using 
list comprehensions. """


def zip(list1, list2):
	return [(x,y) for x in list1 for y in list2 if list1.index(x) == list2.index(y)]
	


print zip([1, 2, 3], ["a", "b", "c"])