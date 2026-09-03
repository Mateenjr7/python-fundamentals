# Python Input and Output

## 1. What is Input and Output?

Input and output are fundamental concepts in programming.

* **Input** → Data provided to a program.
* **Output** → Information displayed or produced by a program.

In Python:

* `input()` is used to receive data from the user.
* `print()` is used to display output.

Example:

```python
name = input("Enter your name: ")

print("Hello", name)
```

If the user enters:

```text
Mateen
```

Output:

```text
Hello Mateen
```

**---**

## 2. Output Using `print()`

The `print()` function is used to display information on the console.

### Syntax

```python
print(value)
```

Example:

```python
print("Hello, World!")
```

Output:

```text
Hello, World!
```

**---**

## 3. Printing Variables

Variables can be passed directly to the `print()` function.

```python
name = "Mateen"

age = 21

print(name)

print(age)
```

Output:

```text
Mateen

21
```

**---**

## 4. Printing Multiple Values

Multiple values can be printed using commas.

```python
name = "Mateen"

age = 21

print(name, age)
```

Output:

```text
Mateen 21
```

By default, Python places a space between multiple values.

```python
print("Python", "Java", "C++")
```

Output:

```text
Python Java C++
```

**---**

## 5. The `sep` Parameter

The `sep` parameter controls the separator between multiple values passed to `print()`.

The default separator is a space.

```python
print("Python", "Java", "C++")
```

Output:

```text
Python Java C++
```

A custom separator can be specified.

```python
print("Python", "Java", "C++", sep=" | ")
```

Output:

```text
Python | Java | C++
```

Another example:

```python
print(2026, 9, 3, sep="-")
```

Output:

```text
2026-9-3
```

**---**

## 6. The `end` Parameter

The `end` parameter controls what Python prints after a `print()` statement.

By default, `print()` ends with a new line.

```python
print("Hello")

print("World")
```

Output:

```text
Hello

World
```

The default value of `end` is:

```python
end="\n"
```

A custom value can be provided.

```python
print("Hello", end=" ")

print("World")
```

Output:

```text
Hello World
```

Another example:

```python
print("Loading", end="...")

print("Done")
```

Output:

```text
Loading...Done
```

**---**

## 7. Escape Sequences

Escape sequences are special characters used inside strings.

### New Line — `\n`

`\n` moves the output to a new line.

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

### Tab — `\t`

`\t` inserts a tab space.

```python
print("Name\tAge")

print("Mateen\t21")
```

Output:

```text
Name    Age
Mateen  21
```

### Backslash — `\\`

`\\` is used to print a backslash.

```python
print("C:\\Users\\Mateen")
```

Output:

```text
C:\Users\Mateen
```

### Double Quote — `\"`

`\"` allows a double quote to be used inside a double-quoted string.

```python
print("He said \"Hello\"")
```

Output:

```text
He said "Hello"
```

**---**

## 8. Taking Input Using `input()`

The `input()` function is used to receive information from the user.

### Syntax

```python
variable = input("Prompt")
```

Example:

```python
name = input("Enter your name: ")

print(name)
```

If the user enters:

```text
Mateen
```

Output:

```text
Mateen
```

**---**

## 9. Understanding `input()`

An important rule in Python is:

> `input()` always returns a string.

Example:

```python
age = input("Enter your age: ")

print(type(age))
```

If the user enters:

```text
21
```

The output is:

```text
<class 'str'>
```

Even though `21` looks like a number, Python initially stores it as a string.

**---**

## 10. Taking Integer Input

The `int()` function can be used to convert user input into an integer.

```python
age = int(input("Enter your age: "))

print(age)

print(type(age))
```

If the user enters:

```text
21
```

Output:

```text
21

<class 'int'>
```

**---**

## 11. Taking Float Input

The `float()` function can be used to convert user input into a floating-point number.

```python
height = float(input("Enter your height: "))

print(height)

print(type(height))
```

If the user enters:

```text
178.5
```

Output:

```text
178.5

<class 'float'>
```

**---**

## 12. Taking Multiple Inputs

Multiple inputs can be taken using separate `input()` statements.

