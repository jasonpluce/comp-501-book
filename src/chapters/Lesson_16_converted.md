# Lesson 16: The Terminal
Owner: Nazari, Mujtaba

TODO: Cover OS return code

## Learning Objectives

By the end of this lesson, students will be able to:

1. Understand what the terminal and shell are and how they differ
2. Navigate the file system using basic command line commands
3. Run Python scripts from the terminal and understand standard input/output streams
4. Pass command line arguments to Python programs using sys.argv
5. Create professional command-line programs using the argparse module
6. Understand program exit codes and their significance

## Materials Needed

- Computer with Python installed
- Terminal/Command Prompt/PowerShell access
- Text editor or IDE (IDLE, VS Code, or similar)
- Sample Python scripts (to be created during the lesson)
- A sample text file for practice exercises

## Introduction (5 minutes)

### Connecting to Previous Learning

Throughout this course, you've been writing Python code and running it in various ways. Perhaps you've been clicking a "Run" button in IDLE, or executing code in an interactive Python shell. In Lesson 9, you worked with Tkinter to create graphical user interfaces with buttons and windows. In Lesson 15, you learned about user inputs and events within programs. Now, we're going to explore another powerful way to interact with your programs: the terminal.

The terminal might seem intimidating at first. It's a text-based interface with no graphics, no buttons to click. But don't let its appearance fool you. The terminal is one of the most powerful tools in a programmer's toolkit, and learning to use it will make you more efficient and capable as a developer.

## What Is the Terminal? What Is a Shell?

People often use the words "terminal" and "shell" interchangeably, but they actually refer to different things. Understanding this distinction will help you communicate clearly with other programmers.

### The Terminal

The Terminal (or terminal emulator) is the program that provides you with a window where you can type commands. Think of it as the frame—the actual window on your screen where text appears. On Mac, this might be the Terminal app. On Windows, it might be Command Prompt or PowerShell. On Linux, it could be GNOME Terminal, Konsole, or any number of other applications. The terminal is just the interface, the canvas where commands are displayed.

### The Shell

The Shell is the program that runs inside the terminal. It's the interpreter that reads your commands, figures out what you want to do, and tells the operating system to do it. The shell is the brain, while the terminal is just the face. Common shells include:

- bash (Bourne Again Shell)
- zsh (Z Shell)
- fish
- PowerShell
- cmd

### Analogy

Imagine you're talking to someone through a video call. The terminal is like the video calling software (Zoom, Teams, etc.)—it's the window that lets you see and hear. The shell is like the person you're talking to—it's what actually understands and responds to what you say.

## A Brief History: Why Text-Based Interfaces?

You might wonder: if we have beautiful graphical interfaces today, why do programmers still use text-based terminals? To understand this, we need to look back at computing history.

In the early days of computing (1960s–1970s), computers had no screens as we know them today. Instead, they used devices called teletypes—essentially electric typewriters connected to the computer. You would type a command on the typewriter, and the computer would type back its response. Everything was text because that was the only option available.

When the Unix operating system was developed in the 1970s at Bell Labs, it was built around a powerful philosophy: "Write programs that do one thing well and work together." This philosophy emphasized creating small, focused tools that could be combined in creative ways. Since everything was text-based, programs could easily pass their output to other programs as input, creating powerful chains of operations.

Even though we now have graphical interfaces, this text-based approach has proven so efficient and powerful that it has never been replaced. Modern programmers still use the terminal because it allows them to:

- Work faster by typing commands instead of clicking through menus
- Automate repetitive tasks by scripting commands
- Combine simple tools to solve complex problems
- Work with remote computers as easily as their local machine
- Use the same tools across different operating systems

Think of it like this: graphical interfaces are like ordering from a picture menu at a restaurant—easy and intuitive. The terminal is like speaking directly to the chef in their language—it takes more learning, but you can make exactly what you want, customize everything, and work much faster once you know the language.

## Why Programmers Prefer the Terminal

There are several compelling reasons why professional programmers often prefer terminal-based tools:

### Speed and Efficiency

