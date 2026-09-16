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

Without parentheses:

```python
10 + 5 * 2
```

Output:

```text
20
```

With parentheses:

```python
(10 + 5) * 2
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

## Important Operators to Remember

```text
Arithmetic:
+  -  *  /  //  %  **

Assignment:
=  +=  -=  *=  /=  //=  %=  **=

Comparison:
==  !=  >  <  >=  <=

Logical:
and  or  not

Identity:
is  is not

Membership:
in  not in

Bitwise:
&  |  ^  ~  <<  >>
```

---

## Key Takeaways

* **Arithmetic operators** perform mathematical operations.
* **Assignment operators** assign or update values.
* **Comparison operators** compare values and return `True` or `False`.
* **Logical operators** combine conditions.
* **Identity operators** check whether objects are the same.
* **Membership operators** check whether a value exists in a collection.
* **Bitwise operators** operate on binary representations.
* **Operator precedence** determines the order in which expressions are evaluated.
