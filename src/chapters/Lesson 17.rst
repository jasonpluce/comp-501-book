Lesson 17: Files & Strings  
Owner: Saban, Michael  
Reviewer: Jason for Saban, Michael   
Per the Guidelines for Content the following items are missing:  
Overview & Introduction is missing connection to prior knowledge  
Assessment  
Summary  
Everything else looks good.  
 
Overview  
Programs often need to save data or read information created elsewhere. In this lesson, 
you'll learn how to work with text files and manipulate string data.  
Learning Objectives  
By the end of this lesson, you should be able to:  
• Open, read, write, and append text files safely.  
• Differentiate file modes ("r", "w", "a") and understand overwriting vs appending.  
• Apply common string methods (strip, split, join, replace) to clean and combine text.  
• Load and dump basic JSON structures and explain pretty -printing and 
character/encoding  
Prerequisites  
• Comfortable with navigating folders and file paths  
• Basic variable and loop syntax  
Lesson Outline  
1. Introduction (5 min)  
When you think about your daily life outside of programming, you might not realize how 
often you interact with text -based data. Although it may not feel like text files are 
everywhere, things like boarding passes, class schedules, directions, notifications ,

receipts, etc. are all built on structured text. However, these things can be messy, including 
inconsistent spacing, symbols, or formatting differences between different sources.  
Because we rely so much on text, the ability to read, write, and manipulate this data gives 
your programs a way to interact with the world. String operations make this information 
usable, and almost every interaction your program will have with external da ta involves 
strings in some way.  
In this lesson, we'll explore how to work safely with files and build on some string tools 
you've seen earlier in the course, applying them to more realistic text.  
1. Working with files (15 min)  
1. Accessing files  
The first step to interacting with external information is opening and reading the files safely. 
Python provides many ways to work with files, but the pathlib module is a reliable way to 
open files cleanly without having to specify absolute raw string paths. A Path creates a 
reference to a file on your computer, which allows you to open it with a context manager. 
Using a context manager to open and work with files addresses the 'safe' part of working 
with files, as it ensures the file is properly closed. Th is ensures files don't become 'locked' 
or you end up with incomplete writes.  
from pathlib import Path  
path = Path(" .txt")  
with path.open(mode="r", encoding="utf -8") as f:  
  for line in f:  
    print(repr(line))  
This example opens a file in read mode and prints each line. The repr() function shows 
invisible characters like newline characters. As soon as the code in the with block ends, 
Python automatically closes the file.  
1. Reading files  
Using the "r" mode opens a file for reading only. Reading line -by-line is optimal, as Python 
only has to load one line of memory at a time instead of loading the entire file. This is 
especially important when working with log files, transcripts, large datasets, or long  text 
documents.  
1. Writing and appending

Writing to a file is similar to reading, but you choose a different mode depending on what 
you want to do.  
with open(" .txt", "w", encoding="utf -8") as f:  
  f.write("first line \n") 
with open(" .txt", "a", encoding="utf -8") as f:  
  f.write("another line \n") 
Opening a file in "w" mode overwrites any existing content which essentially creates a fresh 
file even if one existed before. Using "a" mode appends new content to the end without 
erasing what previously existed.  
1. Misconceptions  
Working with files introduces man challenges. A "file not found" error usually means the 
path is incorrect. Reading text created on different systems may result in encoding 
problems, which is why explicitly using "utf-8", a very common text encoding standard, is a 
good habit. Another common issue is forgetting to include newlines ( \n) between writes to 
a file, which can smash lines together and lead to readability issues when opening later.  
1. String Methods (15 min)  
1. Trimming whitespace  
Many files include extra spaces, tabs, or newline characters. Methods like strip(), lstrip(), 
and rstrip() remove these in different ways.  
text = "   Hello, world!   \n" 
print(repr(text))  
print(repr(text.strip()))  
print(repr(text.lstrip()))  
print(repr(text.rstrip()))  
1. Case transformations  
Changing the case of text is useful for standardizing comparisons between text or creating 
clean output.  
print(repr(text.lower()))  
print(repr(text.upper()))

