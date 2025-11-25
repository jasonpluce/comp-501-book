
# Lesson 18: Error Handling
Reviewer: Mujtaba - I like the contents that will be covered under this section. The only 
thing that I am not sure is that the error message handling is an advanced and complex 
concept. It would be helpful to cover this as one of the last chapters in this series. They 
need to know the concept of class, list, dictionary, and some other stuff before trying to 
come up with the errors that they might get during working with those concepts.  
Owner: Saban, Michael

- Exception handling  
- Try/except blocks  
- Common errors  

Reviewer: Jason for Saban, Michael  
Per the Guidelines for Content the following items are missing:  
Overview & Introduction  
Prerequisites  
Summary  
Next steps  
Everything else looks fine.

## Learning Objectives

- Define "exception" and describe the difference between syntax and runtime errors.  
- Predict and interpret traceback messages in Python.  
- Use try/except/else/finally to catch and respond to errors.  
- Raise exceptions with `raise ValueError()` and handle multiple exception types.  
- Debug basic file handling and data conversion errors safely.

## Lesson Outline

### Warm-up (5 min)

```python
x = int(input("Enter a number: "))
print(10 / x)
````

* What happens if you type `"zero"` or `"0"`? Let's look at some error outputs

### Type of errors (10 min)

| Category      | Example             | Fix                                      |
| ------------- | ------------------- | ---------------------------------------- |
| Syntax Error  | `if x > 3 print(x)` | Read message and fix code before running |
| Runtime Error | `1/0`               | handle via try/except                    |
| Logic Error   | wrong output        | test inputs & print statements           |

* Have students ID error types in 3 snippets

### Basic exception handling (15 min)

```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ValueError:
    print("Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Success!")
finally:
    print("Done.")
```

* Order of except blocks matters
* `else` runs only if no error and `finally` always runs

### Hands-on demos (10 min)

#### File handling error

```python
try:
    with open("data.txt") as f:
        print(f.read())
except FileNotFoundError as e:
    print("File not found:", e)
```

#### Type error in loop

```python
nums = ["1", "2", "three"]
total = 0

for n in nums:
    try:  # Why not use if n.isdigit() instead? (prevent vs catch)
        total += int(n)
    except ValueError:
        print(f"Skipped bad value: {n}")

print("Total:", total)
```

### Guided practice (20 min)

* **Lab 1:** Write `safe_divide(a, b)` that returns `a/b` or `None` and prints a helpful
  message. Test with pairs `(4,2)`, `(5,0)`, `("x", 2)`.
* **Lab 2:** Open `numbers.txt`. Each line has one value. Sum valid ints and skip invalid
  lines using try/except. Try using `raise ValueError` if the file is empty.

### Reflection & Assessment (10 min)

* What is the difference between detecting and handling errors?
* When is it better to prevent than to catch?
* Write a try/except that opens a file and prints `"no file found"` if missing, otherwise prints its first line.

### Optional HW

* Modify Lab 2 to log errors to `error_log.txt` instead of printing them.
* Research `assert` and write 2 assertions that prevent invalid inputs.


