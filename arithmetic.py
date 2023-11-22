num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
sum = (num1 + num2 + num3)
print("sum value is", sum)
average = (num1 + num2 + num3)/3
print("average value is", average)
product = (num1 * num2 * num3)
print("product value is", product)
if num1>num2 and num3:
	print("the highest num is", num1)
elif num2>num3 and num1:
	print("the highest num is", num2)
elif num3>num2 and num1:
	print("the highest num is", num3)
if num1<num2 and num3:
	print("the lowest num is", num1)
elif num2<num3 and num1:
	print("the lowest num is", num2)
elif num3<2 and num1:
	print("the lowest num is", num3)

