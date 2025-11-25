Lesson 16: The Terminal  
Owner: Nazari, Mujtaba  
TODO: Cover OS return code  
Learning Objectives  
By the end of this lesson, students will be able to:  
1. Understand what the terminal and shell are and how they differ  
2. Navigate the file system using basic command line commands  
3. Run Python scripts from the terminal and understand standard input/output 
streams  
4. Pass command line arguments to Python programs using sys.argv  
5. Create professional command -line programs using the argparse module  
6. Understand program exit codes and their significance  
 
Materials Needed  
• Computer with Python installed  
• Terminal/Command Prompt/PowerShell access  
• Text editor or IDE (IDLE, VS Code, or similar)  
• Sample Python scripts (to be created during the lesson)  
• A sample text file for practice exercises  
 
Introduction (5 minutes)  
Connecting to Previous Learning  
Throughout this course, you've been writing Python code and running it in various ways. 
Perhaps you've been clicking a "Run" button in IDLE, or executing code in an interactive 
Python shell. In Lesson 9, you worked with Tkinter to create graphical user int erfaces with 
buttons and windows. In Lesson 15, you learned about user inputs and events within 
programs. Now, we're going to explore another powerful way to interact with your programs: 
the terminal.

The terminal might seem intimidating at first. It's a text -based interface with no graphics, no 
buttons to click. But don't let its appearance fool you. The terminal is one of the most 
powerful tools in a programmer's toolkit, and learning to use it will m ake you more efficient 
and capable as a developer.  
What Is the Terminal? What Is a Shell?  
People often use the words "terminal" and "shell" interchangeably, but they actually refer to 
different things. Understanding this distinction will help you communicate clearly with 
other programmers.  
The Terminal  (or terminal emulator) is the program that provides you with a window where 
you can type commands. Think of it as the frame —the actual window on your screen where 
text appears. On Mac, this might be the Terminal app. On Windows, it might be Command 
Prompt or PowerShell. On Linux, it could be GNOME Terminal, Konsole, or any number of 
other applications. The terminal is just the interface, the canvas where commands are 
displayed.  
The Shell  is the program that runs inside the terminal. It's the interpreter that reads your 
commands, figures out what you want to do, and tells the operating system to do it. The 
shell is the brain, while the terminal is just the face. Common shells include bash (Bourne 
Again Shell), zsh (Z Shell), fish, and on Windows, PowerShell or cmd.  
Here's a helpful analogy: Imagine you're talking to someone through a video call. The 
terminal is like the video calling software (Zoom, Teams, etc.) —it's the window that lets you 
see and hear. The shell is like the person you're talking to —it's what actua lly understands 
and responds to what you say.  
A Brief History: Why Text -Based Interfaces?  
You might wonder: if we have beautiful graphical interfaces today, why do programmers still 
use text-based terminals? To understand this, we need to look back at computing history.  
In the early days of computing (1960s -1970s), computers had no screens as we know them 
today. Instead, they used devices called teletypes —essentially electric typewriters 
connected to the computer. You would type a command on the typewriter, and the 
computer would type back its response. Everything was text because that was the only 
option available.  
When the Unix operating system was developed in the 1970s at Bell Labs, it was built 
around a powerful philosophy: "Write programs that do one thing well and work together." 
This philosophy emphasized creating small, focused tools that could be combined in

creative ways. Since everything was text -based, programs could easily pass their output to 
other programs as input, creating powerful chains of operations.  
Even though we now have graphical interfaces, this text -based approach has proven so 
efficient and powerful that it has never been replaced. Modern programmers still use the 
terminal because it allows them to:  
• Work faster by typing commands instead of clicking through menus  
• Automate repetitive tasks by scripting commands  
• Combine simple tools to solve complex problems  
• Work with remote computers as easily as their local machine  
• Use the same tools across different operating systems  
Think of it like this: graphical interfaces are like ordering from a picture menu at a 
restaurant —easy and intuitive. The terminal is like speaking directly to the chef in their 
language —it takes more learning, but you can make exactly what you want, custo mize 
everything, and work much faster once you know the language.  
Why Programmers Prefer the Terminal  
There are several compelling reasons why professional programmers often prefer terminal -
based tools:  
Speed and Efficiency : Once you learn the commands, typing them is much faster than 
clicking through multiple menus and windows. Imagine having to rename 100 files. With a 
graphical interface, you'd click each file, select rename, type the new name, and repeat 99 
more times. W ith the terminal, you could write a single command that renames all 100 files 
in seconds.  
Precision and Power : The terminal lets you be extremely specific about what you want 
your computer to do. You can perform complex operations that would be tedious or 
impossible with a graphical interface.  
Automation : You can save sequences of commands in files called scripts, allowing you to 
automate repetitive tasks. This connects directly to your Python programming: you can 
write Python scripts that perform tasks automatically when run from the terminal.  
Remote Work : The terminal works the same way whether you're on your laptop or 
connecting to a powerful computer halfway around the world. Graphical interfaces require 
much more bandwidth and can be slow over network connections.

Universal Skill : While different operating systems have different graphical interfaces, 
terminal commands are often similar or identical across systems. Learning terminal skills 
once gives you tools that work almost everywhere.  
 