Once you learn the commands, typing them is much faster than clicking through multiple menus and windows. Imagine having to rename 100 files. With a graphical interface, you'd click each file, select rename, type the new name, and repeat 99 more times. With the terminal, you could write a single command that renames all 100 files in seconds.

### Precision and Power

The terminal lets you be extremely specific about what you want your computer to do. You can perform complex operations that would be tedious or impossible with a graphical interface.

### Automation

You can save sequences of commands in files called scripts, allowing you to automate repetitive tasks. This connects directly to your Python programming: you can write Python scripts that perform tasks automatically when run from the terminal.

### Remote Work

The terminal works the same way whether you're on your laptop or connecting to a powerful computer halfway around the world. Graphical interfaces require much more bandwidth and can be slow over network connections.

### Universal Skill

While different operating systems have different graphical interfaces, terminal commands are often similar or identical across systems. Learning terminal skills once gives you tools that work almost everywhere.

# Section 1: Command Line Basics (12 minutes)

## Opening Your Terminal

Before we can use the terminal, we need to open it. The process differs slightly depending on your operating system:

### On Windows

- Press the Windows key and type "Command Prompt" or "cmd"
- Press Enter to open it
- Alternatively, you can search for "PowerShell," which is a more modern terminal
- For this course, either will work, though PowerShell is recommended

### On Mac

- Press Command + Spacebar to open Spotlight search
- Type "Terminal" and press Enter
- You can also find it in Applications > Utilities > Terminal

### On Linux

- Press Ctrl + Alt + T (on most distributions)
- Or search for "Terminal" in your applications menu

When you open your terminal, you'll see a mostly blank window with some text. This text is called the prompt, and it's the shell's way of saying "I'm ready for your command." The prompt often shows your username, your computer's name, and your current location in the file system. It typically ends with a dollar sign ($) on Mac and Linux, or a greater-than sign (>) on Windows.

Don't be alarmed by the minimal interface. This simplicity is actually a strength. There's no clutter, no distractions—just you and your computer, ready to work together.

## Understanding Your Shell

Let's find out which shell you're using. Type the following command and press Enter:

### On Mac/Linux

```

echo $SHELL

```

### On Windows PowerShell

```

$PSVersionTable.PSVersion

```

This will tell you which shell program is interpreting your commands. On Mac, you might see `/bin/bash` or `/bin/zsh`. On Windows, you'll see version information for PowerShell. Don't worry if this seems cryptic now—the important thing is that your shell is running and ready to accept commands.

## Understanding Your File System

Before we start navigating with commands, let's talk about how your computer organizes files. Your computer's files are organized in a hierarchical structure, like a tree turned upside down. At the top (or the root), you have your main drive. Branching off from there, you have folders (which programmers often call directories), and inside those folders you might have more folders and files.

Think of it like a family tree or an office building. The building (your computer) has floors (main directories), each floor has offices (subdirectories), and each office has desks and filing cabinets (files).

When you're using the terminal, you're always "in" a specific location in this file system. This is called your current working directory. It's like your current position in the office building. You might be on the third floor, in the marketing office, at the second desk from the window.

## Essential Terminal Commands

Let's learn the fundamental commands you'll use to navigate your file system. We'll explore each one in detail.

### pwd — Print Working Directory

The `pwd` command tells you where you currently are in your file system. It stands for "print working directory," which is programmer-speak for "show me my current location."

When you type `pwd` and press Enter, you'll see something like:

```

/Users/yourname/Documents

```

or on Windows:

```

C:\Users\yourname\Documents

```

This is your current path—the full address of where you are in your computer's file system. Think of it like your GPS coordinates in the digital world.

Try this: Open your terminal and type `pwd`, then press Enter. Look at the path it shows you. This is where you're starting from.

### ls (or dir on Windows) — List Contents

The `ls` command (short for "list") shows you what's in your current directory. On Windows Command Prompt, you'll use `dir` instead, though `ls` works in PowerShell.

When you type `ls` and press Enter, you'll see a list of all the files and folders in your current location. It's like opening a folder in Finder (Mac) or File Explorer (Windows), but in text form.