```python
name = input("Enter your name: ")

age = int(input("Enter your age: "))

city = input("Enter your city: ")

print(name)

print(age)

print(city)
```

Example:

```text
Enter your name: Mateen
Enter your age: 21
Enter your city: Hyderabad
```

Output:

```text
Mateen

21

Hyderabad
```

**---**

## 13. Taking Multiple Values in One Line

The `split()` method can be used to separate multiple values entered on the same line.

```python
name, age = input("Enter name and age: ").split()
```

Example input:

```text
Mateen 21
```

Now:

```python
print(name)

print(age)
```

Output:

```text
Mateen

21
```

However, both values are initially strings.

```python
print(type(name))

print(type(age))
```

Output:

```text
<class 'str'>

<class 'str'>
```

**---**

## 14. The `split()` Method

The `split()` method divides a string into multiple parts.

Example:

```python
data = input("Enter three values: ").split()

print(data)
```

Input:

```text
10 20 30
```

Output:

```text
['10', '20', '30']
```

By default, `split()` separates values based on whitespace.

**---**

## 15. Taking Multiple Integers

The `map()` function can be combined with `split()` to convert multiple inputs into integers.

```python
a, b, c = map(int, input().split())
```

Example input:

```text
10 20 30
```

Python processes the input conceptually as:

```text
"10 20 30"
        ↓
split()
        ↓
["10", "20", "30"]
        ↓
map(int, ...)
        ↓
10, 20, 30
```

Example:

```python
a, b, c = map(int, input("Enter three numbers: ").split())

print(a)

print(b)

print(c)
```

Output:

```text
10

20

30
```

**---**

## 16. Formatted Output

Formatted output allows variables and expressions to be included inside strings.

One of the preferred modern approaches in Python is the **f-string**.

### f-Strings

An f-string is created by placing `f` before the string.

```python
name = "Mateen"

age = 21

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Mateen and I am 21 years old.
```

**---**

## 17. Expressions Inside f-Strings

Expressions can be written inside `{}`.

```python
a = 10

b = 20

print(f"Sum = {a + b}")
```

Output:

```text
Sum = 30
```

Another example:

```python
price = 500

quantity = 3

print(f"Total = {price * quantity}")
```

Output:

```text
Total = 1500
```

**---**

## 18. String Concatenation

String concatenation means combining strings using the `+` operator.

```python
first_name = "Abdul"

last_name = "Mateen"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Abdul Mateen
```

Strings can only be directly concatenated with other strings.

Incorrect:

```python
age = 21

print("Age: " + age)
```

This produces a `TypeError`.

Correct:

```python
print("Age:", age)
```

or:

```python
print(f"Age: {age}")
```

**---**

## 19. Type Conversion with Input

Since `input()` returns a string, type conversion is often required.

### Integer

```python
age = int(input("Enter your age: "))
```

### Float

```python
height = float(input("Enter your height: "))
```

### String

```python
value = str(100)
```

Example:

```python
age = int(input("Enter age: "))

next_year = age + 1

print(f"Next year you will be {next_year}.")
```

Input:

```text
21
```

Output:

```text
Next year you will be 22.
```

**---**

## 20. Practical Example — Student Information

```python
name = input("Enter your name: ")

age = int(input("Enter your age: "))

course = input("Enter your course: ")

print("\n--- Student Information ---")

print(f"Name: {name}")

print(f"Age: {age}")

print(f"Course: {course}")
```

Example:

```text
Enter your name: Mateen
Enter your age: 21
Enter your course: Computer Science

--- Student Information ---
Name: Mateen
Age: 21
Course: Computer Science
```

**---**

## 21. Practical Example — Basic Calculator

```python
a = float(input("Enter first number: "))

b = float(input("Enter second number: "))

print(f"Sum: {a + b}")

print(f"Difference: {a - b}")

print(f"Product: {a * b}")

print(f"Division: {a / b}")
```

Example:

```text
Enter first number: 10
Enter second number: 5
```

Output:

```text
Sum: 15.0

Difference: 5.0

Product: 50.0

Division: 2.0
```

**---**

## 22. Common Mistakes

### Mistake 1 — Forgetting that `input()` Returns a String

Incorrect:

```python
age = input("Enter age: ")

print(age + 5)
```

