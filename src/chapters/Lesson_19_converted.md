
# Lesson 19: Testing & Debugging
Owner: Rushikesh Shirsat

## Introduction to Software Testing

### 1.1 What is Software Testing?
Software Testing is a process of verifying that a software application works as expected  
and meets the user’s requirements. It helps identify bugs, errors, and performance issues  
before the software is released.

### Why Testing is Important
- Ensures quality and reliability of software.
- Detects defects early, saving time and cost.
- Improves security, performance, and user satisfaction.
- Prevents system failures after deployment.

### 1.2 Key Testing Terminologies

| Term           | Meaning                                      |
|----------------|----------------------------------------------|
| Bug/Defect     | A flaw that causes software to behave unexpectedly. |
| Error          | A human mistake that introduces a defect.     |
| Test Case      | A set of conditions or inputs to check a specific feature. |
| Test Plan      | A document that outlines scope, approach, and schedule of testing. |
| Expected Output | The correct result we anticipate.            |
| Actual Output  | The real result produced during the test.     |

### 1.3 Goals of Software Testing
- Verification: Are we building the product right?
- Validation: Are we building the right product?
- Defect Detection: Finding issues before deployment.
- Quality Assurance: Ensuring the product meets standards.

---

# 2 Levels of Testing

| Level               | Focus                               | Example                     |
|--------------------|--------------------------------------|-----------------------------|
| Unit Testing        | Testing individual functions or modules. | Function add(a, b)          |
| Integration Testing | Testing the interaction between modules. | user_login() calling db_connect() |
| System Testing      | Testing the whole application end-to-end. | Full web app test           |
| Acceptance Testing  | Validating with client requirements. | UAT before deployment       |

## 2.1 Unit Testing

Goal: Verify that individual parts (functions, methods) work as expected.  
Tool: unittest or pytest

### Example:

```python
# math_utils.py
def multiply(a, b): 
    return a * b
````

### Test:

```python
# test_math_utils.py
import unittest
from math_utils import multiply