For example, if you're in your Documents folder, you might see:

```

homework.txt
python_projects
vacation_photos
essay.docx

```

Some items in the list are files (like `homework.txt`), and others are directories/folders (like `python_projects`). On most systems, directories are displayed in a different color or with special indicators to help you distinguish them.

Try this: After checking where you are with `pwd`, type `ls` (or `dir` on Windows) to see what's in your current location.

### cd — Change Directory

The `cd` command lets you move to a different directory. It's like walking from one room to another in our office building metaphor.

To move into a subdirectory, type:

```

cd python_projects

```

This moves you into the `python_projects` folder. If you type `pwd` now, you'll see that your current location has changed.

To move up one level (to the parent directory), use:

```

cd ..

```

The two dots (`..`) are a special symbol meaning "the directory above the current one." Think of it as taking the elevator up one floor.

To move to your home directory (your personal folder on the computer), type:

```

cd ~

```

The tilde (`~`) is a shortcut representing your home directory.

Try this:

1. Type `ls` to see available folders  
2. Use `cd foldername` to move into one  
3. Type `pwd` to confirm the move  
4. Type `cd ..` to go back up  
5. Type `pwd` again  

### mkdir — Make Directory

The `mkdir` command creates a new directory. It stands for "make directory."

To create a new folder called `terminal_practice`, type:

```

mkdir terminal_practice

```

You won't see much feedback—the shell simply returns a prompt. This is normal. In the terminal world, **no news is good news**. If something goes wrong, *then* you'll see an error.

Verify creation:

```

ls

```

### whoami — Who Am I?

This command tells you which user account you're logged in as:

```

whoami

```

Useful on shared computers or remote systems.

## Practice Activity 1: Navigation Challenge (5 minutes)

Follow these steps:

1. Use `whoami` to see your username  
2. Use `pwd` to see where you are  
3. Use `ls` to see what's in your current location  
4. Create a new directory called `lesson16_practice` using `mkdir`  
5. Use `ls` again to verify it was created  
6. Move into that folder using `cd lesson16_practice`  
7. Use `pwd` to confirm your location  
8. Create directories `scripts` and `data`  
9. Use `ls` to see both folders  
10. Move up one level using `cd ..`  
11. Use `pwd` to confirm you're back at the parent directory

# Section 2: Understanding Input and Output Streams (8 minutes)

## The Three Standard Streams

When programs run on your computer, they communicate with the outside world through three standard channels called *streams*. Understanding these streams is fundamental to working with the terminal and will help you understand how programs interact with users and other programs.

### Standard Input (stdin)

This is where a program receives input data. When you type something into a running program, it comes through stdin. Think of stdin as the program's ears—it's how the program listens to you.

### Standard Output (stdout)

This is where a program sends its normal output. When a Python program uses `print()`, the text goes to stdout. Think of stdout as the program's mouth—it's how the program talks to you.

### Standard Error (stderr)

This is where a program sends error messages and diagnostic information. Even though error messages appear on your screen like regular output, they go through a separate channel. This separation is useful because it allows you to handle errors differently from normal output. Think of stderr as the program's worried voice—it’s how the program tells you when something is wrong.

Here’s a visual way to think about it:

```

User Input → [stdin] → Your Program → [stdout] → Normal Output
↳ [stderr] → Error Messages

````

## Example: Understanding Streams in Python

Create a file named `streams_demo.py`:

```python
import sys

# Writing to standard output (the normal way)
print("This goes to stdout")

# Writing to standard output explicitly
sys.stdout.write("This also goes to stdout\n")

# Writing to standard error
sys.stderr.write("This goes to stderr\n")

# Reading from standard input
user_input = input("Type something: ")
print(f"You typed: {user_input}")
````

Running this script with:

```
python streams_demo.py
```

…produces output that appears mixed together on your screen, but each part is going through the appropriate stream under the hood.

## The echo Command

One of the simplest and most useful terminal commands is:

```
echo "Hello, World!"
```

This outputs text to stdout—similar to:

```python
print("Hello, World!")
```

Try this:

1. Type `echo "Hello from the terminal!"`

2. Create a Python script with:

   ```python
   print("Hello from Python!")
   ```

3. Run the Python script

4. Notice how both send output to the same place: your terminal

## Discussion Prompt

Why do programs separate stdout and stderr?

Consider a program processing thousands of files:

* Successful file messages go to stdout
* Errors go to stderr

How might this separation help you create an error-only log?

---

# Section 3: Running Python Scripts from the Terminal (10 minutes)

## Why Run Scripts From the Terminal?

Running scripts from the terminal provides:

* **Flexibility** — Run any script from any folder
* **Arguments** — Supply input before the script begins
* **Automation** — Schedule or chain scripts in workflows
* **Professional practice** — This is how programs run in real-world environments
* **Access to streams** — stdin, stdout, stderr

## Creating a Simple Script to Run

Create a file called `hello_terminal.py`:

```python
print("Hello from the terminal!")
print("This script is running successfully.")
print("Congratulations on running your first terminal script!")
```

Save it in your `lesson16_practice` folder.

## Running Your Script

Steps:

1. Open your terminal
2. Use `cd` to navigate to the folder containing the script
3. Type:

   ```
   python hello_terminal.py
   ```

(Or `python3` depending on your system.)

If successful, you'll see the printed messages.

## Understanding the python Command

Typing:

```
python hello_terminal.py
```

does the following:

1. The shell finds the Python interpreter
2. It tells Python to open the file
3. Python executes the code line by line
4. Output appears on stdout
5. The script ends, and control returns to the shell

## Exit Codes: Reporting Success or Failure

When a program ends, it sends back an *exit code*:

* `0` = success
* any non-zero value = failure

These codes help automate multi-step workflows.

### Example: exit_demo.py

```python
import sys

choice = input("Should this program succeed? (yes/no): ")

if choice.lower() == "yes":
    print("Success! Exiting with code 0")
    sys.exit(0)   # Success
else:
    print("Failure! Exiting with code 1")
    sys.exit(1)   # Failure
```

After running:

### On Mac/Linux:

```
echo $?
```

### On Windows PowerShell:

```
echo $LASTEXITCODE
```

## Why Exit Codes Matter

They allow scripts to:

* stop workflows on failures
* retry failed steps
* log specific error types

## A More Complex Example

Create `number_analyzer.py`:

```python
def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

def analyze_number(number):
    """Analyze a number and print information about it."""
    print(f"Analyzing the number: {number}")

    if is_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

    if number > 0:
        print(f"{number} is positive")
    elif number < 0:
        print(f"{number} is negative")
    else:
        print(f"{number} is zero")

    print(f"The square of {number} is {number ** 2}")

# Main script logic
user_input = input("Enter a number: ")
number = int(user_input)
analyze_number(number)
```

Run with:

```
python number_analyzer.py
```

Try several values:

* positive
* negative
* zero
* even
* odd

## Practice Activity: Running Scripts and Checking Exit Codes (5 minutes)

1. Create `success_test.py`:

   ```python
   import sys
   print("This script succeeds.")
   sys.exit(0)
````

2. Create `failure_test.py`:

   ```python
   import sys
   print("This script fails.")
   sys.exit(1)
   ```

3. Run both scripts:

   ```
   python success_test.py
   python failure_test.py
   ```

4. Check exit codes:

   ### Mac/Linux:

   ```
   echo $?
   ```

   ### Windows PowerShell:

   ```
   echo $LASTEXITCODE
   ```

Observe how the shell reports different values depending on the script.

---

# Section 4: Command Line Arguments with sys.argv (12 minutes)

So far, the programs you've written ask for input *after* they start running. But what if you want to give your program information *before* it starts running? This is where command line arguments come in.

## What Is sys.argv?

In Python, the `sys` module contains a list called `argv`, which stands for "argument vector." This list contains:

* the name of the Python script (index 0)
* any extra words you type after the script name (index 1 and onward)

### Example: show_arguments.py

```python
import sys

