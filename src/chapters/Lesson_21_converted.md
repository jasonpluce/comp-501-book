Lesson 21: Lists of Dictionaries  
 
Owner: Nazari, Mujtaba  
Reviewer: Al Shaikhli, Ihab  
• Complex data structures  
• Nested data  
• Data organization  
Lists of Dictionaries - From Data Structures to Objects  
 
Learning Objectives  
By the end of this chapter, you will be able to:  
1. Create lists of dictionaries to represent collections of structured records  
2. Access and modify data within nested list -dictionary structures  
3. Implement  CRUD (Create, Read, Update, Delete) operations on collections of 
records  
4. Apply filtering and searching techniques to find specific records  
5. Sort lists of dictionaries using single and multiple criteria  
6. Group and aggregate  data to compute statistics and summaries  
7. Convert between Python dictionaries and JSON format for data exchange  
8. Navigate  nested data structures safely and efficiently  
9. Validate data schemas to ensure consistency across records  
10. Recognize  the conceptual bridge between dictionary -based patterns and object -
oriented programming  
 
Introduction: From Single Records to Collections  
In Chapter 20, you learned how to use dictionaries to represent a single entity —one 
student, one product, or one book —with labeled fields that make your code self -
documenting and easy to understand. You discovered that instead of remembering that 

index 0 is a name and index 1 is an age, you can simply use keys like student["name"]  and 
student["age"] . This makes your code much clearer and less error -prone.  
But what happens when you need to manage not just one student, but an entire 
classroom? Not just one product, but a complete inventory? Not just one book, but an 
entire library? This is where lists of dictionaries  become essential. By combining the 
organizational power of lists (which maintain order and allow iteration) with the clarity of 
dictionaries (which provide labeled access to data), you can build powerful data 
management systems that mirror real -world coll ections.  
Think of a list of dictionaries as a spreadsheet or database table. Each dictionary 
represents one row in the table, with consistent column names (keys) across all rows. The 
list holds all these rows together, allowing you to process them as a collection. This pattern 
appears everywhere in programming: student rosters, product catalogs, employee 
databases, transaction records, and countless other applications where you need to 
manage multiple records with the same structure.  
Throughout this chapter, you will learn not only how to work with lists of dictionaries, but 
also how this pattern prepares you for object -oriented programming. The techniques you 
master here —organizing data, validating structure, implementing operations —will transfer 
directly to working with objects and classes in later chapters. You are building foundational 
skills that will serve you throughout your programming journey.  
 
Section 1: Understanding Lists of Dictionaries  
1.1 Why Use Lists of Dictionaries?  
Before diving into the technical details, let's understand why lists of dictionaries are such a 
common and powerful pattern in Python programming. When you work with data in the real 
world, you rarely deal with isolated pieces of information. Instead, you encounter 
collections of related records that share the same structure.  
Consider a school administration system. The school needs to track information about 
hundreds or thousands of students. Each student has the same type of information: a 
name, an age, a grade level, a GPA, and enrolled courses. You could try to manage this with 
separate lists —one for names, one for ages, one for GPAs —but this quickly becomes a 
maintenance nightmare. What happens when you need to add a new student? You must 
remember to add entries to all the lists in the correct positions. What happens when y ou 
need to remove a student? You must remember to remove the corresponding entries from 
every single list. One mistake, and your data becomes misaligned and corrupted.  

Lists of dictionaries solve this problem elegantly. Each dictionary represents one complete 
student record, with all the information bundled together. The list simply holds these 
records in order. When you add a new student, you add one dictionary to the l ist. When you 
remove a student, you remove one dictionary. Everything stays synchronized because each 
record is a self -contained unit. This mirrors how databases work —each row in a database 
table is complete and independent, with clearly labeled columns.  
Let's look at a concrete example:  
# A single student record (dictionary)  
student = {  
    "name": "Alice Johnson",  
    "age": 20,  
    "major": "Computer Science",  
    "gpa": 3.8,  
    "year": 2  
} 
 
# A collection of student records (list of dictionaries)  
students = [  
    {"name": "Alice Johnson", "age": 20, "major": "Computer Science", "gpa": 3.8, "year": 2},  
    {"name": "Bob Martinez", "age": 22, "major": "Mathematics", "gpa": 3.6, "year": 3},  
    {"name": "Charlie Davis", "age": 21, "major": "Physics", "gpa": 3.9, "year": 3},  
    {"name": "Diana Lee", "age": 19, "major": "Biology", "gpa": 3.7, "year": 1}  
] 
Notice how each dictionary in the students  list has exactly the same keys: "name", "age", 
"major", "gpa", and "year". This consistency is crucial. It means you can write code that 
processes any student record in the same way, without needing to know which specific 
student you are working with. You can loop through all students and access their GPAs with 
confidence that every dictionary will have a "gpa" key.  

This pattern offers several important advantages. First, it provides structured 
organization . Each record is a complete, self -contained unit with clearly labeled fields. 
You don't have to remember what position each piece of data occupies —the keys tell you 
exactly what each value represents. Second, it offers easy access . You can retrieve any 
specific record by its index in the list, then access any field within that record by its key. 
Third, it is scalable . Adding more records is as simple as appending more dictionaries to 
the list, regardless of whether you have ten records or ten thousand. Fourth, it uses 
familiar syntax . You already know how to work with lists and dictionaries separately, so 
combining them requires only understanding how to chain the access operations together. 
Finally, it provides preparation for objects . This pattern maps directly to working with lists 
of objects in object -oriented programming, making your future learning easier.  
Let's see another practical example with a product inventory:  
products = [  
    {"id": 101, "name": "Laptop", "price": 999.99, "quantity": 15, "category": "Electronics"},  
    {"id": 102, "name": "Mouse", "price": 24.99, "quantity": 50, "category": "Electronics"},  
    {"id": 103, "name": "Desk", "price": 299.99, "quantity": 8, "category": "Furniture"},  
    {"id": 104, "name": "Chair", "price": 199.99, "quantity": 12, "category": "Furniture"},  
    {"id": 105, "name": "Monitor", "price": 349.99, "quantity": 20, "category": "Electronics"}  
] 
This inventory system demonstrates the real -world applicability of lists of dictionaries. 
Each product is a dictionary with consistent fields: an ID for unique identification, a name, 
a price, a quantity in stock, and a category for organization. The list holds all products 
together, allowing the business to process inventory as a complete collection. They can 
calculate total inventory value, identify low -stock items, generate reports by category, and 
perform countless other operations —all because the data is organized in this structured, 
consistent way.  
1.2 The One -Dictionary -Per-Record Principle  
A fundamental principle when working with lists of dictionaries is that each dictionary 
represents exactly one complete record . This might seem obvious, but understanding 
this principle deeply will help you avoid common mistakes and design better data 
structures.  

What does "one complete record" mean? It means that each dictionary should contain all 
the information about a single entity. If you are modeling students, each dictionary 
represents one student with all their attributes. If you are modeling products, each  
dictionary represents one product with all its details. You should not split a single entity 
across multiple dictionaries in the list, and you should not combine multiple entities into 
one dictionary.  
Consider this incorrect approach:  
# INCORRECT: Splitting one student across multiple dictionaries  
students = [  
    {"name": "Alice Johnson"},  
    {"age": 20},  
    {"gpa": 3.8}  
] 
This violates the one -dictionary -per-record principle. Here, we have three dictionaries, but 
they don't represent three students —they represent fragments of one student's 
information split across three separate records. This makes the data nearly impossibl e to 
work with. How do you know which age belongs to which name? How do you keep 
everything synchronized when you add or remove students?  
The correct approach keeps each student's complete information together:  
# CORRECT: Each dictionary is one complete student record  
students = [  
    {"name": "Alice Johnson", "age": 20, "gpa": 3.8},  
    {"name": "Bob Martinez", "age": 22, "gpa": 3.6},  
    {"name": "Charlie Davis", "age": 21, "gpa": 3.9}  
] 
Now each dictionary stands alone as a complete, independent record. You can add, 
remove, modify, or process any student without affecting the others. The data structure 
makes logical sense and reflects the real -world relationship between entities and their  
attributes.  
Similarly, consider this incorrect approach that combines multiple entities:  

# INCORRECT: Combining multiple students into one dictionary  
students_data = {  
    "alice": {"age": 20, "gpa": 3.8},  
    "bob": {"age": 22, "gpa": 3.6},  
    "charlie": {"age": 21, "gpa": 3.9}  
} 
While this structure has its uses (we will explore nested dictionaries later), it is not a list of 
dictionaries. If you need to iterate over students in a specific order, maintain a sequence, or 
easily add and remove records, this structure is more cumbers ome than a list of 
dictionaries. The list -of-dictionaries pattern is specifically designed for managing ordered 
collections of records that share a common structure.  
1.3 Ensuring Consistent Structure  
When working with lists of dictionaries, one of your primary responsibilities is ensuring that 
all dictionaries in the list have the same structure —the same keys with compatible value 
types. Without this consistency, your code becomes fragile and error -prone. Imagine trying 
to process student records where some have a "name" key while others have a 
"student_name"  key, or where some have "gpa" as a number while others have it as a string. 
Your code would need constant checks and special cases, making it comp licated and 
unreliable.  
Let's examine the problem:  
# PROBLEMATIC: Inconsistent structures  
students = [  
    {"name": "Alice", "age": 20, "gpa": 3.8},  
    {"name": "Bob", "age": 22},  # Missing "gpa" key  
    {"full_name": "Charlie", "age": 21, "gpa": 3.9},  # Wrong key name  
    {"name": "Diana", "age": "19", "gpa": 3.7}  # Age is a string, not a number  
] 
 
# This code will fail  

for student in students:  
    print(f"{student['name']} has a GPA of {student['gpa']}")  
# KeyError when processing Bob (missing "gpa")  
# KeyError when processing Charlie (missing "name")  
This inconsistency creates problems throughout your code. Every time you access a 
dictionary value, you risk encountering a missing key or an unexpected data type. Your 
code must constantly check whether keys exist and validate data types, adding complexit y 
and slowing development.  
The solution is to enforce consistency from the start. You can achieve this through several 
techniques. The most common approach is using a factory function —a function 
dedicated to creating dictionaries with the correct structure:  
def create_student(name, age, gpa, major="Undecided"):  
    """ 
    Create a student dictionary with a consistent structure.  
     
    This function ensures every student has all required fields  
    with the correct data types. It also provides a default value  
    for the major field in case it is not specified.  
     
    Parameters:  
        name (str): The student's full name  
        age (int): The student's age in years  
        gpa (float): The student's grade point average (0.0 -4.0)  
        major (str): The student's declared major (default: "Undecided")  
     
    Returns:  
        dict: A dictionary representing the student with all required fields  

    """ 
    return {  
        "name": name,  
        "age": age,  
        "gpa": gpa,  
        "major": major  
    } 
 
# Create students using the factory function  
students = []  
students.append(create_student("Alice Johnson", 20, 3.8, "Computer Science"))  
students.append(create_student("Bob Martinez", 22, 3.6, "Mathematics"))  
students.append(create_student("Charlie Davis", 21, 3.9))  # Uses default major  
 
# All students now have the exact same structure  
for student in students:  
    print(f"{student['name']} ({student['major']}) - GPA: {student['gpa']}")  
The factory function approach has multiple benefits. It serves as a single source of truth for 
what a student record should look like. It prevents typos in key names because you only 
type them once, in the function definition. It allows you to set default values for optional 
fields. It makes your code more maintainable because if you need to add a new field to all 
students, you only modify the factory function. And it makes your intent clear —anyone 
reading your code immediately understands that this functio n creates properly structured 
student records.  
You can also add validation to your factory function to catch errors early:  
def create_student(name, age, gpa, major="Undecided"):  
    """ 
    Create a validated student dictionary.  

     
    Raises:  
        TypeError: If parameters have incorrect types  
        ValueError: If parameter values are invalid  
    """ 
    # Validate types  
    if not isinstance(name, str):  
        raise TypeError("Student name must be a string")  
    if not isinstance(age, int):  
        raise TypeError("Student age must be an integer")  
    if not isinstance(gpa, (int, float)):  
        raise TypeError("Student GPA must be a number")  
    if not isinstance(major, str):  
        raise TypeError("Student major must be a string")  
     
    # Validate values  
    if age < 0 or age > 120:  
        raise ValueError("Student age must be between 0 and 120")  
    if gpa < 0.0 or gpa > 4.0:  
        raise ValueError("Student GPA must be between 0.0 and 4.0")  
    if not name.strip():  
        raise ValueError("Student name cannot be empty")  
     
    return {  
        "name": name,  
        "age": age,  

        "gpa": gpa,  
        "major": major  
    } 
 
# Try to create an invalid student  
try: 
    invalid_student = create_student("", -5, 5.0)  
except ValueError as e:  
    print(f"Validation error: {e}")  
    # Output: Validation error: Student name cannot be empty  
This validation ensures that you catch data problems immediately when creating records, 
rather than discovering them later when your code tries to process invalid data. The early 
detection makes debugging much easier and prevents bad data from contaminatin g your 
collection.  
 
Section 2: Creating and Accessing Lists of Dictionaries  
2.1 Three Methods of Creation  
There are three primary methods for creating lists of dictionaries, each with its own use 
cases and advantages. Understanding all three methods gives you flexibility to choose the 
most appropriate approach for each situation.  
Method 1: Direct Definition with List Literals  
The most straightforward method is defining the entire list of dictionaries in one statement 
using Python's list literal syntax. This method works well when you know all the data 
upfront and the list is not too long:  
students = [  
    {"name": "Alice Johnson", "age": 20, "major": "Computer Science", "gpa": 3.8},  
    {"name": "Bob Martinez", "age": 22, "major": "Mathematics", "gpa": 3.6},  
    {"name": "Charlie Davis", "age": 21, "major": "Physics", "gpa": 3.9}  

] 
This method is clear and concise. You can see the entire data structure at a glance, which 
makes it excellent for small datasets, test data, or examples. The visual layout of the code 
matches the tabular structure of the data, making it easy to verify that  each record has the 
correct fields. However, this method becomes unwieldy for large datasets or when data 
comes from user input or external sources.  
Method 2: Incremental Building with append()  
The second method starts with an empty list and builds it incrementally by appending 
dictionaries one at a time. This method is ideal when you are collecting data gradually, 
such as reading from user input or processing data from a file:  
students = []  # Start with an empty list  
 
# Add students one at a time  
students.append({"name": "Alice Johnson", "age": 20, "major": "Computer Science", "gpa": 
3.8})  
students.append({"name": "Bob Martinez", "age": 22, "major": "Mathematics", "gpa": 3.6})  
students.append({"name": "Charlie Davis", "age": 21, "major": "Physics", "gpa": 3.9})  
This method offers flexibility. You can add records conditionally based on logic, validate 
each record before adding it, or build the list through user interaction. It is particularly 
useful when the final size of the list is unknown at the start of the pr ogram:  
students = []  
 
# Collect student data from user input  
while True:  
    name = input("Enter student name (or 'done' to finish): ")  
    if name.lower() == 'done':  
        break  
     
    age = int(input("Enter student age: "))  

    major = input("Enter student major: ")  
    gpa = float(input("Enter student GPA: "))  
     
    # Create and add the student record  
    student = {"name": name, "age": age, "major": major, "gpa": gpa}  
    students.append(student)  
 
print(f"Collected information for {len(students)} students")  
Method 3: Using a Factory Function  
The third method combines the advantages of the previous two by using a factory function 
to ensure consistency while building the list incrementally. This is generally the best 
practice for production code:  
def create_student(name, age, major, gpa):  
    """Factory function to create a properly structured student dictionary"""  
    return {  
        "name": name,  
        "age": age,  
        "major": major,  
        "gpa": gpa  
    } 
 
# Build the list using the factory function  
students = []  
students.append(create_student("Alice Johnson", 20, "Computer Science", 3.8))  
students.append(create_student("Bob Martinez", 22, "Mathematics", 3.6))  
students.append(create_student("Charlie Davis", 21, "Physics", 3.9))  
 

# Or create the list directly if you have all the data  
students = [  
    create_student("Alice Johnson", 20, "Computer Science", 3.8),  
    create_student("Bob Martinez", 22, "Mathematics", 3.6),  
    create_student("Charlie Davis", 21, "Physics", 3.9)  
] 
This method ensures consistency while maintaining flexibility. The factory function 
guarantees that every dictionary has the same structure, regardless of how or when it is 
created. You can add validation to the factory function once, and all records benefi t from 
that validation. If you need to change the structure later (for example, adding a new field), 
you only modify the factory function rather than hunting through your code for every place 
you create a dictionary.  
All three methods produce identical results —a list containing dictionaries with the same 
structure. The method you choose depends on your specific situation: use Method 1 for 
simple, small datasets where all data is known upfront; use Method 2 when buildin g the list 
dynamically; and use Method 3 when you want the benefits of both flexibility and 
consistency.  
2.2 Accessing Data in Nested Structures  
Once you have created a list of dictionaries, you need to know how to access the data 
stored within this nested structure. The key is understanding that you are chaining two 
operations together: first, you access an element from the list (using an index), which gives 
you a dictionary; then, you access a value from that dictionary (using a key).  
Let's start with a simple example:  
students = [  
    {"name": "Alice Johnson", "age": 20, "major": "Computer Science", "gpa": 3.8},  
    {"name": "Bob Martinez", "age": 22, "major": "Mathematics", "gpa": 3.6},  
    {"name": "Charlie Davis", "age": 21, "major": "Physics", "gpa": 3.9}  
] 
 
# Access the first student's name  

