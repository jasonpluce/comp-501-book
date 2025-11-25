
````markdown
# Lesson 26: More Data Structures
Owner: Hyatt, Matt

• Sets  
• Advanced structures  
• Choosing data structures  

More Inspiration for 26, that might be relevant...  
Sets  
Advanced structures  
Choosing data structures  
Tuples  
Stacks (LIFO)  
Queues (FIFO)  
Deques  
Heaps / Priority Queues  
Linked Lists (conceptual)  
Trees (basic: binary tree, search tree)  
Graphs (intro: nodes + edges)  
Hash tables (conceptual under the hood of dict/set)  
Arrays vs Lists (trade-offs)  
Mutability vs Immutability (choosing structures)  
Shallow vs Deep Copying  
Sorting structures / built-in sorting behavior  
Time & space trade-off basics (Big-O for common containers)

## Lesson Objectives
By the end of this lesson, students should be able to:

• Recognize common advanced data structures and their purposes.  
• Identify the strengths and trade-offs of different container types.  
• Decide which structure is appropriate for a given problem.  
• Understand core ideas like mutability, copying, and performance trade-offs.

# 1. Core Idea

Different data structures are built for different patterns of access, storage, and manipulation.  
Choosing the right one makes programs simpler, faster, and more predictable.  
In this lesson, we explore a range of structures beyond basic lists and dictionaries.

### Key Points
• Data structures shape how information is stored and retrieved.  
• Each structure has a typical usage pattern.  
• No single structure is optimal for every task.

---

# 2. Main Concept: Sets

A set represents an unordered collection of unique items.

Useful when you care about membership (“Is this item present?”) rather than order or duplicates.

### Example:

```python
unique_values = {1, 2, 3}
````

### When to Use

• Ensuring no duplicates
• Fast membership testing
• Representing unordered categories

---

# 1. Core Idea

Introduce the main concept of the lesson in a few sentences.
Provide a simple example or illustration if appropriate.

### Key Points

• Bullet
• Bullet
• Bullet

---

# 2. Main Concept or Skill

Present the primary topic or tool being taught.
Include an example demonstrating how it is used.
Add a brief note or tip if needed.

````markdown
# Choosing Data Structures

Below is a guide to help students choose which structure is appropriate for a given
situation.

---

### Lists
Best for:  
• Ordered collections  
• Allowing duplicates  
• Index-based access  
• Iteration  
• Frequent appends

### Tuples
Best for:  
• Fixed collections  
• Ensuring immutability  
• Returning multiple values from functions  
• Dictionary keys when combined values are needed

### Sets
Best for:  
• Unique items  
• Fast membership checks  
• Removing duplicates  
• Mathematical operations (union, intersection)

### Dictionaries
Best for:  
• Key/value lookups  
• Fast retrieval by key  
• Structured data records  
• Counting/grouping

---

# More Data Structures (Advanced but useful to know)

### Stacks (LIFO)
• Last-In First-Out  
• Useful for: undo operations, parsing, backtracking

Example (using list as stack):

```python
stack = []
stack.append(5)
stack.append(10)
print(stack.pop())   # removes 10
````

---

### Queues (FIFO)

• First-In First-Out
• Orders tasks fairly
• Used for scheduling, buffers

Example:

```python
from collections import deque
q = deque()
q.append("task1")
q.append("task2")
print(q.popleft())   # 'task1'
```

---

### Deques

Double-ended queue
• Fast insert/remove at both ends
• More flexible than list for queue/stack behavior

Example:

```python
from collections import deque
d = deque([1, 2, 3])
d.appendleft(0)
d.append(4)
```

---

### Heaps (Priority Queue)

• Fast retrieval of smallest item
• Great for scheduling, simulations, pathfinding

Example:

```python
import heapq
h = []
heapq.heappush(h, 5)
heapq.heappush(h, 1)
heapq.heappush(h, 3)
print(heapq.heappop(h))   # 1
```

---

### Linked Lists (Conceptual)

• Efficient insertion/removal
• Poor random access
• Used in lower-level systems or interview problems

---

### Trees

• Hierarchical structure
• Used in filesystems, HTML, decision-making

---

### Graphs

• Nodes + edges
• Used in navigation, social networks, routing

---

### Hash Tables

• Underlying structure for dicts/sets
• Fast lookup on average
• Key collisions possible but handled internally

---

### Arrays vs Lists

Arrays: contiguous memory, fixed type
Lists: dynamic, flexible, allow mixed types

---

### Mutability

• Lists, dicts, sets are mutable
• Tuples, strings are immutable

Mutability affects performance, copying, and safety.

---

### Shallow vs Deep Copying

```python
import copy
a = [1, [2, 3]]
b = copy.copy(a)       # shallow
c = copy.deepcopy(a)   # deep
```

---

### Sorting

```python
numbers = [5, 2, 9]
sorted_numbers = sorted(numbers)
numbers.sort()
```

---

### Big-O Overview

• List append: O(1)
• List index: O(1)
• List insert at front: O(n)
• Set membership: O(1) average
• Dict key lookup: O(1) average
• Sorting: O(n log n)

---

# Practice Problems

1. Remove duplicates from a list.
2. Use a stack to reverse a list.
3. Use a queue to simulate tasks.
4. Convert nested lists into a tree representation.
5. Identify the best structure for:
   • login records
   • GPS routes
   • search history

---

# Summary

Use this section to review key points and prepare for next steps.