print("Command line arguments:")
print(sys.argv)

print(f"\nNumber of arguments: {len(sys.argv)}")

for i, arg in enumerate(sys.argv):
    print(f"Argument {i}: {arg}")
```

Run it:

```
python show_arguments.py hello world 123
```

Output will show:

* the script name at index 0
* `"hello"` at index 1
* `"world"` at index 2
* `"123"` at index 3

## Example #2 — greet_user.py

```python
import sys

if len(sys.argv) < 2:
    print("Error: Please provide your name")
    print("Usage: python greet_user.py YourName")
    sys.exit(1)

name = sys.argv[1]
print(f"Hello, {name}!")
print(f"Your name has {len(name)} letters.")

sys.exit(0)
```

Run:

```
python greet_user.py Alice
```

## Example #3 — simple_calculator.py

```python
import sys

if len(sys.argv) < 4:
    print("Error: Not enough arguments")
    print("Usage: python simple_calculator.py number1 operation number2")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    operation = sys.argv[2]
    num2 = float(sys.argv[3])
except ValueError:
    print("Error: The first and third arguments must be numbers")
    sys.exit(1)

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero")
        sys.exit(1)
    result = num2 / num1
else:
    print(f"Error: Unknown operation '{operation}'")
    sys.exit(1)

print(f"{num1} {operation} {num2} = {result}")
sys.exit(0)
```

Try:

```
python simple_calculator.py 10 + 5
python simple_calculator.py 8 / 0
python simple_calculator.py 7 * 3
```

## Practice Activity 2: Word Analyzer

Create a script named `word_analyzer.py` that:

1. Takes words as command line arguments
2. Prints each word
3. Prints its length
4. Prints whether it starts with a vowel
5. Prints whether it contains numbers

Example run:

```
python word_analyzer.py apple b4nana orange
```

Example output:

```
apple — length 5 — starts with a vowel — no digits
b4nana — length 6 — starts with consonant — contains digits
orange — length 6 — starts with a vowel — no digits
```

---

# Section 5: Professional Command-Line Programs with argparse (13 minutes)

While `sys.argv` works, it's limited:

* no automatic help messages
* no validation
* no formatting
* no optional/flag arguments

Python’s `argparse` module solves these problems.

## Basic Example: greet_argparse.py

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="A friendly greeting program")

    parser.add_argument("name", help="Your name")
    parser.add_argument("-n", "--number", type=int, default=1,
                        help="Number of times to greet (default: 1)")

    args = parser.parse_args()

    for _ in range(args.number):
        print(f"Hello, {args.name}!")

    return 0

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
```

Try:

```
python greet_argparse.py Alice
python greet_argparse.py Alice -n 5
python greet_argparse.py --help
```

## Complex Example: search_file.py

A professional-grade command-line tool.

```python
import argparse
import sys

def search_file(filename, keyword, case_sensitive=True, line_numbers=False):
    """Search for a keyword in a file and print matching lines."""
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                search_line = line if case_sensitive else line.lower()
                search_keyword = keyword if case_sensitive else keyword.lower()

                if search_keyword in search_line:
                    if line_numbers:
                        print(f"{line_num}: {line.rstrip()}")
                    else:
                        print(line.rstrip())
        return 0
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found", file=sys.stderr)
        return 1
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'", file=sys.stderr)
        return 1

def main():
    parser = argparse.ArgumentParser(
        description="Search for a keyword in a text file",
        epilog="Example: python search_file.py data.txt Python -i -n"
    )

    parser.add_argument("filename", help="Path to the file to search")
    parser.add_argument("keyword", help="Keyword to search for")

    parser.add_argument("-i", "--ignore-case", action="store_true",
                        help="Perform case-insensitive search")
    parser.add_argument("-n", "--line-numbers", action="store_true",
                        help="Show line numbers in output")

    args = parser.parse_args()

    exit_code = search_file(
        args.filename,
        args.keyword,
        case_sensitive=not args.ignore_case,
        line_numbers=args.line_numbers
    )

    return exit_code

if __name__ == "__main__":
    sys.exit(main())
```