class TestMathUtils(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertNotEqual(multiply(2, 2), 5)

if __name__ == "__main__":
    unittest.main()
```

Output:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
OK
```

## 2.2 Integration Testing

Goal: Verify that different modules work together correctly.

```python
# db_module.py
def connect_db():
    return True

# user_module.py
from db_module import connect_db

def login_user(username, password):
    if connect_db() and username == "admin" and password == "1234":
        return "Login Success"
    else:
        return "Login Failed"
```

### Test:

```python
import unittest
from user_module import login_user

class TestIntegration(unittest.TestCase):
    def test_login(self):
        result = login_user("admin", "1234")
        self.assertEqual(result, "Login Success")

if __name__ == "__main__":
    unittest.main()
```

## 2.3 System Testing

Goal: Validate the entire system as a whole (end-to-end functionality).
Often done using automation tools (e.g., Selenium for web apps).

Example:

```python
import unittest
from user_module import login_user

class TestIntegration(unittest.TestCase):
    def test_login(self):
        result = login_user("admin", "1234")
        self.assertEqual(result, "Login Success")

if __name__ == "__main__":
    unittest.main()
```

Output:

```
System test passed!
```

## 2.4 Acceptance Testing

Goal: Confirm the system meets the client’s or stakeholder’s requirements.

Example:

```python
def add(a, b):
    return a + b

def acceptance_test():
    assert add(2, 3) == 5, "Requirement not met"
    print("Acceptance Test Passed!")

acceptance_test()
```

Output:

```
Acceptance Test Passed!
```

---

# Lesson 3: Types of Testing

There are two broad categories:

* Functional Testing
* Non-functional Testing

## 3.1 Functional Testing

Examples:

* Unit Testing
* Integration Testing
* Regression Testing
* User Acceptance Testing
* Smoke Testing

### Example: Regression Testing

```python
def add(a, b):
    return a + b + 0  # minor refactor

def test_regression():
    assert add(2, 3) == 5

test_regression()
print("Regression test passed!")
```

NOTE: Ensures new changes didn’t break old features.

## 3.2 Non-Functional Testing

Examples:

* Performance Testing
* Load Testing
* Stress Testing
* Security Testing
* Usability Testing

### Example (Performance check):

```python
import time

def big_task():
    time.sleep(1)
    return "Done"

start = time.time()
result = big_task()
end = time.time()

assert (end - start) < 2
print("Performance Test Passed!")
```

## 3.3 Exploratory and Ad-hoc Testing

* Exploratory: Explore the system freely.
* Ad-hoc: Informal testing to discover issues quickly.

---

# 4 Automation Testing

## 4.1 Why Automate?

* Saves time for repetitive tests.
* Improves accuracy.
* Enables CI/CD integration.
* Faster feedback for developers.

## 4.2 Automated Testing Tools

| Tool     | Language    | Use Case            |
| -------- | ----------- | ------------------- |
| unittest | Python      | Built-in testing    |
| pytest   | Python      | Simple test writing |
| Selenium | Python/Java | Web UI automation   |
| Jenkins  | Any         | CI server           |

## 4.3 Example: Pytest

```python
# calculator.py
def add(a, b):
    return a + b
```

```python
# test_calculator.py
from calculator import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

Run Command:

```
pytest test_calculator.py
```

Output:

```
============================== test session starts ==============================
collected 1 item
test_calculator.py . [100%]
=============================== 1 passed in 0.01s ===============================
```

---

# 5 Writing and Managing Test Cases

## 5.1 Test Case Template

| Field            | Description                 |
| ---------------- | --------------------------- |
| Test ID          | Unique identifier           |
| Test Description | What the test is validating |
| Input Data       | Test inputs                 |
| Expected Result  | What should happen          |
| Actual Result    | What happened               |
| Status           | Pass/Fail                   |

## 5.2 Example

| Test ID | Description          | Input   | Expected Output | Actual Output | Result |
| ------- | -------------------- | ------- | --------------- | ------------- | ------ |
| TC_01   | Add positive numbers | (2,3)   | 5               | 5             | Pass   |
| TC_02   | Add negative numbers | (-1,-1) | -2              | -2            | Pass   |

---

# Practice Quiz 1

1. What is the main goal of software testing?
2. Define “defect” and “test case.”
3. Why is expected vs actual output important?
4. What could happen if we skip testing?
5. What is regression?

## MCQs

1. Software testing ensures:
   A. Performance only
   B. Code compilation only
   C. Software works as expected
   D. System design
   ➤ **Answer: C**

2. A test case includes:
   A. Input and expected output
   B. Source code only
   C. Documentation only
   D. UI design
   ➤ **Answer: A**

---

# Practice Quiz 2

1. What is the focus of unit testing?
2. What do we test during integration testing?
3. Which testing level involves the whole system?
4. Who performs acceptance testing?
5. Why should testing be layered?

## MCQs

Unit testing verifies:
A. Database connections
B. Entire system behavior
C. Individual functions or classes
D. User interface
➤ **Answer: C**

Integration testing ensures:
A. Code style
B. Module interactions
C. Syntax checking
D. User experience
➤ **Answer: B**

---

# Practice Quiz 3

1. Differentiate functional and non-functional testing.
2. What is regression testing used for?
3. Give an example of performance testing.
4. What is exploratory testing?
5. What does load testing measure?

## MCQs

Non-functional testing includes:
A. Integration Testing
B. Unit Testing
C. Load Testing
D. Acceptance Testing
➤ **Answer: C**

Regression testing is done to:
A. Find new bugs
B. Ensure old features work after changes
C. Optimize UI
D. Speed up performance
➤ **Answer: B**

---

# Practice Quiz 4

1. Why use automation testing?
2. Name two Python testing frameworks.
3. What does pytest do when a test fails?
4. What is the command to run pytest?
5. Which type of testing is best automated?

## MCQs

Automation testing helps:
A. Reduce human error
B. Slow down testing
C. Replace debugging
D. Skip CI/CD
➤ **Answer: A**

Which tool is used for web testing?
A. pytest
B. Selenium
C. unittest
D. coverage
➤ **Answer: B**

---

# Practice Quiz 5

1. What is a test case?
2. What information should it contain?
3. What is the role of a test ID?
4. What do you do if a test fails?
5. Difference between expected and actual output?

Test cases should be:
A. Random
B. Repeatable and clear
C. Unstructured
D. Unplanned
➤ **Answer: B**

---

# DEBUGGING TECHNIQUES

## Learning Objectives

* Understand what debugging is and why it’s necessary.
* Identify types of errors in code.
* Use debugging methods: print, logging, IDE tools.
* Handle exceptions using try-except.
* Use Python’s debugger (pdb).
* Apply systematic strategies to locate bugs.

---

# Lesson 1: Introduction to Debugging

## 1.1 What is Debugging?

Debugging is the process of detecting, analyzing, and fixing bugs.

## 1.2 Common Types of Errors

| Error Type    | Description                                | Example            |
| ------------- | ------------------------------------------ | ------------------ |
| Syntax Error  | Violates Python grammar rules              | `print "Hello"`    |
| Runtime Error | Happens during execution                   | `10 / 0`           |
| Logical Error | Program runs but produces incorrect output | wrong area formula |

## 1.3 Debugging vs Testing

| Aspect       | Testing                 | Debugging                    |
| ------------ | ----------------------- | ---------------------------- |
| Purpose      | Detect presence of bugs | Identify & fix cause of bugs |
| Who performs | QA/Test Engineer        | Developer                    |
| When         | After implementation    | During/after testing         |

### Example

```python
def divide(a, b):
    return a / b

print(divide(10, 0))
```

Error:

```
ZeroDivisionError: division by zero
```

---

# Debugging Process and Strategy

## 2.1 Debugging Steps

1. Identify the bug
2. Reproduce the bug
3. Diagnose the cause
4. Fix the issue
5. Verify the fix

## 2.2 Example Process

```python
def total_marks(a, b, c):
    return a + b - c

print(total_marks(80, 90, 70))  # Expected 240, gets 100
```

Fix:

```python
def total_marks(a, b, c):
    return a + b + c

print(total_marks(80, 90, 70))
```

---

# Tools for Debugging

| Tool             | Description              |
| ---------------- | ------------------------ |
| Print statements | Trace variables          |
| Logging          | Track program flow       |
| IDE Debugger     | Visual debugging tools   |
| pdb              | Built-in Python debugger |
| Assertions       | Check assumptions        |

---

# 3 Print Debugging

## 3.1 What is Print Debugging?

Advantages:

* Simple
* No setup

Disadvantages:

* Clutters code
* Must be removed later

## 3.2 Example

```python
def average(nums):
    print("DEBUG: nums =", nums)
    total = sum(nums)
    print("DEBUG: total =", total)
    avg = total / len(nums)
    print("DEBUG: avg =", avg)
    return avg

print(average([2, 4, 6]))
```

Output:

```
DEBUG: nums = [2, 4, 6]
DEBUG: total = 12
DEBUG: avg = 4.0
4.0
```

---

# Logging for Debugging

## 4.1 What is Logging?

Logging records events for debugging and monitoring.

## 4.2 Example:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

def divide(a, b):
    logging.debug(f"Inputs: a={a}, b={b}")
    try:
        result = a / b
        logging.info(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero!")
        return None

divide(10, 2)
divide(10, 0)
```

Output:

```
DEBUG: Inputs: a=10, b=2
INFO: Result: 5.0
DEBUG: Inputs: a=10, b=0
ERROR: Division by zero!
```

---

# Using a Debugger (pdb)

## What is pdb?

A command-line debugger.

### Example:

```python
def calc_sum(a, b):
    return a + b

import pdb
pdb.set_trace()

x = 5
y = 10
result = calc_sum(x, y)
print(result)
```

Commands:

| Command | Action         |
| ------- | -------------- |
| n       | next line      |
| s       | step into      |
| c       | continue       |
| p var   | print variable |
| q       | quit           |

---

# Exception Handling and Assertions

## 6.1 Exception Handling

```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a number.")
finally:
    print("Execution completed.")
```

## Using Assertions

```python
def square_root(x):
    assert x >= 0, "x must be non-negative"
    return x ** 0.5

print(square_root(9))
print(square_root(-1))
```

---

# Real-World Debugging Practices

## 7.1 Tips

* Reproduce bugs
* Isolate code
* Use version control
* Keep logs
* Add assertions
* Don’t ignore warnings

## 7.2 Example

```python
def calculate_discount(price, discount):
    final_price = price - discount * price
    return final_price

print(calculate_discount(100, 0.1))
print(calculate_discount(100, 10))
```

Fix:

```python
def calculate_discount(price, discount_percent):
    if discount_percent > 1:
        discount_percent = discount_percent / 100
    return price - (discount_percent * price)
```

---

# PRACTICE TESTS

# Practice Quiz 1

1. What is the main goal of software testing?
2. Define “defect” and “test case.”
3. Why is expected vs actual output important?
4. What could happen if we skip testing?
5. What is regression?

## MCQs

1. Software testing ensures:  
A. Performance only  
B. Code compilation only  
C. Software works as expected  
D. System design  
➤ Answer: C

2. A test case includes:  
A. Input and expected output  
B. Source code only  
C. Documentation only  
D. UI design  
➤ Answer: A

---

# Practice Quiz 2

1. What is the focus of unit testing?
2. What do we test during integration testing?
3. Which testing level involves the whole system?
4. Who performs acceptance testing?
5. Why should testing be layered?

## MCQs

Unit testing verifies:  
A. Database connections  
B. Entire system behavior  
C. Individual functions or classes  
D. User interface  
➤ Answer: C

Integration testing ensures:  
A. Code style  
B. Module interactions  
C. Syntax checking  
D. User experience  
➤ Answer: B

---

# Practice Quiz 3

1. Differentiate functional and non-functional testing.
2. What is regression testing used for?
3. Give an example of performance testing.
4. What is exploratory testing?
5. What does load testing measure?

## MCQs

Non-functional testing includes:  
A. Integration Testing  
B. Unit Testing  
C. Load Testing  
D. Acceptance Testing  
➤ Answer: C

Regression testing is done to:  
A. Find new bugs  
B. Ensure old features work after changes  
C. Optimize UI  
D. Speed up performance  
➤ Answer: B

---

# Practice Quiz 4

1. Why use automation testing?
2. Name two Python testing frameworks.
3. What does pytest do when a test fails?
4. What is the command to run pytest?
5. Which type of testing is best automated?

## MCQs

Automation testing helps:  
A. Reduce human error  
B. Slow down testing  
C. Replace debugging  
D. Skip CI/CD  
➤ Answer: A

Which tool is used for web testing?  
A. pytest  
B. Selenium  
C. unittest  
D. coverage  
➤ Answer: B

---

# Practice Quiz 5

1. What is a test case?
2. What information should it contain?
3. What is the role of a test ID?
4. What do you do if a test fails?
5. Difference between expected and actual output?

## MCQs

Test cases should be:  
A. Random  
B. Repeatable and clear  
C. Unstructured  
D. Unplanned  
➤ Answer: B

---

# Practice Quiz 6

1. List the 5 debugging steps.
2. What tool can you use to trace program execution?
3. Why should you reproduce a bug?
4. What is the difference between print and logging?
5. What is the purpose of assertions?

## MCQs

1. The first step in debugging is:  
A. Fix the bug  
B. Verify the fix  
C. Identify and reproduce the bug  
D. Write test cases  
➤ Answer: C

2. Which of the following can be used for command-line debugging?  
A. pytest  
B. pdb  
C. unittest  
D. logging  
➤ Answer: B

3. `finally` blocks:  
A. Run only on error  
B. Always run  
C. Never run if an error occurs  
D. Execute only if no except block exists  
➤ Answer: B

4. AssertionError is raised when:  
A. An exception occurs  
B. A test case fails  
C. An assert condition evaluates to False  
D. Division by zero  
➤ Answer: C