`age` is a string.

Correct:

```python
age = int(input("Enter age: "))

print(age + 5)
```

**---**

### Mistake 2 — Adding Strings Instead of Numbers

```python
a = input()

b = input()

print(a + b)
```

Input:

```text
10
20
```

Output:

```text
1020
```

Why?

Because Python is performing string concatenation:

```text
"10" + "20" = "1020"
```

Correct:

```python
a = int(input())

b = int(input())

print(a + b)
```

Output:

```text
30
```

**---**

### Mistake 3 — Mixing Strings and Integers

Incorrect:

```python
age = 21

print("Age: " + age)
```

Correct:

```python
print("Age:", age)
```

or:

```python
print(f"Age: {age}")
```

**---**

### Mistake 4 — Incorrect Number of Values

If you write:

```python
a, b, c = input().split()
```

the input must contain three values.

Correct:

```text
10 20 30
```

If fewer or more values are provided, Python will raise a `ValueError`.

**---**

### Mistake 5 — Forgetting Float Conversion

Incorrect:

```python
height = input("Enter height: ")
```

If numerical calculations are required, convert it:

```python
height = float(input("Enter height: "))
```

**---**

## 23. Input and Output Summary

| Function / Method | Purpose                      | Example                |
| ----------------- | ---------------------------- | ---------------------- |
| `input()`         | Receives user input          | `input("Name: ")`      |
| `print()`         | Displays output              | `print("Hello")`       |
| `split()`         | Splits a string              | `"10 20".split()`      |
| `int()`           | Converts to integer          | `int("21")`            |
| `float()`         | Converts to float            | `float("10.5")`        |
| `str()`           | Converts to string           | `str(21)`              |
| `map()`           | Applies a function to values | `map(int, values)`     |
| `sep`             | Controls output separator    | `print(a, b, sep="-")` |
| `end`             | Controls output ending       | `print("Hi", end=" ")` |

**---**

## 24. Key Takeaways

* `input()` is used to receive data from the user.

* `input()` always returns a string.

* Use `int()` when integer input is required.

* Use `float()` when decimal input is required.

* `print()` is used to display output.

* `sep` controls the separator between multiple values.

* `end` controls what is printed after the output.

* `\n` creates a new line.

* `\t` creates a tab space.

* `split()` divides a string into multiple values.

* `map()` can be used to convert multiple input values.

* f-strings provide a clean way to format output.

* String concatenation can be performed using `+`.

* Avoid directly combining strings and numbers with `+`.

**---**

## 25. Practice Checklist

Before moving to the next topic, you should be able to:

* [ ] Use `print()`

* [ ] Print variables

* [ ] Print multiple values

* [ ] Use `sep`

* [ ] Use `end`

* [ ] Use escape sequences

* [ ] Take user input using `input()`

* [ ] Convert input using `int()`

* [ ] Convert input using `float()`

* [ ] Use `split()`

* [ ] Use `map()` with `split()`

* [ ] Use f-strings

* [ ] Concatenate strings

* [ ] Build a basic calculator

* [ ] Build a simple user-input program

* [ ] Identify common input/output errors

**---**

## 26. Quick Reference

```python
# Basic output
print("Hello, World!")

# Printing variables
name = "Mateen"
print(name)

# Multiple values
print("Name:", name)

# Custom separator
print("Python", "Java", "C++", sep=" | ")

# Custom ending
print("Hello", end=" ")
print("World")

# User input
name = input("Enter your name: ")

# Integer input
age = int(input("Enter your age: "))

# Float input
height = float(input("Enter your height: "))

# Multiple inputs
a, b = input().split()

# Multiple integers
a, b = map(int, input().split())

# Formatted output
print(f"Name: {name}, Age: {age}")

# New line
print("Hello\nWorld")

# Tab
print("Name\tAge")
```

**---**

## Summary

Python provides simple built-in functions for interacting with users.

The two most important functions are:

```python
input()
```

for receiving data, and:

```python
print()
```

for displaying output.

A common Python program follows this pattern:

```text
Input
  ↓
Processing
  ↓
Output
```

Example:

```python
number = int(input("Enter a number: "))

result = number * 2

print(f"Result: {result}")
```