Section 1: Command Line Basics (12 minutes)  
Opening Your Terminal  
Before we can use the terminal, we need to open it. The process differs slightly depending 
on your operating system:  
On Windows:  
• Press the Windows key and type "Command Prompt" or "cmd"  
• Press Enter to open it  
• Alternatively, you can search for "PowerShell" which is a more modern terminal  
• For this course, either will work, though PowerShell is recommended  
On Mac:  
• Press Command + Spacebar to open Spotlight search  
• Type "Terminal" and press Enter  
• You can also find it in Applications > Utilities > Terminal  
On Linux:  
• Press Ctrl + Alt + T (on most distributions)  
• Or search for "Terminal" in your applications menu  
When you open your terminal, you'll see a mostly blank window with some text. This text is 
called the prompt, and it's the shell's way of saying "I'm ready for your command." The 
prompt often shows your username, your computer's name, and your current loca tion in 
the file system. It typically ends with a dollar sign ( $) on Mac and Linux, or a greater -than 
sign (>) on Windows.  
Don't be alarmed by the minimal interface. This simplicity is actually a strength. There's no 
clutter, no distractions —just you and your computer, ready to work together.  
Understanding Your Shell

Let's find out which shell you're using. Type the following command and press Enter:  
On Mac/Linux:  
echo $SHELL  
On Windows PowerShell:  
$PSVersionTable.PSVersion  
This will tell you which shell program is interpreting your commands. On Mac, you might 
see /bin/bash  or /bin/zsh. On Windows, you'll see version information for PowerShell. Don't 
worry if this seems cryptic now —the important thing is that your shell is running and ready 
to accept commands.  
Understanding Your File System  
Before we start navigating with commands, let's talk about how your computer organizes 
files. Your computer's files are organized in a hierarchical structure, like a tree turned 
upside down. At the top (or the root), you have your main drive. Branching off  from there, 
you have folders (which programmers often call directories), and inside those folders you 
might have more folders and files.  
Think of it like a family tree or an office building. The building (your computer) has floors 
(main directories), each floor has offices (subdirectories), and each office has desks and 
filing cabinets (files).  
When you're using the terminal, you're always "in" a specific location in this file system. 
This is called your current working directory. It's like your current position in the office 
building. You might be on the third floor, in the marketing office, at the second desk from 
the window.  
Essential Terminal Commands  
Let's learn the fundamental commands you'll use to navigate your file system. We'll explore 
each one in detail.  
pwd - Print Working Directory  
The pwd command tells you where you currently are in your file system. It stands for "print 
working directory," which is programmer -speak for "show me my current location."  
When you type pwd and press Enter, you'll see something like:  
/Users/yourname/Documents

or on Windows:  
C:\Users\yourname \Documents  
This is your current path —the full address of where you are in your computer's file system. 
Think of it like your GPS coordinates in the digital world.  
Try this: Open your terminal and type pwd, then press Enter. Look at the path it shows you. 
This is where you're starting from.  
ls (or dir on Windows) - List Contents  
The ls command (short for "list") shows you what's in your current directory. On Windows 
Command Prompt, you'll use dir instead, though ls works in PowerShell.  
When you type ls and press Enter, you'll see a list of all the files and folders in your current 
location. It's like opening a folder in Finder (Mac) or File Explorer (Windows), but in text 
form.  
For example, if you're in your Documents folder, you might see:  
homework.txt  
python_projects  
vacation_photos  
essay.docx  
Some items in the list are files (like homework.txt), and others are directories/folders (like 
python_projects). On most systems, directories are displayed in a different color or with 
special indicators to help you distinguish them.  
Try this: After checking where you are with pwd, type ls (or dir on Windows) to see what's in 
your current location.  
cd - Change Directory  
The cd command lets you move to a different directory. It's like walking from one room to 
another in our office building metaphor.  
To move into a subdirectory, type cd followed by the name of that directory:  
cd python_projects  
This moves you into the python_projects folder. If you type pwd now, you'll see that your 
current location has changed.

To move up one level (to the parent directory), use:  
cd ..  
The two dots ( ..) are a special symbol meaning "the directory above the current one." Think 
of it as taking the elevator up one floor.  
To move to your home directory (your personal folder on the computer), simply type:  
cd ~  
The tilde ( ~) is a shortcut that represents your home directory.  
Try this:  
1. Type ls to see what folders are available  
2. Choose a folder and use cd foldername  to move into it  
3. Type pwd to confirm you've moved  
4. Type cd .. to go back up  
5. Type pwd again to see you're back where you started  
mkdir - Make Directory  
The mkdir command creates a new directory. It stands for "make directory."  
To create a new folder called "terminal_practice", you would type:  
mkdir terminal_practice  
After pressing Enter, the folder is created instantly. You won't see much feedback —the 
shell just gives you a new prompt. This is normal. In the terminal world, no news is good 
news. If something goes wrong, you'll definitely hear about it!  
You can verify the folder was created by typing ls and seeing it in the list.  
Try this: Create a folder called "lesson16_practice" using mkdir lesson16_practice , then 
use ls to verify it was created.  
whoami - Who Am I?  
This simple command tells you which user account you're logged in as:  
whoami

It will display your username. This is useful when you're working on shared computers or 
remote systems and need to verify which account you're using.  
Practice Activity 1: Navigation Challenge (5 minutes)  
Now it's time to put these commands together. Follow these steps:  
1. Use whoami to see your username  
2. Use pwd to see where you are  
3. Use ls to see what's in your current location  
4. Create a new directory called "lesson16_practice" using mkdir  
5. Use ls again to verify the folder was created  
6. Move into that folder using cd lesson16_practice   
7. Use pwd to confirm you're now inside the new folder  
8. Create two more directories inside this one: "scripts" and "data"  
9. Use ls to see both folders  
10. Move up one level using cd ..  
11. Use pwd to confirm you're back to the parent directory  
If you successfully completed all these steps, congratulations! You've just navigated your 
file system using the terminal. This might feel slow and cumbersome now, but with 
practice, you'll find yourself flying through these commands faster than you could click 
through folders.  
 
