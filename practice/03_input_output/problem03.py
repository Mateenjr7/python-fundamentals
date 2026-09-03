# Level 2 — Multiple Inputs
#Q3. Student Marks
#Take marks of 3 subjects and print:

#total
#average

#Example
#Input:
#80
#75
#90

#Output:
#Total: 245
#Average: 81.66666666666667

marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3

print("Total:", total)
print("Average:", average)