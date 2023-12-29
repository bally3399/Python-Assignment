def running_total(numbers):

	running_total = 0
	for index in range(len(numbers)):
		running_total += numbers[index]
	return running_total
numbers = [1, 2, 3, 4, 5]
print(running_total(numbers))