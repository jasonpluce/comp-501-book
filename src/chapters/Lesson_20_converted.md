• Owner: Nazari, Mujtaba  
• Reviewer: Eslami, Behnaz  
• Dictionary basics  
• Key-value pairs  
• Dictionary methods  
 
Dictionaries in Python  
Learning Objectives  
By the end of this chapter, you will be able to:  
1. Define what a dictionary is and explain the key -value pair structure  
2. Create dictionaries using both literal syntax and the dict() constructor  
3. Apply bracket notation and the .get() method to access dictionary values  
4. Implement  operations to add, update, and remove dictionary items  
5. Analyze when dictionaries are more appropriate than lists or tuples for a given 
problem  
6. Evaluate  the rules for valid dictionary keys and explain why immutability is required  
7. Apply dictionary methods including .keys(), .values(), .items(), and .update()   
8. Create programs that use dictionaries to solve real -world data management 
problems  
 
Introduction: A New Way to Organize Data  
In your daily life, you use many types of organizational systems. When you look up a word in 
a dictionary, you don't flip through every page starting from the beginning. Instead, you go 
directly to the section where that word should be, using the alphabeti cal organization. 
When you save a contact in your phone, you don't remember that "Mom" is contact number 
47—you simply search for "Mom" by name.  

These real -world examples illustrate an important concept: sometimes it's more natural to 
find information using a label or name rather than a position number. This is exactly what 
Python dictionaries allow you to do.  
So far in this course, you've learned about lists and tuples, which organize data by position. 
If you want the third item in a list, you write my_list[2] . But what if your data doesn't have a 
natural order? What if you want to store a student's name, age, and major, and access 
them by meaningful labels rather than trying to remember "position 0 is the name, position 
1 is the age"?  
This is where dictionaries come in. A dictionary is Python's way of storing data that has 
natural labels or names. In this chapter, you'll learn how dictionaries work, how to create 
and use them, and when they're the right choice for organizing your data.  
 
Section 1: Understanding Dictionaries  
What Is a Dictionary?  
A dictionary in Python is a collection of items where each item consists of two parts: a key 
and a value. You can think of the key as a label or name, and the value as the data 
associated with that label. Together, a key and its value form what we call a key-value pair . 
The concept is similar to a real dictionary where you look up a word (the key) to find its 
definition (the value). It's also like a phone book where you look up a person's name (the 
key) to find their phone number (the value).  
Let's look at a simple example. Suppose you want to store information about a student. 
Using a dictionary, you might write:  
student = {  
    "name": "Alice",  
    "age": 20,  
    "major": "Computer Science"  
} 
In this example, we have three key -value pairs. The key "name" maps to the value "Alice", 
the key "age" maps to the value 20, and the key "major" maps to the value "Computer 
Science". Notice how each key -value pair is written with the key first, followed by a colon 

(:), and then the value. Multiple pairs are separated by commas, and the entire dictionary is 
enclosed in curly braces ( {}). 
Why Use Dictionaries Instead of Lists?  
You might wonder why we need dictionaries when we already have lists. Let's compare how 
you would store the same student information using a list versus a dictionary.  
Using a list, you might write:  
student = ["Alice", 20, "Computer Science"]  
This stores the same information, but there's a problem: you have to remember that 
position 0 is the name, position 1 is the age, and position 2 is the major. If someone else 
reads your code, they have to figure this out too. And if you later decide to add  more 
information, like a student ID number, you have to remember to insert it in the right position 
and update all your code that accesses these positions.  
With a dictionary, the labels make everything clear:  
student = {  
    "name": "Alice",  
    "age": 20,  
    "major": "Computer Science"  
} 
Now, to get the student's name, you simply ask for student["name"] . The code is self -
documenting —anyone reading it immediately knows what each piece of data represents. 
You can also add new information without worrying about position:  
student["student_id"] = "A12345"  
The order of items in a dictionary doesn't define their meaning (though Python does 
remember the order you added them, starting from version 3.7). What matters is the label 
(key) you use to access each value.  
Key Characteristics of Dictionaries  
Before we dive into creating and using dictionaries, let's establish some important facts 
about how they work:  
First, every key in a dictionary must be unique. You cannot have two items with the same 
key. If you try to add a new item with a key that already exists, the new value will replace the 

old one. This makes sense when you think about it: in a phone book, each name should 
point to one phone number. If the same name appeared twice with different numbers, you 
wouldn't know which one to call.  
Second, keys must be immutable, meaning they cannot be changed after they're created. 
We'll explore this requirement in more detail later, but for now, just remember that strings, 
numbers, and tuples can be keys, but lists cannot.  
Third, values in a dictionary can be anything. They can be strings, numbers, lists, other 
dictionaries, or any other Python data type. A value can also be repeated —multiple keys 
can map to the same value. For example, two different courses might both have the same 
number of credits.  
Fourth, dictionaries are mutable, which means you can change them after you create 
them. You can add new key -value pairs, change existing values, or remove pairs entirely.  
Finally, starting with Python 3.7, dictionaries maintain the order in which you add items. If 
you add "name", then "age", then "major", iterating through the dictionary will give you the 
items in that same order. However, this ordering is a convenience fea ture—you should still 
think of dictionaries as collections where you access items by key, not by position.  
 
Section 2: Creating Dictionaries  
Now that you understand what dictionaries are, let's learn how to create them. Python 
provides several ways to create a dictionary, and each has its own use cases.  
Creating an Empty Dictionary  
The simplest dictionary is an empty one, containing no items. You create an empty 
dictionary using a pair of curly braces with nothing inside:  
empty_dict = {}  
You can verify that this is indeed a dictionary by checking its type:  
empty_dict = {}  
print(type(empty_dict))  
This will output <class 'dict'> , confirming that you've created a dictionary.  
An empty dictionary is useful when you plan to add items to it later, perhaps as you read 
data from a file or receive input from a user. You start with an empty container and fill it as 
you go.  

Creating a Dictionary with Initial Values  
More commonly, you'll create a dictionary that already contains some data. The syntax 
uses curly braces to enclose the entire dictionary, with each key -value pair written as key: 
value, and pairs separated by commas:  
student = {  
    "name": "Alice",  
    "age": 20,  
    "major": "Computer Science"  
} 
Let's break down this syntax carefully. The dictionary starts with an opening curly brace {. 
Then comes the first key -value pair: the key "name" (a string, so it needs quotes), followed 
by a colon :, followed by the value "Alice" (also a string). After this first pair, we have a 
comma , to separate it from the next pair. The pattern continues until all pairs are listed, 
and finally, we close with a curly brace }. 
You can write this dictionary on a single line:  
student = {"name": "Alice", "age": 20, "major": "Computer Science"}  
However, for readability, especially when a dictionary has many items, it's common 
practice to write each key -value pair on its own line, as shown in the first example.  
Understanding Key and Value Types  
In our student example, we've used strings as keys and a mix of strings and numbers as 
values. Let's explore what types of data can be keys and values.  
Keys in a dictionary can be strings, numbers, or tuples (as long as the tuple contains only 
immutable types). Here's an example with different key types:  
mixed_keys = {  
    "name": "Alice",        # string key  
    42: "the answer",       # integer key  
    3.14: "pi",            # float key  
    (0, 0): "origin"       # tuple key  
} 

This dictionary is perfectly valid, though mixing key types like this is unusual in practice. 
Most often, all keys in a single dictionary are the same type, typically strings, because 
they're being used as labels for related data.  
Values can be any Python data type. Here's a dictionary where the values are different 
types:  
student = {  
    "name": "Alice",                    # string value  
    "age": 20,                          # integer value  
    "gpa": 3.8,                         # float value  
    "is_enrolled": True,                # boolean value  
    "courses": ["Math", "Physics"],     # list value  
    "address": {                        # dictionary value  
        "street": "123 Main St",  
        "city": "Boston"  
    } 
} 
This demonstrates that values can even be other dictionaries or lists, allowing you to create 
complex, nested data structures. We'll explore this more in later chapters.  
Creating Dictionaries with the dict() Constructor  
Besides using curly braces, you can also create dictionaries using Python's built -in dict() 
function. This provides alternative ways to construct dictionaries that can be convenient in 
certain situations.  
To create an empty dictionary:  
empty_dict = dict()  
This does exactly the same thing as empty_dict = {} . 
You can create a dictionary with initial values using keyword arguments:  
student = dict(name="Alice", age=20, major="Computer Science")  

