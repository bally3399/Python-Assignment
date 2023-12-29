def largest_number(numbers):

	largest_number = 0
	for index in range(len(numbers)):
		largest_number = numbers[index]
	return largest_number
numbers = [1, 2, 3, 4, 5, 6]
print(largest_number(numbers))