Try:

```
python search_file.py story.txt dragon
python search_file.py story.txt dragon -i
python search_file.py story.txt dragon -i -n
```

Note: `story.txt` must exist.

### Continuing the Example: Exit Codes

```python
print("Success! Exiting with code 0")  
sys.exit(0)
````

```python
print("Failure! Exiting with code 1")  
sys.exit(1)
```

Each time you run the program, Python starts fresh and asks for new input.

---

# Section 4: Command Line Arguments with sys.argv (12 minutes)

So far, you've learned how to get user input using the `input()` function. But what if you want to give information to your program *at the moment you start it*?

This is where **command line arguments** come in.

Command line arguments allow you to:

* pass information to your program instantly
* automate programs without stopping for input
* write more flexible and professional code

## Understanding sys.argv

`sys.argv` is a list that Python creates automatically.

* `sys.argv[0]` — the script name
* `sys.argv[1]` — the first argument
* `sys.argv[2]` — the second argument
* and so on...

Example:

```
python show_arguments.py hello world
```

Inside Python:

```python
['show_arguments.py', 'hello', 'world']
```

Here’s a sample program to explore it:

```python
import sys

print("Command line arguments:")
print(sys.argv)

print(f"\nNumber of arguments: {len(sys.argv)}")

for i, arg in enumerate(sys.argv):
    print(f"Argument {i}: {arg}")
```

Try running:

```
python show_arguments.py hello world 123
```
Now run this script with some arguments:

```

python show_arguments.py hello world 123

```

You'll see output like:

```

Command line arguments:
['show_arguments.py', 'hello', 'world', '123']

Number of arguments: 4
Argument 0: show_arguments.py
Argument 1: hello
Argument 2: world
Argument 3: 123

````

This is powerful because it allows programs to behave differently depending on the arguments provided when started.

---

## Working with Multiple Arguments

Let's create a program that uses multiple command line arguments.

Create a file called `simple_calculator.py`:

```python
import sys

# Check if we have enough arguments
if len(sys.argv) < 4:
    print("Error: Not enough arguments")
    print("Usage: python simple_calculator.py number1 operation number2")
    print("Example: python simple_calculator.py 5 + 3")
    print("Operations: +, -, *, /")
    sys.exit(1)

# Get the arguments
try:
    num1 = float(sys.argv[1])
    operation = sys.argv[2]
    num2 = float(sys.argv[3])
except ValueError:
    print("Error: The first and third arguments must be numbers")
    sys.exit(1)
````

# Continue simple_calculator.py

# Perform the calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero")
        sys.exit(1)
    result = num2 / num1
else:
    print(f"Error: Unknown operation '{operation}'")
    sys.exit(1)

# Print the result
print(f"{num1} {operation} {num2} = {result}")

# Exit with success code
sys.exit(0)
```

### Try running:

```
python simple_calculator.py 10 + 5
python simple_calculator.py 8 / 0
python simple_calculator.py 7 * 3
```

Each call will produce a different result (or error) depending on the arguments.

---

## Practice Activity 2: Word Analyzer

Create `word_analyzer.py` that:

1. Accepts multiple words as command line arguments
2. Prints each word
3. Prints the word length
4. Prints whether it starts with a vowel
5. Prints whether it contains numbers

Example run:

```
python word_analyzer.py apple b4nana orange
```

Example output:

```
apple — length 5 — starts with a vowel — no digits
b4nana — length 6 — starts with consonant — contains digits
orange — length 6 — starts with a vowel — no digits
```

---

# Section 5: Professional Command-Line Programs with argparse (13 minutes)

Using `sys.argv` works, but it has problems:

* no automatic help
* no validation
* no formatting for arguments
* no support for optional flags
* no user-friendly error messages

The **argparse** module solves all of this.

---