Notice that when using this syntax, the keys don't have quotes around them. They're 
written as keyword arguments, which means they must follow Python's rules for variable 
names (no spaces, can't start with a number, etc.). The dict() function takes these keyword 
arguments and creates string keys from them. The result is equivalent to:  
student = {"name": "Alice", "age": 20, "major": "Computer Science"}  
Another way to use dict() is with a list of tuples, where each tuple contains a key and a 
value:  
pairs = [("name", "Alice"), ("age", 20), ("major", "Computer Science")]  
student = dict(pairs)  
This creates the same dictionary as before. Each tuple in the list must have exactly two 
elements: the first is the key, the second is the value.  
When should you use curly braces versus the dict() constructor? In most cases, curly 
braces are more readable and conventional. However, dict() is useful when you're 
dynamically building dictionaries from existing data, such as a list of tuples that you've 
generated or received from another function.  
Common Mistakes When Creating Dictionaries  
As you start working with dictionaries, be aware of some common mistakes beginners 
make.  
First, don't confuse dictionaries with sets. An empty dictionary is {}, but a set with no 
elements is set() (you cannot create an empty set with {}). If you write my_set = {1, 2, 3} , 
you've created a set, not a dictionary. Dictionaries must have key -value pairs with colons, 
while sets just have values.  
this_is_a_set = {1, 2, 3}              # set (no colons)  
this_is_a_dict = {1: "one", 2: "two"}  # dictionary (has colons)  
Second, remember that keys must be immutable. You cannot use a list as a key:  
# This will cause an error!  
bad_dict = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'  
We'll discuss why this restriction exists later in this chapter.  
Third, make sure you use colons ( :) to separate keys from values, not equal signs ( =). This is 
a syntax error:  

# Wrong - this is not valid Python  
bad_dict = {"name" = "Alice"}  # SyntaxError  
 
# Correct - use a colon  
good_dict = {"name": "Alice"}  
 
Section 3: Accessing Dictionary Values  
Once you've created a dictionary, you need to be able to retrieve the values stored in it. 
Python provides straightforward ways to access dictionary values using their keys.  
Using Square Bracket Notation  
The most direct way to access a value in a dictionary is to use square brackets with the key, 
similar to how you access list elements by index:  
student = {  
    "name": "Alice",  
    "age": 20,  
    "major": "Computer Science"  
} 
 
print(student["name"])   # Outputs: Alice  
print(student["age"])    # Outputs: 20  
print(student["major"])  # Outputs: Computer Science  
When you write student["name"] , Python looks up the key "name" in the dictionary and 
returns its associated value, which is "Alice". This lookup operation is very fast, even for 
large dictionaries, making dictionaries efficient for retrieving data.  
You can use the retrieved value in any way you would use that type of value. For example, 
since student["age"]  returns the integer 20, you can use it in calculations:  
years_until_graduation = 4 - (student["age"] - 18) 

print(f"{student['name']} has {years_until_graduation} years until graduation")  
You can also store retrieved values in variables:  
student_name = student["name"]  
student_major = student["major"]  
 
print(f"{student_name} is studying {student_major}")  
The KeyError Problem  
What happens if you try to access a key that doesn't exist in the dictionary? Python raises a 
KeyError: 
student = {  
    "name": "Alice",  
    "age": 20  
} 
 
print(student["grade"])  # KeyError: 'grade'  
This error tells you that the key "grade" is not in the dictionary. It's similar to trying to access 
an index that doesn't exist in a list, which raises an IndexError . 
A KeyError will stop your program from running, which can be a problem if you're not sure 
whether a key exists. For example, if you're reading data from a file where some records 
might be missing certain fields, you don't want your entire program to crash just becaus e 
one record doesn't have a particular key.  
Using the get() Method for Safe Access  
To avoid KeyError exceptions, Python dictionaries provide a method called get(). This 
method attempts to retrieve a value for a given key, but if the key doesn't exist, it returns 
None instead of raising an error:  
student = {  
    "name": "Alice",  
    "age": 20  

} 
 
grade = student.get("grade")  
print(grade)  # Outputs: None  
print(type(grade))  # Outputs: <class 'NoneType'>  
The value None is a special Python value that represents "nothing" or "no value." It's often 
used to indicate the absence of data. When get() returns None, you know that the key 
wasn't found, but your program continues running without an error.  
You can also provide a default value as a second argument to get(). If the key doesn't exist, 
get() will return your default value instead of None: 
student = {  
    "name": "Alice",  
    "age": 20  
} 
 
grade = student.get("grade", "Not assigned")  
print(grade)  # Outputs: Not assigned  
 
major = student.get("major", "Undeclared")  
print(major)  # Outputs: Undeclared  
This is very useful when you want to provide meaningful fallback values. For example, if a 
student's major isn't specified, you might want to use "Undeclared" as the default rather 
than None. 
An important point: when the key does exist, get() works exactly like bracket notation:  
student = {  
    "name": "Alice",  
    "age": 20  

} 
 
name = student.get("name", "Unknown")  
print(name)  # Outputs: Alice (not "Unknown", because the key exists)  
The default value is only used when the key is missing.  
Choosing Between Bracket Notation and get()  
Now that you know both methods for accessing dictionary values, when should you use 
each one?  
Use bracket notation ( dict[key]) when you expect the key to definitely exist, and it would be 
a programming error if it didn't. If the key is missing, the KeyError will alert you to the 
problem immediately. This is useful during development when you want to catch mistakes 
in your code.  
Use get() when it's normal for a key to potentially be missing, and you want to handle that 
gracefully. For example, when processing user input or data from external sources, not all 
expected fields might be present. In these cases, get() lets your program continue running 
and handle missing data appropriately.  
Here's an example that illustrates the difference:  
def display_student_basic(student):  
    """Display basic student info - we expect these fields to exist"""  
    print(f"Name: {student['name']}")  # Use bracket notation  
    print(f"Age: {student['age']}")    # Will raise KeyError if missing  
    print(f"Major: {student['major']}")  
 
def display_student_complete(student):  
    """Display complete info - some fields might be optional"""  
    print(f"Name: {student['name']}")  # Required field  
    print(f"Age: {student['age']}")    # Required field  
    print(f"Major: {student['major']}")  # Required field  

     
    # Optional fields - use get() with defaults  
    gpa = student.get("gpa", "N/A")  
    print(f"GPA: {gpa}")  
     
    email = student.get("email", "Not provided")  
    print(f"Email: {email}")  
Checking if a Key Exists  
Sometimes you want to check whether a key exists before trying to access it. Python 
provides the in operator for this purpose:  
student = {  
    "name": "Alice",  
    "age": 20,  
    "major": "Computer Science"  
} 
 
if "age" in student:  
    print(f"Student's age is {student['age']}")  
 
if "grade" not in student:  
    print("Grade not recorded")  
The in operator returns True if the key exists in the dictionary and False if it doesn't. You can 
use it in if statements to make decisions based on whether certain data is present.  
This is particularly useful when you need to take different actions depending on whether a 
key exists:  
if "gpa" in student:  
    print(f"Current GPA: {student['gpa']}")  

else:  
    print("GPA not yet calculated")  
    student["gpa"] = 0.0  # Initialize it  
Note that the in operator checks for keys, not values. If you want to check whether a value 
exists, you need to use a different approach (we'll learn about that when we cover 
dictionary methods).  
 
Section 4: Adding and Modifying Dictionary Items  
Dictionaries are mutable, meaning you can change them after creation. You can add new 
key-value pairs, update existing values, or remove items entirely. Let's explore each of 
these operations.  
Adding New Items  
To add a new item to a dictionary, you simply assign a value to a new key using bracket 
notation:  
student = {  
    "name": "Alice",  
    "age": 20  
} 
 
print(student)  # {'name': 'Alice', 'age': 20}  
 
student["major"] = "Computer Science"  
print(student)  # {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}  
When you write student["major"] = "Computer Science" , Python checks if the key "major" 
exists. Since it doesn't, Python creates a new key -value pair and adds it to the dictionary. 
The key is "major" and the value is "Computer Science" . 
You can add as many new items as you want:  
student["gpa"] = 3.8  

student["year"] = "Junior"  
student["student_id"] = "A12345"  
 
print(student)  
# {'name': 'Alice', 'age': 20, 'major': 'Computer Science',  
#  'gpa': 3.8, 'year': 'Junior', 'student_id': 'A12345'}  
Updating Existing Values  
To update an existing value, you use the same syntax as adding a new item —simply assign 
a new value to an existing key:  
student = {  
    "name": "Alice",  
    "age": 20,  
    "gpa": 3.7  
} 
 
print(student["gpa"])  # 3.7  
 
student["gpa"] = 3.8  # Update the GPA  
print(student["gpa"])  # 3.8  
When Python sees student["gpa"] = 3.8 , it checks if the key "gpa" already exists. Since it 
does, Python replaces the old value 3.7 with the new value 3.8. 
This is an important point: the same syntax is used for both adding new items and 
updating existing ones . Python looks at whether the key exists or not and behaves 
accordingly. If the key exists, the value is updated. If the key doesn't exist, a new key -value 
pair is added.  
Here's an example that demonstrates both operations:  
grades = {"test1": 85, "test2": 90}  

 
grades["test3"] = 88  # Adding new item (test3 doesn't exist)  
grades["test1"] = 87  # Updating existing item (test1 exists)  
 
print(grades)  # {'test1': 87, 'test2': 90, 'test3': 88}  
Modifying Values Based on Current Values  
You can also update a value based on its current value. This is common when you're doing 
calculations or building up data incrementally:  
inventory = {  
    "apples": 50,  
    "bananas": 30,  
    "oranges": 45  
} 
 
# Sell 10 apples  
inventory["apples"] = inventory["apples"] - 10 
print(inventory["apples"])  # 40  
 
# Restock bananas - using shorthand operator  
inventory["bananas"] += 20  
print(inventory["bananas"])  # 50  
The shorthand operators ( +=, -=, *=, etc.) work with dictionary values just as they do with 
variables. The line inventory["bananas"] += 20  is equivalent to inventory["bananas"] = 
inventory["bananas"] + 20 . 
 
Section 5: Removing Dictionary Items  

Just as you can add items to a dictionary, you can also remove them. Python provides 
several ways to delete items from dictionaries.  
Using the del Statement  
The del statement removes a key -value pair from a dictionary:  
student = {  
    "name": "Alice",  
    "age": 20,  
    "major": "Computer Science",  
    "temp_note": "Remind to update address"  
} 
 
del student["temp_note"]  
print(student)  
# {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}  
When you write del student["temp_note"] , Python removes the entire key -value pair from 
the dictionary. Both the key and its value are deleted.  
If you try to delete a key that doesn't exist, Python raises a KeyError: 
student = {"name": "Alice", "age": 20}  
del student["grade"]  # KeyError: 'grade'  
This is similar to the error you get when accessing a non -existent key. To avoid this error, 
you can check if the key exists before deleting it:  
if "grade" in student:  
    del student["grade"]  
else:  
    print("Grade key doesn't exist")  
Using the pop() Method  

The pop() method provides a safer way to remove items. It removes a key -value pair and 
returns the value:  
student = {  
    "name": "Alice",  
    "age": 20,  
    "major": "Computer Science"  
} 
 
age = student.pop("age")  
print(f"Removed age: {age}")  # Removed age: 20  
print(student)  # {'name': 'Alice', 'major': 'Computer Science'}  
The advantage of pop() over del is that it returns the value, which you can use if needed. 
Additionally, pop() allows you to specify a default value to return if the key doesn't exist:  
student = {"name": "Alice", "major": "Computer Science"}  
 
# This won't raise an error  
grade = student.pop("grade", "Not found")  
print(grade)  # Not found  
print(student)  # Student dictionary unchanged since key didn't exist  
If you don't provide a default value and the key doesn't exist, pop() will raise a KeyError just 
like bracket notation.  
Using the popitem() Method  
The popitem()  method removes and returns the last inserted key -value pair as a tuple:  
student = {  
    "name": "Alice",  
    "age": 20,  
    "major": "Computer Science"  

} 
 
last_item = student.popitem()  
print(last_item)  # ('major', 'Computer Science')  
print(student)  # {'name': 'Alice', 'age': 20}  
Before Python 3.7, popitem()  removed an arbitrary item because dictionaries were 
unordered. Starting with Python 3.7, since dictionaries maintain insertion order, popitem()  
always removes the last added item.  
If you call popitem()  on an empty dictionary, it raises a KeyError. 
Using the clear() Method  
If you want to remove all items from a dictionary at once, use the clear() method:  
student = {  
    "name": "Alice",  
    "age": 20,  
    "major": "Computer Science"  
} 
 
student.clear()  
print(student)  # {}  
After calling clear(), the dictionary still exists but contains no items. It's an empty 
dictionary.  
Deleting the Dictionary Itself  
Finally, you can delete the dictionary entirely using del with just the dictionary name:  
student = {"name": "Alice", "age": 20}  
del student  
# Now the variable 'student' doesn't exist at all  
# print(student)  # This would raise: NameError: name 'student' is not defined  

This is different from clear(). With clear(), the dictionary exists but is empty. With del, the 
variable itself is removed, and trying to use it will cause a NameError . 
 
Section 6: Dictionary Length and Membership  
Two common operations when working with dictionaries are checking how many items 
they contain and determining whether specific keys exist.  
Finding Dictionary Length  
To find out how many key -value pairs a dictionary contains, use the built -in len() function:  
student = {  
    "name": "Alice",  
    "age": 20,  
    "major": "Computer Science",  
    "gpa": 3.8  
} 
 
num_items = len(student)  
print(f"The dictionary has {num_items} items")  # The dictionary has 4 items  
The len() function counts the number of key -value pairs. An empty dictionary has a length 
of 0: 
empty = {}  
print(len(empty))  # 0  
This is useful when you're building dictionaries dynamically and want to check if they 
contain data:  
grades = {}  
 
if len(grades) == 0:  
    print("No grades recorded yet")  

else:  
    print(f"{len(grades)} grades recorded")  
Checking for Key Membership  
As we learned earlier, the in operator checks whether a key exists in a dictionary:  
student = {  
    "name": "Alice",  
    "age": 20,  
    "major": "Computer Science"  
} 
 
if "name" in student:  
    print("Name is present")  # This will print  
 
if "grade" not in student:  
    print("Grade is not present")  # This will print  
The in operator returns True or False, making it perfect for conditional statements. You can 
also use it directly in Boolean expressions:  
has_gpa = "gpa" in student  
print(has_gpa)  # False  
 
missing_email = "email" not in student  
print(missing_email)  # True  
Remember that in only checks for keys, not values. To check if a particular value exists in a 
dictionary, you'll need to use different techniques that we'll learn when we cover dictionary 
methods.  
 
Section 7: Understanding Dictionary Keys  

Now that you understand the basic operations with dictionaries, let's dive deeper into an 
important topic: what can and cannot be used as dictionary keys.  
The Immutability Requirement  
We've mentioned several times that dictionary keys must be immutable. But what does this 
mean, and why is it necessary?  
Immutable means "cannot be changed." In Python, some data types are immutable —once 
you create them, you cannot modify them. Other types are mutable —you can change them 
after creation.  
Immutable types include:  
• Strings ("hello")  
• Numbers (integers like 42, floats like 3.14)  
• Tuples ((1, 2, 3))  
• Booleans ( True, False)  
Mutable types include:  
• Lists ([1, 2, 3])  
• Dictionaries ( {"key": "value"} )  
• Sets ({1, 2, 3})  
Only immutable types can be dictionary keys. This means you can use strings, numbers, 
and tuples as keys, but you cannot use lists, dictionaries, or sets as keys.  
Here are examples of valid dictionary keys:  
valid_dict = {  
    "name": "Alice",           # string key  
    42: "the answer",          # integer key  
    3.14: "pi",               # float key  
    (0, 0): "origin",         # tuple key  
    True: "yes"               # boolean key  
} 

 
print(valid_dict["name"])       # Alice  
print(valid_dict[42])           # the answer  
print(valid_dict[(0, 0)])      # origin  
Now, let's see what happens if you try to use a mutable type as a key:  
# This will cause an error!  
invalid_dict = {  
    [1, 2, 3]: "list key"     # TypeError: unhashable type: 'list'  
} 
Python raises a TypeError  with the message "unhashable type: 'list'." The word 
"unhashable" is important —it's directly related to why keys must be immutable.  
Why Keys Must Be Immutable: Understanding Hashing  
To understand why keys must be immutable, we need to understand a bit about how 
dictionaries work internally. When you create a dictionary and add key -value pairs, Python 
needs a way to store these pairs in memory so that later, when you ask for a value, i t can 
find it quickly.  
Python uses a technique called hashing to achieve this. A hash is a number that Python 
calculates from the key. This hash determines where in memory the key -value pair is 
stored. When you later access the dictionary using that key, Python calculates the hash 
again and uses it to find the store d value instantly.  
Here's a simple analogy: imagine a library where books are stored on shelves numbered 0 
through 99. When a new book arrives, the librarian looks at the book's title and uses a 
formula to calculate which shelf number it should go on. For example, they might  add up 
the letter positions of the title and take the remainder when divided by 100. Later, when 
someone wants to find that book, the librarian uses the same formula on the title to 
calculate the shelf number and goes directly to that shelf.  
This system works great, but there's one critical requirement: the book's title cannot 
change. If the title could change after the book was shelved, then using the formula on the 
new title would give a different shelf number, and the book would be "lost" e ven though it's 
still in the library.  

The same principle applies to dictionary keys. The hash value calculated from a key must 
always be the same for that key. If a key could change, its hash would change, and Python 
wouldn't be able to find the value anymore.  
Immutable types guarantee that an object's value never changes, which means its hash 
never changes. This is why only immutable types can be dictionary keys.  
The Special Case of Tuples  
Tuples can be used as keys because they're immutable, but there's a catch: if a tuple 
contains any mutable elements, you can't use it as a key:  
# Valid - tuple contains only immutable elements  
valid_key = (1, 2, "three")  
point_dict = {valid_key: "location A"}  
print(point_dict[(1, 2, "three")])  # location A  
 
# Invalid - tuple contains a mutable element (a list)  
invalid_key = (1, 2, [3, 4])  
# This will cause an error:  
# bad_dict = {invalid_key: "value"}  # TypeError: unhashable type: 'list'  
The tuple itself is immutable —you can't change what's in it. However, if it contains a list, 
that list is mutable and could change, which would affect the hash. Python detects this and 
prevents you from using such tuples as keys.  
Practical Implications  
In practice, the most common types you'll use as dictionary keys are strings and numbers, 
particularly strings. Most of the time, you're creating dictionaries where keys represent 
labels or names for data:  
person = {  
    "first_name": "Alice",  
    "last_name": "Johnson",  
    "age": 20,  

    "email": "alice@example.com"  
} 
Sometimes you'll use numbers, particularly when mapping IDs to information:  
students_by_id = {  
    101: "Alice Johnson",  
    102: "Bob Smith",  
    103: "Charlie Brown"  
} 
Using tuples as keys is less common but useful in specific situations, such as when you 
need to map coordinate pairs to values:  
grid = {  
    (0, 0): "origin",  
    (1, 0): "right",  
    (0, 1): "up",  
    (1, 1): "diagonal"  
} 
 
print(grid[(1, 0)])  # right  
 
Section 8: Dictionary Methods  
Python dictionaries come with a variety of built -in methods that make working with them 
more convenient and powerful. Let's explore the most important and commonly used 
methods.  
The keys() Method  
The keys() method returns a view of all the keys in a dictionary. This view gives you access 
to all the keys without creating a separate list:  
student = {  

    "name": "Alice",  
    "age": 20,  
    "major": "Computer Science",  
    "gpa": 3.8  
} 
 
keys = student.keys()  
print(keys)  # dict_keys(['name', 'age', 'major', 'gpa'])  
The result is a special dictionary view object, not a list. However, you can use it in many of 
the same ways you use a list. For example, you can iterate over it:  
for key in student.keys():  
    print(key)  
This will print each key on a separate line. Note that you can actually iterate over a 
dictionary directly without calling keys(), and the result is the same:  
for key in student:  
    print(key)  
Both approaches iterate over the keys. However, explicitly using keys() can make your code 
more readable by making it clear that you're working with keys.  
If you need an actual list of keys (for example, to sort them or index them), you can convert 
the view to a list:  
keys_list = list(student.keys())  
print(keys_list)  # ['name', 'age', 'major', 'gpa']  
print(keys_list[0])  # name  
The keys() method is particularly useful when you want to check what keys exist in a 
dictionary during development or debugging.  
The values() Method  
The values() method returns a view of all the values in a dictionary:  

student = {  
    "name": "Alice",  
    "age": 20,  
    "major": "Computer Science",  
    "gpa": 3.8  
} 
 
values = student.values()  
print(values)  # dict_values(['Alice', 20, 'Computer Science', 3.8])  
Like keys(), this returns a view object. You can iterate over it to access each value:  
for value in student.values():  
    print(value)  
This will print:  
Alice  
20 
Computer Science  
3.8 
One useful application of values() is checking whether a specific value exists anywhere in 
the dictionary. Remember that the in operator checks keys by default, but you can use it 
with values() to check for values:  
if "Alice" in student.values():  
    print("Alice is one of the values in this dictionary")  
You can also convert the values view to a list:  
values_list = list(student.values())  
print(values_list)  # ['Alice', 20, 'Computer Science', 3.8]  
This is useful when you need to perform operations that require a list, such as finding the 
maximum value when all values are numbers:  

test_scores = {  
    "test1": 85,  
    "test2": 92,  
    "test3": 88,  
    "final": 95  
} 
 
scores = list(test_scores.values())  
highest_score = max(scores)  
average_score = sum(scores) / len(scores)  
 
print(f"Highest score: {highest_score}")  # 95  
print(f"Average score: {average_score}")  # 90.0  
The items() Method  
The items() method is one of the most useful dictionary methods. It returns a view of all 
key-value pairs in the dictionary, where each pair is represented as a tuple:  
student = {  
    "name": "Alice",  
    "age": 20,  
    "major": "Computer Science"  
} 
 
items = student.items()  
print(items)  
# dict_items([('name', 'Alice'), ('age', 20), ('major', 'Computer Science')])  

Each item in this view is a tuple containing two elements: the key and its corresponding 
value. This method is particularly powerful when used with loops because you can unpack 
both the key and value directly:  
for key, value in student.items():  
    print(f"{key}: {value}")  
This will output:  
name: Alice  
age: 20  
major: Computer Science  
This pattern is very common in Python programs. By using items() and unpacking in the 
loop, you get clean, readable code that processes both keys and values together.  
Here's a practical example that demonstrates the usefulness of items(): 
grades = {  
    "Alice": 92,  
    "Bob": 85,  
    "Charlie": 88,  
    "Diana": 95  
} 
 
print("Grade Report:")  
print("-" * 30)  
for student_name, grade in grades.items():  
    if grade >= 90:  
        letter = "A"  
    elif grade >= 80:  
        letter = "B"  
    else:  

        letter = "C"  
     
    print(f"{student_name}: {grade} ({letter})")  
Like keys() and values(), you can convert the items view to a list:  
items_list = list(student.items())  
print(items_list)  
# [('name', 'Alice'), ('age', 20), ('major', 'Computer Science')]  
This gives you a list of tuples, which can be useful for sorting or other list operations.  
The update() Method  
The update() method allows you to add multiple key -value pairs to a dictionary at once, or 
update multiple existing values:  
student = {  
    "name": "Alice",  
    "age": 20  
} 
 
# Add multiple items at once  
additional_info = {  
    "major": "Computer Science",  
    "gpa": 3.8,  
    "year": "Junior"  
} 
 
student.update(additional_info)  
print(student)  
# {'name': 'Alice', 'age': 20, 'major': 'Computer Science',  

#  'gpa': 3.8, 'year': 'Junior'}  
When you call update() with another dictionary as an argument, Python goes through each 
key-value pair in the argument dictionary and adds it to the original dictionary. If a key 
already exists, its value is replaced with the new value:  
student = {  
    "name": "Alice",  
    "age": 20,  
    "major": "Mathematics"  
} 
 
updates = {  
    "age": 21,  # This will update the existing age  
    "gpa": 3.8  # This will add a new key  
} 
 
student.update(updates)  
print(student)  
# {'name': 'Alice', 'age': 21, 'major': 'Mathematics', 'gpa': 3.8}  
Notice that age was updated from 20 to 21, while gpa was added as a new key.  
The update() method is particularly useful when you're building a dictionary from multiple 
sources or when you need to apply a batch of changes at once. It's more efficient and 
cleaner than updating keys one at a time when you have many updates to make.  
The setdefault() Method  
The setdefault()  method is useful when you want to get a value from a dictionary, but if the 
key doesn't exist, you want to add it with a default value. This is different from get(), which 
doesn't modify the dictionary:  
student = {  
    "name": "Alice",  

    "age": 20  
} 
 
# If the key exists, return its value  
name = student.setdefault("name", "Unknown")  
print(name)  # Alice  
print(student)  # {'name': 'Alice', 'age': 20} - unchanged  
 
# If the key doesn't exist, add it with the default value  
major = student.setdefault("major", "Undeclared")  
print(major)  # Undeclared  
print(student)  # {'name': 'Alice', 'age': 20, 'major': 'Undeclared'} - major added!  
The key difference between get() and setdefault() : 
• get() returns the default value but doesn't change the dictionary  
• setdefault()  returns the default value AND adds the key -value pair to the dictionary  
This method is particularly useful when you're building up dictionaries incrementally and 
want to ensure certain keys exist. A common use case is when creating dictionaries where 
values are lists:  
# Grouping students by major  
students_by_major = {}  
 
# Without setdefault - need to check if key exists  
major = "Computer Science"  
if major not in students_by_major:  
    students_by_major[major] = []  
students_by_major[major].append("Alice")  
 

# With setdefault - much cleaner  
students_by_major.setdefault("Mathematics", []).append("Bob")  
students_by_major.setdefault("Computer Science", []).append("Charlie")  
 
print(students_by_major)  
# {'Computer Science': ['Alice', 'Charlie'], 'Mathematics': ['Bob']}  
In this example, setdefault()  ensures that each major has a list to append to, creating an 
empty list if the major doesn't exist yet.  
The copy() Method  
The copy() method creates a shallow copy of a dictionary. This means it creates a new 
dictionary with the same key -value pairs:  
original = {  
    "name": "Alice",  
    "age": 20,  
    "major": "Computer Science"  
} 
 
copy = original.copy()  
 
# Modify the copy  
copy["age"] = 21  
 
print(original["age"])  # 20 - unchanged  
print(copy["age"])  # 21 - changed  
This is important because simply assigning one dictionary to another doesn't create a 
copy—it creates another reference to the same dictionary:  
original = {"name": "Alice", "age": 20}  

not_a_copy = original  # This is just another name for the same dictionary  
 
not_a_copy["age"] = 21  
print(original["age"])  # 21 - both variables point to the same dictionary!  
When you need an independent copy that you can modify without affecting the original, 
use the copy() method.  
However, be aware that copy() creates a "shallow" copy. This means if your dictionary 
contains mutable objects like lists, those lists are not copied —both dictionaries will 
reference the same lists:  
original = {  
    "name": "Alice",  
    "courses": ["Math", "Physics"]  
} 
 
copy = original.copy()  
copy["courses"].append("Chemistry")  
 
print(original["courses"])  # ['Math', 'Physics', 'Chemistry']  
print(copy["courses"])  # ['Math', 'Physics', 'Chemistry']  
# Both show Chemistry because they share the same list!  
For most introductory use cases, shallow copying is sufficient. We'll discuss deep copying 
in more advanced chapters.  
 
Section 9: When to Use Dictionaries  
Now that you understand how dictionaries work and how to use their methods, let's 
discuss when dictionaries are the right choice compared to other data structures you've 
learned.  
Dictionaries vs. Lists  

Lists and dictionaries serve different purposes, and choosing between them depends on 
how you need to access your data.  
Use a list when:  
• Your data has a natural order that matters  
• You need to access items by their position  
• You want to maintain duplicate values  
• You're storing a collection of similar items (like a list of numbers or names)  
# Good use of a list - items in a specific order  
shopping_list = ["milk", "eggs", "bread", "cheese"]  
print(f"First item to buy: {shopping_list[0]}")  
Use a dictionary when:  
• Your data has natural labels or names  
• You need to look up values by meaningful keys  
• The order of items doesn't define their relationship  
• You're storing related attributes or properties  
# Good use of a dictionary - data accessed by meaningful labels  
student = {  
    "name": "Alice",  
    "age": 20,  
    "major": "Computer Science",  
    "gpa": 3.8  
} 
print(f"Student's major: {student['major']}")  
Sometimes you need both. For example, a list of dictionaries:  
students = [  
    {"name": "Alice", "age": 20, "major": "CS"},  

    {"name": "Bob", "age": 22, "major": "Math"},  
    {"name": "Charlie", "age": 21, "major": "Physics"}  
] 
 
# Access first student's name  
print(students[0]["name"])  # Alice  
This structure is very common when working with collections of records. We'll explore this 
pattern more in the next chapter.  
Dictionaries vs. Tuples  
Tuples are immutable sequences accessed by position, while dictionaries are mutable 
collections accessed by key.  
Use a tuple when:  
• You have a fixed set of values that belong together  
• The position of each value has meaning  
• You don't want the data to change  
# Good use of tuple - coordinates where position matters  
location = (40.7128, -74.0060)  # (latitude, longitude)  
latitude = location[0]  
longitude = location[1]  
Use a dictionary when:  
• You have related data that needs labels  
• You might add, remove, or modify the data  
• Position doesn't define meaning  
# Good use of dictionary - labeled data  
location = {  
    "latitude": 40.7128,  
    "longitude": -74.0060,  

    "city": "New York"  
} 
print(f"City: {location['city']}")  
Dictionaries are more flexible and self -documenting, while tuples are more compact and 
guarantee immutability.  
Real-World Examples  
Let's look at some practical scenarios where dictionaries are the ideal choice:  
Configuration settings:  
settings = {  
    "username": "alice_j",  
    "theme": "dark",  
    "language": "English",  
    "notifications": True,  
    "font_size": 14  
} 
 
if settings["theme"] == "dark":  
    print("Using dark theme")  
Counting occurrences:  
text = "hello world hello python"  
words = text.split()  
 
word_count = {}  
for word in words:  
    word_count[word] = word_count.get(word, 0) + 1  
 

print(word_count)  # {'hello': 2, 'world': 1, 'python': 1}  
Storing contacts:  
contacts = {  
    "Alice": "555 -0001",  
    "Bob": "555 -0002",  
    "Charlie": "555 -0003"  
} 
 
name = "Bob"  
if name in contacts:  
    print(f"{name}'s number is {contacts[name]}")  
Mapping codes to meanings:  
error_messages = {  
    404: "Page not found",  
    500: "Internal server error",  
    403: "Access forbidden",  
    200: "OK"  
} 
 
error_code = 404  
message = error_messages.get(error_code, "Unknown error")  
print(message)  # Page not found  
Each of these examples shows situations where you need to associate one piece of data 
(the key) with another (the value), making dictionaries the natural choice.  
 
Section 10: Common Patterns and Practices  

As you work with dictionaries more, certain patterns and techniques will become second 
nature. Let's explore some common practices that will make your code more effective and 
easier to read.  
Building Dictionaries Incrementally  
Often you'll start with an empty dictionary and build it up as your program runs:  
student_grades = {}  
 
# Add grades as they're recorded  
student_grades["Alice"] = 92  
student_grades["Bob"] = 85  
student_grades["Charlie"] = 88  
 
print(student_grades)  
# {'Alice': 92, 'Bob': 85, 'Charlie': 88}  
This is particularly common when processing data from files or user input:  
def get_student_grades():  
    """Collect student grades from user input"""  
    grades = {}  
     
    while True:  
        name = input("Enter student name (or 'done' to finish): ")  
        if name.lower() == 'done':  
            break  
         
        grade = int(input(f"Enter grade for {name}: "))  
        grades[name] = grade  
     

    return grades  
Using Default Values Effectively  
When you're not sure if a key exists, using get() with a default value often leads to cleaner 
code:  
# Without default - more verbose  
student = {"name": "Alice", "age": 20}  
 
if "email" in student:  
    email = student["email"]  
else:  
    email = "No email provided"  
 
# With default - cleaner  
email = student.get("email", "No email provided")  
This pattern is especially useful in functions that display information:  
def display_contact(contact):  
    """Display contact information with appropriate defaults"""  
    name = contact.get("name", "Unknown")  
    phone = contact.get("phone", "No phone number")  
    email = contact.get("email", "No email address")  
     
    print(f"Name: {name}")  
    print(f"Phone: {phone}")  
    print(f"Email: {email}")  
 
# Works even with incomplete data  

partial_contact = {"name": "Alice", "phone": "555 -0001"}  
display_contact(partial_contact)  
Checking Existence Before Operations  
Before performing operations that might fail, check if keys exist:  
inventory = {  
    "apples": 50,  
    "bananas": 30,  
    "oranges": 20  
} 
 
def sell_item(inventory, item, quantity):  
    """Sell an item if it exists and has enough quantity"""  
    if item not in inventory:  
        print(f"Error: {item} not in inventory")  
        return False  
     
    if inventory[item] < quantity:  
        print(f"Error: Not enough {item}. Only {inventory[item]} available.")  
        return False  
     
    inventory[item] -= quantity  
    print(f"Sold {quantity} {item}")  
    return True  
 
sell_item(inventory, "apples", 10)  # Success  
sell_item(inventory, "grapes", 5)  # Error: not in inventory  

sell_item(inventory, "bananas", 50)  # Error: not enough  
Iterating with Purpose  
Choose the right iteration method based on what you need:  
student = {  
    "name": "Alice",  
    "age": 20,  
    "major": "Computer Science",  
    "gpa": 3.8  
} 
 
# When you only need keys  
for key in student:  
    print(f"Key: {key}")  
 
# When you only need values  
for value in student.values():  
    print(f"Value: {value}")  
 
# When you need both (most common)  
for key, value in student.items():  
    print(f"{key}: {value}")  
Validating Data  
When working with dictionaries that should have specific keys, validate the structure:  
def validate_student(student):  
    """Check if student dictionary has all required fields"""  
    required_fields = ["name", "age", "major"]  

     
    for field in required_fields:  
        if field not in student:  
            print(f"Error: Missing required field '{field}'")  
            return False  
     
    return True  
 
# Valid student  
student1 = {"name": "Alice", "age": 20, "major": "CS"}  
if validate_student(student1):  
    print("Student data is valid")  
 
# Invalid student - missing major  
student2 = {"name": "Bob", "age": 22}  
if not validate_student(student2):  
    print("Student data is invalid")  
 
Practical Examples  
Example 1: Word Frequency Counter  
Let's build a program that counts how often each word appears in a text:  
def count_word_frequency(text):  
    """ 
    Count how many times each word appears in the text.  
    Returns a dictionary with words as keys and counts as values.  
    """ 

    # Convert text to lowercase and split into words  
    words = text.lower().split()  
     
    # Create empty dictionary for counts  
    frequency = {}  
     
    # Count each word  
    for word in words:  
        # Remove common punctuation  
        word = word.strip('.,!?;:"')  
         
        # Skip empty strings  
        if not word:  
            continue  
         
        # Update count using get() with default value  
        frequency[word] = frequency.get(word, 0) + 1  
     
    return frequency  
 
# Test the function  
sample_text = """  
Python is a great programming language. Python is easy to learn.  
Many people choose Python for their first programming language.  
""" 
 

word_counts = count_word_frequency(sample_text)  
 
# Display results  
print("Word Frequency Analysis:")  
print("-" * 40)  
for word, count in word_counts.items():  
    print(f"{word}: {count}")  
This program demonstrates several important concepts:  
• Building a dictionary incrementally  
• Using get() with a default value  
• Iterating with items() to access both keys and values  
• Data cleaning (removing punctuation, converting to lowercase)  
Example 2: Student Grade Manager  
Let's create a simple system to manage student grades:  
def create_grade_book():  
    """Create an empty grade book"""  
    return {}  
 
def add_student(grade_book, name):  
    """Add a new student with an empty grade list"""  
    if name in grade_book:  
        print(f"Student {name} already exists")  
        return False  
     
    grade_book[name] = []  
    print(f"Added student: {name}")  

    return True  
 
def add_grade(grade_book, name, grade):  
    """Add a grade for a student"""  
    if name not in grade_book:  
        print(f"Student {name} not found")  
        return False  
     
    if grade < 0 or grade > 100:  
        print("Grade must be between 0 and 100")  
        return False  
     
    grade_book[name].append(grade)  
    print(f"Added grade {grade} for {name}")  
    return True  
 
def calculate_average(grade_book, name):  
    """Calculate a student's average grade"""  
    if name not in grade_book:  
        return None  
     
    grades = grade_book[name]  
    if len(grades) == 0:  
        return 0.0  
     
    return sum(grades) / len(grades)  

 
def display_grade_book(grade_book):  
    """Display all students and their grades"""  
    if len(grade_book) == 0:  
        print("Grade book is empty")  
        return  
     
    print("\n" + "=" * 50)  
    print("GRADE BOOK")  
    print("=" * 50)  
     
    for name, grades in grade_book.items():  
        average = calculate_average(grade_book, name)  
        print(f"\nStudent: {name}")  
        print(f"Grades: {grades}")  
        print(f"Average: {average:.1f}")  
     
    print("=" * 50)  
 
# Using the grade book system  
grade_book = create_grade_book()  
 
# Add students  
add_student(grade_book, "Alice")  
add_student(grade_book, "Bob")  
add_student(grade_book, "Charlie")  

 
# Add grades  
add_grade(grade_book, "Alice", 92)  
add_grade(grade_book, "Alice", 88)  
add_grade(grade_book, "Alice", 95)  
 
add_grade(grade_book, "Bob", 78)  
add_grade(grade_book, "Bob", 85)  
add_grade(grade_book, "Bob", 82)  
 
add_grade(grade_book, "Charlie", 90)  
add_grade(grade_book, "Charlie", 93)  
 
# Display results  
display_grade_book(grade_book)  
This example shows:  
• Organizing related functions to work with a dictionary  
• Validating input before modifying the dictionary  
• Using dictionaries where values are lists  
• Checking for key existence before operations  
• Calculating statistics from dictionary data  
Example 3: Simple Inventory System  
Let's build an inventory management system for a small store:  
def create_inventory():  
    """Create an empty inventory"""  
    return {}  

 
def add_product(inventory, name, price, quantity):  
    """Add a new product or update existing product"""  
    inventory[name] = {  
        "price": price,  
        "quantity": quantity  
    } 
    print(f"Added/Updated: {name} - ${price:.2f} - Quantity: {quantity}")  
 
def sell_product(inventory, name, quantity):  
    """Sell a product (reduce quantity)"""  
    if name not in inventory:  
        print(f"Error: {name} not found in inventory")  
        return False  
     
    current_qty = inventory[name]["quantity"]  
    if current_qty < quantity:  
        print(f"Error: Not enough {name}. Only {current_qty} available.")  
        return False  
     
    inventory[name]["quantity"] -= quantity  
    total_price = quantity * inventory[name]["price"]  
    print(f"Sold {quantity} {name} for ${total_price:.2f}")  
    return True  
 
def restock_product(inventory, name, quantity):  

    """Add more quantity to an existing product"""  
    if name not in inventory:  
        print(f"Error: {name} not found in inventory")  
        return False  
     
    inventory[name]["quantity"] += quantity  
    new_qty = inventory[name]["quantity"]  
    print(f"Restocked {name}. New quantity: {new_qty}")  
    return True  
 
def get_inventory_value(inventory):  
    """Calculate total value of all inventory"""  
    total = 0  
    for product_info in inventory.values():  
        total += product_info["price"] * product_info["quantity"]  
    return total  
 
def display_inventory(inventory):  
    """Display all products in inventory"""  
    if len(inventory) == 0:  
        print("Inventory is empty")  
        return  
     
    print("\n" + "=" * 70)  
    print("INVENTORY REPORT")  
    print("=" * 70)  

    print(f"{'Product':<20} {'Price':<12} {'Quantity':<10} {'Value':<12}")  
    print("-" * 70)  
     
    for name, info in inventory.items():  
        value = info["price"] * info["quantity"]  
        print(f"{name:<20} ${info['price']:<11.2f} {info['quantity']:<10} ${value:<11.2f}")  
     
    print("-" * 70)  
    total_value = get_inventory_value(inventory)  
    print(f"Total Inventory Value: ${total_value:.2f}")  
    print("=" * 70)  
 
# Using the inventory system  
inventory = create_inventory()  
 
# Add initial stock  
add_product(inventory, "Laptop", 999.99, 10)  
add_product(inventory, "Mouse", 24.99, 50)  
add_product(inventory, "Keyboard", 79.99, 30)  
add_product(inventory, "Monitor", 299.99, 15)  
 
# Display initial inventory  
display_inventory(inventory)  
 
# Perform transactions  
print("\n--- TRANSACTIONS ---") 

sell_product(inventory, "Laptop", 2)  
sell_product(inventory, "Mouse", 5)  
restock_product(inventory, "Keyboard", 10)  
 
# Display updated inventory  
display_inventory(inventory)  
This comprehensive example demonstrates:  
• Nested dictionaries (dictionary values that are themselves dictionaries)  
• Input validation  
• Error handling  
• Calculating totals from dictionary data  
• Formatted output  
• Real-world application of dictionary operations  
 
Practice Exercises  
Exercise 1: Basic Dictionary Operations  
Create a dictionary to store information about your favorite book with keys: title, author, 
year, and genre. Then:  
1. Print the book's title  
2. Add a new key called "rating" with a value from 1 -5  
3. Update the year if it's incorrect  
4. Check if the key "publisher" exists  
5. Print all keys and all values  
Exercise 2: Contact Manager  
Write a program that:  
1. Creates an empty contacts dictionary  

2. Adds at least 3 contacts with keys: name and phone number  
3. Allows looking up a phone number by name  
4. Handles the case where a name doesn't exist  
5. Displays all contacts  
Exercise 3: Grade Calculator  
Create a dictionary where keys are student names and values are lists of test scores. Write 
functions to:  
1. Add a new student  
2. Add a test score for a student  
3. Calculate a student's average  
4. Find the student with the highest average  
5. Display all students and their averages  
Exercise 4: Word Counter  
Write a program that:  
1. Takes a sentence as input  
2. Counts how many times each word appears  
3. Displays the results sorted by frequency (highest first)  
4. Handles punctuation appropriately  
Exercise 5: Menu System  
Create a restaurant menu using a dictionary where keys are item names and values are 
prices. Write a program that:  
1. Displays the menu  
2. Lets users add items to an order (with quantities)  
3. Calculates the total cost  
4. Displays the final bill  
 
Chapter Summary  

In this chapter, you've learned about dictionaries, one of Python's most powerful and 
versatile data structures. Let's review the key concepts:  
What Dictionaries Are:  Dictionaries store data in key -value pairs, allowing you to access 
values using meaningful labels instead of numeric positions. This makes them ideal for 
representing structured data like student records, configuration settings, or any situation 
where dat a has natural names or labels.  
Creating Dictionaries:  You can create dictionaries using curly braces {} with key-value 
pairs separated by colons, or using the dict() constructor. Empty dictionaries serve as 
containers that you build up as your program runs.  
Accessing Values:  Use bracket notation dict[key] to access values directly, or use the 
.get() method to safely access values with default fallbacks. The in operator checks 
whether keys exist.  
Modifying Dictionaries:  Dictionaries are mutable. You can add new key -value pairs, 
update existing values, and remove items using del, .pop(), or .clear(). The same syntax 
handles both adding and updating.  
Key Requirements:  Dictionary keys must be immutable (strings, numbers, tuples) 
because Python uses hashing to store and retrieve values efficiently. This immutability 
guarantees that hash values never change, allowing fast lookups.  
Dictionary Methods:  Python provides powerful methods like .keys(), .values(), .items(), 
.update() , and .setdefault()  that make working with dictionaries convenient and efficient.  
When to Use Dictionaries:  Choose dictionaries over lists when your data has natural 
labels, when you need fast lookups by key, or when position doesn't define the meaning of 
your data. Dictionaries are perfect for configuration, counting, mapping, and representing 
structured recor ds. 
Common Patterns:  Effective use of dictionaries involves building them incrementally, 
using default values appropriately, validating data, and choosing the right iteration method 
for your needs.  
As you continue programming in Python, dictionaries will become one of your most -used 
tools. They appear everywhere —in web development for handling JSON data, in data 
analysis for organizing information, and in everyday programming for managing 
configurati on and state. The skills you've developed in this chapter form the foundation for 
working with more complex data structures in the coming chapters.  
 

Reflection Questions  
Take a moment to think about what you've learned and how it connects to what you already 
know:  
1. Connection to Previous Knowledge:  How are dictionaries similar to and different 
from the lists you learned about earlier? When would you choose one over the 
other?    
2. Real-World Applications:  Think of three situations in your daily life where 
dictionary -like organization would be useful. How would you structure the data 
using Python dictionaries?    
3. Key Concepts:  Why do you think Python requires dictionary keys to be immutable? 
How does this relate to the way dictionaries work internally?    
4. Problem -Solving: If you needed to store information about 100 students, each with 
a name, ID number, major, and list of courses, how would you organize this data? 
Would you use lists, dictionaries, or both? Why?    
5. Code Design:  When writing a function that works with dictionaries, what should you 
consider to make it robust and handle missing keys appropriately?    
 
Looking Ahead  
In the next chapter, we'll explore lists of dictionaries , a powerful pattern that combines 
what you've learned about both data structures. You'll see how to manage collections of 
records, like a class roster where each student is represented by a dictionary. This pattern 
bridges the gap between basic data struc tures and the object -oriented programming 
concepts you'll learn later in the course.  
The skills you've developed with dictionaries will also be essential when you learn about:  
• Working with JSON data from files and web APIs  
• Processing structured data in real -world applications  
• Understanding how objects and classes work (dictionaries and objects are more 
similar than you might think!)  
• Building more complex programs that manage different types of data  
Keep practicing with dictionaries. Try creating small programs that solve real problems —a 
personal contact book, a study schedule manager, or a simple inventory tracker. The more 

you work with dictionaries, the more natural they'll become, and you'll start recognizing 
situations where they're the perfect tool for the job.  
 
Additional Practice Problems  
Beginner Level  
Problem 1: Personal Information  Create a dictionary to store your personal information 
including: name, age, city, favorite_food, and favorite_color. Then:  
• Print each piece of information in a formatted way  
• Add a new key for "hobby"  
• Change your age to one year older  
• Remove the favorite_color key  
• Print the final dictionary  
Problem 2: Simple Calculator History  Create a dictionary to store calculator operations 
where keys are operation names ("addition", "subtraction", etc.) and values are the count of 
how many times each operation was used. Write code to:  
• Initialize the dictionary with all operations set to 0  
• Increment the count when an operation is performed  
• Display the operation that was used most frequently  
Problem 3: Student Record  Create a dictionary for a student with keys: name, student_id, 
major, and credits_completed. Write a program that:  
• Creates the student dictionary  
• Checks if the student has enough credits to graduate (120 or more)  
• Adds a "graduation_status" key with value "Eligible" or "Not Eligible"  
• Prints a formatted report  
Intermediate Level  
Problem 4: Classroom Roster  Create a dictionary where keys are student names and 
values are their grades. Write a program that:  
• Adds 5 students with their grades  

• Calculates the class average  
• Finds and displays the highest and lowest grades  
• Counts how many students are passing (grade >= 60)  
• Updates a student's grade if it was entered incorrectly  
Problem 5: Product Catalog  Create a product catalog dictionary where keys are product 
names and values are dictionaries containing price and category. Write functions to:  
• Add a new product  
• Update a product's price  
• Find all products in a specific category  
• Calculate the average price of all products  
• Find the most expensive product  
Problem 6: Letter Frequency  Write a program that:  
• Takes a sentence as input  
• Creates a dictionary counting how many times each letter appears (ignore case and 
spaces)  
• Displays the results in alphabetical order  
• Shows which letter appears most frequently  
Challenge Level  
Problem 7: Multi -Level Dictionary  Create a dictionary representing a school with multiple 
classes. Each class is a dictionary containing teacher name and a list of students. Write a 
program that:  
• Creates this nested structure for at least 3 classes  
• Finds the total number of students across all classes  
• Lists all unique teacher names  
• Displays which class has the most students  
• Adds a new student to a specific class  

Problem 8: Data Transformation  Given a dictionary where values are lists of numbers, 
write a program that:  
• Calculates the average of each list  
• Creates a new dictionary with the same keys but averages as values  
• Sorts the new dictionary by values (highest to lowest)  
• Displays the results in a formatted table  
Problem 9: Dictionary Validation  Write a function that validates whether a dictionary has 
the correct structure for a specific use case. For example, validating that a "person" 
dictionary has all required fields (name, age, email) and that:  
• The name is a non -empty string  
• The age is a positive integer between 0 and 150  
• The email contains an @ symbol  
• Return True if valid, False with an error message if not  
 
Common Mistakes and How to Avoid Them  
As you work with dictionaries, watch out for these common pitfalls:  
Mistake 1: Forgetting that keys are case -sensitive  
student = {"Name": "Alice", "age": 20}  
print(student["name"])  # KeyError! Should be "Name" with capital N  
Solution:  Be consistent with your key naming. Use lowercase for all keys or establish a 
clear convention.  
Mistake 2: Trying to use mutable types as keys  
my_dict = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'  
Solution:  Only use immutable types (strings, numbers, tuples) as keys.  
Mistake 3: Modifying a dictionary while iterating over it  
grades = {"Alice": 85, "Bob": 92, "Charlie": 78}  
for name in grades:  

    if grades[name] < 80:  
        del grades[name]  # RuntimeError: dictionary changed size during iteration  
Solution:  Create a list of keys to remove first, then remove them in a separate loop.  
Mistake 4: Confusing assignment with copying  
original = {"a": 1, "b": 2}  
not_a_copy = original  
not_a_copy["a"] = 100  
print(original["a"])  # 100 - both variables reference the same dictionary!  
Solution:  Use .copy() when you need an independent copy.  
Mistake 5: Not handling missing keys  
student = {"name": "Alice"}  
print(student["grade"])  # KeyError: 'grade'  
Solution:  Use .get() with a default value, check with in, or use try/except.  
 
Tips for Writing Clean Dictionary Code  
As you become more comfortable with dictionaries, keep these best practices in mind:  
1. Use descriptive key names  
# Poor - unclear keys  
data = {"n": "Alice", "a": 20, "m": "CS"}  
 
# Good - clear, descriptive keys  
student = {"name": "Alice", "age": 20, "major": "Computer Science"}  
2. Be consistent with key naming  
# Poor - inconsistent naming  
person = {"firstName": "Alice", "last_name": "Johnson", "Age": 20}  
 

# Good - consistent snake_case  
person = {"first_name": "Alice", "last_name": "Johnson", "age": 20}  
3. Document expected dictionary structure  
def process_student(student):  
    """ 
    Process a student record.  
     
    Expected dictionary structure:  
    { 
        "name": str,  
        "age": int,  
        "major": str,  
        "gpa": float  
    } 
    """ 
    # function code here  
4. Use meaningful variable names  
# Poor  
d = {"name": "Alice", "age": 20}  
for k, v in d.items():  
    print(k, v)  
 
# Good  
student = {"name": "Alice", "age": 20}  
for key, value in student.items():  
    print(key, value)  

5. Group related functions  
# Instead of scattered functions, organize related operations  
def create_contact(name, phone):  
    return {"name": name, "phone": phone}  
 
def validate_contact(contact):  
    return "name" in contact and "phone" in contact  
 
def display_contact(contact):  
    print(f"Name: {contact['name']}")  
    print(f"Phone: {contact['phone']}")  
 
Debugging Dictionary Code  
When your dictionary code doesn't work as expected, try these debugging strategies:  
Strategy 1: Print the entire dictionary  
student = {"name": "Alice", "age": 20}  
print(student)  # See the complete contents  
print(type(student))  # Verify it's a dictionary  
Strategy 2: Check what keys exist  
student = {"name": "Alice", "age": 20}  
print(student.keys())  # See all keys  
print("grade" in student)  # Check if specific key exists  
Strategy 3: Verify key types  
# Keys are case -sensitive and type -sensitive  
grades = {"test1": 90, 1: 85}  
print(grades["test1"])  # Works  

print(grades[1])  # Works  
# print(grades["1"])  # KeyError - string "1" is different from integer 1  
Strategy 4: Use try/except during development  
student = {"name": "Alice", "age": 20}  
 
try: 
    print(student["grade"])  
except KeyError as e:  
    print(f"KeyError: {e}")  
    print(f"Available keys: {student.keys()}")  
Strategy 5: Check for unexpected mutations  
def test_function(data):  
    original = data.copy()  # Make a copy to compare  
    # ... do operations on data ...  
    print(f"Original: {original}")  
    print(f"Modified: {data}")  
 
Quick Reference Guide  
Here's a handy reference for the dictionary operations you've learned:  
Creating Dictionaries:  
empty = {}  
empty = dict()  
student = {"name": "Alice", "age": 20}  
student = dict(name="Alice", age=20)  
Accessing Values:  
value = my_dict[key]  

value = my_dict.get(key)  
value = my_dict.get(key, default_value)  
Adding/Updating:  
my_dict[key] = value  
my_dict.update(other_dict)  
my_dict.setdefault(key, default_value)  
Removing Items:  
del my_dict[key]  
value = my_dict.pop(key)  
value = my_dict.pop(key, default_value)  
item = my_dict.popitem()  
my_dict.clear()  
Checking Keys:  
if key in my_dict:  
if key not in my_dict:  
keys = my_dict.keys()  
Getting Values:  
values = my_dict.values()  
items = my_dict.items()  
Other Operations:  
length = len(my_dict)  
copy = my_dict.copy()  
Iteration:  
for key in my_dict:  
for value in my_dict.values():  
for key, value in my_dict.items():  

 
Vocabulary Review  
Make sure you understand these key terms from this chapter:  
• Dictionary : A mutable collection that stores data in key -value pairs  
• Key: A unique, immutable identifier used to access a value in a dictionary  
• Value: The data associated with a key in a dictionary  
• Key-Value Pair : A single entry in a dictionary consisting of a key and its associated 
value  
• Immutable : Cannot be changed after creation (required for dictionary keys)  
• Mutable : Can be changed after creation (describes dictionaries themselves)  
• Hash/Hashing : The process Python uses internally to quickly locate keys in a 
dictionary  
• Method: A function that belongs to and operates on a specific data type  
• View Object : A dynamic view of dictionary keys, values, or items that updates when 
the dictionary changes  
• Membership Test : Using the in operator to check if a key exists in a dictionary  
• Default Value : A fallback value used when a key doesn't exist (with .get() or 
.setdefault() )  
 
