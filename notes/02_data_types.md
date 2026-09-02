Yes — **exactly this manner**. Your Variables notes are clean, structured, and not unnecessarily huge. We should make **Data Types** follow the same style and level.

Use this for `notes/02_data_types.md`:

::contentReference[oaicite:0]{index="0"}

# Python Data Types

## 1. What is a Data Type?

A data type tells Python what kind of value an object contains.

```python
name = "Mateen"
age = 21
height = 178.5
is_student = True
```

Here:

* `name` refers to a string
* `age` refers to an integer
* `height` refers to a float
* `is_student` refers to a boolean

---

## 2. Main Python Data Types

Python has several built-in data types.

The main basic types are:

| Data Type  | Description         | Example    |
| ---------- | ------------------- | ---------- |
| `int`      | Whole numbers       | `21`       |
| `float`    | Decimal numbers     | `178.5`    |
| `str`      | Text                | `"Mateen"` |
| `bool`     | True or False       | `True`     |
| `NoneType` | Represents no value | `None`     |

Python also provides collection types such as `list`, `tuple`, `set`, and `dict`, which will be covered separately.

---

## 3. Integer — `int`

An integer is a whole number without a decimal point.

```python
age = 21
marks = 95
temperature = -5
```

Integers can be positive, negative, or zero.

```python
a = 10
b = -10
c = 0
```

---

## 4. Float — `float`

A float is a number that contains a decimal point.

```python
height = 178.5
price = 99.99
temperature = 36.5
```

Negative decimal values are also floats.

```python
temperature = -2.5
```

Note that:

```python
x = 10
y = 10.0
```

Here:

```text
x → int
y → float
```

---

## 5. String — `str`

A string is a sequence of characters used to represent text.

Strings are written inside single or double quotes.

```python
name = "Mateen"
city = "Hyderabad"
college = 'JNTUH'
```

Numbers inside quotes are also strings.

```python
age1 = 21
age2 = "21"
```

Here:

```text
age1 → int
age2 → str
```

---

## 6. Boolean — `bool`

A Boolean represents one of two values:

```python
True
False
```

Example:

```python
is_student = True
is_married = False
```

Boolean values are case-sensitive.

Correct:

```python
is_student = True
```

Incorrect:

```python
is_student = true
```

---

## 7. NoneType — `None`

`None` represents the absence of a value.

```python
result = None
```

The type of `None` is `NoneType`.

```python
print(type(result))
```

Output:

```text
<class 'NoneType'>
```

`None` is different from:

```text
0
""
False
```

It specifically represents no value.

---

## 8. Checking the Data Type

The `type()` function tells us the type of an object.

```python
name = "Mateen"
age = 21
height = 178.5
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
```

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

---

## 9. Dynamic Typing

Python is a dynamically typed language.

We do not need to explicitly declare the data type when creating a variable.

```python
x = 10
print(type(x))

x = "Hello"
print(type(x))

x = 3.14
print(type(x))
```

Output:

```text
<class 'int'>
<class 'str'>
<class 'float'>
```

A variable can refer to objects of different types during program execution.

---

## 10. Type Conversion

Type conversion means converting a value from one data type to another.

Common functions include:

```python
int()
float()
str()
bool()
```

---

## 11. Converting to Integer

The `int()` function converts a value to an integer when possible.

```python
age = "21"

age = int(age)

print(age)
print(type(age))
```

Output:

```text
21
<class 'int'>
```

When converting a float to an integer, the decimal portion is removed.

```python
x = 10.9

print(int(x))
```

Output:

```text
10
```

`int()` does not round the number.

---

## 12. Converting to Float

The `float()` function converts a value to a floating-point number.

```python
price = "99.99"

price = float(price)

print(price)
print(type(price))
```

Output:

```text
99.99
<class 'float'>
```

An integer can also be converted to a float.

```python
x = 10

print(float(x))
```

Output:

```text
10.0
```

---

## 13. Converting to String

The `str()` function converts a value to a string.

```python
age = 21

age = str(age)

print(age)
print(type(age))
```

Output:

```text
21
<class 'str'>
```

---

## 14. Converting to Boolean

The `bool()` function converts a value to `True` or `False`.

```python
print(bool(1))
print(bool(0))
```

Output:

```text
True
False
```

Some commonly false values are:

```python
False
0
0.0
""
None
```

A non-empty string is considered `True`.

```python
print(bool("Hello"))
print(bool("0"))
```

Output:

```text
True
True
```

---

## 15. `input()` and Data Types

The `input()` function always returns a string.

```python
age = input("Enter your age: ")

print(type(age))
```

Even if the user enters:

```text
21
```

the value is still a string.

To receive an integer:

```python
age = int(input("Enter your age: "))
```

To receive a float:

```python
height = float(input("Enter your height: "))
```

---

## 16. `isinstance()`

The `isinstance()` function checks whether an object belongs to a particular data type.

```python
age = 21

print(isinstance(age, int))
```

Output:

```text
True
```

Example:

```python
name = "Mateen"

print(isinstance(name, str))
```

Output:

```text
True
```

It returns `False` if the object is not of the specified type.

```python
print(isinstance(age, str))
```

Output:

```text
False
```

---

## 17. Variable, Value, and Data Type

Consider:

```python
age = 21
```

Here:

* `age` → variable/name
* `21` → value
* `int` → data type

Another example:

```python
name = "Mateen"
```

Here:

* `name` → variable/name
* `"Mateen"` → value
* `str` → data type

---

## 18. Common Mistakes

### Mistake 1 — Numbers inside quotes

```python
age = "21"
```

This is a string.

```python
age = 21
```

This is an integer.

---

### Mistake 2 — Forgetting `input()` returns a string

```python
age = input("Enter age: ")
```

`age` is a string.

Use:

```python
age = int(input("Enter age: "))
```

when an integer is required.

---

### Mistake 3 — Incorrect Boolean capitalization

Incorrect:

```python
is_student = true
```

Correct:

```python
is_student = True
```

---

### Mistake 4 — Assuming `int()` rounds

```python
int(5.9)
```

returns:

```text
5
```

not:

```text
6
```

---

## Key Takeaways

* A data type tells Python what kind of value an object contains.
* `int` → whole numbers.
* `float` → decimal numbers.
* `str` → text.
* `bool` → `True` or `False`.
* `NoneType` → absence of a value.
* Use `type()` to check an object's type.
* Python is dynamically typed.
* A variable can refer to objects of different types.
* Use `int()`, `float()`, `str()`, and `bool()` for type conversion.
* `input()` always returns a string.
* Use `isinstance()` to check whether an object is a particular type.
* `list`, `tuple`, `set`, and `dict` are also Python data types, but they will be covered in their own topics.
