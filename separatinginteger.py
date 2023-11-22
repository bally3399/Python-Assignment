num = int(input('Enter five digit number'))
first_digit = num // 10000
remainder = num % 10000
second_digit = remainder // 1000
remainder1 = remainder % 1000
third_digit = remainder1 // 100
remainder2 = remainder1 % 100
forth_digit = remainder2 // 10
fifth_digit = remainder2 % 10
print(first_digit,' ',second_digit,' ', third_digit,' ', forth_digit,' ', fifth_digit)