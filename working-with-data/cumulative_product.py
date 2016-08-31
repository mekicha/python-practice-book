""" Write a function cumulative_product to compute cumulative
 product of a list of numbers. """

 def cumulative_product(list):
	newlist = []
	prev = list[0]
	newlist.append(prev)
	for i in range(1,len(list)):
		prev = prev * list[i]
		newlist.append(prev)
	return newlist

	
print cumulative_product([1, 2, 3, 4])
print  cumulative_product([4, 3, 2, 1])