Self-Assessment  
Before moving on to the next chapter, make sure you can:  
✓ Explain what a dictionary is and when to use it instead of a list ✓ Create dictionaries 
using both {} notation and dict() ✓ Access values using bracket notation and the .get() 
method ✓ Add new key -value pairs to a dictionary ✓ Update existing values in a dictionary 
✓ Remove items using del, .pop(), and .clear() ✓ Check if a key exists using the in operator 
✓ Explain why dictionary keys must be immutable ✓ Use .keys(), .values(), and .items() 
methods ✓ Iterate over dictionaries using for loops ✓ Choose app ropriate error handling 
strategies for missing keys ✓ Write functions that work with dictionaries ✓ Solve real -world 
problems using dictionaries  

If you're unsure about any of these concepts, review the relevant sections of this chapter 
and practice with the exercises provided.  
 
Congratulations on completing Chapter 20! You've learned a fundamental data structure 
that you'll use throughout your programming journey. Dictionaries are everywhere in 
Python, and mastering them opens the door to more advanced programming concepts. In 
the next chapter, you'll combine dictionaries with lists to manage collections of structured 
data—an essential skill for working with real -world information.  
Keep practicing, and remember: the best way to learn is by doing. Try building small 
projects that use dictionaries, and don't be afraid to experiment and make mistakes. That's 
how you truly learn!  