## Basic Example: greet_argparse.py

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="A friendly greeting program")

    parser.add_argument("name", help="Your name")
    parser.add_argument(
        "-n", "--number",
        type=int,
        default=1,
        help="Number of times to greet (default: 1)"
    )

    args = parser.parse_args()

    for _ in range(args.number):
        print(f"Hello, {args.name}!")

    return 0

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
```

Try:

```
python greet_argparse.py Alice
python greet_argparse.py Alice -n 5
python greet_argparse.py --help
```

---

## More Advanced Example: search_file.py

```python
import argparse
import sys

def search_file(filename, keyword, case_sensitive=True, line_numbers=False):
    """Search for a keyword in a file and print matching lines."""
    try:
        with open(filename, "r") as file:
            for line_num, line in enumerate(file, start=1):
                search_line = line if case_sensitive else line.lower()
                search_keyword = keyword if case_sensitive else keyword.lower()

                if search_keyword in search_line:
                    if line_numbers:
                        print(f"{line_num}: {line.rstrip()}")
                    else:
                        print(line.rstrip())
        return 0
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found", file=sys.stderr)
        return 1
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'", file=sys.stderr)
        return 1
```

def main():
parser = argparse.ArgumentParser(
description="Search for a keyword in a text file",
epilog="Example: python search_file.py data.txt Python -i -n"
)

```
# Add positional arguments
parser.add_argument("filename", help="Path to the file to search")
parser.add_argument("keyword", help="Keyword to search for")

# Add optional arguments
parser.add_argument("-i", "--ignore-case", action="store_true",
                    help="Perform case-insensitive search")
parser.add_argument("-n", "--line-numbers", action="store_true",
                    help="Show line numbers in output")

# Parse arguments
args = parser.parse_args()

# Call the search function
exit_code = search_file(
    args.filename,
    args.keyword,
    case_sensitive=not args.ignore_case,
    line_numbers=args.line_numbers
)

