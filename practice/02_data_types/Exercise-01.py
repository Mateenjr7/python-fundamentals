# Q1 — Identify Data Types

#Create variables for:
#your name
#your age
#your height
#whether you are a student
#a variable with None
#Print the value and data type of each variable.

name = "Mateen"
age = 21
height = 5.11
is_student = True
none_var = None

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
print(none_var, type(none_var))
print("\n")

#Q2 — Integer vs Float
#Create:
a = 25
b = 25.0

print(a, type(a))
print(b, type(b))
print("\n")

#Q3 — String Numbers
#Create:
#age = "21"
#height = "178.5"
#Print their types.
#Then convert:
#age → integer
#height → float
#Print the converted values and their types.

age = "21"
height = "178.5"
print(age, type(age))
print(height, type(height))

age = int(age)
height = float(height)
print(age, type(age))
print(height, type(height))
print("\n")

#Q4 — Boolean Conversion
#Use bool() to convert the following values:
#0
#1
#""
#"Python"
#None
#Print each original value and its Boolean result.

a = 0
b = 1
c = ""
d = "Python"    
e = None

print(a, bool(a))
print(b, bool(b))
print(c, bool(c))
print(d, bool(d))
print(e, bool(e))
print("\n")

#Q5 — Type Checking
#
#Create:
#name = "Mateen"
#age = 21
#height = 178.5
#is_student = True
#
#Use isinstance() to check whether:
#name is a str
#age is an int
#height is a float
#is_student is a bool
#Print the results.

name = "Mateen"
age = 21    
height = 178.5
is_student = True

print(name, isinstance(name, str))
print(age, isinstance(age, int))
print(height, isinstance(height, float))
print(is_student, isinstance(is_student, bool))