Lesson 19: Testing & Debugging  
 
Owner: Rushikesh Shirsat  
 
 
Introduction to Software Testing  
 
1.1 What is Software Testing?  
Software Testing  is a process of verifying that a software application works as expected 
and meets the user’s requirements. It helps identify bugs, errors, and performance issues  
before the software is released.  
Why Testing is Important  
• Ensures quality and reliability  of software.    
• Detects defects early , saving time and cost.    
• Improves security, performance , and user satisfaction .   
• Prevents system failures  after deployment.    
 
1.2 Key Testing Terminologies  
Term  Meaning  
Bug/Defect  A flaw that causes software to behave unexpectedly.  
Error  A human mistake that introduces a defect.  
Test Case  A set of conditions or inputs to check a specific feature.  
Test Plan  A document that outlines scope, approach, and schedule of testing.  
Expected Output  The correct result we anticipate.  
Actual Output  The real result produced during the test.

1.3 Goals of Software Testing  
• Verification : Are we building the product right?    
• Validation : Are we building the right product?    
• Defect Detection : Finding issues before deployment.    
• Quality Assurance : Ensuring the product meets standards.  
 
 
2 Levels of Testing  
Level  Focus  Example  
Unit Testing  Testing individual functions or 
modules.  Function add(a, b)  
Integration Testing  Testing the interaction between 
modules.  user_login()  calling 
db_connect()  
System Testing  Testing the whole application end -to-
end.  Full web app test  
Acceptance 
Testing  Validating with client requirements.  UAT before deployment  
2.1 Unit Testing  
 
Goal: Verify that individual parts  (functions, methods) work as expected.  
Tool: unittest or pytest  
Example:  
# math_utils.py  
def multiply(a, b):     
  return a * b  
Test:  
# test_math_utils.py

import unittest  
from math_utils import multiply  
 
class TestMathUtils(unittest.TestCase):  
    def test_multiply(self):  
        self.assertEqual(multiply(3, 4), 12)  
        self.assertNotEqual(multiply(2, 2), 5)  
 
if __name__ == "__main__":  
    unittest.main()  
 
Output  
. 
----------------------------------------------------------------------  
Ran 1 test in 0.000s  
OK 
 
2.2 Integration Testing  
Goal: Verify that different modules work together correctly.  
 
Example:  
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
 
 
Test:  
import unittest  
from user_module import login_user  
 
class TestIntegration(unittest.TestCase):  
    def test_login(self):  
        result = login_user("admin", "1234")  
        self.assertEqual(result, "Login Success")  
 
if __name__ == "__main__":  
    unittest.main()  
 
 
 
 
2.3 System Testing  
Goal: Validate the entire system as a whole (end -to-end functionality).

Often done using automation tools  (e.g., Selenium for web apps).  
Example  
import unittest  
from user_module import login_user  
 
class TestIntegration(unittest.TestCase):  
    def test_login(self):  
        result = login_user("admin", "1234")  
        self.assertEqual(result, "Login Success")  
 
if __name__ == "__main__":  
    unittest.main()  
 
 
 
Output:  
System test passed!  
 
 
2.4 Acceptance Testing  
Goal: Confirm the system meets the client’s or stakeholder’s requirements.  
Performed at the end by end-users or clients . 
Example:  
Client Requirement: “When I input 2 and 3, I should get 5.”  
def add(a, b):  
    return a + b

def acceptance_test():  
    assert add(2, 3) == 5, "Requirement not met"  
    print("Acceptance Test Passed!")  
 
acceptance_test()  
Output:  
Acceptance Test Passed!  
 
 
 
Lesson 3: Types of Testing  
There are two broad categories:  
• Functional Testing    
• Non-functional Testing    
 
3.1 Functional Testing  
Verifies that each function of the software works in accordance with the requirement.  
Examples:  
• Unit Testing  
• Integration Testing  
• Regression Testing  
• User Acceptance Testing  
• Smoke Testing  
Example: Regression Testing  
# Suppose we updated the add function

def add(a, b):  
    return a + b + 0  # minor refactor  
 
# Old test must still pass  
def test_regression():  
    assert add(2, 3) == 5  
 
test_regression()  
print("Regression test passed!")  
 
NOTE : Ensures new changes didn’t break old features.  
 
3.2 Non-Functional Testing  
Tests the performance, scalability, usability, reliability , etc.  
Examples:  
• Performance Testing (Speed, Response time)  
• Load Testing (Under heavy usage)  
• Stress Testing (Breaking point)  
• Security Testing  
• Usability Testing  
Example (Performance check):  
 
import time  
 
def big_task():  
    time.sleep(1)  # simulate delay

return "Done"  
 
