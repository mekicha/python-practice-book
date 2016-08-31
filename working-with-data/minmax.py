""" Python has built-in functions min and max to compute 
minimum and maximum of a given list. Provide an implementation
 for these functions. What happens when you call your min and max
 functions with a list of strings?"""

 def min(list):
	min = list[0]
	for value in list:
		if value < min :
			min = value
	return min

def max(list):
	max = list[0]
	for value in list:
		if value > max:
			max = value
	return max
	
print min([2,4,2,0])
print max([1,4,5,7,2])