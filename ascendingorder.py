num1 = float(input('Enter first_number'))
num2 = float(input('Enter second_number'))
num3 = float(input('Enter third_number'))
largest = 0
second_largest = 0
smallest = 0
if num1 > num2 and num1 > num3:
	largest = num1
	print('num1 is the largest')
elif num2 > num1 and num2 > num3:
	largest = num2
	print('num2 is the largest')
elif num3 > num1 and num3 > num2:
	largest = num3
	print('num3 is the largest')
if num1 < num2 and num1 < num3:
	smallest = num1
	print('num1 is the smallest')
elif num2 < num1 and num2 < num3:
	smallest = num2
	print('num2 is the smallest')
elif num3 < num1 and num3 < num2:
	smallest = num3
	print('num3 is the smallest')
if num1 < largest and num1 > smallest:
	second_largest = num1
	print('num1 is the second_largest')
elif num2 < largest and num2 > smallest:
	second_largest = num2
	print('num2 is the second_largest')
elif num3 < largest and num3 > smallest:
	second_largest = num3
	print('num3 is the second_largest')

	