start = time.time()  
result = big_task()  
end = time.time()  
 
assert (end - start) < 2  
print("Performance Test Passed!")  
 
 
3.3 Exploratory and Ad -hoc Testing  
• Exploratory:  Tester explores the system freely without predefined test cases.    
• Ad-hoc: Informal testing to discover issues quickly.    
Example:  
“Let’s try what happens if I enter a negative number or a string.”  
 
 
4: Automation Testing  
4.1 Why Automate?  
• Saves time for repetitive tests.  
• Improves accuracy.  
• Enables CI/CD integration.  
• Faster feedback for developers.  
 
4.2 Automated Testing Tools

Tool  Language  Use Case  
unittest  Python  Built-in testing framework  
pytest  Python  Simple, readable test writing  
Selenium  Python/Java  Web UI automation  
Jenkins  Any  Continuous Integration server  
 
4.3 Example: Pytest  
# calculator.py  
def add(a, b):  
    return a + b  
 
# test_calculator.py  
from calculator import add  
 
def test_add():  
    assert add(2, 3) == 5  
    assert add( -1, 1) == 0  
Run Command  
pytest test_calculator.py  
 
Output  
============================== test session starts 
==============================  
collected 1 item  
test_calculator.py .                                                  [100%]

=============================== 1 passed in 0.01s 
===============================  
 
 
 
5: Writing and Managing Test Cases  
 
5.1 Test Case Template  
Field  Description  
Test ID  Unique identifier (e.g., TC_01)  
Test Description  What the test is validating  
Input Data  Test inputs  
Expected Result  What should happen  
Actual Result  What happened  
Status  Pass/Fail  
5.2 Example  
Test ID  Description  Input  Expected Output  Actual Output  Result  
TC_01  Add positive numbers  (2,3)  5 5 Pass  
TC_02  Add negative numbers  (-1,-1) -2 -2 Pass  
Practice Quiz 1  
1. What is the main goal of software testing?  
2. Define “defect” and “test case.”  
3. Why is expected vs actual output important?  
4. What could happen if we skip testing?  
5. What is regression?

MCQs  
1. Software testing ensures:  
A. Performance only  
B. Code compilation only  
C. Software works as expected  
D. System design  
➤ Answer: C   
1. A test case includes:  
A. Input and expected output  
B. Source code only  
C. Documentation only  
D. UI design  
➤ Answer: A 
 
Practice Quiz 2  
1. What is the focus of unit testing?  
2. What do we test during integration testing?  
3. Which testing level involves the whole system?  
4. Who performs acceptance testing?  
5. Why should testing be layered (unit → system → acceptance)?  
 
MCQs  
1. Unit testing verifies:  
A. Database connections  
B. Entire system behavior  
C. Individual functions or classes

D. User interface  
➤ Answer: C   
1. Integration testing ensures:  
A. Code style  
B. Module interactions  
C. Syntax checking  
D. User experience  
➤ Answer: B 
 
Practice Quiz 3  
1. Differentiate functional and non -functional testing.  
2. What is regression testing used for?  
3. Give an example of performance testing.  
4. What is exploratory testing?  
5. What does load testing measure?  
 
MCQs  
1. Non-functional testing includes:  
A. Integration Testing  
B. Unit Testing  
C. Load Testing  
D. Acceptance Testing  
➤ Answer: C   
1. Regression testing is done to:  
A. Find new bugs  
B. Ensure old features work after changes

C. Optimize UI  
D. Speed up performance  
➤ Answer: B 
 
Practice Quiz 4  
1. Why use automation testing?  
2. Name two Python testing frameworks.  
3. What does pytest do when a test fails?  
4. What is the command to run pytest?  
5. Which type of testing is best automated?  
 
MCQs  
1. Automation testing helps:  
A. Reduce human error  
B. Slow down testing  
C. Replace debugging  
D. Skip CI/CD  
➤ Answer: A   
1. Which tool is used for web testing?  
A. pytest  
B. Selenium  
C. unittest  
D. coverage  
➤ Answer: B 
 
Practice Quiz 5

1. What is a test case?  
2. What information should it contain?  
3. What is the role of a test ID?  
4. What do you do if a test fails?  
5. What is the difference between expected and actual output?  
 
Test cases should be:  
A. Random  
B. Repeatable and clear  
C. Unstructured  
D. Unplanned  
➤ Answer: B 
 
 
DEBUGGING TECHNIQUES  
 
Learning Objectives  
After completing this chapter, you will be able to:  
• Understand what debugging is and why it’s necessary.  
• Identify types of errors in code (syntax, runtime, logic).  
• Use different debugging methods like print statements, logging, and IDE tools.  
• Handle exceptions effectively using try-except blocks.    
• Use Python’s built -in debugger ( pdb).   
• Apply systematic strategies to locate and fix bugs efficiently.  
 
