
````markdown
# Lesson 23: Dictionary Algorithms
Owner: Saban, Michael  
Reviewer: Jason for Saban, Michael

Per the Guidelines for Content the following items are missing:  
Overview & Introduction  
Assessment  
Summary  
Next steps  
Everything else looks fine.

## Learning Objectives

- Explain why dictionaries are useful for organizing structured data.  
- Apply common dictionary algorithms including:  
  - counting frequencies  
  - filtering keys and values  
  - grouping items  
  - reversing mappings  
  - merging dictionaries safely  
- Evaluate time complexity of dictionary operations at a basic level.  
- Write programs that process lists of dictionaries (records) using these patterns.

## Introduction

Dictionaries are one of Python’s most powerful data structures because they let us map 
keys to values with extremely fast lookup times. As programs grow in size and complexity, 
dictionaries appear everywhere—representing users, settings, records, statistics, API 
responses, databases, and more.

In this lesson, we explore common dictionary algorithms that appear repeatedly in real 
software.

---

# 1. Counting With Dictionaries

Counting items is one of the most common uses of dictionaries.

## Example: Counting words

```python
words = ["apple", "banana", "apple", "pear", "banana", "apple"]
counts = {}

for w in words:
    if w not in counts:
        counts[w] = 1
    else:
        counts[w] += 1

print(counts)
````

Output:

```
{'apple': 3, 'banana': 2, 'pear': 1}
```

## Pattern

```
for item in data:
    if item not in result:
        result[item] = 1
    else:
        result[item] += 1
```

---

# 2. Filtering Dictionaries

Often we want to create a new dictionary that contains only certain key/value pairs.

## Example: Filter scores above 80

```python
scores = {"A": 95, "B": 82, "C": 71, "D": 99}
filtered = {}

for k, v in scores.items():
    if v > 80:
        filtered[k] = v

print(filtered)
```

Output:

```
{'A': 95, 'B': 82, 'D': 99}
```
Source: **Lesson 23 Dictionary_Algorithms.pdf**


````markdown
# 3. Grouping With Dictionaries

Grouping means placing items that share a characteristic into lists under a key.

## Example: Group words by first letter

```python
words = ["apple", "ant", "banana", "berry", "car", "cat"]

groups = {}

for w in words:
    first = w[0]
    if first not in groups:
        groups[first] = []
    groups[first].append(w)

print(groups)
````

Possible output:

```
{'a': ['apple', 'ant'], 'b': ['banana', 'berry'], 'c': ['car', 'cat']}
```

## Pattern

```
for item in data:
    key = some_property(item)
    if key not in groups:
        groups[key] = []
    groups[key].append(item)
```

---

# 4. Reversing a Dictionary

Sometimes we want to flip keys ↔ values.
This works only if values are unique and hashable.

## Example

```python
grades = {"A": 90, "B": 80, "C": 70}
rev = {}

for k, v in grades.items():
    rev[v] = k

print(rev)
```

Output:

```
{90: 'A', 80: 'B', 70: 'C'}
```

If values are not unique, one value may overwrite another.

---

# 5. Merging Dictionaries

Python 3.9+ supports the merge operator `|`.

```python
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

c = a | b
print(c)
```

Output:

```
{'x': 1, 'y': 3, 'z': 4}
```

Key rule: if both dictionaries share a key, the right-hand dictionary wins.

Older syntax:

```python
c = dict(a)
c.update(b)
```

---

# 6. Safe Access

Using `.get()` prevents key errors.

```python
config = {"debug": True}
print(config.get("mode", "production"))
```

Output:

```
production
```

`.get()` syntax:

```
dictionary.get(key, default_if_missing)
```

---

# 7. Nested Dictionaries

Dictionaries can hold other dictionaries.

```python
student = {
    "name": "Alice",
    "scores": {"math": 90, "science": 85}
}

print(student["scores"]["math"])
```

---

# 8. Working With Lists of Dictionaries

A list of dictionaries is a common data format (CSV rows, JSON records, etc.).

```python
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Cara", "age": 30}
]
```

## Example: Filter

```python
results = []
for p in people:
    if p["age"] == 30:
        results.append(p)

print(results)
```

## Example: Group by field

```python
groups = {}

for p in people:
    age = p["age"]
    if age not in groups:
        groups[age] = []
    groups[age].append(p)
```

---

# 9. Algorithm: Frequency Dictionary

Count how many records share a value for a certain field.

```python
freq = {}

for p in people:
    age = p["age"]
    if age not in freq:
        freq[age] = 1
    else:
        freq[age] += 1

print(freq)
```

---

# 10. Algorithm: Index by Unique Field

Convert list → dictionary keyed by unique field.

```python
index = {}

for p in people:
    index[p["name"]] = p

print(index["Alice"])
```

Useful for fast lookups.

Below is the **next Markdown chunk**, continuing exactly where Chunk 2 ended.
All content is taken verbatim from pages 9–19 of the PDF ().

---

# ✅ **Markdown Conversion — Chunk 3 of N**

````markdown
# 11. Algorithm: Group by Length (Practice)

5. Return the dictionary.  
Try to implement this on your own. Test your function with a few lists of words.

## Solution (click to expand):

```python
def group_by_length(words):
    groups = {}
    for w in words:
        length = len(w)
        # Ensure there's a list for this length
        groups.setdefault(length, []).append(w)
    return groups

# Testing the function
print(group_by_length(["tea", "to", "apple", "jam", "bag"]))
````

---

# 12. Real-World Applications

Dictionaries are used for:

* indexing large datasets
* frequency counting
* grouping and categorizing
* merging structured records
* looking up attributes
* summarizing statistics

Many systems such as analytics pipelines, database records, summarizing survey results by
category, and many more tasks use these dictionary patterns. Recognizing when a problem
can be solved with a dictionary is a valuable skill in Python programming.

Now that we’ve covered the concepts and walked through examples, it’s time to test your
understanding with a Knowledge Check.

---

# Knowledge Check (with Answer Key)

Test your understanding of dictionary algorithms with the following questions. Try to answer
them on your own before checking the answers provided.

## 1. Multiple Choice

You have a list of items and you want to count how many times each item appears. Which
data structure is the most directly suitable for storing the counts?

A. List
B. Dictionary
C. String
D. Set

**Answer:** B

---

## 2. Short Answer

How does using the dictionary method `get(key, 0)` inside a loop help when counting
occurrences of items? Describe what this method call does in the context of the counting
pattern.

**Answer:**
`get(key, 0)` returns the current count for the key if it exists; otherwise, it returns 0.
This avoids key-errors and makes counting concise.

---

## 3. Multiple Choice

When grouping items by a category using a dictionary, what is the typical type of the
dictionary’s values?

A. An integer count
B. A list of items
C. Another dictionary
D. A string describing the group

**Answer:** B

---

## 4. Multiple Choice

Consider the following code snippet:

```python
word = "banana"
freq = {}
for ch in word:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1
```

What is the value of `freq["a"]` after the loop completes?

A. 1
B. 2
C. 3
D. 4

**Answer:** C

---

## 5. Short Answer

Suppose you want to reverse a dictionary where values are not unique. What problem might
occur when reversing, and why?

**Answer:**
Reversing will overwrite keys because multiple original keys may share the same value.

---

# Course Closing Notes

Congratulations on completing Week 9! You learned how dictionaries can be used for
counting occurrences, grouping data, and aggregating values. These patterns are extremely
useful in many programming tasks. Make sure you practice these concepts and review the
exercises. In the next week, we will continue to build on these skills as we explore more
advanced topics in Python programming. Happy coding!


```

```

