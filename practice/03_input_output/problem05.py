#Q5. Seconds Converter

#Take a number of seconds and convert it into:

#minutes
#remaining seconds

#Example
#Input:
#125

#Output:
#Minutes: 2
#Seconds: 5

seconds = int(input("Enter the number of seconds: "))
minutes = seconds // 60
remaining_seconds = seconds % 60
print("Minutes:", minutes)
print("Seconds:", remaining_seconds)