Section 2: Understanding Input and Output Streams (8 minutes)  
The Three Standard Streams  
When programs run on your computer, they communicate with the outside world through 
three standard channels called streams. Understanding these streams is fundamental to 
working with the terminal and will help you understand how programs interact with user s 
and other programs.  
Standard Input (stdin) : This is where a program receives input data. When you type 
something into a running program, it comes through stdin. Think of stdin as the program's 
ears—it's how the program listens to you.

Standard Output (stdout) : This is where a program sends its normal output. When a 
Python program uses print(), the text goes to stdout. Think of stdout as the program's 
mouth—it's how the program talks to you.  
Standard Error (stderr) : This is where a program sends error messages and diagnostic 
information. Even though error messages appear on your screen like regular output, they go 
through a separate channel. This separation is useful because it allows you to handle errors 
differentl y from normal output. Think of stderr as the program's worried voice —it's how the 
program tells you when something goes wrong.  
Here's a visual way to think about it:  
User Input → [stdin] → Your Program → [stdout] → Normal Output  
                                    → [stderr] → Error Messages  
Let's see this in action with Python. Create a simple script called streams_demo.py : 
import sys  
 
# Writing to standard output (the normal way)  
print("This goes to stdout")  
 
# Writing to standard output explicitly  
sys.stdout.write("This also goes to stdout \n") 
 
# Writing to standard error  
sys.stderr.write("This goes to stderr \n") 
 
# Reading from standard input  
user_input = input("Type something: ")  
print(f"You typed: {user_input}")  
When you run this script from the terminal with python streams_demo.py , you'll see all the 
output mixed together on your screen. But they're actually going through different

channels, which becomes important when you want to do more advanced operations like 
saving output to files or connecting programs together.  
The Echo Command  
One of the simplest yet most useful terminal commands is echo. It takes whatever text you 
give it and outputs it to stdout:  
echo "Hello, World!"  
This is remarkably similar to Python's print function:  
print("Hello, World!")  
Both commands do essentially the same thing: they send text to standard output. This 
similarity is not a coincidence —Python was designed to work well with Unix -style 
command -line environments.  
Try this:  
1. Type echo "Hello from the terminal!"  in your terminal  
2. Create a tiny Python script with just print("Hello from Python!")   
3. Run the Python script  
4. Observe how both produce output in the same place (your terminal screen)  
Discussion Prompt  
Think about these questions for a moment:  
Why do you think programs separate normal output (stdout) from error messages (stderr)? 
Can you imagine situations where this separation would be useful?  
Consider a program that processes thousands of files and prints a status message for each 
one. If some files cause errors, how would separating stdout and stderr help you find just 
the errors?  
 
Section 3: Running Python Scripts from the Terminal (10 minutes)  
Why Run Scripts from the Terminal?  
So far in this course, you've probably been running your Python code by clicking a "Run" 
button in IDLE or another IDE. While this works perfectly well for learning and testing, 
running scripts from the terminal offers several advantages:

Flexibility : You can run any Python script from anywhere on your computer without having 
to open it in an editor first.  
Arguments : You can pass information to your program when you run it (we'll learn about 
this in the next section).  
Automation : You can run scripts automatically as part of larger processes or workflows.  
Professional Practice : This is how Python programs are typically run in professional 
environments, on servers, and in production systems.  
Standard Streams : When you run scripts from the terminal, you have full access to stdin, 
stdout, and stderr, allowing for more sophisticated input/output handling.  
Creating a Simple Script to Run  
Let's create a simple Python script that we can run from the terminal. Open your favorite 
text editor and create a new file called hello_terminal.py . Type the following code:  
print("Hello from the terminal!")  
print("This script is running successfully.")  
print("Congratulations on running your first terminal script!")  
Save this file in the "lesson16_practice" folder you created earlier. Make sure you save it 
with the .py extension.  
Running Your Script  
Now comes the exciting part. Let's run this script from the terminal:  
1. Open your terminal if it's not already open  
2. Use cd to navigate to the directory where you saved your script  
3. Use ls to verify you can see hello_terminal.py  in the list  
4. Type the following command and press Enter:  
python hello_terminal.py  
Note: On some systems, you might need to type python3 instead of python  
If everything worked correctly, you should see your three print statements appear in the 
terminal! The program ran, executed all the print statements, and then finished.

This might not seem like much, but you've just done something powerful. You've run a 
Python program from the command line, just like professional developers do.  
Understanding the Python Command  
Let's break down what happened when you typed python hello_terminal.py : 
python - This is the command that tells your computer to run the Python interpreter. The 
Python interpreter is the program that reads and executes Python code.  
hello_terminal.py  - This is an argument to the python command. It tells Python which file 
contains the code you want to run.  
When you press Enter, the following happens:  
1. The shell finds the Python interpreter program  
2. It tells Python to open and read hello_terminal.py  
3. Python executes the code line by line  
4. The output (from print statements) goes to stdout and appears in your terminal  
5. When the script finishes, the program exits and you get your prompt back  
Exit Codes: How Programs Report Success or Failure  
When a program finishes running, it sends a number back to the shell called an exit code 
(also called a return code or exit status). This number tells the shell whether the program 
succeeded or failed:  
• Exit code 0 means success (everything worked correctly)  
• Any non-zero exit code means failure (something went wrong)  
By convention, different non -zero numbers can indicate different types of errors, though 
many simple programs just use 1 for any error.  
Let's create a script that demonstrates exit codes. Create a file called exit_demo.py : 
import sys  
 
choice = input("Should this program succeed? (yes/no): ")  
 
