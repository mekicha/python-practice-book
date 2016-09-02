"""Write a program wrap.py that takes filename and width as
aruguments and wraps the lines longer than width. """



def wrap(filename, delim):
 	string = ''
 	with open(filename) as file:
 		    string += file.read().strip()
 	while string:n
 		s = string[:delim]
 		string = string[delim:]
 		print s



print wrap('she.txt', 20)
