""" Python provides a built-in function filter(f, a) that 
returns items of the list a for which f(item) returns true. 
Provide an implementation for filter using list comprehensions."""



def filter(func, list):
	return [x for x in list if func(x)]

def even(x): return x%2 == 0

print filter(even, range(10))