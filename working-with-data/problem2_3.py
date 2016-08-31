"""Python has a built-in function sum to find sum of all elements
of a list. Provide an implementation for sum.
What happens when the above sum function is called with a list of 
strings?Can you make your sum function work for a list of strings 
s well.
"""

def sum(list):
	result = 0
	for value in list:
		if type(value) == str:
			return "".join(list)
		result += value
	return result


sum([1, 2, 3]) #6
sum(["aa", "bb", "cc"]) #aabbcc