1. Splitting and joining  
Many files store lists of items, often separated by some special character called a 
delimiter. A comma, for example, is one of the most common delimiters, which are found in 
Comma-Separated Value (CSV) files. Similarly, Tab -Separated Value (TSV) files use tabs as 
their delimiter. These formats look like plain text when opened, but the structure of a list or 
table in the file comes from how the text is separated by these delimiters. One way to parse 
this type of text is through Python's split()method.  
sentence = "apples,bananas,pears"  
words = sentence.split(",")  
print(words) # ['apples', 'bananas', 'pears']  
You can also combine a list of strings with the join() method by specifying the desired 
delimiter.  
joined = " | ".join(words)  
print(joined) # "apples | bananas | pears"  
1. Searching and replacing  
Searching within a string might help locate information you care about. For example, you 
might want to check a file for a specific keyword such as "ERROR". The find()method 
returns the index where the substring appears (or -1 if it isn't found), which makes it useful 
for filtering text or detecting certain patterns. Replacing text allows you to correct certain 
patterns, update terminology, or convert text into specific formats that might make it easier 
for your program to hand le. 
message = "hello world"  
print(message.find("world")) # 6  
print(message.find("Python")) # -1 
updated = message.replace("world", "Python")  
print(updated) # "hello Python"  
print(updated.startswith("hello")) # True  
print(updated.endswith("Python")) # True  
1. Other useful tools

Python provides other useful string operations that might be useful.  
• len() returns the length of a string  
• in checks if a substring appears anywhere in a larger string  
• isdigit() and isalpha() detect types of characters  
• startswith()  and endswith()  detect prefixes/suffixes in a string  
• count() checks how many times a substring appears  
1. JSON basics  
Not all text files are unstructured paragraphs or even delimiter separated data (like CSV 
files). JSON is another widely used structured text format because it represents lists and 
dictionaries in a very simple way. The json module provides a straightforward way of 
working with JSON files.  
import json  
with open("config.json") as f:  
  data = json.load(f)  
with open("output.json", "w") as f:  
  json.dump(data, f, indent=2)  
1. Guided practice  
• Exercise 1: Reading and cleaning file output  
Write a short program that:  
• Asks the user to enter a file name  
• Opens the file safely  
• Prints each line with leading and trailing whitespace removed  
• Prints the total number of lines in the file  
• Exercise 2: Word counter  
o Read the file  
o Split each line into individual words  
o Normalize words

o count how many times each distinct word appears  
o Print the most frequent word  
• Exercise 3: JSON modification  
o Load JSON data from a file  
o Modify one field based on user input  
o Sae the updated JSON back to a new file  
1. Assessment  
In many real systems such as healthcare, customer support, cybersecurity, etc., contact 
information is often messy and inconsistent. You will write a Python function that reads a 
text file containing a few messy contact records. Each line of the file conta ins one record, 
and each record may vary in spacing, capitalization, formatting, and missing fields. Your 
job is to transform each record into a clean, standardized format.  
Input file example:  
name: jAnE DOE , email= Jane.Doe@Example.com , phone= 555 -1234  
NAME: alic Johnson , phone= 222 -444  
name: MARK TWAIN, email= mark.twain@books.org  
Email=someone@nowhere.net , name: nobody special  
name: John Johnson  
Write a function:  
def clean_contact(record):  
  ... 
The function must:  
1. Read the file line -by-line, treating each line as one contact record  
2. Trim any leading or trailing whitespace  
3. Normalize labels case -insensitively  
4. Split each record into cleaned fields  
5. Properly capitalize the name

6. Standardize email formatting  
7. If a field is missing, fill in with "UNKNOWN"  
8. Return a pipe -delimited ( |) file Expected Output:  
NAME: Jane Doe | EMAIL: jane.doe@example.com | PHONE: 555 -1234  
NAME: Alice Johnson | EMAIL: UNKNOWN | PHONE: 222 -444  
NAME: Mark Twain | EMAIL: mark.twain@books.org | PHONE: UNKNOWN  
NAME: Nobody Special | EMAIL: someone@nowhere.net | PHONE: UNKNOWN  
NAME: John Johnson | EMAIL: UNKNOWN | PHONE: UNKNOWN  
1. Challenge problems  
2. Summary  
Key takeaways:  
• Use context managers ( with statements) to handle files safely  
• Understand file modes ( "r", "w", "a") and when to use each  
• Apply string operations to clean and interpret real -world data  
• Recognize that even simple tasks often require combining file I/O with multiple 
string methods  
 
Connection to next lessons:  
The next lessons (L18/L19) will build on this by introducing error handling, where you'll 
learn to:  
• Detect and handle missing files or incorrect file names  
• Address improperly formatted data  
• Anticipate edge cases  
• Write code that fails safely rather than crashing