first_student_name = students[0]["name"]  
print(first_student_name)  # Output: Alice Johnson  
Let's break down what happens in the expression students[0]["name"] . First, Python 
evaluates students[0] . The square brackets with the index 0 tell Python to access the first 
element of the students  list. Since lists are zero -indexed, 0 refers to the first element. This 
operation returns a dictionary: {"name": "Alice Johnson", "age": 20, "major": "Computer 
Science", "gpa": 3.8} . 
Next, Python evaluates ["name"]  on the dictionary it just retrieved. The square brackets 
with the string key "name" tell Python to look up the value associated with the key "name" 
in the dictionary. This operation returns the string "Alice Johnson" . 
The entire expression students[0]["name"]  can be read as: "Go to the students list, get the 
element at index 0 (which is a dictionary), and from that dictionary, get the value 
associated with the key 'name'." This two -step process is how you navigate nested 
structures in Python.  
Let's look at more examples to reinforce this pattern:  
# Access the second student's major  
second_student_major = students[1]["major"]  
print(second_student_major)  # Output: Mathematics  
 
# Access the last student's GPA (using negative indexing)  
last_student_gpa = students[ -1]["gpa"]  
print(last_student_gpa)  # Output: 3.9  
 
# Access and compute with the data  
first_student_age = students[0]["age"]  
next_year_age = first_student_age + 1  
print(f"Next year, {students[0]['name']} will be {next_year_age}")  
# Output: Next year, Alice Johnson will be 21  
You can also chain multiple operations to create more complex expressions:  

# Create a formatted string using multiple accesses  
print(f"{students[0]['name']} is studying {students[0]['major']} with a GPA of 
{students[0]['gpa']}")  
# Output: Alice Johnson is studying Computer Science with a GPA of 3.8  
 
# Compare two students  
if students[0]['gpa'] > students[1]['gpa']:  
    print(f"{students[0]['name']} has a higher GPA than {students[1]['name']}")  
# Output: Alice Johnson has a higher GPA than Bob Martinez  
2.3 Iterating Through Records  
While accessing individual records is useful, the real power of lists of dictionaries emerges 
when you iterate through the entire collection. Python's for loop makes this straightforward 
and natural.  
The basic pattern for iteration is:  
students = [  
    {"name": "Alice Johnson", "age": 20, "major": "Computer Science", "gpa": 3.8},  
    {"name": "Bob Martinez", "age": 22, "major": "Mathematics", "gpa": 3.6},  
    {"name": "Charlie Davis", "age": 21, "major": "Physics", "gpa": 3.9}  
] 
 
# Iterate through all students  
for student in students:  
    print(f"Name: {student['name']}")  
    print(f"Age: {student['age']}")  
    print(f"Major: {student['major']}")  
    print(f"GPA: {student['gpa']}")  
    print()  # Print a blank line for spacing  

In this loop, the variable student takes on the value of each dictionary in the list, one at a 
time. On the first iteration, student is {"name": "Alice Johnson", "age": 20, "major": 
"Computer Science", "gpa": 3.8} . On the second iteration, student is {"name": "Bob 
Martinez", "age": 22, "major": "Mathematics", "gpa": 3.6} . And so on. Within the loop body, 
you can access any field of the current student dictionary using student["key"] . 
This pattern is extremely common and powerful. It allows you to process every record in 
the collection with the same code, regardless of how many records exist. Whether you have 
three students or three thousand, the same loop works unchanged.  
You can perform various operations within the loop:  
# Calculate and display each student's status  
for student in students:  
    if student['gpa'] >= 3.7:  
        status = "Dean's List"  
    elif student['gpa'] >= 3.0:  
        status = "Good Standing"  
    else:  
        status = "Academic Probation"  
     
    print(f"{student['name']}: {status}")  
# Output:  
# Alice Johnson: Dean's List  
# Bob Martinez: Good Standing  
# Charlie Davis: Dean's List  
Sometimes you need both the index and the value. Python's enumerate()  function provides 
this:  
# Display students with their position numbers  
for index, student in enumerate(students):  
    print(f"Student #{index + 1}: {student['name']}")  

# Output:  
# Student #1: Alice Johnson  
# Student #2: Bob Martinez  
# Student #3: Charlie Davis  
The enumerate()  function returns pairs of (index, value) for each element in the list. The 
index starts at 0 by default, so we add 1 when displaying to create human -friendly 
numbering that starts at 1.  
You can also iterate to collect or transform data:  
# Create a list of all student names  
names = []  
for student in students:  
    names.append(student['name'])  
print(names)  
# Output: ['Alice Johnson', 'Bob Martinez', 'Charlie Davis']  
 
# Or use a more Pythonic list comprehension  
names = [student['name'] for student in students]  
print(names)  
# Output: ['Alice Johnson', 'Bob Martinez', 'Charlie Davis']  
The list comprehension [student['name'] for student in students]  is a compact way to 
transform a list of dictionaries into a list of values extracted from those dictionaries. It is 
equivalent to the for loop that builds the list incrementally, but written in a single, readable 
line. List comprehensions are a powerful P ython feature that we will use extensively when 
filtering and transforming data.  
 
Section 3: CRUD Operations on Collections  
CRUD stands for Create, Read, Update, and Delete —the four fundamental operations you 
perform on data in any system. Whether you are building a simple student roster or a 

complex e -commerce platform, these four operations form the core of data management. 
In this section, you will learn how to implement each operation for lists of dictionaries, 
building a solid foundation for working with structured data.  
3.1 Create: Adding New Records  
Creating new records means adding new dictionaries to your list. The most common 
method is using the append()  method, which adds a dictionary to the end of the list. As 
discussed earlier, you should use a factory function to ensure consistency:  
def create_student(name, age, major, gpa):  
    """Factory function for creating student dictionaries"""  
    return {  
        "name": name,  
        "age": age,  
        "major": major,  
        "gpa": gpa  
    } 
 
students = [  
    create_student("Alice Johnson", 20, "Computer Science", 3.8),  
    create_student("Bob Martinez", 22, "Mathematics", 3.6)  
] 
 
# Add a new student  
new_student = create_student("Diana Lee", 19, "Biology", 3.7)  
students.append(new_student)  
 
print(f"Total students: {len(students)}")  # Output: Total students: 3  

You can wrap the creation process in a function that handles both creating the dictionary 
and adding it to the list:  
def add_student(students, name, age, major, gpa):  
    """ 
    Add a new student to the list.  
     
    Parameters:  
        students (list): The list of student dictionaries  
        name (str): Student's name  
        age (int): Student's age  
        major (str): Student's major  
        gpa (float): Student's GPA  
     
    Returns:  
        dict: The newly created student dictionary  
    """ 
    new_student = create_student(name, age, major, gpa)  
    students.append(new_student)  
    print(f"Added student: {name}")  
    return new_student  
 
# Use the function  
students = []  
add_student(students, "Alice Johnson", 20, "Computer Science", 3.8)  
add_student(students, "Bob Martinez", 22, "Mathematics", 3.6)  
add_student(students, "Charlie Davis", 21, "Physics", 3.9)  

 
print(f"Current roster: {len(students)} students")  
This approach encapsulates the creation logic, making your main code cleaner and easier 
to maintain. The function returns the newly created student, which can be useful if you 
need to perform additional operations on it immediately after creation.  
Sometimes you need to add a record at a specific position rather than at the end. Python's 
insert() method accomplishes this:  
# Insert a student at the beginning of the list  
students.insert(0, create_student("Adam Wilson", 20, "Chemistry", 3.5))  
 
# Insert a student at a specific position (index 2, which will be the third position)  
students.insert(2, create_student("Eve Taylor", 21, "Engineering", 3.6))  
The insert() method takes two arguments: the index where you want to insert the element, 
and the element itself. Remember that existing elements shift to make room for the new 
element. Using insert() is less common than append()  because most collections do not 
require a specific order during creation, but it is useful when order matters.  
3.2 Read: Finding and Displaying Records  
Reading operations involve accessing data from your collection. This can range from 
displaying all records to finding specific records that match certain criteria.  
Displaying All Records:  
The most basic read operation is displaying all records in a formatted way. Let's create a 
function that presents student data in an organized, readable format:  
def display_all_students(students):  
    """ 
    Display all students in a formatted table.  
     
    Parameters:  
        students (list): List of student dictionaries to display  

    """ 
    if not students:  
        print("No students to display")  
        return  
     
    # Print header  
    print("\n" + "=" * 70)  
    print("STUDENT ROSTER")  
    print("=" * 70)  
    print(f"{'Name':<25} {'Age':<5} {'Major':<20} {'GPA':<5}")  
    print("-" * 70)  
     
    # Print each student  
    for student in students:  
        print(f"{student['name']:<25} {student['age']:<5} {student['major']:<20} 
{student['gpa']:<5}")  
     
    print("=" * 70)  
    print(f"Total students: {len(students)}")  
    print()  
 
# Test the function  
students = [  
    create_student("Alice Johnson", 20, "Computer Science", 3.8),  
    create_student("Bob Martinez", 22, "Mathematics", 3.6),  
    create_student("Charlie Davis", 21, "Physics", 3.9)  

] 
 
display_all_students(students)  
This function demonstrates several important programming practices. First, it checks 
whether the list is empty before attempting to display anything, preventing errors and 
providing helpful feedback. Second, it uses formatted strings with alignment specifi ers 
(:<25 means left -align in a field of 25 characters) to create neat, table -like output. Third, it 
separates the display logic into its own function, making the code modular and reusable.  
Finding Specific Records:  
Often you need to find a specific record based on some criterion. The most common 
approach is searching by a unique identifier or name:  
def find_student_by_name(students, name):  
    """ 
    Find a student by their name.  
     
    Parameters:  
        students (list): List of student dictionaries  
        name (str): Name to search for (case -insensitive)  
     
    Returns:  
        dict or None: The student dictionary if found, None otherwise  
    """ 
    # Convert search name to lowercase for case -insensitive comparison  
    name_lower = name.lower()  
     
    for student in students:  
        if student['name'].lower() == name_lower:  

            return student  
     
    # If we get here, the student was not found  
    return None  
 
# Test the function  
students = [  
    create_student("Alice Johnson", 20, "Computer Science", 3.8),  
    create_student("Bob Martinez", 22, "Mathematics", 3.6),  
    create  
create_student("Charlie Davis", 21, "Physics", 3.9)  
] 
 
# Find a student  
found = find_student_by_name(students, "Bob Martinez")  
if found:  
    print(f"Found: {found['name']}, Major: {found['major']}, GPA: {found['gpa']}")  
else:  
    print("Student not found")  
# Output: Found: Bob Martinez, Major: Mathematics, GPA: 3.6  
 
# Try to find a non -existent student  
not_found = find_student_by_name(students, "David Lee")  
if not_found:  
    print(f"Found: {not_found['name']}")  
else:  

    print("Student 'David Lee' not found")  
# Output: Student 'David Lee' not found  
This function demonstrates an important pattern in search operations: returning None 
when the item is not found. This allows the calling code to check whether the search was 
successful using a simple if statement. The function also implements case -insensitive 
searching by converting both the search term and the stored names to lowercase before 
comparing, making the search more user -friendly.  
You can create variations of this function to search by other criteria:  
def find_student_by_id(students, student_id):  
    """ 
    Find a student by their ID number.  
     
    This assumes students have an 'id' field in their dictionary.  
    """ 
    for student in students:  
        if student.get('id') == student_id:  
            return student  
    return None  
 
def find_students_by_major(students, major):  
    """ 
    Find all students in a specific major.  
     
    Returns:  
        list: A list of student dictionaries matching the major  
    """ 
    matching_students = []  

    for student in students:  
        if student['major'].lower() == major.lower():  
            matching_students.append(student)  
    return matching_students  
 
# Test finding by major  
students = [  
    create_student("Alice Johnson", 20, "Computer Science", 3.8),  
    create_student("Bob Martinez", 22, "Mathematics", 3.6),  
    create_student("Charlie Davis", 21, "Physics", 3.9),  
    create_student("Diana Lee", 19, "Computer Science", 3.7)  
] 
 
cs_students = find_students_by_major(students, "Computer Science")  
print(f"Found {len(cs_students)} Computer Science students:")  
for student in cs_students:  
    print(f"  - {student['name']} (GPA: {student['gpa']})")  
# Output:  
# Found 2 Computer Science students:  
#   - Alice Johnson (GPA: 3.8)  
#   - Diana Lee (GPA: 3.7)  
Notice the difference between find_student_by_name()  and find_students_by_major() . The 
first function returns a single dictionary (or None), because names are typically unique. The 
second function returns a list of dictionaries, because multiple students can have the 
same major. This distinction is important when designing search functions —consider 
whether you expect multiple matches or just  one.  
3.3 Update: Modifying Existing Records  

Update operations involve changing data within existing dictionaries. You can update a 
single field or multiple fields at once. The key is first finding the record you want to modify, 
then changing the appropriate values.  
Updating a Single Field:  
Let's create a function that updates a student's GPA:  
def update_student_gpa(students, name, new_gpa):  
    """ 
    Update a student's GPA.  
     
    Parameters:  
        students (list): List of student dictionaries  
        name (str): Name of the student to update  
        new_gpa (float): New GPA value  
     
    Returns:  
        bool: True if student was found and updated, False otherwise  
    """ 
    # Find the student  
    for student in students:  
        if student['name'].lower() == name.lower():  
            # Store old value for reporting  
            old_gpa = student['gpa']  
            # Update the GPA  
            student['gpa'] = new_gpa  
            print(f"Updated {name}'s GPA from {old_gpa} to {new_gpa}")  
            return True  
     

    # Student not found  
    print(f"Student '{name}' not found")  
    return False  
 
# Test the function  
students = [  
    create_student("Alice Johnson", 20, "Computer Science", 3.8),  
    create_student("Bob Martinez", 22, "Mathematics", 3.6),  
    create_student("Charlie Davis", 21, "Physics", 3.9)  
] 
 
# Update Alice's GPA  
update_student_gpa(students, "Alice Johnson", 3.9)  
# Output: Updated Alice Johnson's GPA from 3.8 to 3.9  
 
# Verify the change  
alice = find_student_by_name(students, "Alice Johnson")  
print(f"Alice's current GPA: {alice['gpa']}")  # Output: Alice's current GPA: 3.9  
 
# Try to update a non -existent student  
update_student_gpa(students, "David Lee", 3.5)  
# Output: Student 'David Lee' not found  
An important aspect of this function is that it modifies the dictionary in place. When you 
change student['gpa'] , you are modifying the dictionary that exists in the students  list. This 
is because Python passes dictionaries by reference —the student variable in the loop refers 
to the same dictionary object that is stored in the list, not a copy of it. Therefore, changes 
made to student directly affect the list.  

Updating Multiple Fields:  
Sometimes you need to update several fields at once. You can use Python's **kwargs  
(keyword arguments) to create a flexible update function:  
def update_student_info(students, name, **updates):  
    """ 
    Update multiple fields for a student.  
     
    Parameters:  
        students (list): List of student dictionaries  
        name (str): Name of the student to update  
        **updates: Keyword arguments representing fields to update  
     
    Returns:  
        bool: True if student was found and updated, False otherwise  
     
    Example:  
        update_student_info(students, "Alice", age=21, major="Data Science")  
    """ 
    # Find the student  
    for student in students:  
        if student['name'].lower() == name.lower():  
            # Update each field provided in the updates  
            for field, value in updates.items():  
                if field in student:  
                    student[field] = value  
                else:  

                    print(f"Warning: Student does not have field '{field}', skipping")  
             
            print(f"Updated {name}'s information")  
            return True  
     
    # Student not found  
    print(f"Student '{name}' not found")  
    return False  
 
# Test updating multiple fields  
students = [  
    create_student("Alice Johnson", 20, "Computer Science", 3.8),  
    create_student("Bob Martinez", 22, "Mathematics", 3.6)  
] 
 
# Update multiple fields at once  
update_student_info(students, "Alice Johnson", age=21, gpa=3.9)  
# Output: Updated Alice Johnson's information  
 
# Verify the changes  
alice = find_student_by_name(students, "Alice Johnson")  
print(f"Alice's updated info: Age {alice['age']}, GPA {alice['gpa']}")  
# Output: Alice's updated info: Age 21, GPA 3.9  
 
# Try to update a field that doesn't exist  
update_student_info(students, "Bob Martinez", age=23, email="bob@email.com")  

# Output:  
# Warning: Student does not have field 'email', skipping  
# Updated Bob Martinez's information  
This function demonstrates the power and flexibility of Python's **kwargs  syntax. The 
**updates  parameter collects any keyword arguments passed to the function into a 
dictionary. You can then iterate over this dictionary to update each specified field. The 
function includes a safety check to warn you if you try to update a field that does not exist 
in the student dictionary, but it continues with the other updates. This design choice 
depends on your needs —you could instead raise an error if an invalid field  is provided, or 
you could allow adding new fields dynamically.  
Important Note About Update Behavior:  
When you call update_student_info()  with fields that don't exist in the student dictionary, 
the function skips those fields rather than adding them. This is intentional to maintain 
schema consistency —all students should have the same fields. If you wanted to allow 
adding new fields, you cou ld modify the function:  
def update_student_info_flexible(students, name, **updates):  
    """ 
    Update or add fields for a student (more flexible, but less safe).  
    """ 
    for student in students:  
        if student['name'].lower() == name.lower():  
            # Update or add each field  
            for field, value in updates.items():  
                student[field] = value  # This will add the field if it doesn't exist  
            print(f"Updated {name}'s information")  
            return True  
     
    print(f"Student '{name}' not found")  
    return False  

However, this flexibility comes at a cost: your students could end up with inconsistent 
structures if you are not careful. In most cases, maintaining strict schema consistency is 
preferable.  
3.4 Delete: Removing Records  
Delete operations involve removing dictionaries from the list. There are several approaches 
depending on whether you want to remove by value, by index, or based on some criterion.  
Deleting by Matching Value:  
The most common approach is finding a record by some identifying value (like a name or 
ID) and removing it:  
def delete_student_by_name(students, name):  
    """ 
    Remove a student from the list by name.  
     
    Parameters:  
        students (list): List of student dictionaries  
        name (str): Name of the student to remove  
     
    Returns:  
        bool: True if student was found and removed, False otherwise  
    """ 
    # Iterate with enumerate to get both index and value  
    for index, student in enumerate(students):  
        if student['name'].lower() == name.lower():  
            # Remove the student using pop() with the index  
            removed_student = students.pop(index)  
            print(f"Removed student: {removed_student['name']}")  
            return True  

     
    # Student not found  
    print(f"Student '{name}' not found")  
    return False  
 
# Test the function  
students = [  
    create_student("Alice Johnson", 20, "Computer Science", 3.8),  
    create_student("Bob Martinez", 22, "Mathematics", 3.6),  
    create_student("Charlie Davis", 21, "Physics", 3.9),  
    create_student("Diana Lee", 19, "Biology", 3.7)  
] 
 
print(f"Initial student count: {len(students)}")  # Output: Initial student count: 4  
 
# Delete a student  
delete_student_by_name(students, "Bob Martinez")  
# Output: Removed student: Bob Martinez  
 
print(f"Student count after deletion: {len(students)}")  # Output: Student count after 
deletion: 3  
 
# Verify Bob is gone  
remaining_names = [student['name'] for student in students]  
print(f"Remaining students: {remaining_names}")  
# Output: Remaining students: ['Alice Johnson', 'Charlie Davis', 'Diana Lee']  

This function uses enumerate()  to get both the index and the student dictionary during 
iteration. Once it finds the matching student, it uses pop(index)  to remove the dictionary at 
that position. The pop() method both removes the element and returns it, which is useful 
for logging or confirmation messages.  
Important Consideration: Modifying a List During Iteration  
You might be tempted to remove items directly while iterating, like this:  
# PROBLEMATIC CODE - DO NOT USE  
for student in students:  
    if student['name'] == "Bob":  
        students.remove(student)  # Modifying list during iteration  
This can cause problems because you are modifying the list while iterating over it, which 
can lead to skipped elements or errors. The approach using enumerate()  and pop() is safer 
because it returns immediately after removing the element, preventing any issues with 
continued iteration.  
Deleting Multiple Records Based on Criteria:  
Sometimes you need to remove all records that match a certain condition. For this, you can 
use list comprehension to create a new list containing only the records you want to keep:  
def delete_students_by_criteria(students, field, value):  
    """ 
    Remove all students where a specific field matches a value.  
     
    Parameters:  
        students (list): List of student dictionaries (modified in place)  
        field (str): The field name to check  
        value: The value to match for deletion  
     
    Returns:  
        int: Number of students removed  

    """ 
    initial_count = len(students)  
     
    # Create a new list excluding students that match the criteria  
    # The [:] slice assignment replaces the list contents in place  
    students[:] = [s for s in students if s.get(field) != value]  
     
    removed_count = initial_count - len(students)  
    print(f"Removed {removed_count} student(s)")  
    return removed_count  
 
# Test the function  
students = [  
    create_student("Alice Johnson", 20, "Computer Science", 3.8),  
    create_student("Bob Martinez", 22, "Mathematics", 3.6),  
    create_student("Charlie Davis", 21, "Computer Science", 3.9),  
    create_student("Diana Lee", 19, "Biology", 3.7)  
] 
 
print(f"Initial count: {len(students)}")  # Output: Initial count: 4  
 
# Delete all Computer Science students  
delete_students_by_criteria(students, "major", "Computer Science")  
# Output: Removed 2 student(s)  
 
print(f"Remaining count: {len(students)}")  # Output: Remaining count: 2  

 
remaining_majors = [student['major'] for student in students]  
print(f"Remaining majors: {remaining_majors}")  
# Output: Remaining majors: ['Mathematics', 'Biology']  
This function uses an important Python technique: students[:] = [...] . The [:] slice on the left 
side of the assignment means "replace all elements of the list" rather than "create a new 
list." This distinction matters because if you simply wrote students = [...] , you would create 
a new list and assign it to the local variable students , but the original list that was passed to 
the function would remain unchanged. By using students[:] = , you modify the original list in 
place, ensuring that the changes are visible to the calling code.  
The list comprehension [s for s in students if s.get(field) != value]  creates a new list 
containing only students where the specified field does not equal the specified value. 
Using s.get(field)  instead of s[field] provides safety —if the field does not exist in a student 
dictionary, get() returns None rather than raising a KeyError. 
 
Section 4: Filtering and Searching Records  
One of the most common tasks when working with collections of data is finding records 
that match specific criteria. You might need to find all students with a GPA above 3.5, all 
products in a certain category, or all orders placed in the last month. Python  provides 
several powerful techniques for filtering data, and mastering these techniques will make 
your code more concise and expressive.  
4.1 Basic Filtering with List Comprehensions  
List comprehensions provide a concise, readable way to filter data. The basic pattern is:  
[item for item in collection if condition]  
This creates a new list containing only the items from the original collection that satisfy the 
condition. Let's see this in action:  
students = [  
    {"name": "Alice Johnson", "age": 20, "major": "Computer Science", "gpa": 3.8},  
    {"name": "Bob Martinez", "age": 22, "major": "Mathematics", "gpa": 3.6},  
    {"name": "Charlie Davis", "age": 21, "major": "Computer Science", "gpa": 3.9},  

    {"name": "Diana Lee", "age": 19, "major": "Physics", "gpa": 3.7},  
    {"name": "Eve Taylor", "age": 20, "major": "Mathematics", "gpa": 3.5}  
] 
 
# Find all students with GPA above 3.7  
high_gpa_students = [student for student in students if student['gpa'] > 3.7]  
print(f"Students with GPA > 3.7:")  
for student in high_gpa_students:  
    print(f"  {student['name']}: {student['gpa']}")  
# Output:  
# Students with GPA > 3.7:  
#   Alice Johnson: 3.8  
#   Charlie Davis: 3.9  
Let's break down this list comprehension step by step. The expression student for student 
in students  means "take each student from the students list." The if student['gpa'] > 3.7  part 
adds a filter condition —only include students whose GPA is greater than 3.7. The entire 
expression creates a new list containing only the dictionaries that pass the filter.  
List comprehensions are not only concise but also often more readable than the equivalent 
for loop. Compare the list comprehension above to this traditional approach:  
# Equivalent code using a for loop  
high_gpa_students = []  
for student in students:  
    if student['gpa'] > 3.7:  
        high_gpa_students.append(student)  
Both approaches produce the same result, but the list comprehension expresses the intent 
more directly: "Create a list of students where GPA is greater than 3.7." Once you become 
comfortable with list comprehensions, you will find them more natural and eas ier to read 
than the longer for -loop version.  

Let's explore more filtering examples:  
# Find all Computer Science students  
cs_students = [s for s in students if s['major'] == "Computer Science"]  
print(f"\nComputer Science students: {[s['name'] for s in cs_students]}")  
# Output: Computer Science students: ['Alice Johnson', 'Charlie Davis']  
 
# Find all students aged 20 or younger  
young_students = [s for s in students if s['age'] <= 20]  
print(f"\nStudents aged 20 or younger: {[s['name'] for s in young_students]}")  
# Output: Students aged 20 or younger: ['Alice Johnson', 'Diana Lee', 'Eve Taylor']  
 
# Find students in specific majors  
stem_majors = ["Computer Science", "Mathematics", "Physics"]  
stem_students = [s for s in students if s['major'] in stem_majors]  
print(f"\nSTEM students: {len(stem_students)}")  
# Output: STEM students: 5 (all of them in this case)  
The last example introduces a useful technique: checking whether a value is in a list using 
the in operator. The condition s['major'] in stem_majors  evaluates to True if the student's 
major is any of "Computer Science", "Mathematics", or "Physics".  
4.2 Combining Multiple Filter Conditions  
Often you need to filter based on multiple criteria simultaneously. You can combine 
conditions using and and or operators:  
# Find Computer Science students with GPA above 3.7  
cs_high_gpa = [  
    s for s in students  
    if s['major'] == "Computer Science" and s['gpa'] > 3.7  
] 

print("CS students with GPA > 3.7:")  
for student in cs_high_gpa:  
    print(f"  {student['name']}: {student['gpa']}")  
# Output:  
# CS students with GPA > 3.7:  
#   Alice Johnson: 3.8  
#   Charlie Davis: 3.9  
 
# Find students who are either in Math or Physics  
math_or_physics = [  
    s for s in students  
    if s['major'] == "Mathematics" or s['major'] == "Physics"  
] 
print(f"\nMath or Physics students: {[s['name'] for s in math_or_physics]}")  
# Output: Math or Physics students: ['Bob Martinez', 'Diana Lee', 'Eve Taylor']  
 
# More concise version using 'in'  
math_or_physics = [  
    s for s in students  
    if s['major'] in ["Mathematics", "Physics"]  
] 
 
# Complex condition: young students with high GPA  
young_and_smart = [  
    s for s in students  
    if s['age'] <= 20 and s['gpa'] >= 3.7  

] 
print(f"\nYoung students (≤20) with high GPA (≥3.7):")  
for student in young_and_smart:  
    print(f"  {student['name']}: Age {student['age']}, GPA {student['gpa']}")  
# Output:  
# Young students (≤20) with high GPA (≥3.7):  
#   Alice Johnson: Age 20, GPA 3.8  
#   Diana Lee: Age 19, GPA 3.7  
When combining conditions, remember that and requires both conditions to be true, while 
or requires at least one condition to be true. You can use parentheses to group conditions 
when the logic becomes complex:  
# Students who are either (CS majors) OR (have GPA > 3.8 AND are 20 or younger)  
complex_filter = [  
    s for s in students  
    if s['major'] == "Computer Science" or (s['gpa'] > 3.8 and s['age'] <= 20)  
] 
4.3 Extracting Specific Fields  
Sometimes you do not need the entire dictionary —you only need specific fields from the 
filtered records. You can extract these fields directly in the list comprehension:  
# Get just the names of high -GPA students  
high_gpa_names = [s['name'] for s in students if s['gpa'] > 3.7]  
print(f"High -GPA student names: {high_gpa_names}")  
# Output: High -GPA student names: ['Alice Johnson', 'Charlie Davis']  
 
# Get name -GPA pairs for CS students  
cs_info = [(s['name'], s['gpa']) for s in students if s['major'] == "Computer Science"]  
print("CS students (name, GPA):")  

for name, gpa in cs_info:  
    print(f"  {name}: {gpa}")  
# Output:  
# CS students (name, GPA):  
#   Alice Johnson: 3.8  
#   Charlie Davis: 3.9  
 
# Create a dictionary mapping names to GPAs for all students  
name_to_gpa = {s['name']: s['gpa'] for s in students}  
print(f"\nAlice's GPA: {name_to_gpa['Alice Johnson']}")  
# Output: Alice's GPA: 3.8  
The last example demonstrates a dictionary comprehension , which is similar to a list 
comprehension but creates a dictionary instead. The syntax is {key: value for item in 
collection} . This is extremely useful when you need to create lookup tables or indexes from 
your data.  
4.4 Building a Flexible Search Function  
While list comprehensions are powerful for one -off filtering, you often want a reusable 
search function that can filter by multiple criteria. Let's build a flexible search function that 
accepts various optional parameters:  
def search_students(students, name=None, major=None, min_gpa=None, 
max_age=None):  
    """ 
    Search for students matching any combination of criteria.  
     
    Parameters:  
        students (list): List of student dictionaries to search  
        name (str, optional): Search for name containing this string (case -insensitive)  
        major (str, optional): Filter by exact major (case -insensitive)  

        min_gpa (float, optional): Filter for GPA >= this value  
        max_age (int, optional): Filter for age <= this value  
     
    Returns:  
        list: List of student dictionaries matching all specified criteria  
     
    Examples:  
        search_students(students, major="Computer Science")  
        search_students(students, min_gpa=3.7, max_age=20)  
        search_students(students, name="John")  
    """ 
    results = students  # Start with all students  
     
    # Apply each filter if the parameter was provided  
    if name is not None:  
        name_lower = name.lower()  
        results = [s for s in results if name_lower in s['name'].lower()]  
     
    if major is not None:  
        major_lower = major.lower()  
        results = [s for s in results if s['major'].lower() == major_lower]  
     
    if min_gpa is not None:  
        results = [s for s in results if s['gpa'] >= min_gpa]  
     
    if max_age is not None:  

        results = [s for s in results if s['age'] <= max_age]  
     
    return results  
 
# Test the search function  
students = [  
    {"name": "Alice Johnson", "age": 20, "major": "Computer Science", "gpa": 3.8},  
    {"name": "Bob Martinez", "age": 22, "major": "Mathematics", "gpa": 3.6},  
    {"name": "Charlie Davis", "age": 21, "major": "Computer Science", "gpa": 3.9},  
    {"name": "Diana Lee", "age": 19, "major": "Physics", "gpa": 3.7},  
    {"name": "Eve Johnson", "age": 20, "major": "Mathematics", "gpa": 3.5}  
] 
 
# Search for Computer Science students  
print("Computer Science students:")  
results = search_students(students, major="Computer Science")  
for student in results:  
    print(f"  {student['name']}")  
# Output:  
# Computer Science students:  
#   Alice Johnson  
#   Charlie Davis  
 
# Search for students with GPA >= 3.7  
print("\nStudents with GPA >= 3.7:")  
results = search_students(students, min_gpa=3.7)  

for student in results:  
    print(f"  {student['name']}: {student['gpa']}")  
# Output:  
# Students with GPA >= 3.7:  
#   Alice Johnson: 3.8  
#   Charlie Davis: 3.9  
#   Diana Lee: 3.7  
 
# Search with multiple criteria  
print("\nYoung CS students with high GPA:")  
results = search_students(students, major="Computer Science", min_gpa=3.7, 
max_age=20)  
for student in results:  
    print(f"  {student['name']}: Age {student['age']}, GPA {student['gpa']}")  
# Output:  
# Young CS students with high GPA:  
#   Alice Johnson: Age 20, GPA 3.8  
 
# Search by partial name match  
print("\nStudents with 'Johnson' in their name:")  
results = search_students(students, name="Johnson")  
for student in results:  
    print(f"  {student['name']}")  
# Output:  
# Students with 'Johnson' in their name:  
#   Alice Johnson  

#   Eve Johnson  
This search function demonstrates several important programming concepts. First, it uses 
optional parameters with default values of None. This allows callers to specify only the 
criteria they care about, ignoring the others. Second, it applies filters sequentially, with 
each filter operating on the results of the previous filter. This ensures that all specified 
criteria must be satisfied ( AND logic). Third, it implements case -insensitive searching for 
text fields, making the function more user -friendly. Fou rth, it uses the in operator for name 
searching, allowing partial matches rather than requiring exact names.  
The beauty of this design is its flexibility. The same function can handle simple single -
criterion searches or complex multi -criterion searches, and it is easy to add new search 
criteria by adding new optional parameters.  
 
Section 5: Sorting Lists of Dictionaries  
Sorting data is essential for organizing information in a meaningful way. You might want to 
sort students by GPA to identify top performers, sort products by price to find deals, or sort 
employees by years of experience for seniority -based decisions. Pytho n's sorted() function 
provides powerful sorting capabilities, but working with lists of dictionaries requires 
understanding how to specify which field to sort by.  
5.1 Basic Sorting with the key Parameter  
When you call sorted() on a list of dictionaries, Python needs to know how to compare the 
dictionaries to determine their order. You specify this using the key parameter, which 
should be a function that extracts the comparison value from each dictionary.  
The most common approach uses a lambda function  (an anonymous, single -expression 
function):  
students = [  
    {"name": "Charlie Davis", "age": 21, "gpa": 3.9},  
    {"name": "Alice Johnson", "age": 20, "gpa": 3.8},  
    {"name": "Bob Martinez", "age": 22, "gpa": 3.6},  
    {"name": "Diana Lee", "age": 19, "gpa": 3.7}  
] 
 

# Sort by name (alphabetically)  
by_name = sorted(students, key=lambda s: s['name'])  
print("Sorted by name:")  
for student in by_name:  
    print(f"  {student['name']}")  
# Output:  
# Sorted by name:  
#   Alice Johnson  
#   Bob Martinez  
#   Charlie Davis  
#   Diana Lee  
Let's understand the lambda function: lambda s: s['name'] . The word lambda indicates this 
is a lambda function. The s before the colon is the parameter name (representing one 
student dictionary). The s['name']  after the colon is the expression that gets evaluated and 
returned—in this case, the student's name. This lambda function is equivalent to:  
def get_name(s):  
    return s['name']  
 
by_name = sorted(students, key=get_name)  
Both approaches work identically, but the lambda version is more concise for simple 
extraction operations. Lambda functions are a powerful Python feature that you will 
encounter frequently when working with sorting, filtering, and data transformations.  
Let's sort by different fields:  
# Sort by age (youngest first)  
by_age = sorted(students, key=lambda s: s['age'])  
print("\nSorted by age (youngest first):")  
for student in by_age:  

    print(f"  {student['name']}: {student['age']} years old")  
# Output:  
# Sorted by age (youngest first):  
#   Diana Lee: 19 years old  
#   Alice Johnson: 20 years old  
#   Charlie Davis: 21 years old  
#   Bob Martinez: 22 years old  
 
# Sort by GPA (lowest first)  
by_gpa = sorted(students, key=lambda s: s['gpa'])  
print("\nSorted by GPA (lowest first):")  
for student in by_gpa:  
    print(f"  {student['name']}: {student['gpa']}")  
# Output:  
# Sorted by GPA (lowest first):  
#   Bob Martinez: 3.6  
#   Diana Lee: 3.7  
#   Alice Johnson: 3.8  
#   Charlie Davis: 3.9  
5.2 Reverse Sorting  
Often you want to sort in descending order rather than ascending order. The sorted() 
function accepts a reverse parameter for this:  
# Sort by GPA (highest first)  
by_gpa_desc = sorted(students, key=lambda s: s['gpa'], reverse=True)  
print("Sorted by GPA (highest first):")  
for student in by_gpa_desc:  

    print(f"  {student['name']}: {student['gpa']}")  
# Output:  
# Sorted by GPA (highest first):  
#   Charlie Davis: 3.9  
#   Alice Johnson: 3.8  
#   Diana Lee: 3.7  
#   Bob Martinez: 3.6  
 
# Sort by age (oldest first)  
by_age_desc = sorted(students, key=lambda s: s['age'], reverse=True)  
print("\nSorted by age (oldest first):")  
for student in by_age_desc:  
    print(f"  {student['name']}: {student['age']}")  
# Output:  
# Sorted by age (oldest first):  
#   Bob Martinez: 22  
#   Charlie Davis: 21  
#   Alice Johnson: 20  
#   Diana Lee: 19  
Setting reverse=True  sorts in descending order instead of ascending order. This works for 
numbers (largest to smallest), strings (Z to A), and any other comparable values.  
5.3 Multi -Level Sorting  
Sometimes you need to sort by multiple criteria. For example, you might want to sort 
students first by major, and within each major, sort by GPA. Python handles this elegantly 
by allowing the key function to return a tuple:  
students = [  
    {"name": "Charlie Davis", "major": "Physics", "gpa": 3.8},  

    {"name": "Alice Johnson", "major": "Computer Science", "gpa": 3.8},  
    {"name": "Bob Martinez", "major": "Computer Science", "gpa": 3.9},  
    {"name": "Diana Lee", "major": "Physics", "gpa": 3.7},  
    {"name": "Eve Taylor", "major": "Mathematics", "gpa": 3.6}  
] 
 
# Sort by major, then by GPA within each major  
sorted_students = sorted(students, key=lambda s: (s['major'], s['gpa']))  
print("Sorted by major, then by GPA:")  
for student in sorted_students:  
    print(f"  {student['major']}: {student['name']} (GPA: {student['gpa']})")  
# Output:  
# Sorted by major, then by GPA:  
#   Computer Science: Alice Johnson (GPA: 3.8)  
#   Computer Science: Bob Martinez (GPA: 3.9)  
#   Mathematics: Eve Taylor (GPA: 3.6)  
#   Physics: Diana Lee (GPA: 3.7)  
#   Physics: Charlie Davis (GPA: 3.8)  
When the key function returns a tuple like (s['major'], s['gpa']) , Python first sorts by the first 
element of the tuple (major), and then uses the second element (GPA) to break ties within 
the same major. This creates a hierarchical sort where the leftmost values in the tuple have 
the highest priority.  
You can sort with different directions for different levels by using negative numbers for 
numeric fields you want in descending order:  
# Sort by major (ascending), then by GPA (descending) within each major  
sorted_students = sorted(students, key=lambda s: (s['major'], -s['gpa']))  
print("\nSorted by major, then by GPA (highest first):")  

for student in sorted_students:  
    print(f"  {student['major']}: {student['name']} (GPA: {student['gpa']})")  
# Output:  
# Sorted by major, then by GPA (highest first):  
#   Computer Science: Bob Martinez (GPA: 3.9)  
#   Computer Science: Alice Johnson (GPA: 3.8)  
#   Mathematics: Eve Taylor (GPA: 3.6)  
#   Physics: Charlie Davis (GPA: 3.8)  
#   Physics: Diana Lee (GPA: 3.7)  
The negative sign in -s['gpa'] reverses the sort order for that field. This technique only works 
with numeric fields. For string fields, you would need to perform multiple sorts or use more 
complex techniques.  
Here's another example with more complex sorting logic:  
# Sort by GPA (descending), then by name (ascending) for students with the same GPA  
sorted_students = sorted(students, key=lambda s: ( -s['gpa'], s['name']))  
print("\nSorted by GPA (desc), then by name (asc):")  
for student in sorted_students:  
    print(f"  {student['name']}: GPA {student['gpa']}")  
# Output:  
# Sorted by GPA (desc), then by name (asc):  
#   Bob Martinez: GPA 3.9  
#   Alice Johnson: GPA 3.8  
#   Charlie Davis: GPA 3.8  
#   Diana Lee: GPA 3.7  
#   Eve Taylor: GPA 3.6  

Notice that Alice Johnson comes before Charlie Davis even though they have the same GPA 
(3.8), because Alice comes before Charlie alphabetically. This demonstrates how the 
second element in the tuple (name) breaks the tie when the first element (GPA) is eq ual.  
5.4 In-Place vs. Creating New Lists  
Understanding the difference between sorted() and the .sort() method is crucial:  
students = [  
    {"name": "Charlie Davis", "gpa": 3.9},  
    {"name": "Alice Johnson", "gpa": 3.8},  
    {"name": "Bob Martinez", "gpa": 3.6}  
] 
 
# sorted() creates a NEW list, leaving the original unchanged  
sorted_students = sorted(students, key=lambda s: s['gpa'])  
print("Original list after sorted():")  
print([s['name'] for s in students])  
# Output: ['Charlie Davis', 'Alice Johnson', 'Bob Martinez'] (unchanged)  
 
print("\nNew sorted list:")  
print([s['name'] for s in sorted_students])  
# Output: ['Bob Martinez', 'Alice Johnson', 'Charlie Davis'] (sorted)  
 
# .sort() modifies the list IN PLACE, returning None  
students.sort(key=lambda s: s['gpa'])  
print("\nOriginal list after .sort():")  
print([s['name'] for s in students])  
# Output: ['Bob Martinez', 'Alice Johnson', 'Charlie Davis'] (now sorted)  

The sorted() function is a built -in function that takes a list as an argument and returns a 
new sorted list, leaving the original unchanged. This is useful when you need to keep both 
the original order and a sorted version, or when you don't want to modify the origina l list.  
The .sort() method is a list method that sorts the list in place, modifying the original list and 
returning None. This is more memory -efficient when you only need the sorted version and 
don't care about preserving the original order.  
Choose based on your needs:  
• Use sorted() when you need to preserve the original order or when sorting other 
iterables (like tuples or generator expressions)  
• Use .sort() when you want to save memory and don't need the original order  
 
Section 6: Grouping and Aggregating Data  
Grouping data means organizing records into categories based on some criterion, like 
grouping students by major or products by category. Aggregating data means computing 
summary statistics like counts, sums, averages, minimums, and maximums. These 
operations are fundamental for data analysis and reporting.  
6.1 Grouping with defaultdict  
Python's defaultdict  from the collections  module makes grouping operations simple and 
elegant. A defaultdict  is a dictionary that automatically creates entries with a default value 
when you access a key that doesn't exist yet. This eliminates the need to check whether a 
key exists before appending to its value.  
Let's group students by their major:  
from collections import defaultdict  
 
students = [  
    {"name": "Alice Johnson", "major": "Computer Science", "gpa": 3.8},  
    {"name": "Bob Martinez", "major": "Mathematics", "gpa": 3.6},  
    {"name": "Charlie Davis", "major": "Computer Science", "gpa": 3.9},  
    {"name": "Diana Lee", "major": "Physics", "gpa": 3.7},  

    {"name": "Eve Taylor", "major": "Mathematics", "gpa": 3.5},  
    {"name": "Frank Wilson", "major": "Computer Science", "gpa": 3.7}  
] 
 
# Group students by major  
students_by_major = defaultdict(list)  
for student in students:  
    major = student['major']  
    students_by_major[major].append(student)  
 
# Display the grouped data  
print("Students grouped by major:")  
for major, student_list in students_by_major.items():  
    print(f"\n{major}:")  
    for student in student_list:  
        print(f"  - {student['name']} (GPA: {student['gpa']})")  
# Output:  
# Students grouped by major:  
# 
# Computer Science:  
#   - Alice Johnson (GPA: 3.8)  
#   - Charlie Davis (GPA: 3.9)  
#   - Frank Wilson (GPA: 3.7)  
# 
# Mathematics:  
#   - Bob Martinez (GPA: 3.6)  

#   - Eve Taylor (GPA: 3.5)  
# 
# Physics:  
#   - Diana Lee (GPA: 3.7)  
Let's understand how defaultdict(list)  works. When you create a defaultdict(list) , you are 
telling Python: "If I try to access a key that doesn't exist, automatically create it with an 
empty list as its value." This means that the first time you execute 
students_by_major['Computer Science'].append(student) , Python automatically creates 
the key 'Computer Science'  with an empty list [] as its value, then appends the student to 
that list. Without defaultdict , you would need to write:  
# Without defaultdict (more verbose)  
students_by_major = {}  
for student in students:  
    major = student['major']  
    if major not in students_by_major:  
        students_by_major[major] = []  # Create the list if it doesn't exist  
    students_by_major[major].append(student)  
The defaultdict  version is cleaner and less error -prone because you don't need to 
remember to check whether the key exists before using it.  
6.2 Grouping by Multiple Criteria  
Sometimes you need to group by more than one field. You can nest defaultdict  objects to 
create hierarchical groupings:  
students = [  
    {"name": "Alice Johnson", "major": "Computer Science", "year": 2, "gpa": 3.8},  
    {"name": "Bob Martinez", "major": "Mathematics", "year": 3, "gpa": 3.6},  
    {"name": "Charlie Davis", "major": "Computer Science", "year": 3, "gpa": 3.9},  
    {"name": "Diana Lee", "major": "Physics", "year": 2, "gpa": 3.7},  
    {"name": "Eve Taylor", "major": "Mathematics", "year": 2, "gpa": 3.5},  

    {"name": "Frank Wilson", "major": "Computer Science", "year": 2, "gpa": 3.7}  
] 
 
# Group by major, then by year within each major  
by_major_and_year = defaultdict(lambda: defaultdict(list))  
for student in students:  
    major = student['major']  
    year = student['year']  
    by_major_and_year[major][year].append(student)  
 
# Display the nested grouping  
print("Students grouped by major and year:")  
for major, years in sorted(by_major_and_year.items()):  
    print(f"\n{major}:")  
    for year, student_list in sorted(years.items()):  
        print(f"  Year {year}:")  
        for student in student_list:  
            print(f"    - {student['name']}")  
# Output:  
# Students grouped by major and year:  
# 
# Computer Science:  
#   Year 2:  
#     - Alice Johnson  
#     - Frank Wilson  
#   Year 3:  

#     - Charlie Davis  
# 
# Mathematics:  
#   Year 2:  
#     - Eve Taylor  
#   Year 3:  
#     - Bob Martinez  
# 
# Physics:  
#   Year 2:  
#     - Diana Lee  
The expression defaultdict(lambda: defaultdict(list))  creates a defaultdict where the default 
value is itself another defaultdict with list default values. This might look complex at first, 
but it follows the same pattern: when you access a key that doesn't exist, Python 
automatically creates it with the spec ified default value —in this case, another 
defaultdict(list) . 
The lambda function lambda: defaultdict(list)  is necessary because defaultdict  expects a 
callable (a function) that returns the default value. Each time a new key is accessed, this 
lambda function is called to create a new defaultdict(list)  for that key.  
6.3 Creating Indexes for Fast Lookups  
An index is a dictionary that maps some unique identifier to the full record, enabling instant 
lookups. This is similar to how database indexes work —they trade space for speed. Instead 
of searching through a list linearly (which takes O(n) time), you can l ook up a record by its 
key instantly (which takes O(1) time).  
students = [  
    {"id": 101, "name": "Alice Johnson", "email": "alice@university.edu", "gpa": 3.8},  
    {"id": 102, "name": "Bob Martinez", "email": "bob@university.edu", "gpa": 3.6},  
    {"id": 103, "name": "Charlie Davis", "email": "charlie@university.edu", "gpa": 3.9}  
] 

 
# Create an index by student ID for instant lookups  
students_by_id = {student['id']: student for student in students}  
 
# Now lookups are instant (O(1) instead of O(n))  
student = students_by_id[102]  
print(f"Found student with ID 102: {student['name']}")  
# Output: Found student with ID 102: Bob Martinez  
 
# Create an index by email  
students_by_email = {student['email']: student for student in students}  
student = students_by_email['charlie@university.edu']  
print(f"Found student with email charlie@university.edu: {student['name']}")  
# Output: Found student with email charlie@university.edu: Charlie Davis  
The dictionary comprehension {student['id']: student for student in students}  creates a 
dictionary where each key is a student ID and each value is the complete student 
dictionary. This pattern is extremely useful when you need to perform many lookups by a 
specific field.  
The speed advantage of indexes becomes significant with large datasets. Searching 
through a list of 10,000 students to find one by ID requires checking up to 10,000 records. 
Looking up by ID in an index requires checking just one dictionary entry, regardle ss of how 
many students exist.  
When to use indexes:  
• When you need to look up records frequently by a specific field  
• When the field values are unique (or you only care about one record per value)  
• When you have enough memory to store the index alongside the original list  
• When lookup speed is more important than memory usage  
6.4 Computing Aggregate Statistics  

Aggregation operations compute summary values from collections of data. Common 
aggregations include counting, summing, averaging, finding minimums and maximums, 
and computing other statistical measures.  
Basic Aggregations:  
students = [  
    {"name": "Alice Johnson", "age": 20, "gpa": 3.8, "credits": 60},  
    {"name": "Bob Martinez", "age": 22, "gpa": 3.6, "credits": 90},  
    {"name": "Charlie Davis", "age": 21, "gpa": 3.9, "credits": 75},  
    {"name": "Diana Lee", "age": 19, "gpa": 3.7, "credits": 45}  
] 
 
# Count total students  
total_students = len(students)  
print(f"Total students: {total_students}")  
# Output: Total students: 4  
 
# Calculate average GPA  
total_gpa = sum(student['gpa'] for student in students)  
average_gpa = total_gpa / len(students)  
print(f"Average GPA: {average_gpa:.2f}")  
# Output: Average GPA: 3.75  
 
# Calculate average age  
average_age = sum(student['age'] for student in students) / len(students)  
print(f"Average age: {average_age:.1f} years")  
# Output: Average age: 20.5 years  
 

# Find minimum and maximum GPA  
min_gpa = min(student['gpa'] for student in students)  
max_gpa = max(student['gpa'] for student in students)  
print(f"GPA range: {min_gpa} to {max_gpa}")  
# Output: GPA range: 3.6 to 3.9  
 
# Find the student with the highest GPA  
top_student = max(students, key=lambda s: s['gpa'])  
print(f"Top student: {top_student['name']} with GPA {top_student['gpa']}")  
# Output: Top student: Charlie Davis with GPA 3.9  
 
# Calculate total credits across all students  
total_credits = sum(student['credits'] for student in students)  
print(f"Total credits earned by all students: {total_credits}")  
# Output: Total credits earned by all students: 270  
Notice the use of generator expressions like sum(student['gpa'] for student in students) . 
These are similar to list comprehensions but don't create an intermediate list —they 
generate values one at a time, making them more memory -efficient for large datasets.  
The max() function with a key parameter finds the student with the maximum GPA value. 
The key parameter works the same way as in sorted()—it specifies how to extract the 
comparison value from each dictionary.  
Aggregating by Groups:  
One of the most powerful analysis techniques is computing aggregates for each group in 
your data:  
from collections import defaultdict  
 
students = [  

    {"name": "Alice Johnson", "major": "Computer Science", "gpa": 3.8},  
    {"name": "Bob Martinez", "major": "Mathematics", "gpa": 3.6},  
    {"name": "Charlie Davis", "major": "Computer Science", "gpa": 3.9},  
    {"name": "Diana Lee", "major": "Physics", "gpa": 3.7},  
    {"name": "Eve Taylor", "major": "Mathematics", "gpa": 3.5},  
    {"name": "Frank Wilson", "major": "Computer Science", "gpa": 3.7}  
] 
 
# Calculate average GPA by major  
gpa_by_major = defaultdict(list)  
for student in students:  
    gpa_by_major[student['major']].append(student['gpa'])  
 
print("Average GPA by major:")  
for major, gpas in sorted(gpa_by_major.items()):  
    average = sum(gpas) / len(gpas)  
    student_count = len(gpas)  
    print(f"  {major}: {average:.2f} (from {student_count} student{'s' if student_count != 1 else 
''})")  
# Output:  
# Average GPA by major:  
#   Computer Science: 3.80 (from 3 students)  
#   Mathematics: 3.55 (from 2 students)  
#   Physics: 3.70 (from 1 student)  
This pattern —group the data, then compute aggregates for each group —is extremely 
common in data analysis. You first use defaultdict  to organize the data into groups, then 
iterate over the groups to compute the desired statistics.  

6.5 Using Counter for Frequency Analysis  
Python's Counter class from the collections  module provides a convenient way to count 
occurrences of values. It is particularly useful for frequency analysis:  
from collections import Counter  
 
students = [  
    {"name": "Alice Johnson", "major": "Computer Science", "year": 2},  
    {"name": "Bob Martinez", "major": "Mathematics", "year": 3},  
    {"name": "Charlie Davis", "major": "Computer Science", "year": 3},  
    {"name": "Diana Lee", "major": "Physics", "year": 2},  
    {"name": "Eve Taylor", "major": "Computer Science", "year": 2},  
    {"name": "Frank Wilson", "major": "Mathematics", "year": 3}  
] 
 
# Count students by major  
major_counts = Counter(student['major'] for student in students)  
print("Students per major:")  
for major, count in major_counts.most_common():  
    print(f"  {major}: {count}")  
# Output:  
# Students per major:  
#   Computer Science: 3  
#   Mathematics: 2  
#   Physics: 1  
 
# Count students by year  

year_counts = Counter(student['year'] for student in students)  
print("\nStudents per year:")  
for year, count in sorted(year_counts.items()):  
    print(f"  Year {year}: {count}")  
# Output:  
# Students per year:  
#   Year 2: 3  
#   Year 3: 3  
The Counter object is a specialized dictionary that counts how many times each value 
appears. The most_common()  method returns the items sorted by frequency (most 
common first), which is useful for finding the top categories or identifying trends.  
You can also perform set operations with counters:  
# Count students by major  
major_counts_2023 = Counter(['Computer Science', 'Mathematics', 'Computer Science', 
'Physics'])  
major_counts_2024 = Counter(['Computer Science', 'Computer Science', 'Computer 
Science', 'Biology'])  
 
# Find majors that increased in popularity  
increased = major_counts_2024 - major_counts_2023  
print(f"Majors with more students in 2024: {increased}")  
# Output: Majors with more students in 2024: Counter({'Computer Science': 1, 'Biology': 1})  
 
Section 7: Working with JSON  
JSON (JavaScript Object Notation) is a text -based format for storing and exchanging 
structured data. It is the standard format for web APIs, configuration files, and data 
interchange between different programming languages. Understanding how to work with 
JSON is essential for modern programming because it allows your Python programs to 

communicate with web services, save data in a portable format, and integrate with other 
systems.  
7.1 Understanding JSON Format  
JSON syntax is remarkably similar to Python dictionaries and lists, which makes it natural 
to work with in Python. However, there are some important differences you need to 
understand:  
JSON vs. Python:  
JSON  Python  Notes  
true  True  Boolean values are lowercase in JSON  
false  False  Boolean values are lowercase in JSON  
null  None  Null is represented differently  
"string"  "string"  Strings must use double quotes in JSON  
123  123  Numbers work the same  
[1, 2, 3]  [1, 2, 3]  Arrays/lists work the same  
{"key": "value"}  {"key": "value"}  Objects/dictionaries work the same  
Here's a side -by-side comparison:  
# Python dictionary  
python_dict = {  
    "name": "Alice Johnson",  
    "age": 20,  
    "enrolled": True,  
    "courses": ["Math", "Physics", "CS"],  
    "advisor": None  
} 
 
# Equivalent JSON (as a string)  

json_string = '''  
{ 
    "name": "Alice Johnson",  
    "age": 20,  
    "enrolled": true,  
    "courses": ["Math", "Physics", "CS"],  
    "advisor": null  
} 
''' 
The structural similarity makes converting between Python and JSON straightforward, but 
you must remember that JSON has stricter syntax rules: all keys must be strings enclosed 
in double quotes, and JSON doesn't support Python -specific types like tuples, s ets, or 
custom objects directly.  
7.2 Converting Between Python and JSON  
Python's json module provides functions for converting between Python objects and JSON 
strings. The key functions are:  
• json.dumps()  - Converts a Python object to a JSON string (dump string)  
• json.dump()  - Converts a Python object to JSON and writes it to a file (dump to file)  
• json.loads()  - Converts a JSON string to a Python object (load from string)  
• json.load()  - Reads JSON from a file and converts it to a Python object (load from 
file)  
The "s" in dumps and loads stands for "string" —these functions work with JSON as strings 
in memory. The versions without "s" work with files.  
Converting Python to JSON String:  
import json  
 
student = {  
    "name": "Alice Johnson",  

    "age": 20,  
    "major": "Computer Science",  
    "gpa": 3.8,  
    "courses": ["Data Structures", "Algorithms", "Databases"]  
} 
 
# Convert to JSON string  
json_string = json.dumps(student)  
print("Compact JSON:")  
print(json_string)  
# Output: {"name": "Alice Johnson", "age": 20, "major": "Computer Science", "gpa": 3.8, 
"courses": ["Data Structures", "Algorithms", "Databases"]}  
 
# Convert to pretty -printed JSON (with indentation)  
json_pretty = json.dumps(student, indent=2)  
print("\nPretty JSON:")  
print(json_pretty)  
# Output:  
# { 
#   "name": "Alice Johnson",  
#   "age": 20,  
#   "major": "Computer Science",  
#   "gpa": 3.8,  
#   "courses": [  
#     "Data Structures",  
#     "Algorithms",  

#     "Databases"  
#   ] 
# } 
The indent parameter controls the formatting. With indent=2 , each nested level is indented 
by 2 spaces, making the JSON human -readable. Without indentation, the JSON is compact 
(all on one line), which saves space but is harder to read.  
Converting JSON String to Python:  
# JSON string (received from an API, file, etc.)  
json_string = '''  
{ 
    "name": "Bob Martinez",  
    "age": 22,  
    "major": "Mathematics",  
    "gpa": 3.6  
} 
''' 
 
# Convert to Python dictionary  
student = json.loads(json_string)  
print(f"Student name: {student['name']}")  
print(f"Student major: {student['major']}")  
# Output:  
# Student name: Bob Martinez  
# Student major: Mathematics  
 
# You can now work with it like any Python dictionary  
student['gpa'] = 3.7  

print(f"Updated GPA: {student['gpa']}")  
# Output: Updated GPA: 3.7  
7.3 Reading and Writing JSON Files  
Most often, you will work with JSON data stored in files. Python makes this straightforward 
with the json.dump()  and json.load()  functions:  
Writing to a JSON File:  
import json  
 
students = [  
    {"name": "Alice Johnson", "age": 20, "major": "Computer Science", "gpa": 3.8},  
    {"name": "Bob Martinez", "age": 22, "major": "Mathematics", "gpa": 3.6},  
    {"name": "Charlie Davis", "age": 21, "major": "Physics", "gpa": 3.9}  
] 
 
# Write to JSON file  
with open("students.json", "w") as file:  
    json.dump(students, file, indent=2)  
    print("Data saved to students.json")  
 
# The file now contains properly formatted JSON  
The with open()  statement creates a context manager that automatically closes the file 
when done, even if an error occurs. The mode "w" means "write" (creating a new file or 
overwriting an existing one). The json.dump()  function takes two required arguments: the 
Python object to convert and the file object to write to. The optional indent=2  parameter 
makes the file human -readable.  
Reading from a JSON File:  
# Read from JSON file  

with open("students.json", "r") as file:  
    loaded_students = json.load(file)  
    print(f"Loaded {len(loaded_students)} students from file")  
     
    # Display the loaded data  
    for student in loaded_students:  
        print(f"  - {student['name']}: {student['major']}, GPA {student['gpa']}")  
# Output:  
# Loaded 3 students from file  
#   - Alice Johnson: Computer Science, GPA 3.8  
#   - Bob Martinez: Mathematics, GPA 3.6  
#   - Charlie Davis: Physics, GPA 3.9  
The mode "r" means "read." The json.load()  function reads the entire file, parses the JSON, 
and returns the corresponding Python object (in this case, a list of dictionaries).  
7.4 Handling JSON Errors  
Not all strings that look like JSON are valid JSON. Missing commas, extra commas, single 
quotes instead of double quotes, or other syntax errors will cause json.loads()  or 
json.load()  to raise a JSONDecodeError . You should always handle these errors gracefully:  
import json  
 
# Invalid JSON examples  
invalid_examples = [  
    '{"name": "Alice", "age": 20,}',  # Extra comma  
    "{'name': 'Alice'}",  # Single quotes instead of double quotes  
    '{"name": "Alice" "age": 20}',  # Missing comma  
    '{name: "Alice"}',  # Keys not quoted  
] 

 
for json_string in invalid_examples:  
    try: 
        data = json.loads(json_string)  
        print(f"Successfully parsed: {data}")  
    except json.JSONDecodeError as e:  
        print(f"JSON Error: {e}")  
        print(f"  Problematic JSON: {json_string} \n") 
# Output shows specific errors for each invalid JSON  
When working with external data sources (files, APIs, user input), always wrap JSON 
operations in try -except blocks:  
def safe_load_json_file(filename):  
    """ 
    Safely load JSON from a file with error handling.  
     
    Returns:  
        The parsed JSON data, or None if an error occurred  
    """ 
    try: 
        with open(filename, "r") as file:  
            return json.load(file)  
    except FileNotFoundError:  
        print(f"Error: File '{filename}' not found")  
        return None  
    except json.JSONDecodeError as e:  
        print(f"Error: Invalid JSON in '{filename}'")  

        print(f"  {e}")  
        return None  
    except Exception as e:  
        print(f"Unexpected error reading '{filename}': {e}")  
        return None  
 
# Use the safe function  
data = safe_load_json_file("students.json")  
if data:  
    print(f"Successfully loaded {len(data)} records")  
else:  
    print("Failed to load data")  
This function demonstrates robust error handling by catching three types of errors: file not 
found, invalid JSON, and any other unexpected errors. This prevents your program from 
crashing when encountering bad data.  
 
Section 8: Working with Nested Data Structures  
Real-world data is often more complex than simple flat lists of dictionaries. You will 
frequently encounter nested data structures —dictionaries containing lists, lists 
containing dictionaries within dictionaries, or even deeper nesting levels. Learning to 
navigate and manipulate nested structures is essential for working with realistic data from 
APIs, databases, and files.  
8.1 Understanding Nested Structures  
A nested data structure is one where the values in a dictionary can themselves be 
dictionaries or lists, and those nested structures can contain further nesting. This allows 
representing complex hierarchical relationships:  
# A university with departments, each containing students  
university = {  

    "name": "Tech University",  
    "established": 1990,  
    "departments": [  
        { 
            "name": "Computer Science",  
            "head": "Dr. Smith",  
            "students": [  
                {"name": "Alice Johnson", "year": 2, "gpa": 3.8},  
                {"name": "Bob Martinez", "year": 3, "gpa": 3.6}  
            ], 
            "courses": ["Intro to Programming", "Data Structures", "Algorithms"]  
        }, 
        { 
            "name": "Mathematics",  
            "head": "Dr. Johnson",  
            "students": [  
                {"name": "Charlie Davis", "year": 2, "gpa": 3.9},  
                {"name": "Diana Lee", "year": 1, "gpa": 3.7}  
            ], 
            "courses": ["Calculus", "Linear Algebra", "Statistics"]  
        } 
    ] 
} 
This structure represents a university containing a list of departments, where each 
department dictionary contains a list of student dictionaries. This models real -world 
relationships: a university has departments, and departments have students.  
8.2 Accessing Nested Data  

Accessing data in nested structures requires chaining multiple access operations. You 
navigate through the structure level by level:  
# Access university name (top level)  
print(f"University: {university['name']}")  
# Output: University: Tech University  
 
# Access first department name (one level deep)  
first_dept = university['departments'][0]  
print(f"First department: {first_dept['name']}")  
# Output: First department: Computer Science  
 
# Access department head (two levels deep)  
print(f"Department head: {university['departments'][0]['head']}")  
# Output: Department head: Dr. Smith  
 
# Access first student in first department (three levels deep)  
first_student = university['departments'][0]['students'][0]  
print(f"First student: {first_student['name']}")  
# Output: First student: Alice Johnson  
 
# Access a specific student's GPA (four levels deep)  
gpa = university['departments'][0]['students'][1]['gpa']  
print(f"Bob's GPA: {gpa}")  
# Output: Bob's GPA: 3.6  
 
# Access third course in second department  

course = university['departments'][1]['courses'][2]  
print(f"Course: {course}")  
# Output: Course: Statistics  
Each access operation returns the value at that level, which you then use for the next level 
of access. Think of it as following a path through the structure: start at the top, go to 
'departments' , then to index [0], then to 'students' , then to index [0], then to 'name'. 
8.3 Iterating Through Nested Structures  
To process all data in a nested structure, you need nested loops:  
# Print all students in all departments  
print("All students:")  
for department in university['departments']:  
    print(f"\n{department['name']}:")  
    for student in department['students']:  
        print(f"  - {student['name']} (Year {student['year']}, GPA: {student['gpa']})")  
# Output:  
# All students:  
# 
# Computer Science:  
#   - Alice Johnson (Year 2, GPA: 3.8)  
#   - Bob Martinez (Year 3, GPA: 3.6)  
# 
# Mathematics:  
#   - Charlie Davis (Year 2, GPA: 3.9)  
#   - Diana Lee (Year 1,  
GPA: 3.7)  
 

The outer loop iterates through departments, and the inner loop iterates through students 
within each department. This pattern of nested loops matches the nested structure of the 
data.  
 
You can extract specific information while iterating:  
 
```python  
# Find all students across all departments with GPA > 3.7  
high_achievers = []  
for department in university['departments']:  
    for student in department['students']:  
        if student['gpa'] > 3.7:  
            # Add department information to the student data  
            student_with_dept = student.copy()  
            student_with_dept['department'] = department['name']  
            high_achievers.append(student_with_dept)  
 
print("\nHigh achievers (GPA > 3.7):")  
for student in high_achievers:  
    print(f"  {student['name']} - {student['department']} - GPA: {student['gpa']}")  
# Output:  
# High achievers (GPA > 3.7):  
#   Alice Johnson - Computer Science - GPA: 3.8  
#   Charlie Davis - Mathematics - GPA: 3.9  
This example demonstrates flattening nested data —extracting records from a hierarchy 
into a simple list while preserving necessary context (the department name).  
8.4 Safe Access to Nested Data  

Accessing deeply nested data is risky because any level might be missing or have an 
unexpected structure. A robust approach uses the .get() method with default values or 
implements a safe access function:  
# Potentially problematic access  
try: 
    gpa = university['departments'][5]['students'][0]['gpa']  
except (KeyError, IndexError) as e:  
    print(f"Error accessing nested data: {e}")  
# Output: Error accessing nested data: list index out of range  
 
# Safe access using .get()  
dept = university.get('departments', [])  
if len(dept) > 0:  
    students = dept[0].get('students', [])  
    if len(students) > 0:  
        gpa = students[0].get('gpa', 0.0)  
        print(f"GPA: {gpa}")  
For frequent nested access, create a helper function:  
def safe_nested_get(data, *keys, default=None):  
    """ 
    Safely access nested dictionary/list values.  
     
    Example:  
        safe_nested_get(university, 'departments', 0, 'students', 1, 'name')  
     
    Parameters:  
        data: The data structure to navigate  

        *keys: Series of keys/indexes to follow  
        default: Value to return if path doesn't exist  
     
    Returns:  
        The value at the specified path, or default if path doesn't exist  
    """ 
    result = data  
    for key in keys:  
        try: 
            result = result[key]  
        except (KeyError, IndexError, TypeError):  
            return default  
    return result  
 
# Test safe access  
name = safe_nested_get(university, 'departments', 0, 'students', 0, 'name')  
print(f"Student name: {name}")  
# Output: Student name: Alice Johnson  
 
# Access non -existent path  
missing = safe_nested_get(university, 'departments', 5, 'students', 0, 'name', default='Not 
found')  
print(f"Missing data: {missing}")  
# Output: Missing data: Not found  
 
# Access with wrong type  

wrong_type = safe_nested_get(university, 'name', 0, 'students', default='N/A')  
print(f"Wrong type access: {wrong_type}")  
# Output: Wrong type access: N/A  
This function attempts to navigate the specified path through the data structure. If any key 
doesn't exist, any index is out of range, or any intermediate value isn't the expected type 
(dictionary or list), it returns the default value instead of raising a n error. This makes your 
code much more robust when dealing with data from external sources that might have 
missing or malformed fields.  
8.5 Flattening Nested Data  
Flattening means converting a nested hierarchical structure into a simpler, flat structure. 
This is useful when you need to analyze data without caring about the hierarchy, or when 
exporting to formats that don't support nesting (like CSV files).  
To flatten means to transform nested data into a single -level structure. For example, 
converting a university with departments containing students into a simple list where each 
entry contains both student and department information:  
def flatten_university_students(university_data):  
    """ 
    Flatten nested university structure to a list of student records.  
     
    Each student record will include department information.  
     
    Parameters:  
        university_data: Nested university dictionary  
     
    Returns:  
        list: Flat list of student dictionaries with department info  
    """ 
    all_students = []  

     
    for department in university_data.get('departments', []):  
        dept_name = department.get('name', 'Unknown')  
        dept_head = department.get('head', 'Unknown')  
         
        for student in department.get('students', []):  
            # Create a flattened record combining student and department data  
            flat_student = {  
                'student_name': student.get('name', 'Unknown'),  
                'year': student.get('year', 0),  
                'gpa': student.get('gpa', 0.0),  
                'department': dept_name,  
                'department_head': dept_head,  
                'university': university_data.get('name', 'Unknown')  
            } 
            all_students.append(flat_student)  
     
    return all_students  
 
# Flatten the data  
flat_students = flatten_university_students(university)  
print("Flattened student data:")  
for student in flat_students:  
    print(f"  {student['student_name']} - {student['department']} - Year {student['year']} - GPA 
{student['gpa']}")  
# Output:  

# Flattened student data:  
#   Alice Johnson - Computer Science - Year 2 - GPA 3.8  
#   Bob Martinez - Computer Science - Year 3 - GPA 3.6  
#   Charlie Davis - Mathematics - Year 2 - GPA 3.9  
#   Diana Lee - Mathematics - Year 1 - GPA 3.7  
The flattened structure is now a simple list of dictionaries where each dictionary contains 
all the information about one student, including their department. This format is easier to 
analyze, sort, filter, and export.  
8.6 Restructuring Data  
Restructuring means transforming data from one organization to another. You might need 
to reorganize data to make it more suitable for a specific task or to match a different 
schema.  
For example, converting a flat list back into a nested structure:  
def group_students_by_department(flat_students):  
    """ 
    Convert flat student list back to department -grouped structure.  
     
    Parameters:  
        flat_students: List of flat student dictionaries  
     
    Returns:  
        dict: Dictionary mapping department names to lists of students  
    """ 
    from collections import defaultdict  
     
    grouped = defaultdict(list)  
     

    for student in flat_students:  
        department = student.get('department', 'Unknown')  
        # Create a simplified student record without redundant department info  
        simple_student = {  
            'name': student['student_name'],  
            'year': student['year'],  
            'gpa': student['gpa']  
        } 
        grouped[department].append(simple_student)  
     
    return dict(grouped)  
 
# Restructure the flattened data  
restructured = group_students_by_department(flat_students)  
print("\nRestructured by department:")  
for dept, students in restructured.items():  
    print(f"\n{dept}:")  
    for student in students:  
        print(f"  {student['name']} - Year {student['year']}")  
# Output:  
# Restructured by department:  
# 
# Computer Science:  
#   Alice Johnson - Year 2  
#   Bob Martinez - Year 3  
# 

# Mathematics:  
#   Charlie Davis - Year 2  
#   Diana Lee - Year 1  
8.7 Visualizing Nested Structures  
Understanding complex nested data is easier when you can visualize its structure. Here's a 
function that recursively prints the structure of nested data:  
def print_structure(data, indent=0, max_depth=5):  
    """ 
    Recursively print the structure of nested data.  
     
    Helps you understand complex JSON/dictionary structures.  
     
    Parameters:  
        data: The data structure to visualize  
        indent: Current indentation level (used internally)  
        max_depth: Maximum depth to print (prevents infinite recursion)  
    """ 
    if indent >= max_depth:  
        print("  " * indent + "... (max depth reached)")  
        return  
     
    spaces = "  " * indent  
     
    if isinstance(data, dict):  
        for key, value in data.items():  
            if isinstance(value, (dict, list)):  

                print(f"{spaces}{key}:")  
                print_structure(value, indent + 1, max_depth)  
            else:  
                print(f"{spaces}{key}: {type(value).__name__} = {value}")  
     
    elif isinstance(data, list):  
        if len(data) == 0:  
            print(f"{spaces}(empty list)")  
        else:  
            print(f"{spaces}[{len(data)} items]")  
            # Show first item as example  
            if len(data) > 0:  
                print(f"{spaces}Example item [0]:")  
                print_structure(data[0], indent + 1, max_depth)  
     
    else:  
        print(f"{spaces}{type(data).__name__} = {data}")  
 
# Visualize the university structure  
print("University data structure:")  
print_structure(university)  
# Output shows the complete nested structure in an easy -to-read format  
This function uses recursion (which we will study in more detail in later chapters) to 
traverse nested structures of any depth. It shows you the keys in dictionaries, the types and 
values of simple data, and the structure of nested dictionaries and lists. This is invaluable 
when you receive complex JSON data from an API and need to understand its organization 
before writing code to process it.  

 
Section 9: Data Validation and Schema Consistency  
As you work with collections of dictionaries, especially when receiving data from external 
sources like user input, files, or APIs, ensuring data quality becomes crucial. Invalid or 
inconsistent data can cause your program to crash, produce incorrect resul ts, or corrupt 
your database. Data validation and schema enforcement help prevent these problems by 
catching errors early.  
9.1 Understanding Data Schemas  
A schema is a formal definition of what structure your data should have. For dictionaries, a 
schema specifies which keys must be present, what types of values each key should have, 
and any constraints on those values (like ranges, formats, or relationships between  fields).  
Consider a student record schema:  
# Informal schema description  
student_schema = {  
    "name": str,           # Required, must be a non -empty string  
    "age": int,            # Required, must be integer between 16 and 100  
    "major": str,          # Required, must be a non -empty string  
    "gpa": float,          # Required, must be float between 0.0 and 4.0  
    "email": str,          # Optional, must be valid email format if present  
} 
This schema tells you what a valid student dictionary should look like. Without enforcing 
this schema, your collection might contain inconsistent data:  
# Valid student  
valid_student = {  
    "name": "Alice Johnson",  
    "age": 20,  
    "major": "Computer Science",  
    "gpa": 3.8  

} 
 
# Invalid students (various problems)  
invalid_students = [  
    {"name": "Bob", "age": "22", "major": "Math", "gpa": 3.6},  # age is string  
    {"name": "", "age": 20, "major": "Physics", "gpa": 3.7},    # empty name  
    {"name": "Charlie", "age": 21, "major": "CS"},               # missing gpa  
    {"name": "Diana", "age": 19, "major": "Bio", "gpa": 5.0},   # invalid gpa  
] 
Without validation, these invalid records could enter your system and cause problems later 
when your code assumes all data follows the correct schema.  
9.2 Implementing Schema Validation  
Let's build a comprehensive validation function that checks whether a student dictionary 
conforms to our schema:  
def validate_student(student):  
    """ 
    Validate a student dictionary against the expected schema.  
     
    Parameters:  
        student: Dictionary to validate  
     
    Returns:  
        tuple: (is_valid, error_message)  
               is_valid is True if valid, False otherwise  
               error_message describes the problem, or "Valid" if no problems  
    """ 
    # Define required fields and their types  

    required_fields = {  
        "name": str,  
        "age": int,  
        "major": str,  
        "gpa": (int, float)  # Allow both int and float for GPA  
    } 
     
    # Check that all required fields exist  
    for field, expected_type in required_fields.items():  
        if field not in student:  
            return False, f"Missing required field: '{field}'"  
         
        # Check type  
        if not isinstance(student[field], expected_type):  
            actual_type = type(student[field]).__name__  
            if isinstance(expected_type, tuple):  
                type_names = " or ".join(t.__name__ for t in expected_type)  
                expected_name = type_names  
            else:  
                expected_name = expected_type.__name__  
            return False, f"Field '{field}' has wrong type. Expected {expected_name}, got 
{actual_type}"  
     
    # Validate name is not empty  
    if not student["name"].strip():  
        return False, "Name cannot be empty"  

     
    # Validate age is in reasonable range  
    if student["age"] < 16 or student["age"] > 100:  
        return False, f"Age must be between 16 and 100, got {student['age']}"  
     
    # Validate major is not empty  
    if not student["major"].strip():  
        return False, "Major cannot be empty"  
     
    # Validate GPA is in valid range  
    if student["gpa"] < 0.0 or student["gpa"] > 4.0:  
        return False, f"GPA must be between 0.0 and 4.0, got {student['gpa']}"  
     
    # If we get here, the student is valid  
    return True, "Valid"  
 
# Test validation with various inputs  
test_students = [  
    {"name": "Alice Johnson", "age": 20, "major": "Computer Science", "gpa": 3.8},  
    {"name": "Bob", "age": "22", "major": "Math", "gpa": 3.6},  
    {"name": "", "age": 20, "major": "Physics", "gpa": 3.7},  
    {"name": "Charlie", "age": 21, "major": "CS"},  
    {"name": "Diana", "age": 19, "major": "Bio", "gpa": 5.0},  
    {"name": "Eve", "age": 150, "major": "Chemistry", "gpa": 3.5},  
] 
 

print("Validation results:")  
for student in test_students:  
    is_valid, message = validate_student(student)  
    status = "✓" if is_valid else " ✗" 
    name = student.get("name", "Unknown")  
    print(f"{status} {name}: {message}")  
# Output:  
# ✓ Alice Johnson: Valid  
# ✗ Bob: Field 'age' has wrong type. Expected int, got str  
# ✗ : Name cannot be empty  
# ✗ Charlie: Missing required field: 'gpa'  
# ✗ Diana: GPA must be between 0.0 and 4.0, got 5.0  
# ✗ Eve: Age must be between 16 and 100, got 150  
This validation function checks multiple aspects of the data: field presence, data types, 
and value constraints. It returns both a boolean indicating validity and a descriptive error 
message, allowing calling code to either reject invalid data or provide h elpful feedback to 
users.  
Notice that the function allows GPA to be either int or float by specifying (int, float)  as the 
expected type. This flexibility is important because a GPA of 3 (integer) and 3.0 (float) 
represent the same value, and both should be considered valid.  
9.3 Validating Collections  
When working with a list of dictionaries, you should validate all records to ensure 
collection -wide consistency:  
def validate_student_collection(students):  
    """ 
    Validate an entire collection of student dictionaries.  
     

    Parameters:  
        students: List of student dictionaries  
     
    Returns:  
        tuple: (all_valid, validation_report)  
               all_valid is True if all students are valid  
               validation_report is a list of (index, is_valid, message) tuples  
    """ 
    report = []  
    all_valid = True  
     
    for index, student in enumerate(students):  
        is_valid, message = validate_student(student)  
        report.append((index, is_valid, message))  
        if not is_valid:  
            all_valid = False  
     
    return all_valid, report  
 
# Test collection validation  
students = [  
    {"name": "Alice Johnson", "age": 20, "major": "Computer Science", "gpa": 3.8},  
    {"name": "Bob", "age": "22", "major": "Math", "gpa": 3.6},  
    {"name": "Charlie", "age": 21, "major": "Physics", "gpa": 3.9},  
    {"name": "Diana", "age": 19, "major": "Biology", "gpa": 5.0},  
] 

 
all_valid, report = validate_student_collection(students)  
 
print(f"Collection valid: {all_valid} \n") 
print("Detailed validation report:")  
for index, is_valid, message in report:  
    status = "✓" if is_valid else " ✗" 
    student_name = students[index].get('name', 'Unknown')  
    print(f"  {status} Student {index} ({student_name}): {message}")  
# Output:  
# Collection valid: False  
# 
# Detailed validation report:  
#   ✓ Student 0 (Alice Johnson): Valid  
#   ✗ Student 1 (Bob): Field 'age' has wrong type. Expected int, got str  
#   ✓ Student 2 (Charlie): Valid  
#   ✗ Student 3 (Diana): GPA must be between 0.0 and 4.0, got 5.0  
This collection validator provides a complete report showing which records are valid and 
which have problems, along with specific error messages. This is invaluable when 
importing large datasets —you can identify and fix all problems at once rather than 
discovering them one at a time as your program crashes.  
9.4 Safe Data Cleaning  
Sometimes you receive data that is almost correct but needs minor adjustments. Data 
cleaning involves transforming data to match your schema:  
def clean_student_data(raw_student):  
    """ 
    Clean and normalize student data to match schema.  

     
    Attempts to fix common data quality issues:  
    - Convert string numbers to actual numbers  
    - Trim whitespace from strings  
    - Normalize text casing  
     
    Parameters:  
        raw_student: Dictionary that might need cleaning  
     
    Returns:  
        tuple: (cleaned_student, warnings)  
               cleaned_student is the cleaned dictionary  
               warnings is a list of issues that were fixed  
    """ 
    cleaned = {}  
    warnings = []  
     
    # Clean name  
    if "name" in raw_student:  
        cleaned["name"] = raw_student["name"].strip()  
        if raw_student["name"] != cleaned["name"]:  
            warnings.append("Trimmed whitespace from name")  
     
    # Clean and convert age  
    if "age" in raw_student:  
        if isinstance(raw_student["age"], str):  

            try: 
                cleaned["age"] = int(raw_student["age"])  
                warnings.append("Converted age from string to integer")  
            except ValueError:  
                cleaned["age"] = raw_student["age"]  # Keep as -is, will fail validation  
                warnings.append(f"Could not convert age '{raw_student['age']}' to integer")  
        else:  
            cleaned["age"] = raw_student["age"]  
     
    # Clean major  
    if "major" in raw_student:  
        cleaned["major"] = raw_student["major"].strip()  
        if raw_student["major"] != cleaned["major"]:  
            warnings.append("Trimmed whitespace from major")  
     
    # Clean and convert GPA  
    if "gpa" in raw_student:  
        if isinstance(raw_student["gpa"], str):  
            try: 
                cleaned["gpa"] = float(raw_student["gpa"])  
                warnings.append("Converted GPA from string to float")  
            except ValueError:  
                cleaned["gpa"] = raw_student["gpa"]  # Keep as -is, will fail validation  
                warnings.append(f"Could not convert GPA '{raw_student['gpa']}' to float")  
        else:  
            cleaned["gpa"] = raw_student["gpa"]  

     
    return cleaned, warnings  
 
# Test data cleaning  
messy_students = [  
    {"name": "  Alice Johnson  ", "age": "20", "major": "Computer Science  ", "gpa": "3.8"},  
    {"name": "Bob Martinez", "age": "twenty -two", "major": "Math", "gpa": "3.6"},  
    {"name": "Charlie", "age": 21, "major": "Physics", "gpa": 3.9},  
] 
 
print("Data cleaning results: \n") 
for raw in messy_students:  
    cleaned, warnings = clean_student_data(raw)  
    print(f"Original: {raw}")  
    print(f"Cleaned:  {cleaned}")  
    if warnings:  
        print("Warnings:")  
        for warning in warnings:  
            print(f"  - {warning}")  
    print()  
Data cleaning should be applied cautiously. You want to fix obvious problems (like 
whitespace or string numbers) without making assumptions that could corrupt data. 
Always log what changes you make so you can review them and ensure your cleaning logic 
is correct.  
9.5 Combining Validation and Cleaning  
A robust data import pipeline combines cleaning and validation:  
def import_student_safely(raw_student):  

    """ 
    Import a student record with cleaning and validation.  
     
    Returns:  
        tuple: (student, success, messages)  
               student is the cleaned dictionary (or None if invalid)  
               success is True if import succeeded  
               messages is a list of informational/error messages  
    """ 
    messages = []  
     
    # Step 1: Clean the data  
    cleaned, clean_warnings = clean_student_data(raw_student)  
    messages.extend(clean_warnings)  
     
    # Step 2: Validate the cleaned data  
    is_valid, validation_msg = validate_student(cleaned)  
    messages.append(f"Validation: {validation_msg}")  
     
    if is_valid:  
        return cleaned, True, messages  
    else:  
        return None, False, messages  
 
# Test safe import  
test_records = [  

    {"name": "  Alice  ", "age": "20", "major": "CS", "gpa": "3.8"},  
    {"name": "Bob", "age": "invalid", "major": "Math", "gpa": "3.6"},  
    {"name": "", "age": "20", "major": "Physics", "gpa": "3.7"},  
] 
 
print("Safe import results: \n") 
successfully_imported = []  
for raw in test_records:  
    student, success, messages in import_student_safely(raw):  
     
    if success:  
        successfully_imported.append(student)  
        print(f"✓ Successfully imported: {student['name']}")  
    else:  
        print(f"✗ Failed to import: {raw}")  
     
    if messages:  
        for msg in messages:  
            print(f"  {msg}")  
    print()  
 
print(f"\nSuccessfully imported {len(successfully_imported)} out of {len(test_records)} 
records")  
This pipeline ensures that only valid, clean data enters your system. Invalid records are 
rejected with clear explanations of what went wrong, allowing you to fix the source data 
and retry the import.  
 

Section 10: Preparing for Object -Oriented Programming  
Throughout this chapter, you have been working with a pattern that organizes data 
(dictionaries) and operations on that data (functions) separately. This works well for many 
tasks, but as your programs grow more complex, you will discover limitations. This  section 
introduces the conceptual bridge between dictionary -based programming and object -
oriented programming (OOP), preparing you for the transition you will make in upcoming 
chapters.  
10.1 Recognizing the Limitations  
As your programs grow, the dictionary -based approach reveals some challenges:  
Problem 1: Scattered Functionality  
Functions that operate on student dictionaries are defined separately from the data:  
students = [  
    {"name": "Alice", "gpa": 3.8, "courses": []},  
    {"name": "Bob", "gpa": 3.6, "courses": []}  
] 
 
def add_course(student, course_name):  
    student['courses'].append(course_name)  
 
def calculate_status(student):  
    if student['gpa'] >= 3.5:  
        return "Dean's List"  
    return "Good Standing"  
 
def display_student(student):  
    print(f"{student['name']}: {calculate_status(student)}")  
 

# Using the system  
add_course(students[0], "Math")  
display_student(students[0])  
The functions are separate from the data they operate on. As you add more functions, it 
becomes harder to remember which functions work with students, which work with 
courses, and how they all relate.  
Problem 2: No Encapsulation  
Anyone can modify the dictionary directly, potentially breaking assumptions:  
student = {"name": "Alice", "gpa": 3.8}  
 
# Nothing prevents invalid modifications  
student['gpa'] = 5.0  # Invalid GPA!  
student['age'] = -10  # Invalid age!  
del student['name']   # Broke the structure!  
There is no way to protect the data or enforce rules about how it can be modified. You rely 
entirely on discipline and careful coding to maintain data integrity.  
Problem 3: Unclear Relationships  
When you see a dictionary in code, you can't immediately tell what it represents without 
looking at its keys:  
# What does this represent?  
mystery_dict = {"name": "Alice", "gpa": 3.8}  
 
# Could it be a student? An employee? Something else?  
# You have to examine the keys to figure it out  
10.2: The Object -Oriented Solution Preview  
Object-oriented programming addresses these limitations by bundling data and behavior 
together into objects. Here's a preview of how the student system looks with OOP (don't 
worry about understanding all the syntax yet —we'll cover this thoroughly in later chapters):  

class Student:  
    """Represents a student with academic information"""  
     
    def __init__(self, name, gpa):  
        """Initialize a new student"""  
        self.name = name  
        self.gpa = gpa  
        self.courses = []  
     
    def add_course(self, course_name):  
        """Add a course to the student's schedule"""  
        self.courses.append(course_name)  
     
    def calculate_status(self):  
        """Determine academic status"""  
        if self.gpa >= 3.5:  
            return "Dean's List"  
        return "Good Standing"  
     
    def update_gpa(self, new_gpa):  
        """Update GPA with validation"""  
        if 0.0 <= new_gpa <= 4.0:  
            self.gpa = new_gpa  
        else:  
            raise ValueError("GPA must be between 0.0 and 4.0")  
     

    def display(self):  
        """Display student information"""  
        print(f"{self.name}: {self.calculate_status()}")  
 
# Using the object -oriented version  
alice = Student("Alice", 3.8)  
alice.add_course("Math")  
alice.display()  
 
# Attempting invalid modification raises an error  
try: 
    alice.update_gpa(5.0)  
except ValueError as e:  
    print(f"Error: {e}")  
Notice the differences:  
• Data and methods are bundled together in a class  
• Methods like add_course()  and calculate_status()  belong to the student  
• The syntax is cleaner: alice.add_course("Math")  instead of add_course(alice, 
"Math")  
• Validation is built into the update_gpa()  method, protecting data integrity  
• The code is more self -documenting —it's clear what a Student object represents  
10.3 Mapping Dictionaries to Objects  
Understanding the parallels between dictionary patterns and objects will make learning 
OOP easier:  
Dictionary Keys ↔ Object Attributes  
# Dictionary approach  
student_dict = {"name": "Alice", "age": 20, "gpa": 3.8}  

print(student_dict["name"])  # Access using brackets and string key  
 
# Object approach (preview)  
student_obj = Student("Alice", 20, 3.8)  
print(student_obj.name)  # Access using dot notation  
Dictionary keys become object attributes . Instead of student["name"] , you write 
student.name . The dot notation is cleaner and allows development tools to provide better 
autocomplete and error checking.  
Functions on Dictionaries ↔ Methods on Objects  
# Dictionary approach: function is separate  
def update_gpa(student, new_gpa):  
    student["gpa"] = new_gpa  
 
update_gpa(student_dict, 3.9)  
 
# Object approach: method belongs to the object  
student_obj.update_gpa(3.9)  
Functions become methods  that belong to the object. The object -oriented syntax makes it 
clear that update_gpa  is an operation specifically for students, not some general function.  
Lists of Dictionaries ↔ Lists of Objects  
# Dictionary approach  
students_dicts = [  
    {"name": "Alice", "gpa": 3.8},  
    {"name": "Bob", "gpa": 3.6}  
] 
 
# Object approach  

students_objects = [  
    Student("Alice", 3.8),  
    Student("Bob", 3.6)  
] 
 
# Both can be processed similarly  
for student in students_objects:  
    student.display()  
The patterns you've learned for working with lists of dictionaries —iterating, filtering, 
sorting, grouping —transfer directly to lists of objects.  
Factory Functions ↔ Constructors  
# Dictionary approach: factory function  
def create_student(name, gpa):  
    return {"name": name, "gpa": gpa, "courses": []}  
 
# Object approach: constructor (__init__ method)  
class Student:  
    def __init__(self, name, gpa):  
        self.name = name  
        self.gpa = gpa  
        self.courses = []  
Your factory functions become constructors  that initialize new objects with consistent 
structure.  
10.4 Why Learn Dictionaries First?  
You might wonder: if objects are better, why learn dictionaries first? There are several good 
reasons:  

1. Simpler Mental Model:  Dictionaries are simpler to understand initially. You're working 
with familiar built -in data types and straightforward functions. This allows you to focus on 
program logic without the additional complexity of class syntax and object -oriented 
concepts.  
2. Still Useful:  Dictionaries remain extremely useful even when you know OOP. They're 
perfect for configuration data, JSON/API responses, temporary data transformations, and 
situations where defining a full class would be overkill.  
3. Natural Progression:  Learning dictionaries first makes learning OOP easier because you 
already understand the problems that OOP solves. You've experienced the limitations 
firsthand, so you'll appreciate why objects organize code better.  
4. Foundation for Understanding:  Many object -oriented concepts map directly to 
patterns you've already learned:  
• Schema validation → Type checking and property validation  
• Factory functions → Constructors  
• Consistent structure → Class definitions  
• Related functions → Methods  
10.5 Looking Ahead  
In upcoming chapters on object -oriented programming, you will learn:  
Classes and Objects:  How to define your own data types (classes) and create instances of 
those types (objects).  
Encapsulation:  How to bundle data and methods together, protecting internal state and 
exposing a clean interface.  
Inheritance:  How to create specialized types based on existing types, reusing and 
extending functionality.  
Polymorphism:  How different objects can respond to the same method calls in type -
appropriate ways.  
Design Patterns:  How to structure larger programs using objects to create maintainable, 
scalable code.  
As you make this transition, remember that the skills you've developed with dictionaries 
transfer directly. You already understand data modeling, validation, CRUD operations, and 

data transformations. Now you'll learn how to express these concepts more elegantly with 
objects.  
 
**Common Mistakes and How to Avoid Them**  
As you work with lists of dictionaries, you will likely encounter certain common mistakes. 
Learning to recognize and avoid these pitfalls will make you a more effective programmer.  
Mistake 1: Inconsistent Dictionary Structures  
# WRONG: Different keys in different dictionaries  
students = [  
    {"name": "Alice", "age": 20, "gpa": 3.8},  
    {"full_name": "Bob", "age": 22, "gpa": 3.6},  # Wrong key name!  
    {"name": "Charlie", "gpa": 3.9}  # Missing age!  
] 
 
# This will cause errors  
for student in students:  
    print(f"{student['name']} is {student['age']} years old")  
    # KeyError when processing Bob and Charlie  
Solution:  Always use factory functions or validation to ensure consistent structure:  
# CORRECT: Use factory function  
def create_student(name, age, gpa):  
    return {"name": name, "age": age, "gpa": gpa}  
 
students = [  
    create_student("Alice", 20, 3.8),  
    create_student("Bob", 22, 3.6),  
    create_student("Charlie", 21, 3.9)  

] 
Mistake 2: Modifying a List While Iterating  
# WRONG: Removing items during iteration  
students = [  
    {"name": "Alice", "gpa": 3.8},  
    {"name": "Bob", "gpa": 2.5},  
    {"name": "Charlie", "gpa": 2.3}  
] 
 
for student in students:  
    if student['gpa'] < 3.0:  
        students.remove(student)  # Dangerous!  
 
# This can skip elements or cause unexpected behavior  
Solution:  Use list comprehension to create a new list, or iterate over a copy:  
# CORRECT: List comprehension  
students = [s for s in students if s['gpa'] >= 3.0]  
 
# CORRECT: Iterate over a copy  
for student in students[:]:  # [:] creates a shallow copy  
    if student['gpa'] < 3.0:  
        students.remove(student)  
Mistake 3: Forgetting That Dictionaries Are Mutable  
# WRONG: Unintended modification  
template = {"name": "", "gpa": 0.0}  
students = []  

 
# This creates three references to the SAME dictionary!  
for i in range(3):  
    students.append(template)  
     
students[0]['name'] = "Alice"  
print(students[1]['name'])  # Output: Alice (unexpected!)  
# All three students share the same dictionary  
Solution:  Create new dictionaries, don't reuse the same one:  
# CORRECT: Create new dictionary each time  
for i in range(3):  
    students.append({"name": "", "gpa": 0.0})  
 
# Or use copy()  
for i in range(3):  
    students.append(template.copy())  
Mistake 4: Not Handling Missing Keys  
# WRONG: Assuming all keys exist  
students = [  
    {"name": "Alice", "gpa": 3.8},  
    {"name": "Bob"}  # Missing gpa!  
] 
 
total_gpa = sum(s['gpa'] for s in students)  # KeyError!  
Solution:  Use .get() with default values:  
# CORRECT: Safe access with default  

total_gpa = sum(s.get('gpa', 0.0) for s in students)  
average_gpa = total_gpa / len(students)  
Mistake 5: Confusing sorted() and .sort()  
# WRONG: Expecting sorted() to modify the original list  
students = [{"name": "Charlie"}, {"name": "Alice"}]  
sorted(students, key=lambda s: s['name'])  
print(students[0]['name'])  # Still Charlie! sorted() doesn't modify in place  
Solution:  Understand the difference:  
# CORRECT: sorted() returns a new list  
sorted_students = sorted(students, key=lambda s: s['name'])  
 
# CORRECT: .sort() modifies in place  
students.sort(key=lambda s: s['name'])  
Mistake 6: Incorrect Multi -Level Sorting  
# WRONG: Trying to sort by multiple fields separately  
students.sort(key=lambda s: s['major'])  
students.sort(key=lambda s: s['gpa'])  
# This only sorts by GPA, losing the major ordering  
Solution:  Return a tuple in the key function:  
# CORRECT: Multi -level sort with tuple  
students.sort(key=lambda s: (s['major'], s['gpa']))  
Mistake 7: Not Validating JSON Data  
# WRONG: Assuming external JSON is valid  
import json  
 
with open('students.json') as f:  

    students = json.load(f)  
     
# Immediately using the data without validation  
for student in students:  
    print(f"{student['name']}: {student['gpa']}")  # Might fail!  
Solution:  Always validate data from external sources:  
# CORRECT: Validate after loading  
with open('students.json') as f:  
    raw_students = json.load(f)  
 
students = []  
for raw in raw_students:  
    is_valid, message = validate_student(raw)  
    if is_valid:  
        students.append(raw)  
    else:  
        print(f"Warning: Invalid student data - {message}")  
 
Practice Exercises  
Beginner Level  
Exercise 1: Book Library  Create a list of book dictionaries with fields: title, author, year, 
isbn, available. Implement:  
• Add a new book  
• Find a book by title (case -insensitive)  
• Mark a book as checked out (set available to False)  
• Mark a book as returned (set available to True)  

• Display all available books  
Exercise 2: Product Inventory  Create a list of product dictionaries with fields: name, price, 
quantity, category. Implement:  
• Add a new product  
• Update product quantity  
• Find all products in a specific category  
• Calculate total inventory value  
• Display all products sorted by price  
Exercise 3: Student Grades  Create a list of student dictionaries with fields: name, grades 
(a list), major. Implement:  
• Add a student  
• Add a grade to a student's grades list  
• Calculate average grade for each student  
• Find all students with average above 85  
• Display students sorted by average grade (highest first)  
Intermediate Level  
Exercise 4: Restaurant Menu Management  Create a restaurant menu system with 
dictionaries for items: name, category (appetizer/entree/dessert), price, ingredients (list), 
vegetarian (boolean). Implement:  
• Add/remove menu items  
• Find all vegetarian options  
• Find items by ingredient (e.g., all items containing "chicken")  
• Calculate average price by category  
• Generate a formatted menu organized by category  
Exercise 5: Employee Database  Create an employee database with fields: id, name, 
department, salary, hire_date, email. Implement:  
• Add/remove employees with validation (ensure unique IDs and valid emails)  

• Update employee information  
• Calculate average salary by department  
• Find employees hired in a specific year  
• Generate a report of all employees sorted by department then by salary  
Exercise 6: Movie Collection with Ratings  Create a movie collection with fields: title, 
director, year, genres (list), rating, watched (boolean). Implement:  
• Add movies with validation  
• Mark movies as watched  
• Filter by genre, year range, and rating threshold  
• Calculate average rating for watched vs. unwatched movies  
• Generate recommendations (unwatched movies with rating > 4.0)  
• Export to JSON file and read back  
Challenge Level  
Exercise 7: Course Enrollment System  Create a system with two types of records:  
• Students: id, name, email, enrolled_courses (list of course_ids)  
• Courses: id, name, instructor, max_students, enrolled_students (list of student_ids)  
Implement:  
• Add students and courses  
• Enroll a student in a course (update both records, check max_students)  
• Drop a student from a course  
• Find all students in a course  
• Find all courses for a student  
• Identify courses that are full  
• Calculate enrollment statistics per course  
Exercise 8: E -commerce Order System  Create a complete e -commerce system with:  
• Products: id, name, price, stock  

• Customers: id, name, email, order_history (list of order_ids)  
• Orders: id, customer_id, items (list of {product_id, quantity}), total, status  
Implement:  
• Add products and customers  
• Create an order (validate stock, calculate total, update inventory)  
• Update order status (pending, shipped, delivered)  
• Get customer order history  
• Calculate total revenue  
• Find best -selling products  
• Generate a sales report  
• Save entire system to JSON and load it back  
Exercise 9: Social Network Analysis  Create a simplified social network with:  
• Users: id, name, friends (list of user_ids), posts (list of post objects)  
• Posts: id, author_id, content, timestamp, likes (list of user_ids)  
Implement:  
• Add users and posts  
• Add/remove friendships (bidirectional)  
• Like a post  
• Get a user's feed (posts from friends, sorted by timestamp)  
• Find most popular posts (most likes)  
• Calculate average posts per user  
• Find users with most friends  
• Suggest friends (friends of friends who aren't already friends)  
 
Reflection Questions  
After completing this chapter, reflect on these questions to deepen your understanding:  

1. Why is consistency important  when working with lists of dictionaries? What 
problems arise when dictionaries in the same list have different structures?    
2. Compare and contrast  list comprehensions with traditional for loops for filtering 
data. When would you choose one over the other?    
3. How does the key parameter  in sorted() work? Why is a lambda function often 
used with it?    
4. What are the trade -offs between using sorted() versus .sort()? When would you 
prefer each?    
5. Why is defaultdict  useful for grouping operations? How does it simplify code 
compared to regular dictionaries?    
6. What is the purpose of JSON  in modern programming? Why is it important that 
JSON is language -independent?    
7. How would you explain  the difference between json.dumps()/loads()  and 
json.dump()/load()  to someone learning Python?    
8. What strategies  can you use to safely access nested data structures without 
causing KeyError or IndexError exceptions?    
9. Why is data validation critical  when working with external data sources? What 
could go wrong without validation?    
10. How do the patterns  you learned with lists of dictionaries prepare you for object -
oriented programming? What parallels do you see?    
 
Key Takeaways  
Let's summarize the essential concepts from this chapter:  
1. Organization and Structure  Lists of dictionaries combine the ordering of lists with the 
labeled access of dictionaries, creating a powerful pattern for managing collections of 
structured records. Each dictionary represents one complete record, and all dictionaries in 
a list should have consistent structure (the same keys with compatible types).  
2. CRUD Operations Are Fundamental  Create, Read, Update, and Delete operations form 
the foundation of data management. You learned to implement each operation safely, with 
proper error handling and validation. These operations will appear in virtually every data -
driven application you buil d. 

3. Filtering and Searching  List comprehensions provide a concise, readable way to filter 
data based on conditions. You can combine multiple conditions with and/or, extract 
specific fields, and build flexible search functions that accept multiple optional criteria. 
Generator expressions offer memory -efficient alternatives for large datasets.  
4. Sorting and Organization  The sorted() function with lambda key functions allows sorting 
by any field or combination of fields. Multi -level sorting uses tuples to specify priority order. 
Understanding the difference between sorted() (returns new list) and .sort() (modifies in 
place) is crucial for correct program behavior.  
5. Grouping and Aggregation  defaultdict  simplifies grouping operations by automatically 
creating default values for new keys. Aggregations like sum, average, min, and max 
compute summary statistics. The pattern of grouping data then computing per -group 
aggregates is fundamental to data analysis . 
6. JSON: The Universal Data Format  JSON is the standard format for data exchange in 
modern programming. Understanding how to convert between Python objects and JSON 
(using dumps/loads  for strings, dump/load  for files) allows your programs to communicate 
with web APIs, save data portably, and integrate with other systems.  
7. Nested Structures Require Care  Real-world data often involves nested structures. 
Navigate nested data by chaining access operations. Use safe access patterns ( .get() with 
defaults, try -except blocks, or helper functions) to prevent crashes when data is missing or 
malformed. Understand when to flatten nested data into simpler structures for analysis.  
8. Validation Ensures Quality  Always validate data from external sources before using it. 
Check for required fields, correct types, and valid value ranges. Combine validation with 
data cleaning to handle common issues like whitespace or string numbers. Early validation 
prevents subtle  bugs and data corruption.  
9. From Dictionaries to Objects  The patterns you learned —organizing data in dictionaries, 
using factory functions, implementing operations as functions —map directly to object -
oriented programming. Dictionary keys become object attributes, functions become 
methods, and factory functions become constructors. Understanding these parallels will 
make learning OOP easier.  
10. Choose the Right Tool  Dictionaries are perfect for dynamic data, JSON interchange, 
configuration, and prototyping. Objects are better for complex behavior, encapsulation, 
and large systems. Understanding both gives you flexibility to choose the most appropriate 
tool for each s ituation.  
 

Vocabulary Review  
List of Dictionaries:  A list where each element is a dictionary, typically with consistent 
structure, representing a collection of records.  
CRUD Operations:  Create, Read, Update, Delete —the four fundamental operations 
performed on data.  
Schema:  A formal definition of the structure data should have, including required fields, 
data types, and constraints.  
Factory Function:  A function dedicated to creating dictionaries (or objects) with 
consistent structure and validated data.  
List Comprehension:  A concise Python syntax for creating lists by filtering or transforming 
existing sequences: [expr for item in sequence if condition] . 
Lambda Function:  An anonymous, single -expression function often used with sorted(), 
filter(), and similar functions: lambda x: x['field'] . 
Aggregation:  Computing summary statistics (count, sum, average, min, max) from 
collections of data.  
Grouping:  Organizing data into categories based on field values, often using defaultdict . 
JSON (JavaScript Object Notation):  A text-based format for data interchange, structurally 
similar to Python dictionaries and lists.  
Nested Data Structure:  Data where values can themselves be dictionaries or lists, 
creating hierarchies of arbitrary depth.  
Flattening:  Converting nested hierarchical data into a simpler, single -level structure.  
Validation:  Checking data against a schema to ensure it has required fields, correct types, 
and valid values.  
Data Cleaning:  Transforming data to fix common quality issues like whitespace, type 
mismatches, or formatting inconsistencies.  
Encapsulation:  Bundling data and operations together (a concept from OOP that 
dictionaries partially support through related functions).  
Index (data structure):  A dictionary mapping unique keys to records for fast O(1) lookup 
instead of O(n) linear search.  
 

Looking Ahead to Object -Oriented Programming  
In this chapter, you mastered working with lists of dictionaries —a powerful pattern for 
organizing and manipulating structured data collections. You learned to create consistent 
structures, perform CRUD operations, filter and sort data, compute aggregates,  work with 
JSON, navigate nested structures, and validate data quality.  
These skills form a solid foundation for the next major topic in your programming journey: 
object-oriented programming (OOP) . In upcoming chapters, you will learn how to:  
• Define classes  that serve as blueprints for creating objects with consistent 
structure and behavior  
• Create objects  (instances of classes) that bundle data and methods together  
• Implement encapsulation  to protect data and expose clean interfaces  
• Use inheritance  to create specialized types based on existing ones, promoting 
code reuse  
• Apply polymorphism  to write flexible code that works with different types of 
objects  
• Design larger systems  using objects as building blocks  
The transition from dictionaries to objects will feel natural because you already understand 
the concepts —you simply need to learn the new syntax and additional capabilities that 
OOP provides. Remember: a dictionary with related functions is very similar t o an object 
with methods. The key difference is that objects formalize this relationship, making your 
code more organized, maintainable, and scalable.  
As you move forward, keep practicing with lists of dictionaries. These patterns remain 
useful even when you know OOP, particularly for JSON data, configuration, prototyping, 
and situations where defining a full class would be overkill. The best programmers  know 
multiple approaches and choose the most appropriate tool for each situation.  
Congratulations on completing Chapter 21!  You have gained essential skills for working 
with structured data collections —skills you will use throughout your programming career.  
 
Additional Resources  
For Further Practice:  
• Work through all practice exercises, starting with beginner level  

• Create your own mini -projects using lists of dictionaries (personal budget tracker, 
recipe organizer, etc.)  
• Explore real -world datasets in JSON format and practice importing, analyzing, and 
transforming them  
For Deeper Understanding:  
• Python's official documentation on lists: 
https://docs.python.org/3/tutorial/datastructures.html   
• Python's official documentation on dictionaries: 
https://docs.python.org/3/tutorial/datastructures.html#dictionaries   
• Python's json module documentation: https://docs.python.org/3/library/json.html   
• Python's collections  module documentation (for defaultdict  and Counter): 
https://docs.python.org/3/library/collections.html   
Preparation for OOP:  
• Review the parallels between dictionaries and objects discussed in Section 10  
• Think about programs you've written —where would bundling data and behavior 
together make the code clearer?  
• Look ahead at the next chapter's learning objectives to see what's coming  
 
End of Chapter 21  
 
Nazari, Mujtaba  Please check the review below and let me know if you have any questions. 
Thank you  
Overview of Week 8 Content Review (Lists of Dictionaries)  
The Week 8 content on "Lists of Dictionaries"  is comprehensive and generally well -aligned 
with the course goals. It covers creating and using list -of-dict structures, CRUD operations, 
filtering, sorting, grouping, JSON serialization, and transitions toward object -oriented 
design. The core concepts ar e well chosen, and the real -world examples (students, 
products, books, etc.) make the material relatable.  
After a close reading, we identified a few minor errors (mostly formatting issues in code 
blocks) and several opportunities to clarify explanations or add emphasis  to ensure 

student understanding. We also noted places where content could be slightly restructured 
for better flow or consistency (for example, addressing a duplicated topic and aligning 
section titles with content).  
<style>  
        :root {  
        --accent: #464feb;  
        --timeline-ln: linear-gradient(to bottom, transparent 0%, #b0beff 15%, #b0beff 85%, 
transparent 100%);  
        --timeline-border: #ffffff;  
        --bg-card: #f5f7fa;  
        --bg-hover: #ebefff;  
        --text-title: #424242;  
        --text-accent: var( --accent);  
        --text-sub: #424242;  
        --radius: 12px;  
        --border: #e0e0e0;  
        --shadow: 0 2px 10px rgba(0, 0, 0, 0.06);  
        --hover-shadow: 0 4px 14px rgba(39, 16, 16, 0.1);  
        --font: "Segoe Sans", "Segoe UI", "Segoe UI Web (West European)", -apple-system, 
"system-ui", Roboto, "Helvetica Neue", sans -serif;  
        --overflow-wrap: break -word;  
    } 
 
    @media (prefers -color-scheme: dark) {  
        :root {  
            --accent: #7385ff;  

            --timeline-ln: linear-gradient(to bottom, transparent 0%, transparent 3%, #6264a7 
30%, #6264a7 50%, transparent 97%, transparent 100%);  
            --timeline-border: #424242;  
            --bg-card: #1a1a1a;  
            --bg-hover: #2a2a2a;  
            --text-title: #ffffff;  
            --text-sub: #ffffff;  
            --shadow: 0 2px 10px rgba(0, 0, 0, 0.3);  
            --hover-shadow: 0 4px 14px rgba(0, 0, 0, 0.5);  
            --border: #3d3d3d;  
        } 
    } 
 
    @media (prefers -contrast: more),  
    (forced-colors: active) {  
        :root {  
            --accent: ActiveText;  
            --timeline-ln: ActiveText;  
            --timeline-border: Canvas;  
            --bg-card: Canvas;  
            --bg-hover: Canvas;  
            --text-title: CanvasText;  
            --text-sub: CanvasText;  
            --shadow: 0 2px 10px Canvas;  
            --hover-shadow: 0 4px 14px Canvas;  
            --border: ButtonBorder;  

        } 
    } 
 
    .insights-container {  
        display: grid;  
        grid-template -columns: repeat(2,minmax(240px,1fr));  
        padding: 0px 16px 0px 16px;  
        gap: 16px;  
        margin: 0 0;  
        font-family: var( --font);  
    } 
 
    .insight-card:last -child:nth -child(odd){  
        grid-column: 1 / -1; 
    } 
 
    .insight-card {  
        background -color: var( --bg-card);  
        border-radius: var( --radius);  
        border: 1px solid var( --border);  
        box-shadow: var( --shadow);  
        min-width: 220px;  
        padding: 16px 20px 16px 20px;  
    } 
 
    .insight-card:hover {  

        background -color: var( --bg-hover);  
    } 
 
    .insight-card h4 {  
        margin: 0px 0px 8px 0px;  
        font-size: 1.1rem;  
        color: var( --text-accent);  
        font-weight: 600;  
        display: flex;  
        align-items: center;  
        gap: 8px;  
    } 
 
    .insight-card .icon {  
        display: inline -flex;  
        align-items: center;  
        justify-content: center;  
        width: 20px;  
        height: 20px;  
        font-size: 1.1rem;  
        color: var( --text-accent);  
    } 
 
    .insight-card p {  
        font-size: 0.92rem;  
        color: var( --text-sub);  

        line-height: 1.5;  
        margin: 0px;  
        overflow-wrap: var( --overflow-wrap);  
    } 
 
    .insight-card p b, .insight -card p strong {  
        font-weight: 600;  
    } 
 
    .metrics-container {  
        display:grid;  
        grid-template -columns:repeat(2,minmax(210px,1fr));  
        font-family: var( --font);  
        padding: 0px 16px 0px 16px;  
        gap: 16px;  
    } 
 
    .metric-card:last -child:nth -child(odd){  
        grid-column:1 / -1;  
    } 
 
    .metric-card {  
        flex: 1 1 210px;  
        padding: 16px;  
        background -color: var( --bg-card);  
        border-radius: var( --radius);  

        border: 1px solid var( --border);  
        text-align: center;  
        display: flex;  
        flex-direction: column;  
        gap: 8px;  
    } 
 
    .metric-card:hover {  
        background -color: var( --bg-hover);  
    } 
 
    .metric-card h4 {  
        margin: 0px;  
        font-size: 1rem;  
        color: var( --text-title);  
        font-weight: 600;  
    } 
 
    .metric-card .metric -card-value {  
        margin: 0px;  
        font-size: 1.4rem;  
        font-weight: 600;  
        color: var( --text-accent);  
    } 
 
    .metric-card p {  

        font-size: 0.85rem;  
        color: var( --text-sub);  
        line-height: 1.45;  
        margin: 0;  
        overflow-wrap: var( --overflow-wrap);  
    } 
 
    .timeline -container {  
        position: relative;  
        margin: 0 0 0 0;  
        padding: 0px 16px 0px 56px;  
        list-style: none;  
        font-family: var( --font);  
        font-size: 0.9rem;  
        color: var( --text-sub);  
        line-height: 1.4;  
    } 
 
    .timeline -container::before {  
        content: "";  
        position: absolute;  
        top: 0;  
        left: calc( -40px + 56px);  
        width: 2px;  
        height: 100%;  
        background: var( --timeline-ln); 

    } 
 
    .timeline -container > li {  
        position: relative;  
        margin-bottom: 16px;  
        padding: 16px 20px 16px 20px;  
        border-radius: var( --radius);  
        background: var( --bg-card);  
        border: 1px solid var( --border);  
    } 
 
    .timeline -container > li:last -child {  
        margin-bottom: 0px;  
    } 
 
    .timeline -container > li:hover {  
        background -color: var( --bg-hover);  
    } 
 
    .timeline -container > li::before {  
        content: "";  
        position: absolute;  
        top: 18px;  
        left: -40px;  
        width: 14px;  
        height: 14px;  

        background: var( --accent);  
        border: var( --timeline-border) 2px solid;  
        border-radius: 50%;  
        transform: translateX( -50%);  
        box-shadow: 0px 0px 2px 0px #00000012, 0px 4px 8px 0px #00000014;  
    } 
 
    .timeline -container > li h4 {  
        margin: 0 0 5px;  
        font-size: 1rem;  
        font-weight: 600;  
        color: var( --accent);  
    } 
 
    .timeline -container > li h4 em {  
        margin: 0 0 5px;  
        font-size: 1rem;  
        font-weight: 600;  
        color: var( --accent);  
        font-style: normal;        
    } 
 
    .timeline -container > li * {  
        margin: 0;  
        font-size: 0.9rem;  
        color: var( --text-sub);  

        line-height: 1.4;  
    } 
 
    .timeline -container > li * b, .timeline -container > li * strong {  
        font-weight: 600;  
    } 
        @media (max -width:600px){  
      .metrics-container,  
      .insights-container{  
        grid-template -columns:1fr;  
      } 
    } 
</style>  
<div class="insights -container">  
  <div class="insight -card">  
    <h4>  Code & Formatting Fixes</h4>  
    <p>Correct HTML -escaped characters in code (e.g. `&lt;`, `&gt;`) and minor typos. 
Ensure all Python examples run without errors and display as intended.</p>  
  </div>  
  <div class="insight -card">  
    <h4>      Clarity & Explanation</h4>  
    <p>Add brief explanations when introducing new or advanced concepts (like lambda 
functions, <code>defaultdict</code>, etc.). Enhance or simplify wording in a few places to 
be more beginner -friendly.</p>  
  </div>  
  <div class="insight -card">  
    <h4>    Structural Tweaks</h4>  

    <p>Align section content with headings (e.g. cover "map" or adjust title), merge or 
reference overlapping sections to avoid redundancy, and highlight important terms or 
takeaways for emphasis.</p>  
  </div>  
</div>  
Detailed Recommendations by Section  
The table below summarizes the recommended edits and improvements for each section 
of the Week 8 content. Each recommendation includes whether to add, remove, or edit 
content, along with specific details and the rationale:  
Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
Part B: Querying (Filter, Map, 
Sort, Aggregate)  Edit  Adjust section title or 
content – If the content 
doesn’t explicitly cover 
the map() function, 
remove "Map" from the 
title (e.g. "Filter, Sort, 
and Aggregate") or add a 
short example using 
map to extract or 
transform data from the 
list of dictionaries.  Align section title 
with actual 
content. “Map” is 
mentioned in the 
heading but not 
demonstrated, 
which could 
confuse 
students. Either 
include an 
example for 
completeness or 
avoid the term if 
it’s not taught.  
21.1 Why Use Lists of 
Dictionaries?  Add  Emphasize one -
dictionary -per-item – 
Insert a sentence 
explicitly stating that 
each dictionary in the list 
represents one record 
(e.g., one student, one 
product). For example: 
“Each dictionary holds Ensures students 
immediately 
grasp the 
concept that a 
list of dictionaries 
means multiple 
items of the same 
structure. This 
clarity reinforces 

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
data for one student; a 
list allows us to manage 
multiple students.”  the motivation for 
this data 
structure pattern.  
21.2 Creating and Accessing 
Nested Structures  Add  Note on creation 
methods producing 
same structure  – After 
showing the three 
methods of building the 
students  list, mention 
that all methods result in 
an equivalent list of 
dictionaries. For 
instance: “All three 
approaches above 
create the same list 
structure for students.”  Reassures 
students that 
different coding 
styles yield the 
same outcome. 
This confirmation 
can help prevent 
confusion when 
they see multiple 
ways to do the 
same thing.  
21.3 CRUD Operations 
(Create/Read/Update/Delete
) Add  Clarify update function 
behavior  – In the 
explanation of 
update_student_info , 
note that any field name 
passed that isn’t in the 
student dictionary will 
be ignored. E.g., “If an 
invalid field name is 
given, the function safely 
ignores it and leaves the 
student record 
unchanged for that field.”  Highlights a 
design decision 
(ignoring 
unknown keys) so 
students 
understand the 
code won’t add 
new keys 
accidentally. This 
manages 
expectations and 
links to the earlier 
idea of 
maintaining a 
consistent 
schema.  

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
21.4 Ensuring Data 
Consistency (Schema)  Edit  Improve validation 
message format  – In 
validate_student() , 
format the output for 
missing keys more 
clearly. For example, 
instead of printing a 
Python set like {'major'}, 
change the print to: 
Missing keys: major  
(joining the set into a 
comma-separated string 
if multiple).  Makes error 
messages more 
readable for 
learners. Seeing 
Missing keys: 
major is cleaner 
and less 
intimidating than 
Python’s set 
notation. It 
focuses attention 
on what exactly is 
missing.  
21.4 Ensuring Data 
Consistency (Schema)  Add  Note on safe default 
access – When 
introducing 
safe_get_student_info , 
add a short remark that 
this approach prevents 
runtime errors when 
data is inconsistent, but 
it doesn’t enforce fixing 
the data. For example: 
“Using safe getters 
avoids crashes (by 
providing defaults), but 
keep in mind it doesn’t 
correct the missing data. 
It’s a way to handle 
inconsistencies 
gracefully.”  Emphasizes the 
trade-off between 
safety and data 
integrity. 
Students learn 
that while default 
values prevent 
errors, relying on 
them might hide 
underlying data 
issues – a critical 
thinking point as 
they design 
programs.  
21.5 Complete Example: 
Product Catalog  Edit  Fix code formatting in 
display – Correct the f -
string format specifiers Ensures the 
provided code is 
error-free and can 

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
in display_catalog() . For 
instance, change 
{'ID':&lt;5}  to {'ID':<5} 
(and similarly for other 
fields) so the alignment 
works. Currently the < 
appears as &lt; due to an 
encoding issue.  be executed as 
shown. Fixing the 
HTML escape 
sequences for < 
and > in code 
blocks is crucial 
for students who 
might copy and 
run the examples.  
21.5 Complete Example: 
Product Catalog  Add  Explain f -string 
alignment  – Add a brief 
comment or footnote 
explaining the formatting 
used in 
display_catalog() . For 
example: # {'Name':<20} 
left-aligns text in a 20 -
char field, ${price:<9.2f} 
formats price in 9 spaces 
with 2 decimals . Helps students 
understand the 
more advanced f -
string syntax. This 
section might be 
their first 
encounter with 
alignment and 
numeric 
formatting in f -
strings, so a short 
explanation will 
demystify the 
output 
formatting.  
21.6 Comparing Dicts to 
Future Objects  Remove/Merg
e Avoid repetition with 
21.19 – This brief section 
previewing objects can 
be merged with or 
moved to section 21.19. 
If 21.19 already re -
introduces the same 
comparison, consider 
removing 21.6 or 
converting it to a forward Prevents 
redundancy. 
Covering the “dict 
vs object” 
parallels twice 
can be repetitive. 
Merging them 
consolidates the 
concept, 
ensuring 

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
reference (e.g., “(We’ll 
revisit this comparison in 
section 21.19)”).  students focus 
once and get the 
full explanation at 
the appropriate 
point (likely in 
Part D when OOP 
is discussed in 
depth).  
21.7 Filtering and Searching 
Records  Edit  Correct comparison 
operators in code  – 
Several filter examples 
use symbols like > or <= 
that appeared as &gt; or 
&lt;= in the text. Ensure 
all comparison operators 
(<, >, <=, >=) display 
properly in the code 
blocks. (For instance, 
print the condition 
s["gpa"] > 3.7  exactly as 
written, not as &gt;.) Fixes a formatting 
error so that 
students see 
valid Python 
syntax. This 
prevents 
confusion or 
copy-paste errors 
– it’s important 
that every code 
snippet is 
accurate and 
ready to run.  
21.7 Filtering and Searching 
Records  Add  Briefly explain lambda  
– When introducing 
filter() with a lambda, 
add a short explanation 
of what a lambda 
function is. E.g., “Here 
we use a lambda (an 
anonymous one -line 
function) to specify the 
filter condition on the 
fly.” Similarly, clarify the 
generator expression 
example by mentioning Introduces new 
Python concepts 
in a student -
friendly way. 
Lambdas and 
generator 
expressions 
might be new to 
students; a one -
liner explanation 
ensures they 
understand the 
code used and 

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
it’s like a memory -
efficient list 
comprehension.  aren’t left puzzled 
by unfamiliar 
syntax.  
21.8 Sorting Lists of 
Dictionaries  Add  Clarify multi -key sort 
logic – After showing the 
example 
sorted(students, 
key=lambda s: 
(s["major"], -s["gpa"])) , 
explain how Python sorts 
by tuple: “The list is 
sorted first by major; 
within each major, the -
gpa ensures a secondary 
sort by GPA in 
descending order.”  You 
could also explicitly note 
that using a tuple in the 
key allows multi -level 
sorting.  Reinforces 
understanding of 
a slightly complex 
concept. While 
the code works, 
explaining the 
mechanism 
(primary vs 
secondary sort 
criteria) helps 
students 
conceptually 
grasp how to 
extend sorting to 
multiple keys, a 
useful skill 
beyond the 
example given.  
21.9 Grouping and Indexing 
Data  Add  Explain defaultdict  
usage – Include a brief 
note about what 
defaultdict(list)  does. For 
example: “We use 
defaultdict(list)  so that if 
a major isn’t in the 
dictionary yet, it starts 
with an empty list 
automatically, saving us 
from having to initialize 
keys.” Likewise, for the 
nested Helps demystify 
the code. 
defaultdict  is a 
powerful tool but 
might be 
unfamiliar; a 
concise 
explanation of its 
auto-initialization 
behavior will 
make the 
grouping 
examples easier 

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
defaultdict(lambda: 
defaultdict(list)) , clarify 
that it creates a 
dictionary -of-
dictionaries structure on 
the fly.  to follow. This 
reduces cognitive 
load when 
students read the 
code, letting 
them focus on 
the grouping 
concept instead 
of the intricacies 
of the data 
structure.  
21.9 Grouping and Indexing 
Data  Add  Highlight dictionary 
lookup speed  – When 
demonstrating the by_id 
(or by_email ) index, add 
a sentence to emphasize 
why this is useful. E.g., 
“Looking up a student by 
ID with by_id[102]  is 
instantaneous, rather 
than looping through the 
list – a big efficiency gain 
when managing large 
datasets.”  Connects the 
concept to 
performance 
benefits. 
Students may 
intuit a dictionary 
is faster, but 
explicitly stating it 
reinforces good 
practices (using 
dictionaries for 
quick lookups). It 
also subtly 
introduces the 
idea of 
algorithmic 
efficiency in an 
accessible way.  
21.10 Aggregations: Counts, 
Sums, Averages  Edit  Fix minor text/grammar 
issues – In the output or 
explanations, correct 
minor typos such as 
“from 1 students” to Polishes the 
content and 
avoids confusion. 
Small 
grammatical 

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
“from 1 student” 
(singular). Also ensure 
consistent formatting 
(e.g., one decimal place 
vs two) if any values are 
displayed.  errors can 
distract or 
confuse learners 
(“1 students” 
might make them 
question if it’s a 
mistake), so fixing 
them maintains 
professionalism 
and clarity in the 
instructional 
material.  
21.11 Practical Exercise: 
Student GPA Analysis  Edit  Remove unused 
import/variable  – The 
code snippet imports 
Counter but doesn’t end 
up using it in the 
analysis. Eliminate the 
unused from collections 
import Counter  (or if 
intended, show its use). 
Similarly, any variable or 
branch of code not used 
in the final output should 
be cleaned up.  Avoids confusion 
and sets a good 
example. 
Including 
unnecessary 
code can confuse 
students (“Why is 
Counter imported 
if we don’t use 
it?”) and may 
lead them to 
think they missed 
something. A 
clean code 
example 
exemplifies best 
practices in 
coding (no 
unused 
components) and 
focuses attention 
on relevant parts.  

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
21.11 Practical Exercise: 
Student GPA Analysis  Add  Frame the complexity 
for students  – Precede 
the example with a note 
like: “This is a 
comprehensive example 
pulling together many 
concepts. Don’t worry if 
it looks complex – it’s 
meant to show 
possibilities. Take time to 
read through and 
understand each part.”  
You might mark it as an 
advanced or optional 
example.  Manages student 
expectations and 
anxiety. This 
exercise is quite 
extensive; letting 
learners know 
that it’s okay if 
they don’t fully 
grasp it 
immediately will 
encourage them 
to engage with it 
without feeling 
intimidated. It 
signals that the 
example is 
illustrative and 
that they can 
progress even if 
they don’t 
replicate it on 
their own yet.  
21.12 Intro to JSON (Dict vs 
JSON)  Edit  Use formatting for 
JSON vs Python literals  
– In the comparison of 
JSON to Python dict, 
format true/false  vs 
True/False  and null vs 
None in code style or 
quotes. For instance: 
“JSON uses true/false 
(lowercase) whereas 
Python uses True/False. Enhances 
readability and 
comprehension. 
By clearly 
formatting the 
literals, students 
can visually 
distinguish the 
JSON version 
from the Python 
version. This 
minimizes 

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
JSON null is equivalent 
to Python None.” confusion, 
especially since 
the words are so 
similar – the 
formatting draws 
attention to the 
subtle but 
important 
differences in 
capitalization and 
spelling.  
21.13 Working with JSON in 
Python  Add  Clarify dumps vs dump 
– After demonstrating 
json.dumps  (producing a 
string) and json.dump  
(writing to a file), add a 
clarifying note: 
“json.dumps()  returns a 
JSON-formatted string, 
which we printed. 
json.dump()  writes the 
JSON data directly to a 
file.” Also, confirm that 
reading with json.load  
indeed reconstructs the 
same list of dicts 
structure.  Ensures that 
students 
understand the 
context of each 
function. This 
prevents any 
confusion 
between the 
similar names 
and helps 
learners grasp file 
I/O vs in-memory 
string conversion. 
It reinforces that 
the data remains 
the same through 
serialization -
deserialization, 
connecting back 
to the original 
Python structure.  

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
21.14 Working with Nested 
Data  Add  Encourage visualization 
of nesting  – Suggest that 
students inspect the 
nested structure by 
using the provided 
print_nested_structure  
function or even by 
sketching a tree diagram. 
For example: “It can help 
to print the structure or 
draw it out to see how 
lists and dictionaries are 
layered (departments → 
students → courses, 
etc.).”  Aids 
understanding of 
complex nested 
data. Students 
new to nesting 
can easily lose 
track of levels; 
encouraging 
them to actively 
visualize the 
hierarchy will 
improve 
comprehension. 
This addition 
makes the 
learning process 
more interactive 
and bridges the 
gap between 
abstract data and 
a mental model.  
21.15 Flattening and 
Restructuring Data  Add  Define ‘flatten’ and 
‘restructure’  – Before 
diving into the code, 
briefly define these 
terms. E.g., “Flattening 
data means converting a 
nested structure into a 
simple list of records. 
Restructuring (or 
grouping) does the 
reverse, organizing flat 
data back into a nested 
form.” This sets context Introduces 
terminology in a 
digestible way. By 
defining the 
concepts first, 
students can 
better anticipate 
what the code 
will do, making it 
easier to follow 
the logic. It 
ensures that 
readers 

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
for the functions 
flatten_students  and 
students_by_departmen
t that follow.  understand the 
goal of the code 
(not just the 
mechanics), 
which ties the 
section together 
conceptually.  
21.16 Converting Between 
Formats (CSV)  Add  Note on data types 
when using CSV  – 
Mention that when you 
read data back from CSV 
using csv.DictReader , all 
values come in as 
strings. For instance: 
“Notice that when we 
load from CSV, even 
numeric values (like age 
or GPA) are read as 
strings. We would need 
to convert them (e.g., 
using int() or float()) if we 
wanted to perform 
numerical operations.”  Preempts a 
common source 
of confusion. 
Students might 
be puzzled if they 
try to use the 
loaded data for 
calculations and 
it doesn’t work as 
expected (since 
“90” is a string, 
not an int). This 
note connects 
back to data 
typing and 
reinforces a real -
world 
consideration 
when moving 
data between 
formats, without 
going off-topic.  
21.17 Schema Validation  Edit  Correct code symbols 
in validation  – Ensure 
comparison operators in 
validate_student  are 
displayed properly (e.g., Maintains code 
accuracy. Like 
earlier code 
corrections, this 
prevents 

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
use <= instead of &lt;= 
for the age range, and 
similarly >= for GPA). If 
any “<” or “>” signs are 
HTML-escaped in the 
text, fix them in the code 
block.  confusion and 
ensures that the 
validation logic is 
clearly 
presented. 
Students can 
then trust the 
code as written 
and learn the 
intended lesson 
about validation 
without tripping 
over a simple 
formatting glitch.  
21.17 Schema Validation  Add  Explain type choice for 
GPA – In the validation 
function, there’s a tuple 
(int, float)  allowed for 
GPA. Add a brief inline 
comment: # allow int or 
float for gpa (e.g., 4 or 
3.5) to explain why both 
types are accepted.  Anticipates a 
question 
students might 
have (“Why do we 
accept an int for 
GPA?”). This 
small clarification 
ties back to real 
examples (some 
might input GPA 
as 4 instead of 
4.0). It shows 
thoughtful coding 
and helps 
students 
understand how 
to allow flexibility 
in input without 
compromising 
the schema.  

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
21.18 Working with APIs: 
JSON Example  Add  Connect to real API 
context – Explain that 
the given JSON string 
simulates data one 
might get from a web 
API. For example: “(In 
practice, this data might 
come from an API call. 
Here we simulate the 
response as a JSON 
string.)” You could also 
mention that 
process_api_response  
would be used after 
fetching data via an HTTP 
request in a real 
scenario.  Provides real -
world context to 
the exercise. This 
helps students 
understand why 
this example 
matters and how 
it would be used 
outside of this 
lesson. It makes 
the exercise more 
concrete by 
linking it to the 
concept of web 
APIs, thereby 
reinforcing the 
relevance of 
JSON parsing.  
21.19 Recognizing the 
Parallels  See 21.6  No separate changes 
needed beyond the 
merge with 21.6 
discussed above.  Ensure 
that any content retained 
here is consistent with 
(or includes) the key 
points from 21.6, so the 
comparison between 
dictionaries and objects 
is covered thoroughly 
once. Covered in 21.6 
merge 
recommendation
. 
21.20 Refactoring: 
Dictionaries to Objects  Add  Highlight function -to-
method transition  – 
After showing the class -
based version of the Reinforces the 
benefit of the 
refactor in clear 
terms. While the 

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
student system, 
explicitly point out how 
the standalone functions 
(add_course , 
calculate_status , etc.) 
from the dictionary 
approach became 
methods of the Student 
class. E.g., “Notice that 
in the class design, these 
behaviors are 
encapsulated as 
methods – 
student.update_gpa(3.9)  
– which is more intuitive 
than passing the student 
dictionary into a 
separate function.”  code illustrates 
this, an 
explanation 
solidifies the 
learning: that 
object-oriented 
design ties data 
and behavior 
together. This 
draws a clear line 
from the earlier 
approach to the 
new one, helping 
students 
appreciate why 
the refactor is 
beneficial.  
21.21 Understanding 
Encapsulation  Edit (Minor)  No major changes 
needed. This section is 
clear and effectively 
demonstrates 
encapsulation. Optional:  
You might briefly 
mention that Python 
doesn’t strictly prevent 
direct attribute access 
(since we don’t have 
truly private variables), 
but by convention, one 
should use methods like 
update_gpa  to maintain 
data integrity.  The content is 
solid. The 
optional note 
could preempt 
advanced 
questions and 
highlight that the 
provided 
interface 
(methods) should 
be used instead 
of manually 
tweaking 
attributes. This 
reinforces the 
concept of 

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
encapsulation as 
a guideline in 
Python.  
21.22 Classes as Data 
Schemas  Edit (Minor)  No major changes 
needed. The section 
properly shows that 
classes enforce a 
schema by requiring all 
parameters. You could 
uncomment and run the 
Book("C++ 101", "Bob 
Smith") example (or 
describe its error) to 
explicitly show the 
TypeError for missing 
arguments, emphasizing 
that the class enforces 
completeness.  The example 
already implies 
this, but actively 
demonstrating 
the error (or 
describing it in 
text rather than a 
comment) can 
drive home the 
point about 
schema 
enforcement. 
Otherwise, the 
section is 
pedagogically 
sound, clearly 
illustrating how 
classes provi de a 
formal structure.  
21.23 Comparison: Dict vs 
Class Design  Edit  Format comparison 
table properly  – Ensure 
the comparison 
summary between the 
dictionary approach and 
class approach is 
presented as a clear 
table or well -aligned list. 
Use a Markdown table 
with columns for Aspect, 
Dictionary Approach, 
and Class Approach (for Improves 
readability of the 
side-by-side 
comparison. A 
table format will 
allow students to 
quickly scan 
differences and 
reinforces the 
contrasts in a 
structured way. It 
transforms a 

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
example, listing Syntax, 
Structure, Validation, 
etc. as rows). If it’s 
already intended as a 
table, adjust spacing or 
syntax so it renders 
correctly.  potentially hard -
to-read text block 
into a neat 
summary, making 
the takeaway 
points more 
accessible.  
21.24 Practical Exercise: 
Refactor CRUD (Library)  Add  Mention data integrity 
consideration  – In the 
Library.add_book  
method, optionally 
suggest a check for 
duplicate ISBNs before 
adding a new book. For 
instance, “(You might 
enhance this by 
checking if a book with 
the same ISBN already 
exists to avoid 
duplicates.)”  This could 
be a footnote or 
comment rather than 
changing the code, to 
avoid complicating the 
main example.  Introduces a real -
world 
consideration 
and an 
opportunity for 
critical thinking. It 
gently challenges 
students to think 
beyond the given 
code and 
consider how 
they might handle 
such a case. This 
addition keeps 
the flow (doesn’t 
require teaching 
new methods)  
but adds depth 
for keen learners 
who might be 
testing the 
system’s limits.  
Chapter Summary  Edit  Emphasize key terms  – 
Within the summary 
bullets, highlight 
important concepts and 
terminology in bold. For Enhances the 
utility of the 
summary as a 
study tool. By 
bolding 

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
example: CRUD, 
filtering, json.dumps() , 
objects. Also, ensure 
the language is concise 
(it’s okay if the summary 
is somewhat lengthy, as 
it recaps the chapter 
thoroughly). Consider 
breaking a long bullet 
into sub-bullets for 
readability if needed.  keywords, 
students 
reviewing the 
summary will 
quickly spot the 
main topics and 
concepts. The 
summary is quite 
detailed (which is 
good for 
completeness); 
formatting key 
points in bold and 
using sub -bullets 
for multi-part 
ideas will make it 
less daunting to 
skim and 
reinforce the 
chapter’s 
learning 
objectives.  
Practice Exercises (End of 
Chapter)  Add (Notation)  Label 
difficulty/optional 
exercises  – It’s good that 
exercises are divided by 
level. To further guide 
students, explicitly label 
the Intermediate and 
Challenge exercises as 
such, and reassure that 
Challenge exercises (7 –
9) are extension tasks. 
E.g., add a note: Sets appropriate 
expectations. 
This helps less 
confident 
students focus on 
the essential 
exercises first, 
while inviting 
advanced 
students to 
attempt more 
difficult 

Section Title/Number  Suggested 
Change  Details of 
Recommendation  Reason for 
Change  
“Challenge exercises are 
for deeper exploration 
and may go beyond the 
chapter; they are 
optional but 
recommended for those 
who want to push 
themselves.”  problems. It 
ensures no one 
feels the 
challenge 
exercises are 
mandatory or 
feels discouraged 
by them, keeping 
the course 
accessible to a 
range of skill 
levels.  
Note: Sections not listed above (or marked as "No major changes needed") were found to 
be well-written, accurate, and aligned with the learning goals. They should be kept as -is 
aside from minor proofreading, if necessary. Implementing the recommended changes wil l 
correct the small errors and enhance clarity, resulting in a more polished Week 8 module 
that is both beginner -friendly and pedagogically effective.  
 
 
 
 
 
 

