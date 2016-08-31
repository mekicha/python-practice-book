"""Implement a function product, to compute product of a list 
of numbers.
Write a function factorial to compute factorial of a number.
 Can you use the product function defined in the previous 
 example to compute factorial? """

 def product(list):
 	result = 1
 	for num in list:
 		result *= num
 	return result

def factorial(num):
	if num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		return product(range(1, num +1))