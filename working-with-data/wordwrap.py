"""write a new program wordwrap.py that works like wrap.py,
 but breaks the line only at the word boundaries """



def wordwrap(filename, delim):
	string = ''
	with open(filename) as file:
		string += file.read().strip()
	while string:
		s = string[:delim]
		if s[delim] != ' ':
			delim += 1
		string = string[delim:]
		print s

wordwrap('she.txt', 30)