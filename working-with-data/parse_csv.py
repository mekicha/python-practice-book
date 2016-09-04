"""Write a python function parse_csv to parse csv 
(comma separated values) files."""

import csv
def parse_cv(file):
	arr = []
	with open(file,'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			arr.append(row)
	print arr

parse_cv('a.csv')
