""" Write a program to print each line of a file in 
reverse order. """

def reverse(filename):
 	lines = open(filename).readlines()
 	for line in  reversed(lines):
 		print line[::-1]



print reverse('she.txt')