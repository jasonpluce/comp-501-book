Lesson 14: More Practice with For Loops
======================================

Owner: Hyatt, Matt

- Nested loops
- Loop patterns
- Loop debugging

Lesson 14: More Practice with For Loops
---------------------------------------

In this lesson, you will learn how Python decides how to execute repeated code
in sequence, using loop logic and terminating conditions. We will:

- Repeat work with for loops and ``range()``
- Control loops using ``break``, ``continue``, and ``else``
- Use ``pass`` as a placeholder
- Work with nested loops (loops inside loops)
- Recognize common loop patterns (accumulators, counters, searching, building lists)
- Develop simple strategies for loop debugging

By the end of this lesson, you should be able to read, write, and debug basic loop-based code, and organize it into small, reusable parts.

1. The ``if`` Statement
----------------------

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

Key points:

- ``elif`` means *else if*
- The ``else`` part is optional
- You can have as many ``elif`` parts as you want

2. The ``for`` Loop
-------------------

A ``for`` loop repeats code for each item in a sequence (like a list or string).

.. code-block:: python

    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))

**Tip:** Don’t change the list while looping through it — loop over a *copy* if needed:

.. code-block:: python

    for user, status in users.copy().items():
        if status == 'inactive':
            del users[user]

3. The ``range()`` Function
---------------------------

``range()`` produces a lazy, constant-memory integer sequence that the loop
consumes on demand. It supports configurable ``start``, ``stop``, and ``step`` parameters.

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

- ``break`` stops a loop early
- ``continue`` skips to the next iteration

.. code-block:: python

    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                break  # stop checking this n

.. code-block:: python

    for num in range(2, 10):
        if num % 2 == 0:
            continue  # skip even numbers
        print(num)

5. ``else`` with Loops
----------------------

The ``else`` block is executed only if the loop terminates without a ``break``.

This is useful for algorithms where exhausting the loop signals success, such as primality testing, search routines, or validation passes.

6. ``pass``
-----------

A do-nothing placeholder when Python requires a statement but none is needed.

.. code-block:: python

    if condition_met:
        pass  # do nothing

Useful for:

- Empty class or function definitions
- Stubbing out branches, handlers, or TODO sections during development

7. Nested Loops
---------------

A nested loop is a loop inside another loop.

.. code-block:: python

    for i in range(3):  # outer loop
        for j in range(2):  # inner loop
            print(i, j)

Key points:

- The inner loop runs completely each time the outer loop runs once.
- Total iterations = outer × inner.
- Good for working with 2D lists, tables, or coordinate pairs.

8. Loop Patterns
----------------

Common looping patterns:

a. Accumulator Pattern  
   Collect values as you go.

b. Counter Pattern  
   Track how many items match a condition.

c. Searching Pattern  
   Look for an element that meets a condition.

d. Building Lists  
   Use loop results to create a new list.

**Tip:** These can often be done more compactly with comprehensions.

8.5 BONUS: Comprehension Patterns
---------------------------------

Python comprehensions allow loop-driven construction of iterables in one expression.

a. List Comprehensions

.. code-block:: python

    squares = [n**2 for n in range(5)]

Mapping:

.. code-block:: python

    lengths = [len(w) for w in words]

Filtering:

.. code-block:: python

    evens = [n for n in nums if n % 2 == 0]

Flattening nested loops:

.. code-block:: python

    pairs = [(i, j) for i in A for j in B]

b. Dictionary Comprehensions

.. code-block:: python

    square_map = {n: n**2 for n in range(5)}

Inversion:

.. code-block:: python

    inv = {v: k for k, v in d.items()}

Filtering entries:

.. code-block:: python

    filtered = {k: v for k, v in d.items() if v > 0}

Transforming values:

.. code-block:: python

    scaled = {k: v * 0.1 for k, v in metrics.items()}

c. Set Comprehensions

.. code-block:: python

    unique_lengths = {len(w) for w in words}

Common patterns:

- Extract distinct attributes:

  .. code-block:: python

      first_letters = {w[0] for w in words}

- Filtered membership:

  .. code-block:: python

      positives = {n for n in nums if n > 0}

- Projection from structured data:

  .. code-block:: python

      ids = {record.id for record in records}

9. Loop Debugging
-----------------

Debugging loops involves figuring out why they iterate incorrectly or produce wrong results.

Common issues:

1. Off-by-one errors – wrong ``range`` boundaries.
