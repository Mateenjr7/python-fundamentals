#Q4. Age Calculator

#Take the user's birth year and current year.

#Print their approximate age.

#Example

#Input:
#2005
#2026

#Output:
#Age: 21

birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter the current year: "))

age = current_year - birth_year
print("Age:", age)