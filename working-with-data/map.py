""" Python provides a built-in function map that applies a 
function to each element of a list. Provide an implementation
for map using list comprehensions. """


def map(func, list):
	return [func(x) for x in list]

def square(x): return x * x

print map(square, range(5))