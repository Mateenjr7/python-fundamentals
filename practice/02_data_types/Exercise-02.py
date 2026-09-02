#Focus: type conversion

#Q6 — Type Conversion
#Convert:
#x = 50
#into:
#float
#str
#bool
#Print the value and type of each.

x = 50
print(x, type(x))
x_float = float(x)
print(x_float, type(x_float))
x_str = str(x)
print(x_str, type(x_str))
x_bool = bool(x)
print(x_bool, type(x_bool))
print("\n")

#Q7

#Convert:
#x = 99.99
#into an integer.
#Print the result and explain why the decimal part is not present.

x = 99.99

x1 = int(x)
print(x1, type(x1))
print("The decimal part is not present because the int() function truncates the decimal portion when converting a float to an integer.")
print("\n")

#Q8

#Convert these strings into their appropriate types:
#age = "21"
#height = "178.5"
#Then print their types.

age = "21"
height = "178.5"
age_int = int(age)
height_float = float(height)
print(age_int, type(age_int))
print(height_float, type(height_float))
print("\n")

#Q9
#
#Take two numbers as input from the user.
#Convert them into integers and print their:
#values
#data types

n= input("Enter first number: ")
m= input("Enter second number: ")
n_int = int(n)
m_int = int(m)
print(n_int, type(n_int))
print(m_int, type(m_int))
print("\n")

#Q10
#
#Take a person's
#name
#age
#height
#as input.
#Convert age to int and height to float.
#Print all three values with their data types.

name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height: ")
age_int = int(age)
height_float = float(height)    
print(name, type(name))
print(age_int, type(age_int))
print(height_float, type(height_float))