""" Implement unix command grep. The grep command takes a string
and a file as arguments and prints all lines in the file which
contain the specified string."""


def grep(filename, string):
	with open(filename) as file:
		for line in file:
			if string in line:
				print line

grep('he.txt','Management')