""" Write a program center_align.py to center align all lines
in the given file. """



def center(filename):
	with open(filename) as file:
		for line in file:
			#print line.center(80)
			print "{0:^70}".format(line)

center('she.txt')

