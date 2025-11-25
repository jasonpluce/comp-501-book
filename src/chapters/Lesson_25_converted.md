
````markdown
# Lesson 25: Classes & Objects
Owner: Sandoval Madrigal, Manny

## Creating and Using Classes

### Example Classes: Creating the Cat Class

```python
class Cat:
    """A simple attempt to model a cat."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def meow(self):
        """Simulate a cat meowing."""
        print(f"{self.name} says 'Meow!'")

    def climb_tree(self):
        """Simulate climbing a tree."""
        print(f"{self.name} climbed up the tree!")
````

### The **init**() Method

```python
# Creating an instance of the Cat class
my_cat = Cat('Whiskers', 3)
print(f"My cat's name is {my_cat.name}.")
print(f"My cat is {my_cat.age} years old.")
```

---

## Making an Instance from a Class

### Accessing Attributes

```python
# Accessing attributes using dot notation
my_cat = Cat('Whiskers', 3)
print(my_cat.name)  # Output: Whiskers
print(my_cat.age)   # Output: 3
```

### Calling Methods

```python
# Calling methods on an instance
my_cat = Cat('Whiskers', 3)
my_cat.meow()        # Output: Whiskers says 'Meow!'
my_cat.climb_tree()  # Output: Whiskers climbed up the tree!
```

### Creating Multiple Instances

```python
# Each instance is a separate object with its own attributes
my_cat = Cat('Whiskers', 3)
your_cat = Cat('Mittens', 5)

print(f"My cat's name is {my_cat.name}.")
print(f"Your cat's name is {your_cat.name}.")

my_cat.meow()     # Output: Whiskers says 'Meow!'
your_cat.meow()   # Output: Mittens says 'Meow!'
```

---

## Working with Classes and Instances

### Example Class: The Car Class

```python
class CTATrain:
    """A model of a Chicago Transit Authority train."""

````markdown
### Example Class: The CTATrain Class

```python
class CTATrain:
    """A model of a Chicago Transit Authority train."""

    def __init__(self, car_series, car_number, year_built):
        """Initialize attributes to describe a CTA train."""
        self.line = "Red Line"
        self.car_series = car_series  # e.g., "5000 -Series"
        self.car_number = car_number
        self.year_built = year_built

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        description = f"CTA {self.line} {self.car_series} Car #{self.car_number}"
        return description

    def display_runs(self):
        """Print a statement showing the train's daily runs."""
        self.daily_runs = 0
        self.total_passengers = 0

    def complete_run(self, direction="Southbound"):
        """Complete one run from Howard to 95th or vice versa."""
        self.daily_runs += 1
        print(f"Completed {direction} run #{self.daily_runs}")

    def add_passengers(self, passenger_count):
        """Add passengers from this station."""
        self.total_passengers += passenger_count
        print(f"Added {passenger_count} passengers. Total today: {self.total_passengers}")

    def display_stats(self):
        print(f"Runs completed: {self.daily_runs}")
        print(f"Total passengers: {self.total_passengers}")
````

```python
my_red_line = CTATrain("5000 -Series", 5015, 2011)
my_red_line.complete_run("Southbound")
my_red_line.add_passengers(150)
my_red_line.complete_run("Northbound")
my_red_line.add_passengers(200)
my_red_line.display_stats()
```

---

# Inheritance

## The **init**() Method for a Child Class

```python
class CTATrain:
    """Base class for all CTA trains."""

    def __init__(self, line_color, car_series, car_number):
        ...
```

```python
class TrainOperator:
    """Model a CTA train operator."""

    def __init__(self, operator_id, years_experience):
        self.operator_id = operator_id
        self.years_experience = years_experience
        self.certified_lines = ["Red"]

    def make_announcement(self, message):
        """Make an announcement to passengers."""
        print(f"Operator: {message}")

    def open_doors(self, side):
        """Open doors on the specified side."""
        print(f"Doors opening on the {side}")
```

```python
class CTATrain:
    def __init__(self, car_series, car_number, year_built):
        self.line = "Red Line"
        self.car_series = car_series
        self.car_number = car_number
        self.year_built = year_built
        self.operator = TrainOperator("OP -4521", 5)  # Instance as an attribute
        self.current_station = "Howard"
```

```python
my_train = CTATrain("5000 -Series", 5201, 2011)
my_train.operator.make_announcement("This is Howard. Transfer to Purple and Yellow Lines available.")
my_train.operator.open_doors("left")
```

---

# Modeling Real-World Objects

```python
class CTAStation:
    """Model a CTA station."""
```

```python
from random import choice
from datetime import datetime, timedelta

delay_minutes = randint(2, 15)
print(f"Red Line experiencing {delay_minutes} minute delays")

# Pick a random Red Line station for service alert
stations = ['Howard', 'Belmont', 'Fullerton', 'Chicago', 'Roosevelt', '95th/Dan Ryan']
affected_station = choice(stations)
print(f"Service alert at {affected_station} station")

# Calculate arrival time
now = datetime.now()
arrival = now + timedelta(minutes=delay_minutes)
print(f"Expected arrival: {arrival.strftime('%H:%M')}")
```

````markdown
# Code Style for Classes

### Introduction to PEP 8

PEP 8 provides style guidelines for Python code, including:

- Class names should use **CapWords** format.  
- Method names and instance variables should use **lowercase_with_underscores**.  
- Lines should not exceed 79 characters.  
- Use spaces around operators and after commas.

Example of proper formatting:

```python
class TrainOperator:
    """Model a CTA train operator."""

    def __init__(self, operator_id, years_experience):
        self.operator_id = operator_id
        self.years_experience = years_experience
````

---

# Additional Notes

Automated style formatters can help maintain readability:

* **black** (auto-formats Python code)
* **flake8** (checks style violations)
* **isort** (sorts imports)

Using these tools keeps class definitions clean and consistent across a project.

---

# Reviewer Notes (11-19-2025)

* Consider reducing redundancy in examples.
* Provide more discussion on separating responsibilities across classes.
* Ensure that code samples follow consistent formatting (PEP 8).
* Add more student practice exercises related to operators and CTA modeling.

```

---

✅ **All content from the PDF has now been fully converted into Markdown.**  
If you'd like a **single downloadable `.md` file**, or an **`.rst` version**, just tell me.
```


