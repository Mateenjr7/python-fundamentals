#Q6. Swap Two Numbers

#Take two numbers and swap them.

#Example

#Input:
#10
#20

#Output:
#Before Swap: 10 20
#After Swap: 20 10


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Before Swap:", num1, num2)
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("After Swap:", num1, num2)