#Q7. Last Digit

#Take an integer and print its last digit.

#Example

#Input:
#5837

#Output:
#Last Digit: 7
num = int(input("Enter an integer: "))
last_digit = num % 10
print("Last Digit:", last_digit)