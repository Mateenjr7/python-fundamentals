# Python Operators

## 1. What is an Operator?

An **operator** is a symbol or keyword used to perform an operation on values or variables.

```python
a = 10
b = 3

print(a + b)
```

Here:

* `a` and `b` are **operands**
* `+` is the **operator**
* `a + b` is an **expression**

---

## 2. Types of Operators in Python

Python provides several types of operators:

1. **Arithmetic Operators**
2. **Assignment Operators**
3. **Comparison Operators**
4. **Logical Operators**
5. **Identity Operators**
6. **Membership Operators**
7. **Bitwise Operators**

---

# 3. Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

| Operator | Name           | Example   |     Result |
| -------- | -------------- | --------- | ---------: |
| `+`      | Addition       | `10 + 3`  |       `13` |
| `-`      | Subtraction    | `10 - 3`  |        `7` |
| `*`      | Multiplication | `10 * 3`  |       `30` |
| `/`      | Division       | `10 / 3`  | `3.333...` |
| `//`     | Floor Division | `10 // 3` |        `3` |
| `%`      | Modulus        | `10 % 3`  |        `1` |
| `**`     | Exponentiation | `10 ** 3` |     `1000` |

### Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

### Division `/`

The `/` operator performs normal division and returns a `float`.

```python
print(10 / 2)
```

Output:

```text
5.0
```

### Floor Division `//`

The `//` operator returns the floor of the division result.

```python
print(10 // 3)
```

Output:

```text
3
```

### Modulus `%`

The `%` operator returns the remainder.

```python
print(10 % 3)
```

Output:

```text
1
```

### Exponentiation `**`

The `**` operator raises a number to a power.

```python
print(2 ** 3)
```

Output:

```text
8
```

---

# 4. Assignment Operators

Assignment operators are used to assign values to variables.

### Basic Assignment

```python
x = 10
```

The `=` operator assigns `10` to `x`.

Python also provides compound assignment operators.

| Operator | Example   | Equivalent To |
| -------- | --------- | ------------- |
| `=`      | `x = 5`   | `x = 5`       |
| `+=`     | `x += 5`  | `x = x + 5`   |
| `-=`     | `x -= 5`  | `x = x - 5`   |
| `*=`     | `x *= 5`  | `x = x * 5`   |
| `/=`     | `x /= 5`  | `x = x / 5`   |
| `//=`    | `x //= 5` | `x = x // 5`  |
| `%=`     | `x %= 5`  | `x = x % 5`   |
| `**=`    | `x **= 5` | `x = x ** 5`  |

### Example

```python
x = 10

x += 5
print(x)

x *= 2
print(x)

x -= 5
print(x)
```

Output:

```text
15
30
25
```

---

# 5. Comparison Operators

Comparison operators are used to compare two values.

The result of a comparison is a Boolean value:

```text
True
```

or

```text
False
```

| Operator | Meaning                  | Example    | Result  |
| -------- | ------------------------ | ---------- | ------- |
| `==`     | Equal to                 | `10 == 10` | `True`  |
| `!=`     | Not equal to             | `10 != 5`  | `True`  |
| `>`      | Greater than             | `10 > 5`   | `True`  |
| `<`      | Less than                | `10 < 5`   | `False` |
| `>=`     | Greater than or equal to | `10 >= 10` | `True`  |
| `<=`     | Less than or equal to    | `10 <= 5`  | `False` |

### Example

```python
age = 21

print(age == 21)
print(age != 18)
print(age > 18)
print(age < 18)
print(age >= 21)
print(age <= 20)
```

Output:

```text
True
True
True
False
True
False
```

### `=` vs `==`

This is an important distinction.

`=` is used for **assignment**:

```python
x = 10
```

`==` is used for **comparison**:

```python
x == 10
```

---

# 6. Logical Operators

Logical operators are used to combine or modify conditions.

Python has three logical operators:

* `and`
* `or`
* `not`

## `and`

Returns `True` only when **both conditions are True**.

```python
age = 21
has_id = True

print(age >= 18 and has_id)
```

Output:

```text
True
```

### Truth Table

