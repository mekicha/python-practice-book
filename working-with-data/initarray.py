""" Write a function array to create an 2-dimensional array. 
The function should take both dimensions as arguments. 
Value of each element can be initialized to None: """


def array(x,y):
	return [[None for i in range(y)] for j in range(x)]
	
print array(2,3)