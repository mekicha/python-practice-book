"""Functions to calculate the number of characters, words and
lines in a given file """


def charcount(filename):
	return len(open(filename).read())

def worcount(filename):
	return len(open(filename).read().split())

def linecount(filename):
	return len(open(filename).readlines())