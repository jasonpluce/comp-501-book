Lesson 15: User Inputs & Events
================================

Introduction
------------

Up to this point, our programs have worked with data that we have written
directly into the code. For example, we may have created a list of numbers, a
string, or a variable that our program used to perform some task. But what if we
want our programs to react to information that changes while the program is
running, or to actions that come from the user?

Imagine that we are writing a power monitoring application. It would need to
check a power source repeatedly to gather new information about energy use.
Or consider a video game: the program must respond instantly to a player’s
actions, such as pressing keys or clicking the mouse, in order to control the
character and interact with the game world. In both cases, the program must be
able to handle input or events that come from outside of the code itself.

Python provides several ways to make our programs interactive. We can instruct
our program to read data from a file allowing it to process information stored
elsewhere. We can also allow the user to pass arguments when the program is
started, making it possible to change the program’s behavior without editing
the source code. Finally, we can ask the user to type in responses directly
during execution, letting the program collect information as needed. Together,
these approaches help us build programs that are flexible, responsive, and
capable of adapting to different situations and inputs.

Objectives
----------

By the end of this lesson, you will understand the purpose of user input and
event handling in interactive programs. You will learn how to use Python to
capture information from users through manual input, command-line
arguments, and files. You will also learn when and why each type of input
method is useful. Developing the ability to handle user input is an essential step
toward creating applications that are dynamic, adaptable, and capable of
responding to real-world data.

- Understand the purpose of user input and event handling in interactive programs.
- Use Python to capture information from users through manual input, command-line arguments, and files.
- Recognize when and why each type of input method is useful.
- Develop applications that are dynamic, adaptable, and capable of responding to real-world data.

Materials (2)
-------------

???

Outline (2)
-----------

???

Lesson Content
--------------

In the previous lessons, we worked with fixed values and explored how
programs use variables, data types, and operations to perform specific tasks. In
this lesson, we are moving beyond static data and learning how to make our
programs interactive. We will explore several ways to collect input from users
and other data sources so that our applications can react to real-world
information.

We will begin by introducing the ``input()`` keyword, which allows a program
to pause and wait for the user to type a response. Next, we will examine how
the ``argparse`` module enables developers to create command-line interfaces
that receive input before a program starts running. Finally, we will study how to
read data from files, a key skill for working with persistent information and
automating larger workflows. Together, these techniques will help us
understand how Python programs can become dynamic, adaptable, and
capable of responding to changing inputs.

In the following lessons, we will build on these ideas by learning how to validate
the data we receive, how to make decisions based on user input using
conditionals, and how to design functions that handle these interactions
efficiently. This progression will lead us toward developing more complex and
responsive applications that can reason about the data they process.

input Keyword
-------------

Introduction: The ``input()`` function is the simplest and most direct way to
receive information from the user during program execution. When ``input()``
is called, the program pauses and waits for the user to type something into the
command line, followed by pressing the Enter key. This makes the application
interactive, as users can provide information that changes the program’s
behavior or output each time it runs. Such interaction helps bridge the gap
between static programs that use fixed data and dynamic programs that
respond to real-time user actions.

Concept: The ``input()`` function displays a prompt message, waits for the
user’s response, and returns that response as a string. The string can then be
processed or converted into another data type such as an integer or a floating-
point number. Because the function always returns text, it is important to
convert the result to the correct type if numeric input is expected.

Code Example

How would you test if the inputs from a user are valid?

Reflection: Testing for valid user input often involves checking whether the
provided data can be safely converted into the expected type. You can use
exception handling, as shown above, or conditional statements that inspect the
structure of the input. When using ``input()``, it is good practice to assume that
user input may not always be correct and to include safeguards that guide
users back toward valid responses.

argparse Command Line Interfaces
--------------------------------

Introduction: The ``argparse`` module allows developers to create a command-
line interface (CLI) for their Python programs. Unlike the ``input()`` function,
which pauses execution for the user to type a response interactively, a CLI
allows users to define input values before the program begins running. This is
especially helpful when automating tasks, running scripts repeatedly with
different inputs, or integrating your program into larger systems or workflows.

Concept: Using ``argparse``, you can define specific command-line arguments
that correspond to parameters in your program. When the program starts,
``argparse`` reads the arguments from the command line, checks that they are
valid, and makes them available to your program as variables. Once the
program begins execution, the user cannot change these arguments without
restarting the program. This approach provides a structured and repeatable way
to control program behavior.

Code examples:

To test this program, run it from the command line:

How would you test if the inputs from a user are valid? When is a CLI
useful? When is it impractical?

Reflection: To test the validity of user inputs in a CLI, ``argparse`` can enforce
data types, require certain arguments, or even restrict input to a set of valid
choices. A CLI is useful for applications that run in automated environments or
for power users who need repeatable, scriptable execution. It can be
impractical, however, for casual users who prefer interactive prompts or
graphical interfaces.

Reading Files
-------------

Introduction: Many Python programs need to work with data that is stored
outside the program itself, such as text documents, spreadsheets, or
configuration files. Reading and writing files enables your programs to share
information with other software, preserve results for later use, and process large
datasets without requiring user input for each value. This ability makes Python a
powerful “glue language,” capable of connecting different applications and
workflows together.

Concept: Python’s built-in ``open()`` function allows a program to access files for
reading or writing. When reading from a file, the program loads the file’s
contents into memory, where it can process, transform, or analyze the data.
Files can be opened in text mode for human-readable data or in binary mode
for data such as images or executable files. The ``pathlib.Path`` class,
introduced in modern Python, provides a more object-oriented way to handle
file paths but ultimately uses similar mechanisms under the hood.

Code examples:

What’s the difference between the ``open`` keyword and the
``pathlib.Path`` class?

Reflection: The ``open()`` function provides a simple way to work with files using
plain string paths. The ``pathlib.Path`` class, on the other hand, offers an
object-oriented approach that allows methods such as ``.read_text()`` and
``.write_text()`` directly on path objects. Both approaches achieve similar
results, but ``pathlib`` is often considered cleaner and more modern. Choosing
between them depends on project style and readability preferences.

Reflection
----------

Throughout this lesson, we explored three primary ways that Python programs
can receive and respond to input: directly from users through the ``input()``
keyword, indirectly through command-line arguments using the ``argparse``
module, and from files that store data created by other applications or
processes. Each approach offers a different kind of interaction and serves a
distinct purpose within program design.

The ``input()`` function introduced the concept of interactive control flow,
where a running program pauses and waits for human input before continuing.
This approach is ideal for simple, conversational, or educational programs
where user interaction guides execution step by step. By contrast, the
``argparse`` module allows input to be supplied before the program runs,
creating a more structured and repeatable interface suited to automation and
scripting. Finally, file reading demonstrated how Python can handle external
data sources, allowing programs to operate on large or persistent datasets
without requiring direct user interaction.
