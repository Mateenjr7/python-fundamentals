#Q9. Three-Digit Number

#Take a three-digit number and print:

#first digit
#middle digit
#last digit

#Example

#Input:
#583

#Output:
#First Digit: 5
#Middle Digit: 8
#Last Digit: 3

num = int(input("Enter a three-digit number: "))
first_digit = num // 100
middle_digit = (num // 10) % 10
last_digit = num % 10
print("First Digit:", first_digit)
print("Middle Digit:", middle_digit)    
print("Last Digit:", last_digit)