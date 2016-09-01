"""Write a function lensort to sort a list of strings based 
on length. """



def lensort(list):
	list.sort(key=len)
	return list
	""" alternatively we can do
	    sorted(a) which returns a
	    new list """


	
print lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
