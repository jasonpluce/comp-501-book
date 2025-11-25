# Lesson 14: More Practice with

For Loops
Owner: Hyatt, Matt

* Nested loops
* Loop patterns
* Loop debugging

# Lesson 14: More Practice with For Loops

In this lesson, you will learn how Python decides how to execute repeated code in sequence, using loop logic and terminating conditions. We will:

* Repeat work with `for` loops and `range()`.
* Control loops using `break`, `continue`, and `else`.
* Use `pass` as a placeholder.
* Work with nested loops (loops inside loops).
* Recognize common loop patterns (accumulators, counters, searching, building lists).
* Develop simple strategies for loop debugging.

By the end of this lesson, you should be able to read, write, and debug basic loop-based code, and organize it into small, reusable parts.

---

# 1. The `if` Statement

We use `if`, `elif`, and `else` to make decisions in programs.

```python
x = int(input("Enter a number: "))
if x < 0:
    print("Negative changed to zero")
    x = 0
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")
```

**Key points**

* `elif` means *“else if”*.
* The `else` part is optional.
* You can have as many `elif` parts as you want.

---

# 2. The `for` Loop

A `for` loop repeats code for each item in a sequence (like a list or string).

```python
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
```

**Tip:** Don’t change the list while looping through it — loop over a *copy* if needed:

```python
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
```

---

# 3. The `range()` Function

`range()` produces a lazy, constant-memory integer sequence that the loop consumes on demand. It supports configurable `start`, `stop`, and `step` parameters, enabling precise control over numeric iteration without materializing the full list.

```python
for i in range(5):
    print(i)
# 0, 1, 2, 3, 4
```

You can also set:

* a start value → `range(5, 10)`
* a step → `range(0, 10, 2)`
* a negative step → `range(10, 0, -1)`

---

# 4. `break` and `continue`

* `break` stops a loop early.
* `continue` skips the rest of the current loop and moves to the next.

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            break  # stop checking this n
```

```python
for num in range(2, 10):
    if num % 2 == 0:
        continue  # skip even numbers
    print(num)
```

---

# 5. `else` with Loops

The `else` block is executed only if the loop terminates without a `break`, making it a post-condition hook tied to the loop’s control flow. This is useful for algorithms where “exhausting the loop” signals success — such as primality testing, search routines, or validation passes.

```
1 for n in range(2, 10):
2     for x in range(2, n):
3         if n % x == 0:
4             break          # abnormal termination of inner loop
5     else:
6         print(n, "is a prime number")  # runs only if no divisor triggered break
```

---

# 6. `pass`

A do-nothing placeholder. It acts as a syntactic stand-in when Python requires a statement but you don’t want any runtime behavior. `pass` generates no bytecode effect beyond occupying the spot where a statement must legally appear.

```
1 if condition_met:
2     pass  # do nothing (for now)
```

**Useful for:**

* Empty class or function definitions where the body cannot be blank
* Stubbing out branches, handlers, or TODO sections during incremental development

---

# 7. Nested Loops

A nested loop is a loop inside another loop.
You use them when you need to repeat work in multiple levels — for example, looping through rows and columns of a grid.

```
1 for i in range(3):     # outer loop
2     for j in range(2): # inner loop
3         print(i, j)
```

**Output**

```
Python
Python
```

**Key points**

* The inner loop runs completely every time the outer loop runs once.
* Total iterations = outer × inner.
* Good for working with 2D lists, tables, or coordinate pairs.

---

# 8. Loop Patterns

Some software patterns show up often when using loops:

### a. Accumulator Pattern

Add up or collect values as you go.

### b. Counter Pattern

Count how many items match a condition.

### c. Searching Pattern

Look for an element that meets a condition.

### d. Building Lists

Create a new list using results from a loop.

**Tip:** These same patterns can be written compactly with list comprehensions.

---

# 8.5 BONUS — Comprehension Patterns

Python’s comprehensions provide loop-driven construction of lists, dictionaries, and sets in a single expressive expression. They fuse iteration, filtering, and transformation into a compact form while avoiding the boilerplate of `.append()` or manual accumulation.

## a. List Comprehensions

Produce a list by applying an expression to each item in an iterable.

```python
squares = [n**2 for n in range(5)]
```

**Common patterns:**

* Mapping / transformation:

  ```python
  lengths = [len(w) for w in words]
  ```
* Filtering:

  ```python
  evens = [n for n in nums if n % 2 == 0]
  ```
* Flattening nested loops:

  ```python
  pairs = [(i, j) for i in A for j in B]
  ```

## b. Dictionary Comprehensions

Construct a dictionary by computing keys and values from an iterable.

```python
square_map = {n: n**2 for n in range(5)}
```

**Common patterns:**

* Inversion:

  ```python
  inv = {v: k for k, v in d.items()}
  ```
* Filtering entries:

  ```python
  filtered = {k: v for k, v in d.items() if v > 0}
  ```
* Transforming values:

  ```python
  scaled = {k: v * 0.1 for k, v in metrics.items()}
  ```

## c. Set Comprehensions

Build a set by evaluating an expression, automatically deduplicating results.

```python
unique_lengths = {len(w) for w in words}
```

**Common patterns:**

* Extract distinct attributes:

  ```python
  first_letters = {w[0] for w in words}
  ```
* Filtered membership:

  ```python
  positives = {n for n in nums if n > 0}
  ```
* Projection from structured data:

  ```python
  ids = {record.id for record in records}
  ```

**Tip:**
Comprehensions mirror the same patterns as manual loops — accumulation, transformation, filtering, search — but compress them into a single expression and often run faster.

---

# 9. Loop Debugging

Debugging loops is about figuring out why they run too many or too few times, or produce wrong results.

**Common issues**

1. Off-by-one errors — wrong range boundaries.

---