| A     | B     | A `and` B |
| ----- | ----- | --------- |
| True  | True  | True      |
| True  | False | False     |
| False | True  | False     |
| False | False | False     |

---

## `or`

Returns `True` when **at least one condition is True**.

```python
age = 16
has_permission = True

print(age >= 18 or has_permission)
```

Output:

```text
True
```

### Truth Table

| A     | B     | A `or` B |
| ----- | ----- | -------- |
| True  | True  | True     |
| True  | False | True     |
| False | True  | True     |
| False | False | False    |

---

## `not`

Reverses a Boolean value.

```python
is_raining = False

print(not is_raining)
```

Output:

```text
True
```

### Truth Table

| A     | `not A` |
| ----- | ------- |
| True  | False   |
| False | True    |

---

# 7. Identity Operators

Identity operators are used to check whether two variables refer to the **same object**.

Python has two identity operators:

* `is`
* `is not`

### Example

```python
a = [1, 2, 3]
b = a

print(a is b)
```

Output:

```text
True
```

Both variables refer to the same list object.

---

## `is` vs `==`

This is an important distinction.

* `==` checks whether two values are equal.
* `is` checks whether two variables refer to the same object.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

The lists contain the same values, but they are different objects.

---

# 8. Membership Operators

Membership operators are used to check whether a value exists inside a sequence or collection.

Python has:

* `in`
* `not in`

### `in`

```python
numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 in numbers)
```

Output:

```text
True
False
```

### `not in`

```python
numbers = [10, 20, 30, 40]

print(50 not in numbers)
```

Output:

```text
True
```

Membership operators can also be used with strings.

```python
name = "Mateen"

print("M" in name)
print("z" in name)
```

Output:

```text
True
False
```

---

# 9. Bitwise Operators

Bitwise operators work with numbers at the **binary/bit level**.

| Operator | Name        | Example  |
| -------- | ----------- | -------- |
| `&`      | Bitwise AND | `5 & 3`  |
| `\|`     | Bitwise OR  | `5 \| 3` |
| `^`      | Bitwise XOR | `5 ^ 3`  |
| `~`      | Bitwise NOT | `~5`     |
| `<<`     | Left Shift  | `5 << 1` |
| `>>`     | Right Shift | `5 >> 1` |

### Example

```python
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
```

Binary representation:

```text
5 = 101
3 = 011
```

### Bitwise AND `&`

```text
  101
  011
  ---
  001
```

Therefore:

```python
print(5 & 3)
```

Output:

```text
1
```

### Bitwise OR `|`

```text
  101
  011
  ---
  111
```

Therefore:

```python
print(5 | 3)
```

Output:

```text
7
```

### Bitwise XOR `^`

XOR returns `1` when the bits are different.

```text
  101
  011
  ---
  110
```

Therefore:

```python
print(5 ^ 3)
```

Output:

```text
6
```

---

# 10. Operator Precedence

When an expression contains multiple operators, Python follows a specific order of evaluation.

For example:

```python
result = 10 + 5 * 2
print(result)
```

Output:

```text
20
```

Multiplication is performed before addition.

```text
5 * 2 = 10
10 + 10 = 20
```

### Common Precedence Order

From higher to lower:

```text
()
**
+x, -x, ~x
*, /, //, %
+, -
<<, >>
&
^
|
<, <=, >, >=, ==, !=
not
and
or
```

### Using Parentheses

Parentheses can be used to control the order of operations.

```python
result = (10 + 5) * 2
print(result)
```

Output:

```text
30
```

---

# 11. Quick Summary

| Category   | Operators                  |
| ---------- | -------------------------- |
| Arithmetic | `+ - * / // % **`          |
| Assignment | `= += -= *= /= //= %= **=` |
| Comparison | `== != > < >= <=`          |
| Logical    | `and or not`               |
| Identity   | `is is not`                |
| Membership | `in not in`                |
| Bitwise    | `& \| ^ ~ << >>`           |

---

# 12. Beginner Practice Exercises

> **Try solving these yourself before checking the answers.**

## Exercise 1 — Basic Arithmetic

