""" Write a program reverse.py to print lines of a file in
 reverse order. """


def reverse(filename):
 	lines = open(filename).readlines()
 	for line in  reversed(lines):
 		print line



print reverse('she.txt')