if choice.lower() == "yes":

print("Success! Exiting with code 0")  
    sys.exit(0)  # Success  
else:  
    print("Failure! Exiting with code 1")  
    sys.exit(1)  # Failure  
Run this script and try both options. After the program finishes, you can check what exit 
code it returned:  
On Mac/Linux:  
echo $?  
On Windows PowerShell:  
echo $LASTEXITCODE  
This will show you the exit code from the last program that ran. Try running your script with 
both "yes" and "no" answers and check the exit code each time.  
Why does this matter?  Exit codes are crucial for automation and scripting. If you write a 
script that runs multiple programs in sequence, you can check each program's exit code to 
see if it succeeded before running the next one. If a program fails (non -zero exit code), your 
script can handle the error appropriately —maybe by stopping, trying again, or alerting 
someone.  
A More Complex Example  
Let's create a slightly more interesting script. Create a new file called number_analyzer.py : 
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
 
# This is the main part of our script  
user_input = input("Enter a number: ")  
number = int(user_input)  
analyze_number(number)  
Save this file in your lesson16_practice folder and run it from the terminal using:  
python number_analyzer.py  
Notice that the program waits for you to type a number. This is because of the input() 
function, which reads from stdin. The terminal can handle interactive programs just like the 
Python shell or IDLE can. Type a number and press Enter to see the analysis.  
Try this: Run the script several times with different numbers: try positive numbers, negative 
numbers, zero, even numbers, and odd numbers. Each time, the program runs fresh and 
asks for new input.

Section 4: Command Line Arguments with sys.argv (12 minutes)  
Moving Beyond Interactive Input  
In the previous section, our scripts asked for input while they were running using the input() 
function. This works fine, but it means you have to wait for the program to ask you 
questions, and you have to interact with it while it's running. There's another way to provide 
information to a program: command line arguments.  
Command line arguments are pieces of information you provide to a program when you 
start it. Instead of the program asking you questions after it starts, you give it the answers 
right from the beginning.  
Think of it like this: Interactive input is like ordering food at a restaurant where the waiter 
asks you questions ("What would you like to drink? What size? Any appetizers?"). 
Command line arguments are like mobile ordering, where you specify everything u pfront in 
the app before confirming your order. You make all your choices at once, and the restaurant 
receives your complete order immediately.  
A Real-World Comparison  
Imagine you have a calculator program. With interactive input:  
$ python calculator.py  
Enter first number: 5  
Enter operation (+, -, *, /): +  
Enter second number: 3  
Result: 8  
With command line arguments:  
$ python calculator.py 5 + 3  
Result: 8  
See the difference? With command line arguments, you provide all the information in one 
line, and the program can produce results immediately without stopping to ask questions. 
This is especially useful when you want to run the same program many times with  different 
inputs, or when you want to automate tasks.  
Understanding sys.argv

Python provides a built -in way to access command line arguments through a special list 
called sys.argv. To use it, you need to import the sys module, which you learned about in 
Lesson 8 when you studied modules.  
Let's create a simple script to see how this works. Create a file called show_arguments.py : 
import sys  
 
print("Command line arguments:")  
print(sys.argv)  
print(f"\nNumber of arguments: {len(sys.argv)}")  
 
for i, arg in enumerate(sys.argv):  
    print(f"Argument {i}: {arg}")  
Now run this script with some arguments:  
python show_arguments.py hello world 123  
You'll see output like:  
Command line arguments:  
['show_arguments.py', 'hello', 'world', '123']  
 
Number of arguments: 4  
Argument 0: show_arguments.py  
Argument 1: hello  
Argument 2: world  
Argument 3: 123  
Let's understand what happened here:  
sys.argv is a list  - Remember lists from Lesson 4? sys.argv is a list containing all the 
command line arguments. This means you can use all the list operations you've learned: 
indexing, slicing, looping, checking length, and so on.

The first element (index 0) is always the script name  - sys.argv[0]  contains 
'show_arguments.py', which is the name of the script itself. This is useful if your program 
needs to know its own name, perhaps for printing help messages.  
The rest are your arguments  - sys.argv[1]  is 'hello', sys.argv[2]  is 'world', and sys.argv[3]  is 
'123'. These are the actual arguments you provided.  
Everything is a string  - Notice that even 123 is stored as the string '123', not the number 
123. If you want to use it as a number, you'll need to convert it using int() or float(). This is 
similar to how the input() function always returns strings.  
Accessing Individual Arguments  
Let's create a more practical example. Create a file called greet_user.py : 
import sys  
 
# Check if a name was provided  
if len(sys.argv) < 2:  
    print("Error: Please provide your name")  
    print("Usage: python greet_user.py YourName")  
    sys.exit(1)  # Exit with error code  
 
name = sys.argv[1]  
print(f"Hello, {name}!")  
print(f"Your name has {len(name)} letters.")  
sys.exit(0)  # Exit with success code  
Let's break down what this script does:  
Lines 4-7: We check if the user provided enough arguments. Remember, sys.argv[0]  is 
always the script name, so if the list length is less than 2, that means the user didn't 
provide a name. We print an error message and usage instructions to help the user.  
Line 7: We exit with code 1 to indicate an error occurred. The shell can check this code to 
know the program didn't succeed.

