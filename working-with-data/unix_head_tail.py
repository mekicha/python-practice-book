"""Implement unix commands head and tail. The head and 
tail commands take a file as argument and prints its first
 and last 10 lines of the file respectively. """


def head(filename):
	with open(filename) as file:
		head =[line for line in file][:10]
	#for  i in range(10):
	for line in head:
		print line

def tail(filename):
	with open(filename) as file:
		length = len(file.readlines())
		file.seek(0)
		tail = [line for line in file][length-10:]
	for line in tail:
		print line

		

head('he.txt')
tail('he.txt')