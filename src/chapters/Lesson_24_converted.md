
# Lesson 24: Introduction to Recursion
Owner: Saban, Michael  
Reviewer: Jason for Saban, Michael

Per the Guidelines for Content the following items are missing:  
Overview & Introduction  
Assessment  
Next steps  
Everything else looks fine.

## Learning Objectives

- Define recursion and identify recursive structures (lists, trees, mathematical sequences).  
- Trace simple recursive functions by hand.  
- Implement basic recursive algorithms (countdown, factorial, fibonacci).  
- Explain the importance of base cases and how infinite recursion occurs.  
- Compare recursion to iteration and describe when recursion is useful.  

---

# Introduction

Recursion is a programming technique where a function calls itself in order to solve a 
problem. While this idea may seem strange at first, recursive patterns appear everywhere: 
mathematical sequences, nested folders, fractal patterns, and more.

In Python, recursion is especially useful when a problem can be broken down into smaller 
versions of itself. However, recursion must be used carefully to avoid infinite loops and 
stack overflow errors.

In this lesson, you will learn the fundamental concepts of recursion and practice tracing and 
writing simple recursive functions.

---

# 1. What Is Recursion? (5 min)

Recursion occurs when a function solves a small part of a problem and then calls itself to 
solve the rest. Recursion always includes:

1. A **base case** — the simplest version of the problem, which stops recursion.  
2. A **recursive case** — where the function calls itself on a smaller input.

## Example: Countdown

```python
def countdown(n):
    if n == 0:            # base case
        print("Blast off!")
    else:                 # recursive case
        print(n)
        countdown(n - 1)
````

Calling:

```
countdown(5)
```

prints:

```
5
4
3
2
1
Blast off!
```

---

# 2. Base Cases (10 min)

A base case prevents infinite recursion. Without it, the function will call itself forever
until Python stops the program with:

```
RecursionError: maximum recursion depth exceeded
```

## Example without a base case (danger!)

```python
def recurse():
    print("hello")
    recurse()      # no base case!
```

Running this will print "hello" many times and then crash.

---

# 3. Visualizing Recursion

A recursive call creates a new “frame” (a saved state of the function). Python keeps these
frames in a **call stack**.

Example:

```python
def f(n):
    if n == 0:
        return 0
    return n + f(n - 1)
```

Calling `f(3)` evaluates like this:

```
f(3)
3 + f(2)
    2 + f(1)
        1 + f(0)
            0
```

Each call waits for the next one to return.

# 4. Classic Recursive Algorithms (15 min)

## 4.1 Factorial

The factorial of a number *n* (written as n!) is:

```

n! = n × (n-1) × (n-2) × ... × 1

```

By definition:

```

0! = 1

````

Recursive implementation:

```python
def factorial(n):
    if n == 0:           # base case
        return 1
    return n * factorial(n - 1)
````

Example:

```
factorial(4)
→ 4 * factorial(3)
→ 4 * 3 * factorial(2)
→ 4 * 3 * 2 * factorial(1)
→ 4 * 3 * 2 * 1 * factorial(0)
→ 4 * 3 * 2 * 1 * 1
→ 24
```

---

## 4.2 Fibonacci Sequence

The Fibonacci sequence is defined as:

```
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)
```

Recursive implementation:

```python
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
```

Example:

```
fib(4)
= fib(3) + fib(2)
= (fib(2) + fib(1)) + (fib(1) + fib(0))
```

While elegant, this version is extremely slow for large n due to repeated calculations.

---

## 4.3 Sum of a List

```python
def list_sum(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + list_sum(nums[1:])
```

Call example:

```
list_sum([5, 2, 7])
→ 5 + list_sum([2, 7])
→ 5 + 2 + list_sum([7])
→ 5 + 2 + 7 + list_sum([])
→ 14
```

---

# 5. Recursion vs Iteration (10 min)

Both recursion and loops can solve repetitive problems.

### Iterative Factorial

```python
def fact_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

### Recursive Factorial

```python
def fact_rec(n):
    if n == 0:
        return 1
    return n * fact_rec(n - 1)
```

### Key Differences

* Recursion uses function calls; iteration uses loops.
* Recursion is elegant but can be slower.
* Recursion can cause stack overflows for deep calls.
* Some problems are naturally recursive (trees, nested data).

---

# 6. Common Recursion Errors (5 min)

## 6.1 Missing Base Case

```python
def bad(n):
    return bad(n - 1)
```

This runs until Python crashes.

---

## 6.2 Base Case Doesn’t Reduce the Problem

```python
def bad2(n):
    if n == 0:
        return 0
    return bad2(n)
```

This never moves toward the base case.

---

## 6.3 Wrong Return Value

```python
def wrong(n):
    if n == 0:
        return 1
    wrong(n - 1)      # missing return
```

This results in returning `None`.

---

# 7. Tracing Practice (10 min)

Trace the following by hand:

```python
def f(n):
    if n <= 1:
        return 1
    return n * f(n - 2)
```

Evaluate:

```
f(5)
f(4)
f(3)
```

````markdown
# 8. Practice Problems

Try these recursion problems on your own. Trace them carefully, identify the base case,
and determine the recursive pattern.

---

## Problem 1: Count Digits

Write a recursive function that counts how many digits are in an integer.

```python
def count_digits(n):
    ...
````

Examples:

```
count_digits(7)      → 1
count_digits(42)     → 2
count_digits(12345)  → 5
```

---

## Problem 2: Reverse a String

Write a recursive function to reverse a string.

```python
def reverse(s):
    ...
```

Example:

```
reverse("cat")  → "tac"
```

---

## Problem 3: Power Function

Implement:

```
power(a, b) = a^b
```

Using recursion only (no `**` or loops).

```python
def power(a, b):
    ...
```

---

## Problem 4: Product of List

Compute the product of all items in a list using recursion.

```python
def product(nums):
    ...
```

Example:

```
product([2, 3, 4]) → 24
```

---

## Problem 5: Check Palindrome

Write:

```python
def is_palindrome(s):
    ...
```

A recursive function that returns True if a string is a palindrome.

Examples:

```
is_palindrome("racecar") → True
is_palindrome("python")  → False
```

---

# 9. Challenge Problems (Optional)

These problems push you to apply recursion creatively.

---

## Challenge 1: Sum of Nested Lists

A nested list may contain integers or other lists:

```
[1, [2, 3], [[4], 5]]
```

Write a recursive function that sums all integers regardless of depth.

```python
def nested_sum(data):
    ...
```

---

## Challenge 2: Flatten a Nested List

Example:

```
flatten([1, [2, 3], [4, [5]]]) → [1, 2, 3, 4, 5]
```

Write:

```python
def flatten(data):
    ...
```

---

## Challenge 3: Path Count in a Grid

Count how many ways to move from top-left to bottom-right in a grid
(moving only down or right), using recursion.

Example for 2×2 grid:

```
paths(2, 2) → 2
```

---

# 10. Reflection Questions

1. Why is a base case required in every recursive function?
2. What happens if the recursive call does not make progress toward the base case?
3. When might recursion be more appropriate than iteration?
4. Why can recursion be slower than loops?
5. How does the call stack relate to recursion?

---

# 11. Summary

In this lesson, you learned:

* The definition and structure of recursion
* The importance of base cases
* How recursive calls use the call stack
* Classic examples like factorial, Fibonacci, and list processing
* How to compare recursion vs iteration
* How to avoid common recursion errors

Recursion is a foundational programming concept that appears in algorithms, data
structures, and many real-world problems. Understanding how recursive functions work will
help you approach complex problems more systematically.


```