Lesson 1: Introduction to Debugging

1.1 What is Debugging?  
Debugging  is the process of detecting, analyzing, and fixing bugs (errors or unexpected 
behaviors) in a program.  
A “bug” is any flaw or defect in the code that causes the program to behave incorrectly or 
crash.  
 
1.2 Common Types of Errors  
Error Type  Description  Example  
Syntax 
Error  Occurs when code violates the grammar rules 
of Python.  print "Hello"   (missing 
parentheses)  
Runtime 
Error  Happens while the program is running, usually 
due to invalid operations.  10 / 0 (ZeroDivisionError)  
Logical 
Error  The program runs but produces incorrect 
output.  area = 2 * 3.14 * r  instead of 
3.14 * r * r  
 
1.3 Debugging vs Testing  
Aspect  Testing  Debugging  
Purpose  Detect the presence of 
bugs.  Identify and fix the cause of bugs.  
Who performs  QA/Test Engineer  Developer  
When 
performed  After code implementation  During or after testing  
Example  Test fails due to incorrect 
output  Finding and correcting the logic that caused 
the failure  
Example  
def divide(a, b):  
    return a / b

# This will cause a runtime error  
print(divide(10, 0))  
Error:  
ZeroDivisionError: division by zero  
 
 
Debugging Process and Strategy  
 
2.1 Debugging Steps  
1. Identify the bug  – Observe unexpected behavior or failed test.    
2. Reproduce the bug  – Run the code consistently to see the same error.    
3. Diagnose the cause  – Trace code logic, use print or logging.    
4. Fix the issue  – Modify and retest the code.    
5. Verify the fix  – Re-run all tests to ensure stability.  
 
2.2 Example Process  
Let’s say the code returns wrong total marks:  
def total_marks(a, b, c):  
    return a + b - c  # Logical error  
 
print(total_marks(80, 90, 70))  # Expected 240, gets 100  
Fix:  
def total_marks(a, b, c):  
    return a + b + c

print(total_marks(80, 90, 70))  # Output: 240  
 
Tools for Debugging  
Tool  Description  
Print statements  Simple way to trace variable values.  
Logging  Tracks program flow using logging module.  
IDE Debugger  Built-in debugger in tools like VSCode, PyCharm.  
Python Debugger (pdb)  Command -line debugging tool.  
Assertions  Automatically check assumptions in code.  
 
 
3: Print Debugging  
3.1 What is Print Debugging?  
Print debugging involves adding print() statements in your code to track variable values and 
execution flow.  
Advantages:  
• Simple and quick for small programs.  
• Doesn’t require setup.  
Disadvantages:  
• Clutters code for large projects.  
• Must be removed later.  
 
3.2 Example:  
def average(nums):  
    print("DEBUG: nums =", nums)  
    total = sum(nums)

print("DEBUG: total =", total)  
    avg = total / len(nums)  
    print("DEBUG: avg =", avg)  
    return avg  
 
print(average([2, 4, 6]))  
Output:  
DEBUG: nums = [2, 4, 6]  
DEBUG: total = 12  
DEBUG: avg = 4.0  
4.0 
 
 
 
Logging for Debugging  
4.1 What is Logging?  
Logging records events that happen while the program runs — helpful for debugging and 
monitoring without printing to the console.  
 
4.2 Example:  
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
DEBUG:root:Inputs: a=10, b=2  
INFO:root:Result: 5.0  
DEBUG:root:Inputs: a=10, b=0  
ERROR:root:Division by zero!  
Benefits of Logging  
• Keeps a record of errors over time.  
• Helps analyze production issues.  
• Levels like DEBUG, INFO, WARNING, ERROR, CRITICAL.  
 
Using a Debugger (pdb)  
What is pdb?  
pdb (Python Debugger) lets you pause program execution  and inspect variables, line -by-
line.  
5.2 Example:  
 
def calc_sum(a, b):  
    return a + b

import pdb  
pdb.set_trace()  # Sets a breakpoint  
x = 5  
y = 10  
result = calc_sum(x, y)  
print(result)  
When you run it, you’ll enter interactive mode:  
> <stdin>(6)<module>()  
(Pdb)  
Command  Action  
n Go to next line  
s Step into function  
c Continue execution  
p <var>  Print variable value  
q Quit debugging  
Example Output  
(Pdb) p x  
5 
(Pdb) n  
(Pdb) p y  
10 
(Pdb) c  
15

Exception Handling and Assertions  
6.1 Exception Handling  
try: 
    x = int(input("Enter a number: "))  
    print(10 / x)  
except ZeroDivisionError:  
    print("Cannot divide by zero.")  
