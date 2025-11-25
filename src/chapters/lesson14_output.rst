Lesson 14: More Practice with For Loops
=======================================

Owner: Hyatt, Matt

- Nested loops
- Loop patterns
- Loop debugging

Lesson 14: More Practice with For Loops
---------------------------------------

In this lesson, you will learn how Python decides how to execute repeated code
in sequence, using loop logic and terminating conditions. We will:

- Repeat work with ``for`` loops and ``range()``.
- Control loops using ``break``, ``continue``, and ``else``.
- Use ``pass`` as a placeholder.
- Work with nested loops (loops inside loops).
- Recognize common loop patterns (accumulators, counters, searching,
  building lists).
- Develop simple strategies for loop debugging.

By the end of this lesson, you should be able to read, write, and debug basic
loop-based code, and organize it into small, reusable parts.

1. The ``if`` Statement
-----------------------

We use ``if``, ``elif``, and ``else`` to make decisions in programs.

.. code-block:: python

    x = int(input("Enter a number: "))
    if x < 0:
        print("Negative changed to zero")
        x = 0
    elif x == 0:
        print("Zero")
    elif x == 1:
        print("Single")
    else:
        print("More")

Key points

- ``elif`` means *“else if”*.
- The ``else`` part is optional.
- You can have as many ``elif`` parts as you want.

2. The ``for`` Loop
-------------------

A ``for`` loop repeats code for each item in a sequence (like a list or string).

.. code-block:: python

    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))

**Tip:** Don’t change the list while looping through it — loop over a *copy* if
needed:

.. code-block:: python

    for user, status in users.copy().items():
        if status == 'inactive':
            del users[user]

3. The ``range()`` Function
---------------------------

``range()`` produces a lazy, constant-memory integer sequence that the loop
consumes on demand. It supports configurable ``start``, ``stop``, and ``step``
parameters.

.. code-block:: python

    for i in range(5):
        print(i)
        # 0, 1, 2, 3, 4

You can also set:

- a start value → ``range(5, 10)``
- a step → ``range(0, 10, 2)``
- a negative step → ``range(10, 0, -1)``

4. ``break`` and ``continue``
-----------------------------

- ``break`` stops a loop early.
- ``continue`` skips the rest of the current loop.

.. code-block:: python

    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                break

.. code-block:: python

    for num in range(2, 10):
        if num % 2 == 0:
            continue
        print(num)

5. ``else`` with Loops
----------------------

The ``else`` block runs only if the loop finishes without hitting a ``break``.

.. code-block:: python

    for n in range(2, 10):
        for x in range(2, n):
            if n % 2 == 0:
                break
        else:
            print(n, "is a prime number")

6. ``pass``
-----------

A placeholder that does nothing.

.. code-block:: python

    if condition_met:
        pass

Useful for:

- Empty function or class definitions
- Stubbing out branches during development

7. Nested Loops
---------------

A nested loop is a loop inside another loop.

.. code-block:: python

    for i in range(3):
        for j in range(2):
            print(i, j)

Output::

    0 0
    0 1
    1 0
    1 1
    2 0
    2 1

Key points:

- The inner loop runs fully each time the outer loop runs.
- Total iterations = outer × inner.

8. Loop Patterns
----------------

a. Accumulator Pattern  
b. Counter Pattern  
c. Searching Pattern  
d. Building Lists

8.5 BONUS Comprehension Patterns
--------------------------------

a. List Comprehensions

.. code-block:: python

    squares = [n**2 for n in range(5)]

b. Dictionary Comprehensions

.. code-block:: python

    square_map = {n: n**2 for n in range(5)}

c. Set Comprehensions

.. code-block:: python

    unique_lengths = {len(w) for w in words}

9. Loop Debugging
-----------------

Common issues:

1. Off-by-one errors – wrong range boundaries.