Line 9: We get the name from sys.argv[1] , which is the first argument after the script name.  
Lines 10-11: We use that name in our greeting.  
Line 12: We exit with code 0 to indicate success.  
Try running this script different ways:  
Without arguments:  
python greet_user.py  
You'll see the error message and usage instructions, and the program exits with code 1.  
With a name:  
python greet_user.py Alice  
You'll see a personalized greeting, and the program exits with code 0.  
With multiple words:  
python greet_user.py Alice Smith  
Interesting! You'll only see "Hello, Alice!" because each space -separated word is treated as 
a separate argument. sys.argv[1]  is "Alice" and sys.argv[2]  is "Smith", but we only used the 
first one.  
Working with Multiple Arguments  
Let's create a program that uses multiple command line arguments. Create a file called 
simple_calculator.py : 
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
 
# Perform the calculation  
if operation == "+":  
    result = num1 + num2  
elif operation == " -": 
    result = num1 - num2  
elif operation == "*":  
    result = num1 * num2  
elif operation == "/":  
    if num2 == 0:  
        print("Error: Cannot divide by zero")  
        sys.exit(1)  
    result = num1 / num2  
else:  
    print(f"Error: Unknown operation '{operation}'")  
    print("Supported operations: +, -, *, /")  
    sys.exit(1)

# Display the result  
print(f"{num1} {operation} {num2} = {result}")  
sys.exit(0)  
This is a more sophisticated program. Let's explore its features:  
Lines 4-9: We check if the user provided three arguments (plus the script name makes 4 
total). If not, we show helpful usage instructions and exit with an error code.  
Lines 12-18: We extract our three arguments and convert the numbers from strings to 
floats using float(). We wrap this in a try -except block to handle the case where the user 
provides non -numeric arguments.  
Lines 21-35: We use conditionals (from Lesson 10) to perform different operations based 
on what the user requested. We handle the edge case of division by zero, which would 
crash our program otherwise.  
Lines 38-39: We display the result in a clear, formatted way and exit with a success code.  
Try running this calculator:  
python simple_calculator.py 15 + 7  
python simple_calculator.py 10 - 3 
python simple_calculator.py 4 * 9  
python simple_calculator.py 20 / 4  
python simple_calculator.py 20 / 0  
Each time, you get an immediate result without the program asking you questions! The last 
example demonstrates error handling —the program detects the division by zero and exits 
gracefully with an error message.  
Practice Activity 2: Word Analyzer (5 minutes)  
Create a script called word_info.py  that takes a word as a command line argument and 
prints:  
1. The word itself  
2. The number of characters in the word

3. The word in uppercase  
4. The word in lowercase  
5. The word reversed (hint: use string slicing word[::-1])  
6. Whether the word is a palindrome (reads the same forwards and backwards)  
Example usage:  
python word_info.py Python  
Should output something like:  
Word: Python  
Length: 6 characters  
Uppercase: PYTHON  
Lowercase: python  
Reversed: nohtyP  
Palindrome: No  
Make sure your script handles the case where no word is provided by checking the length of 
sys.argv and printing a helpful message with an appropriate exit code.  
 
Section 5: Professional Command -Line Programs with argparse (13 minutes)  
Beyond sys.argv: The Need for argparse  
While sys.argv is simple and works well for basic scripts, real -world programs often need 
more sophisticated command -line interfaces. Consider professional command -line tools 
you might have used:  
• Optional flags that modify behavior (like -v for verbose output)  
• Named parameters instead of relying on position  
• Automatic help messages  
• Type checking and validation  
• Default values for optional parameters

Building all of this from scratch using sys.argv would require a lot of code. Fortunately, 
Python provides a powerful built -in module called argparse that handles all of this for you.  
Think of sys.argv like building furniture with just a hammer and nails —it works, but it's 
basic. The argparse  module is like having a full workshop with power tools —you can build 
much more sophisticated things with less effort.  
Your First argparse Program  
Let's create a simple program using argparse. Create a file called greet_argparse.py : 
import argparse  
 
def main():  
    # Create the parser  
    parser = argparse.ArgumentParser(description="A friendly greeting program")  
     
    # Add arguments  
    parser.add_argument("name", help="Your name")  
    parser.add_argument(" -n", "--number", type=int, default=1,  
                       help="Number of times to greet (default: 1)")  
     
    # Parse the arguments  
    args = parser.parse_args()  
     
    # Use the arguments  
    for _ in range(args.number):  
        print(f"Hello, {args.name}!")  
     
    return 0

if __name__ == "__main__":  
    exit_code = main()  
    exit(exit_code)  
Let's break down this program piece by piece:  
Line 5: We create an ArgumentParser object. This object will handle all the work of parsing 
command -line arguments. The description  parameter provides text that will appear in help 
messages.  
Line 8: We add a positional argument called "name". Positional arguments are required and 
must be provided in a specific order. The help parameter describes what this argument is 
for. 
Lines 9-10: We add an optional argument with both a short form ( -n) and a long form ( --
number). Optional arguments start with dashes. We specify that this should be an integer 
(type=int), and we provide a default value of 1. This means if the user doesn't provide this 
argument, it will automatically be 1.  
Line 13: We call parse_args() , which does the actual work of reading sys.argv, validating the 
arguments, and converting them to the appropriate types. It returns an object containing all 
the parsed arguments.  
Lines 16-17: We access the parsed arguments using dot notation: args.name  and 
args.number . Notice how much cleaner this is than indexing into sys.argv! The argument 
names become attributes of the args object.  
Line 19: We return 0 to indicate success.  
Lines 21-23: This is a common Python pattern. The if __name__ == "__main__":  check 
ensures this code only runs when the script is executed directly (not when it's imported as 
a module). We call our main function and use its return value as our exit code.  
Now let's try running this program in different ways:  
Basic usage:  
python greet_argparse.py Alice  
Output: Hello, Alice!  
With the repeat option (short form):  
python greet_argparse.py Alice -n 3

