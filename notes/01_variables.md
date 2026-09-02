# Python Variables

## 1. What is a Variable?

A variable is a name that refers to a value (object) in Python.

```python
name = "Mateen"
age = 20
height = 178.5
```

Here:

* `name` refers to a string
* `age` refers to an integer
* `height` refers to a float

---

## 2. Creating Variables

Python does not require us to declare the data type before creating a variable.

```python
x = 10
name = "Python"
price = 99.99
is_student = True
```

Python automatically determines the type of the value.

---

## 3. Dynamic Typing

A variable can refer to objects of different types during program execution.

```python
x = 10
print(x)

x = "Hello"
print(x)

x = 3.14
print(x)
```

Output:

```text
10
Hello
3.14
```

---

## 4. Checking the Type

The `type()` function tells us the type of an object.

```python
age = 20
name = "Mateen"

print(type(age))
print(type(name))
```

Output:

```text
<class 'int'>
<class 'str'>
```

---

## 5. Variable Naming Rules

A variable name:

1. Can contain letters, numbers and underscores.
2. Cannot start with a number.
3. Cannot contain spaces.
4. Cannot use Python keywords.
5. Is case-sensitive.

### Valid

```python
student_name = "Ali"
age2 = 21
_total = 500
```

### Invalid

```python
2age = 20          # Cannot start with a number
student name = ""  # Spaces are not allowed
class = 10         # 'class' is a Python keyword
```

---

## 6. Case Sensitivity

Python treats uppercase and lowercase names as different variables.

```python
age = 20
Age = 30

print(age)
print(Age)
```

Output:

```text
20
30
```

---

## 7. Multiple Assignment

Multiple variables can be assigned in one statement.

```python
x, y, z = 10, 20, 30

print(x)
print(y)
print(z)
```

---

## 8. Assigning the Same Value

The same value can be assigned to multiple variables.

```python
a = b = c = 100
```

---

## 9. Swapping Variables

Python allows two variables to be swapped without using a temporary variable.

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

Output:

```text
20
10
```

---

## 10. Deleting a Variable

The `del` keyword removes a variable reference.

```python
x = 100

del x
```

After this, trying to use `x` will cause a `NameError`.

---

## 11. Variable Identity

The `id()` function returns the identity of an object.

```python
x = 10

print(id(x))
```

`id()` is useful for understanding that Python variables refer to objects rather than simply acting as fixed memory boxes.

---

## 12. Constants

Python does not have a special `constant` keyword.

By convention, uppercase names are used for values that should not be changed.

```python
PI = 3.14159
MAX_USERS = 100
```

This is a convention, not a restriction enforced by Python.

---

## 13. Naming Best Practices

Use descriptive names:

```python
student_name = "Mateen"
total_marks = 450
average_score = 85.5
```

Prefer `snake_case` for normal variables:

```python
first_name = "Ali"
total_price = 500
```

Avoid unnecessarily vague names:

```python
x = 500       # Less descriptive
total_price = 500  # Better
```

---

## Key Takeaways

* Variables are names that refer to objects.
* Python uses dynamic typing.
* Variables do not need explicit type declarations.
* Use `type()` to check an object's type.
* Variable names are case-sensitive.
* Use descriptive `snake_case` names.
* Python uses uppercase naming conventions for constants.
* Variables can be reassigned to objects of different types.
