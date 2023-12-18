def zeroed(numbers):

	for num in numbers:
		
		if num == 0 or num == len(numbers) -1:
			numbers[num] = 0
	return numbers


numbers = [2, 5, 7, 8, 9]
num = zeroed(numbers)