return exit_code
```

if **name** == "**main**":
sys.exit(main())

This program demonstrates several important argparse features:

* We create a parser with both a description (shown at the top of the help
  message) and an epilog (shown at the bottom, useful for examples).
* We define two required positional arguments: `filename` and `keyword`.
* We define optional flag arguments using `action="store_true"`. These are
  boolean flags that are `False` by default, but become `True` if the user
  includes them. Notice they don't take a value; they are either present or
  absent.
* We parse all arguments using `parse_args()`, which automatically reads from
  `sys.argv`.
* We pass the parsed arguments into our `search_file()` function in a clean,
  readable way.
* We return an exit code that reflects success or failure, then use
  `sys.exit()` to pass that code to the shell.

You can view the help message for this program with:

```bash
python search_file.py --help
```

This will show:

* usage line
* description
* argument list
* epilog with an example

---

## Reflection and Discussion (5 minutes)

Let's take a moment to think deeply about what we've learned:

**Question 1:** We learned about three standard streams: stdin, stdout, and stderr. Why do
you think it's useful to have separate channels for regular output and error messages? Can
you think of a real-world scenario where this separation would be important?

Consider this: Imagine you're running a program that processes 10,000 files. Most files
process successfully (messages go to stdout), but some have errors (messages go to
stderr). How could you use this separation to create a log of just the errors?

**Question 2:** Think about programs you use daily (web browsers, text editors, games). Some
have graphical interfaces, others use the command line. When do you think a command
line interface is better than a graphical interface? When is a graphical interface better?

**Question 3:** We've seen two ways to get command-line input: `sys.argv` and `argparse`. If you
were writing a simple script just for yourself that takes one filename as input, which would
you use? What if you were writing a tool that other people would use?

**Question 4:** Exit codes let programs communicate success or failure to the shell. Why
might this be useful when you're running multiple programs in sequence? Can you think of
an example where one program's exit code should determine whether another program
runs?

**Question 5:** We used argparse to create a file search tool similar to `grep` (a famous Unix
tool). The Unix philosophy is to create small programs that do one thing well and can be
combined. How does this philosophy relate to functions in Python? How is writing a small
command-line tool similar to writing a function?

Take a few minutes to discuss these questions with a partner or write down your thoughts.
These questions are designed to help you connect terminal concepts to broader
programming principles and real-world applications.

---

## Assessment and Checks for Understanding (5 minutes)

Use these quick checks to assess understanding:

* **Quick Quiz (verbal or written):**

  * What is the difference between a terminal and a shell?
  * Name the three standard streams and what they are used for.
  * What does an exit code of `0` usually mean?
  * How do `sys.argv` and `argparse` differ when handling command line arguments?

* **Short Practical Task:**

  * Ask students to write a tiny script that:

    * takes a single argument (a name)
    * prints `"Hello, <name>!"`
    * exits with code `0` if a name is provided, or `1` otherwise.

Review their code and clarify any misunderstandings.

---

## Homework Assignment

Create a Python script called `process_numbers.py` that:

* Accepts one or more numbers as command line arguments (e.g. `5 10 15 20`)
* Has optional flags:

  * `--sum` — prints the sum of the numbers
  * `--average` — prints the average of the numbers
  * `--max` — prints the maximum number
  * `--min` — prints the minimum number
* Uses `argparse` to define and parse these arguments
* Validates input and exits with a non-zero code on invalid data

Hints:

* Use `type=float` or `type=int` in `add_argument` so `argparse` converts inputs for you.
* Use the `nargs='+'` parameter in `argparse` to accept multiple values.

Example:

```bash
python process_numbers.py 5 10 15 20 --sum --average
```

Output:

```text
Sum: 50
Average: 12.5
```

---

## Challenge Problems (Optional)

### Challenge 1: Multi-File Search Tool

Create a comprehensive search tool called `multi_search.py` that:

* Takes a search pattern and searches through multiple files
* Has flags for:

  * `--directory` or `-d`: Search in a specific directory (default: current directory)
  * `--extension` or `-e`: Only search files with a specific extension (e.g., `.txt`, `.py`)
  * `--ignore-case` or `-i`: Case-insensitive search
  * `--count` or `-c`: Show count of matches instead of the matches themselves
  * `--recursive` or `-r`: Search in subdirectories too
* Reports which files contain matches
* Uses proper exit codes and error handling
* Hint: You'll need to use the `os` or `pathlib` module along with file operations

### Challenge 2: Configuration File Generator

Create a tool called `config_maker.py` that:

* Uses `argparse` with subcommands (look up `add_subparsers()`)
* Has three subcommands:

  * `create`: Creates a new config file with default values
  * `set`: Sets a specific configuration value
  * `get`: Retrieves a configuration value
* Stores configuration in a simple text file or JSON format

Example usage:

```bash
python config_maker.py create myconfig.txt
python config_maker.py set myconfig.txt theme dark
python config_maker.py get myconfig.txt theme
```

---

## Summary and Closing Thoughts

In this lesson, you've learned how to:

* Open and navigate the terminal on your operating system
* Understand the difference between a terminal (the window) and a shell (the interpreter)
* Use basic commands such as `pwd`, `ls`/`dir`, `cd`, `mkdir`, and `whoami`
* Understand the three standard streams: stdin, stdout, and stderr
* Run Python scripts from the terminal and observe their output and exit codes
* Use `sys.argv` to accept command line arguments
* Build more professional command-line interfaces using `argparse`
* Write programs that provide useful help messages, validate input, and communicate
  success or failure via exit codes

The terminal may feel unfamiliar or even a bit uncomfortable at first, but that discomfort is a
sign that you are stretching yourself and learning powerful new skills. Every experienced
programmer has gone through this phase—confusion, experimentation, and eventually
confidence.

As you continue your programming journey, you'll find that the terminal becomes second
nature. The commands that feel awkward now will flow from your fingers effortlessly. The
concepts that seem abstract—streams, exit codes, argument parsing—will become the
foundation for understanding how software systems communicate and work together.

Keep practicing, stay curious, and remember: every time you use the terminal, you're
building skills that will serve you throughout your entire programming career. The terminal
is not just a tool—it's your direct line to the heart of the computer, and now you know how
to speak its language.

Welcome to the world of command-line programming. You're now equipped with tools that
professional developers use every day. The next step is to practice, experiment, and build.

The terminal awaits your commands!