except ValueError:  
    print("Invalid input. Please enter a number.")  
finally:  
    print("Execution completed.")  
Output  
Enter a number: 0  
Cannot divide by zero.  
Execution completed.  
 
Using Assertions  
Assertions are used to check for conditions that must be true.  
def square_root(x):  
    assert x >= 0, "x must be non -negative"  
    return x ** 0.5  
 
print(square_root(9))  
print(square_root( -1))  # AssertionError

Real-World Debugging Practices  
7.1 Common Debugging Tips  
Reproduce bugs consistently.  
Isolate problematic sections of code.  
Use version control (Git) to revert if needed.  
Keep logs for long -term analysis.  
Add assertions in critical code paths.  
Don’t ignore minor warnings —they often lead to bigger issues.  
 
7.2 Real Example: Debugging a Function  
def calculate_discount(price, discount):  
    final_price = price - discount * price  
    return final_price  
 
print(calculate_discount(100, 0.1))  # Expected 90, got 90  
print(calculate_discount(100, 10))   # Expected 90, got -900  
 
FIX 
def calculate_discount(price, discount_percent):  
    if discount_percent > 1:  
        discount_percent = discount_percent / 100  
    return price - (discount_percent * price)  
 
 
Output  
90.0

90.0  
 
 
PRACTICE TESTS  
Practice Quiz 1  
1. What is debugging?  
2. Define syntax, runtime, and logical errors.  
3. Who performs debugging?  
4. What is the difference between testing and debugging?  
5. What kind of error happens when dividing by zero?  
 
  MCQs  
1. Which error occurs when Python cannot understand your code syntax?  
A. Logical Error  
B. Runtime Error  
C. Syntax Error  
D. Exception  
➤ Answer: C   
1. Debugging is mainly done by:  
A. Testers  
B. Developers  
C. Users  
D. Designers  
➤ Answer: B 
 
Practice Quiz 2

1. List the 5 debugging steps.  
2. What tool can you use to trace program execution?  
3. Why should you reproduce a bug?  
4. What is the difference between print and logging?  
5. What is the purpose of assertions?  
 
  MCQs  
1. The first step in debugging is:  
A. Fix the bug  
B. Verify the fix  
C. Identify and reproduce the bug  
D. Write test cases  
➤ Answer: C   
1. Which of the following can be used for command -line debugging?  
A. pytest  
B. pdb  
C. pylint  
D. coverage  
➤ Answer: B 
 
Practice Quiz 3  
1. What is print debugging used for?  
2. When should you remove print statements?  
3. What can you print to find logic errors?  
4. What is one advantage of print debugging?  
5. What is one disadvantage?

MCQs  
1. Print debugging is best suited for:  
A. Large-scale projects  
B. Web applications  
C. Small scripts  
D. Automated pipelines  
➤ Answer: C   
1. Print statements should be removed after debugging because:  
A. They make code run faster  
B. They slow down compilation  
C. They clutter logs and output  
D. They cause runtime errors  
➤ Answer: C 
 
Practice Quiz 4  
1. What is the main purpose of logging?  
2. What are the five main log levels?  
3. How does logging differ from print?  
4. What happens when a division by zero occurs in the above example?  
5. Why use different logging levels?  
 
MCQs  
1. Which of these is a log level?  
A. NOTICE  
B. WARNING

C. TRACE  
D. ALERT  
➤ Answer: B   
1. Logging is preferred over print because:  
A. It’s faster  
B. It provides configurable severity levels  
C. It can’t handle errors  
D. It’s shorter to write  
➤ Answer: B 
 
Practice Quiz 5  
1. What is pdb used for?  
2. Which command continues execution?  
3. What does p <var> do?    
4. What happens when you call pdb.set_trace() ?   
5. What command exits the debugger?  
 
MCQs  
1. Which command in pdb steps into a function call?  
A. c  
B. s  
C. n  
D. q  
➤ Answer: B   
1. pdb stands for:  
A. Python Debugger

B. Program Debug Bridge  
C. Print Debug Base  
D. Python Debug Base  
➤ Answer: A 
 
Practice Quiz 6  
1. What happens if an exception isn’t handled?  
2. What is the purpose of the finally block?    
3. What does an assert statement do?    
4. What error occurs when dividing by zero?  
5. Why is exception handling important?  
 
  MCQs  
1. What will the finally block do?  
A. Execute only if try succeeds  
B. Execute always  
C. Execute only if an error occurs  
D. Execute only if no except block exists  
➤ Answer: B   
1. AssertionError is raised when:  
A. An exception occurs  
B. A test case fails  
C. An assert condition evaluates to False  
D. Division by zero  
➤ Answer: C