Create two variables:

```python
a = 20
b = 6
```

Print:

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Floor division
6. Remainder
7. Power

---

## Exercise 2 — Predict the Output

Without running the code, predict the output:

```python
a = 15
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
```

---

## Exercise 3 — Assignment Operators

What will be the final value of `x`?

```python
x = 10

x += 5
x *= 2
x -= 10
x //= 2

print(x)
```

---

## Exercise 4 — Comparison Operators

Given:

```python
age = 20
```

Write expressions to check:

1. Is age equal to `20`?
2. Is age greater than `18`?
3. Is age less than `18`?
4. Is age greater than or equal to `21`?
5. Is age not equal to `25`?

---

## Exercise 5 — Even or Odd

Given:

```python
number = 17
```

Use the modulus operator `%` to determine whether the number is even or odd.

**Hint:**

```python
number % 2
```

---

## Exercise 6 — Logical Operators

Given:

```python
age = 22
has_id = True
```

Write expressions to check:

1. Is the person at least 18 **and** has an ID?
2. Is the person under 18 **or** without an ID?
3. Does the person **not** have an ID?

---

## Exercise 7 — Membership

Given:

```python
fruits = ["apple", "banana", "mango", "orange"]
```

Check:

1. Is `"mango"` in the list?
2. Is `"grapes"` in the list?
3. Is `"grapes"` not in the list?

---

## Exercise 8 — String Membership

Given:

```python
text = "Python Programming"
```

Check whether:

1. `"Python"` is present.
2. `"Java"` is present.
3. `"P"` is present.
4. `"z"` is not present.

---

## Exercise 9 — Operator Precedence

Predict the output:

```python
result = 10 + 5 * 2
print(result)
```

Then predict:

```python
result = (10 + 5) * 2
print(result)
```

Explain why the outputs are different.

---

## Exercise 10 — Mixed Operators

Predict the output:

```python
x = 10
y = 3

print(x > y)
print(x == y)
print(x % y == 1)
print(x > 5 and y < 5)
```

---

## Exercise 11 — Simple Calculator

Create two variables:

```python
a = 25
b = 5
```

Print:

```text
Addition:
Subtraction:
Multiplication:
Division:
```

Example format:

```text
Addition: 30
Subtraction: 20
...
```

---

## Exercise 12 — Shopping Bill

Given:

```python
price = 100
quantity = 3
```

Calculate the total price using an arithmetic operator.

Expected result:

```text
300
```

---

## Exercise 13 — Age Check

Given:

```python
age = 19
```

Create a Boolean expression that checks whether the person is eligible for an age requirement of `18` or above.

Expected result:

```text
True
```

---

## Exercise 14 — Multiple Conditions

Given:

```python
age = 25
salary = 50000
```

Write an expression that checks whether:

* age is at least `18`
* **and**
* salary is at least `30000`

Expected result:

```text
True
```

---

## Exercise 15 — Bitwise Practice

Given:

```python
a = 5
b = 3
```

Find the output of:

```python
print(a & b)
print(a | b)
print(a ^ b)
```

Convert `5` and `3` to binary first.

---

# 13. Mini Challenge

Write a program using operators to calculate the following for a student:

```python
marks1 = 80
marks2 = 75
marks3 = 90
```

Calculate:

1. Total marks
2. Average marks
3. Whether the average is greater than or equal to `40`
4. Whether all three marks are greater than or equal to `35`

Use arithmetic, comparison, and logical operators.

---

# 14. Practice Checklist

After completing these exercises, you should be comfortable with:

* [ ] `+`, `-`, `*`
* [ ] `/`, `//`, `%`
* [ ] `**`
* [ ] `=`, `+=`, `-=`, `*=`
* [ ] `==`, `!=`, `>`, `<`, `>=`, `<=`
* [ ] `and`, `or`, `not`
* [ ] `is`, `is not`
* [ ] `in`, `not in`
* [ ] Basic bitwise operators
* [ ] Operator precedence
* [ ] Combining multiple operators
* [ ] Predicting simple expressions
* [ ] Writing small programs using operators
