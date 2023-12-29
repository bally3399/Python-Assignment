def sum_number(numbers):

	sum = 0
	for index in range(len(numbers)):
		sum += numbers[index]
	return sum
def sum1_number(numbers):
	sum1 = 0
	index = 0
	while index < len(numbers):
		sum1 += numbers[index]
		index = index + 1
	return sum1
numbers = [1, 2, 3, 4, 5]
print(sum_number(numbers))
print(sum1_number(numbers))
