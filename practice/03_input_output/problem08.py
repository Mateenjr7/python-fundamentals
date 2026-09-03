#Q8. Remove Last Digit

#Take an integer and print it without the last digit.

#Example

#Input:
#5837

#Output:
#Number without Last Digit: 583

num = int(input("Enter an integer: "))
remove_last_digit = num // 10
print("Number without Last Digit:", remove_last_digit)