Output:  
Hello, Alice!  
Hello, Alice!  
Hello, Alice!  
With the repeat option (long form):  
python greet_argparse.py Bob --number 2  
Output:  
Hello, Bob!  
Hello, Bob!  
Automatic Help Messages  
One of argparse's most useful features is automatic help generation. Try running:  
python greet_argparse.py --help  
You'll see a professionally formatted help message that argparse generated automatically:  
usage: greet_argparse.py [ -h] [-n NUMBER] name  
 
A friendly greeting program  
 
positional arguments:  
  name                  Your name  
 
optional arguments:  
  -h, --help            show this help message and exit  
  -n NUMBER, --number NUMBER  
                        Number of times to greet (default: 1)  
This help message is created from the descriptions and help text you provided when adding 
arguments. Users can always run your program with --help or -h to learn how to use it. You 
didn't have to write any of this help text yourself —argparse built it automatically!

A More Complex Example: File Search Tool  
Let's create a more practical program that searches for a keyword in a file. Create a file 
called search_file.py : 
import argparse  
import sys  
 
def search_file(filename, keyword, case_sensitive=True, line_numbers=False):  
    """Search for a keyword in a file and print matching lines."""  
    try: 
        with open(filename, 'r') as file:  
            for line_num, line in enumerate(file, start=1):  
                # Prepare the line for comparison  
                search_line = line if case_sensitive else line.lower()  
                search_keyword = keyword if case_sensitive else keyword.lower()  
                 
                # Check if keyword is in the line  
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
    # Create parser with a detailed description  
    parser = argparse.ArgumentParser(  
        description="Search for a keyword in a text file",  
        epilog="Example: python search_file.py data.txt Python -i -n" 
    ) 
     
    # Add positional arguments  
    parser.add_argument("filename", help="Path to the file to search")  
    parser.add_argument("keyword", help="Keyword to search for")  
     
    # Add optional arguments  
    parser.add_argument(" -i", "--ignore-case", action="store_true",  
                       help="Perform case -insensitive search")  
    parser.add_argument(" -n", "--line-numbers", action="store_true",  
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
 
if __name__ == "__main__":  
    sys.exit(main())  
This program demonstrates several important argparse features:  
Lines 28-31: We create a parser with both a description (shown at the top of the help 
message) and an epilog (shown at the bottom, useful for examples).  
Lines 34-35: Two required positional arguments: filename and keyword.  
Lines 38-41: Optional flag arguments using action="store_true" . These are boolean flags 
that are False by default but become True if the user includes them. Notice they don't 
require a value —their presence is the value.  
Lines 47-52: We call our search function, converting the parsed arguments into function 
parameters. Notice how we use not args.ignore_case  to convert the flag into the 
case_sensitive parameter.  
Lines 20-24: We handle errors properly, printing to stderr (using file=sys.stderr ) and 
returning appropriate exit codes.  
Before testing this program, create a sample text file called sample.txt  with some content:  
Python is a powerful programming language.  
Many people learn Python as their first language.  
python can be used for web development, data science, and more.  
The Python community is welcoming and helpful.  
Now try different searches:  
Basic search:

python search_file.py sample.txt Python  
Output:  
Python is a powerful programming language.  
Many people learn Python as their first language.  
The Python community is welcoming and helpful.  
Case-insensitive search:  
python search_file.py sample.txt python -i 
Output:  
Python is a powerful programming language.  
Many people learn Python as their first language.  
python can be used for web development, data science, and more.  
The Python community is welcoming and helpful.  
With line numbers:  
python search_file.py sample.txt language -n 
Output:  
1: Python is a powerful programming language.  
2: Many people learn Python as their first language.  
Both flags together:  
python search_file.py sample.txt python -i -n 
Understanding action="store_true"  
The action="store_true"  parameter is particularly useful for flag arguments. Without it, 
argparse would expect you to provide a value:  
--ignore-case true  
But with action="store_true" , the flag's presence is enough:  
--ignore-case  
This is much more convenient and matches how professional command -line tools work.

Practice Activity 3: Temperature Converter (5 minutes)  
Create a script called temp_convert.py  using argparse that:  
• Takes a temperature value as a positional argument  
• Has a required flag to specify the input scale: --from-celsius, --from-fahrenheit , or --
from-kelvin  
• Has an optional flag --verbose that, if included, prints additional information about 
the conversion  
The conversions:  
• Celsius to Fahrenheit: F = (C × 9/5) + 32  
• Fahrenheit to Celsius: C = (F - 32) × 5/9  
• Celsius to Kelvin: K = C + 273.15  
• Kelvin to Celsius: C = K - 273.15  
Example usage:  
python temp_convert.py 100 --from-celsius  
Should output: 100.0°C = 212.0°F = 373.15K  
With verbose:  
python temp_convert.py 100 --from-celsius --verbose  
Should output:  
Converting from Celsius  
Input: 100.0°C  
100.0°C = 212.0°F = 373.15K  
Water boils at this temperature!  
Why Use argparse Over sys.argv?  
Let's compare what we'd need to do with sys.argv versus argparse for the same 
functionality:  
With sys.argv:  
• Manually check argument count

• Write custom code to parse flags  
• Handle errors for each argument type  
• Write your own help message  
• Parse and validate each argument individually  
• Handle both short and long forms of flags yourself  
With argparse:  
• Automatically validates argument count  
• Built-in flag parsing  
• Automatic type conversion and validation  
• Free help message generation  
• Simple, declarative argument definitions  
• Short and long forms handled automatically  
For simple scripts with one or two arguments, sys.argv is fine. But as soon as you need 
optional arguments, flags, or type checking, argparse saves you enormous amounts of time 
and makes your code more maintainable.  
 
Reflection and Discussion (5 minutes)  
Let's take a moment to think deeply about what we've learned:  
Question 1 : We learned about three standard streams: stdin, stdout, and stderr. Why do 
you think it's useful to have separate channels for regular output and error messages? Can 
you think of a real -world scenario where this separation would be important?  
Consider this: Imagine you're running a program that processes 10,000 files. Most files 
process successfully (messages go to stdout), but some have errors (messages go to 
stderr). How could you use this separation to create a log of just the errors?  
Question 2 : Think about programs you use daily (web browsers, text editors, games). Some 
have graphical interfaces, others use the command line. When do you think a command 
line interface is better than a graphical interface? When is a graphical interface better?

Question 3 : We've seen two ways to get command -line input: sys.argv and argparse. If you 
were writing a simple script just for yourself that takes one filename as input, which would 
you use? What if you were writing a tool that other people would use?  
Question 4 : Exit codes let programs communicate success or failure to the shell. Why 
might this be useful when you're running multiple programs in sequence? Can you think of 
an example where one program's exit code should determine whether another program 
runs?  
Question 5 : We used argparse to create a file search tool similar to grep (a famous Unix 
tool). The Unix philosophy is to create small programs that do one thing well and can be 
combined. How does this philosophy relate to functions in Python? How is writing a small  
command -line tool similar to writing a function?  
Take a few minutes to discuss these questions with a partner or write down your thoughts. 
These questions are designed to help you connect terminal concepts to broader 
programming principles and real -world applications.  
 
Assessment  
To verify you've met the learning objectives, complete the following tasks:  
Task 1: Terminal Navigation and Understanding  (Demonstrates Objectives 1 and 2)  
• Open your terminal and type echo $SHELL  (Mac/Linux) or check your shell type  
• Create a directory structure using only terminal commands:  
o Create a folder called "assessment"  
o Inside it, create folders called "scripts", "data", and "output"  
o Navigate into each folder and use pwd to show your location  
o Return to the parent directory  
• Write a brief explanation (3 -4 sentences) of the difference between a terminal and a 
shell  
Task 2: Basic Script Execution with Streams  (Demonstrates Objective 3)  
• Create a Python script called stream_demo.py  that:  
o Prints a welcome message to stdout

o Asks the user for their age (reading from stdin)  
o If the age is less than 0, prints an error message to stderr and exits with code 
1  
o If the age is valid, prints a message to stdout and exits with code 0  
• Run this script from the terminal and verify it works correctly  
• Test both valid and invalid inputs and check the exit codes  
Task 3: sys.argv Command -Line Arguments  (Demonstrates Objective 4)  
• Create a Python script called rectangle.py  that:  
o Takes two command -line arguments: width and height  
o Calculates the area and perimeter of a rectangle  
o Prints the results  
o Handles the edge case where the user doesn't provide enough arguments  
o Uses appropriate exit codes  
• Example: python rectangle.py 5 3  should output area and perimeter  
Task 4: Professional argparse Program  (Demonstrates Objectives 5 and 6)  
• Create a Python script called word_counter.py  that:  
o Takes a filename as a positional argument  
o Has an optional -w or --word flag to search for a specific word and count 
occurrences  
o Has an optional -l or --lines flag that shows total line count  
o Has an optional -c or --chars flag that shows total character count  
o If no optional flags are provided, shows all statistics  
o Handles file not found errors with appropriate error messages to stderr  
o Returns exit code 0 on success, 1 on error  
o Has proper help documentation  
Example usage:  
python word_counter.py sample.txt

python word_counter.py sample.txt --word Python  
python word_counter.py sample.txt -l -c 
python word_counter.py --help  
 
Homework and Further Practice  
Required Homework  
Assignment 1: Enhanced Calculator  Create a script called calculator_advanced.py  using 
argparse that:  
• Takes three positional arguments: number1, operator, number2  
• Supports operations: +, -, *, /, ** (power), % (modulo)  
• Has an optional --round flag that takes an integer and rounds the result to that many 
decimal places  
• Has an optional --verbose flag that shows the calculation step -by-step  
• Handles division by zero and invalid operators  
• Returns appropriate exit codes  
Example:  
python calculator_advanced.py 10 / 3 --round 2  
Result: 3.33  
 
python calculator_advanced.py 10 / 3 --verbose  
10.0 divided by 3.0 equals 3.333333333333333  
Assignment 2: Text File Statistics  Create a script called text_stats.py  that:  
• Takes a filename as a positional argument  
• Analyzes the file and prints:  
o Total number of lines  
o Total number of words  
o Total number of characters

o Average word length  
o Longest word in the file  
• Has an optional --top flag that takes a number N and shows the N most common 
words  
• Handles file errors appropriately with stderr and exit codes  
Assignment 3: List Processor  Create a script called process_numbers.py  using argparse 
that:  
• Takes multiple numbers as positional arguments (any amount)  
• Has optional flags for different operations:  
o --sum: Show the sum  
o --average: Show the average  
o --min: Show minimum value  
o --max: Show maximum value  
o --sort: Show the numbers sorted     
• If no flags are provided, show all statistics  
• Use the nargs='+'  parameter in argparse to accept multiple values  
Example:  
python process_numbers.py 5 10 15 20 --sum --average  
Sum: 50  
Average: 12.5  
Challenge Problems (Optional)  
Challenge 1: Multi -File Search Tool  Create a comprehensive search tool called 
multi_search.py  that:  
• Takes a search pattern and searches through multiple files  
• Has flags for:  
o --directory  or -d: Search in a specific directory (default: current directory)  
o --extension  or -e: Only search files with specific extension (e.g., .txt, .py)

o --ignore-case or -i: Case-insensitive search  
o --count or -c: Show count of matches instead of the matches themselves  
o --recursive  or -r: Search in subdirectories too     
• Reports which files contain matches  
• Uses proper exit codes and error handling  
• Hint: You'll need to use the os or pathlib module along with file operations  
Challenge 2: Configuration File Generator  Create a tool called config_maker.py  that:  
• Uses argparse with subcommands (look up add_subparsers() )  
• Has three subcommands:  
o create: Creates a new config file with default values  
o set: Sets a specific configuration value  
o get: Retrieves a configuration value     
• Stores configuration in a simple text file or JSON format  
• Example usage:  
python config_maker.py create myconfig.txt  
python config_maker.py set myconfig.txt username Alice  
python config_maker.py get myconfig.txt username  
Challenge 3: Command -Line Todo List  Create a complete todo list manager called 
todo.py that:  
• Uses argparse subcommands for different actions:  
o add: Add a new todo item  
o list: Show all todos  
o complete : Mark a todo as complete  
o delete: Remove a todo     
• Stores todos in a file (use the json module to save/load)  
• Each todo has: description, priority (high/medium/low), and completion status

• Has flags like --priority for filtering  
• Example:  
python todo.py add "Learn argparse" --priority high  
python todo.py list  
python todo.py complete 1  
python todo.py delete 1  
This challenge combines file I/O, JSON handling, argparse subcommands, and data 
management.  
 
Further Reading and Resources  
Terminal and Shell Basics:  
• Practice terminal commands at least 10 minutes per day to build muscle memory  
• Try organizing your files entirely from the command line  
• Explore additional commands like cp (copy), mv (move), and rm (remove) —but be 
careful with rm as it permanently deletes files!  
• Learn about your shell's history feature (usually the up arrow key) to recall previous 
commands  
Python and Command -Line Arguments:  
• Experiment with running different Python scripts you've written in previous lessons 
from the terminal  
• Read the official Python documentation on argparse (available at docs.python.org)  
• Try converting some of your old interactive scripts to use command -line arguments  
• Practice writing help messages that would make sense to someone who's never 
used your program before  
Standard Streams:  
• Learn about output redirection in your shell (using > to save output to a file)  
• Explore piping ( |) to connect programs together (covered more in advanced courses)

• Understand how professional tools use stdin/stdout/stderr effectively  
Exit Codes:  
• Practice checking exit codes after running programs  
• Learn how scripts can use exit codes for error handling  
• Understand common exit code conventions (0 = success, 1 = general error, 2 = 
misuse of shell command, etc.)  
Advanced Topics to Explore Later:  
• The click library, an alternative to argparse with different design philosophy  
• Environment variables and how programs use them  
• Shell scripting to automate multiple commands  
• The subprocess  module for running other programs from Python  
• The pathlib module for working with file paths elegantly  
• Configuration files and how professional programs manage settings  
Professional Development:  
• Study how popular command -line tools structure their interfaces (git, npm, docker)  
• Learn about the POSIX standards that govern Unix command -line behavior  
• Explore cross -platform considerations (Windows vs Unix -like systems)  
 
Summary  
In this lesson, you've taken significant steps in your programming journey by learning to use 
the terminal and create professional command -line programs.  
You now understand that the terminal  is the application that provides a text -based 
interface, while the shell is the program running inside it that interprets your commands. 
You've learned that this distinction matters when discussing how computers process 
commands.  
You've discovered the three standard streams  (stdin, stdout, stderr) that programs use to 
communicate with users and other programs. Understanding these streams is

fundamental to command -line programming and will serve you well as you advance in your 
programming career.  
You've mastered basic terminal commands  for navigating your file system: pwd to see 
where you are, ls to see what's in your current location, cd to move between directories, 
and mkdir to create new directories. You've also learned whoami and echo for basic system 
interaction.  
You've learned to run Python scripts from the terminal , which is how professional 
developers execute their programs. You now understand that when a program finishes, it 
returns an exit code  to the shell (0 for success, non -zero for errors), and why these codes 
are important for automation and error handling.  
You've explored two methods for handling command -line arguments . With sys.argv, you 
learned the basics of accessing command -line input as a simple list. With the argparse 
module, you learned to create sophisticated command -line interfaces with optional 
arguments, flags, automatic help messages, type checking, and default values.  
Most importantly, you've begun thinking like a professional programmer. You've seen how 
the Unix philosophy of creating small, focused tools that work together relates to writing 
good functions. You've learned that good command -line programs handle errors gracefully, 
provide helpful messages, and return meaningful exit codes.  
The terminal might have seemed mysterious at first, but it's simply another way to interact 
with your computer —one that gives you more power, precision, and automation 
capabilities than graphical interfaces alone. Every expert programmer started exactly 
where you are now, typing their first commands into a black screen and wondering if they 
were doing it right.  
As you continue your programming journey, you'll find that the terminal becomes second 
nature. The commands that feel awkward now will flow from your fingers effortlessly. The 
concepts that seem abstract —streams, exit codes, argument parsing —will become th e 
foundation for understanding how software systems communicate and work together.  
Keep practicing, stay curious, and remember: every time you use the terminal, you're 
building skills that will serve you throughout your entire programming career. The terminal 
is not just a tool —it's your direct line to the heart of the computer, and now you know how 
to speak its language.  
Welcome to the world of command -line programming. You're now equipped with tools that 
professional developers use every day. The next step is to practice, experiment, and build. 
The terminal awaits your commands!
