from math import sqrt
def divide_or_square(number):
	if number % 5 == 0:
		return sqrt(number)
	else: 
		return  number

