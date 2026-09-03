#Q11. Three-Digit Number Sum

#Take a three-digit number and calculate the sum of its digits.

#Example

#Input:
#583

#Output:
#Sum: 16

NUM = int(input("Enter a three-digit number: "))
digit_sum = 0
for i in range(3):
    digit_sum += NUM % 10 
    NUM //= 10
print("Sum:", digit_sum)