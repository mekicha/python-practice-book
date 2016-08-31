"""Write a function reverse to reverse a list. 
Can you do this without using list slicing? """

def reverse(list):
	newlist = []
	for i in range(len(list) - 1, -1, -1):
		newlist.append(list[i])
	return newlist
