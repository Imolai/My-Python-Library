# Python Quickly

## Contents

- [Python Quickly](#python-quickly)
  - [Contents](#contents)
  - [Introduction](#introduction)
  - [Why Python](#why-python)
    - [Use Cases of Python](#use-cases-of-python)
  - [Calling the Python](#calling-the-python)
  - [Introduction to Python](#introduction-to-python)
  - [Control Flow](#control-flow)
  - [Data Structures](#data-structures)
  - [Modules](#modules)
  - [Input and Output](#input-and-output)
  - [Errors and Exceptions](#errors-and-exceptions)
  - [Classes](#classes)
    - [Example: Creating a Class Based on builtin type `dict`](#example-creating-a-class-based-on-builtin-type-dict)
  - [Tour of the Standard Library](#tour-of-the-standard-library)
  - [Virtual Environments and Packages](#virtual-environments-and-packages)
  - [Built-in Functions](#built-in-functions)
  - [Built-in Constants](#built-in-constants)
  - [Built-in Types](#built-in-types)
    - [Boolean Type](#boolean-type)
    - [Numeric Types](#numeric-types)
    - [Sequence Types](#sequence-types)
    - [Iterator, Generator Types](#iterator-generator-types)
    - [Text Sequence Type](#text-sequence-type)
    - [Binary Sequence Types](#binary-sequence-types)
    - [Set Types](#set-types)
    - [Mapping Types](#mapping-types)
    - [Context Manager Types](#context-manager-types)
    - [Type Annotation Types](#type-annotation-types)
    - [Special Attributes, Regular Dunder Methods](#special-attributes-regular-dunder-methods)
    - [Built-in Exceptions](#built-in-exceptions)
  - [Text Processing Services](#text-processing-services)
    - [`string` Module](#string-module)
    - [`re` Module](#re-module)
  - [Data Types](#data-types)
    - [Detailed Modules](#detailed-modules)
    - [More Information](#more-information)
  - [Functional Programming Modules](#functional-programming-modules)
  - [File and Directory Access](#file-and-directory-access)
    - [Key Modules](#key-modules)
  - [File Formats](#file-formats)
  - [Generic Operating System Services](#generic-operating-system-services)
    - [Key Modules](#key-modules-1)
  - [Concurrent Execution](#concurrent-execution)
    - [Key Modules](#key-modules-2)
  - [Miscellaneous Modules](#miscellaneous-modules)
    - [`asyncio`](#asyncio)
    - [`json`](#json)
    - [`typing`](#typing)
    - [`unittest`](#unittest)
    - [`unittest.mock`](#unittestmock)
    - [`sys`](#sys)
    - [`dataclasses`](#dataclasses)
    - [`abc`](#abc)
    - [`ast`](#ast)
  - [End](#end)

## Introduction

Python is a powerful and easy-to-learn programming language with efficient high-level data structures and a simple approach to object-oriented programming. Its elegant syntax, dynamic typing, and interpreted nature make it ideal for scripting and rapid application development. Python and its extensive standard library are freely available for all major platforms from [python.org](https://www.python.org/). The interpreter can be extended with C/C++ for custom applications. This tutorial introduces basic Python concepts, suitable for offline reading, and prepares readers to explore the Python Standard Library and further resources.

## Why Python

- **Automation**: Perfect for tasks like search-and-replace in text files, renaming files, or creating small databases.
- **Quick Development**: Faster than C/C++/Java due to no need for compilation. Great for quick prototypes.
- **High-Level Language**: Built-in high-level data types (arrays, dictionaries) and more error checking than C.
- **Modular**: Split programs into reusable modules; extensive standard libraries included.
- **Interpreted**: Use interactively, experiment, and save development time.
- **Readable**: Compact, readable code due to high-level operations, indentation-based grouping, and no variable declarations.

### Use Cases of Python

- **Web Development**: Frameworks such as `Django` and `Flask`.
- **Data Science**: Libraries like `NumPy` and `SciPy`.
- **Data Science and Analytics**: Data analysis, visualization, and machine learning with libraries like `Pandas`, `Matplotlib`, and `Scikit-learn`.
- **Artificial Intelligence and Machine Learning**: Libraries like `TensorFlow` and `PyTorch`.
- **Software Development, DevOps**: Prototyping, building applications.
- **Automation and Scripting**: Automate repetitive tasks, build scripts.
- **Education**: Widely used for teaching programming.

## Calling the Python

**Starting the Interpreter**

- **Unix/Mac**: `python3.12` or `python`
- **Windows**: `python3.12` or `py`

**Exiting the Interpreter**
- **Unix**: `Ctrl-D`
- **Windows**: `Ctrl-Z` + `Enter`
- Or type `quit()`

**Interactive Mode**
- **Prompt**: `>>>` for new lines, `...` for continuation lines
- Example:
  ```python
  >>> if True:
  ...     print("Hello, Python!")
  ...
  Hello, Python!
  ```

**Running Scripts**
- **Command Line**: `python script.py`
- **With `-i` flag**: Enters interactive mode after running script

**Command Execution**
- Execute a command: `python -c "import sys; print(sys.version)"`
- Run a module: `python -m http.server`

**Argument Passing**
- Access command-line arguments via `sys.argv`

**Source Code Encoding**
- Default: **UTF-8**
- Specify encoding: Add `# -*- coding: utf-8 -*-` at the top of the file.

## Introduction to Python

**The simplest familiar things**

- **Numbers (classes `int`, `float`, `complex`)**:
  - Arithmetic: `+`, `-`, `*`, `/`
  - Division returns float: `8 / 5` → `1.6`
  - Floor division: `17 // 3` → `5`
  - Remainder: `17 % 3` → `2`
  - Powers: `5 ** 2` → `25`

- **Variable `_`**:
  - Interactive Interpreter Result: `_ * 2` → `50` *(last result was 25)*
  - Throwaway Variable: `for _ in range(5): ...`
  - Ignoring Values in Unpacking: `x, _, y = (1, 2, 3)`
  - Internationalization (i18n): `from gettext import gettext as _`
  - Match Statement Wildcard: `case _: ...`

- **Text (class `str`)**:
  - Strings: `'...'` or `"..."`, can concatenate with `+`, and repeated with `*`
    - At string literals: `'Py' 'thon'` → `'Python'`
    - To break long strings:
      ```python
      text = ('Put several strings within parentheses '
      'to have them joined together.')
      ```
  - Escape characters: `\'` or `\"`
  - Multi-line: `"""..."""` or `'''...'''`
  - Indexing: `word[0]` → `'P'` *(last index -1)*
  - Slicing: `word[0:2]` → `'Py'` *(0: included, 2:excluded)*
  - Length of String: `len('supercalifragilisticexpialidocious')` → `34`

- **Lists (class `list`)**:
  - List creation: `[1, 2, 3]`
  - Indexing: `squares[0]` → `1`
  - Slicing: `squares[-3:]` → `[9, 16, 25]`
  - Lists are mutable: `cubes[3] = 64`
  - Shallow Copy: `correct_rgba = rgba[:]`
  - Length of List: `len(['a', 'b', 'c', 'd'])` → `4`

**Basic Programming**

- **Fibonacci Example**:
  ```python
  a, b = 0, 1
  while a < 10:
      print(a)
      a, b = b, a + b
  ```
- **Features**:
  - Multiple assignment, `while` loop, indentation, `print()` function.

## Control Flow

**if Statements**
- Basic structure:
  ```python
  x = int(input("Please enter an integer: "))
  if x < 0:
      x = 0
      print('Negative changed to zero')
  elif x == 0:
      print('Zero')
  elif x == 1:
      print('Single')
  else:
      print('More')
  ```

**for Statements**
- Iterates over sequences:
  ```python
  words = ['cat', 'window', 'defenestrate']
  for w in words:
      print(w, len(w))
  ```

**range() Function**
- Generates arithmetic progressions:
  ```python
  for i in range(5):
      print(i)
  ```

**break and continue Statements**
- `break`: Exits loop.
- `continue`: Skips to next iteration.
  ```python
  for num in range(2, 10):
      if num % 2 == 0:
          print("Found an even number", num)
          continue
      print("Found an odd number", num)
  ```

**pass Statements**
- Does nothing, placeholder:
  ```python
  while True:
      pass  # Busy-wait for keyboard interrupt (Ctrl+C)
  ```

**match Statements**
- Pattern matching:
  ```python
  def http_error(status):
      match status:
          case 400:
              return "Bad request"
          case 404:
              return "Not found"
          case 418:
              return "I'm a teapot"
          case _:
              return "Something's wrong with the internet"
  ```

**Defining Functions**
- Basic structure:
  ```python
  def fib(n):
      """Print a Fibonacci series up to n."""
      a, b = 0, 1
      while a < n:
          print(a, end=' ')
          a, b = b, a + b
      print()
  ```

**Default Argument Values**
- Example:
  ```python
  def ask_ok(prompt, retries=4, reminder='Please try again!'):
      while True:
          reply = input(prompt)
          if reply in ('y', 'ye', 'yes'):
              return True
          if reply in ('n', 'no', 'nop', 'nope'):
              return False
          retries -= 1
          if retries < 0:
              raise ValueError('invalid user response')
          print(reminder)
  ```

**Keyword Arguments**
- Example:
  ```python
  def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
      print("-- This parrot wouldn't", action, end=' ')
      print("if you put", voltage, "volts through it.")
      print("-- Lovely plumage, the", type)
      print("-- It's", state, "!")
  ```

**Positional and Keyword Arguments**
- Example:
  ```python
  def cheeseshop(kind, *arguments, **keywords):
      print("-- Do you have any", kind, "?")
      print("-- I'm sorry, we're all out of", kind)
      for arg in arguments:
          print(arg)
      print("-" * 40)
      for kw in keywords:
          print(kw, ":", keywords[kw])
  ```

**Arbitrary Argument Lists**
- Example:
  ```python
  def write_multiple_items(file, separator, *args):
      file.write(separator.join(args))
  ```

**Unpacking Argument Lists**
- Example:
  ```python
  args = [3, 6]
  list(range(*args))
  # → [3, 4, 5]
  ```

**Lambda Expressions**
- Example:
  ```python
  inc = lambda x: x + 42
  inc(7)
  # → 49
  def make_incrementor(n):
      return lambda x: x + n

  f = make_incrementor(42)
  f(7)
  # → 49
  ```

**Documentation Strings**
- Example:
  ```python
  def my_func():
      """Document this function."""
      pass

  print(my_func.__doc__)
  # → Document this function.
  ```

**Function Annotations**
- Example:
  ```python
  def f(ham: str, eggs: str = 'eggs') -> str:
      print("Annotations:", f.__annotations__)
      print("Arguments:", ham, eggs)
      return ham + ' and ' + eggs

  f('spam')
  # → Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
  # → Arguments: spam eggs
  # → 'spam and eggs'
  ```

## Data Structures

**More on Lists**
- Methods: `append(x)`, `extend(iterable)`, `insert(i, x)`, `remove(x)`, `pop([i])`, `clear()`, `index(x[, start[, end]])`, `count(x)`, `sort(*, key=None, reverse=False)`, `reverse()`, `copy()`

**Using Lists as Stacks**
- Use `append()` to add and `pop()` to retrieve.
- Example:
  ```python
  stack = [3, 4, 5]
  stack.append(6)
  stack.append(7)
  print(stack)
  # → [3, 4, 5, 6, 7]
  stack.pop()
  # → 7
  print(stack)
  # → [3, 4, 5, 6]
  ```

**Using Lists as Queues**
- Use `collections.deque` for efficient FIFO operations.
- Example:
  ```python
  from collections import deque
  queue = deque(["Eric", "John", "Michael"])
  queue.append("Terry")
  queue.append("Graham")
  queue.popleft()
  # → 'Eric'
  queue.popleft()
  # → 'John'
  print(queue)
  # → deque(['Michael', 'Terry', 'Graham'])
  ```

**List Comprehensions**
- Example: `[x**2 for x in range(10)]`
- Filter the list: `[x for x in vec if x >= 0]`

**Nested List Comprehensions**
- Transpose example: `[[row[i] for row in matrix] for i in range(4)]`

**del Statement**
- Remove items or slices: `del a[0]`, `del a[2:4]`, `del a[:]`
- Delete entire variables: `del a`

**Tuples and Sequences**
- Immutable, can be packed/unpacked: `t = 12345, 54321, 'hello!'`, `x, y, z = t`

**Sets, Set Comprehensions**
- Unordered collections, no duplicates: `a = set('abracadabra')`, `{x for x in 'abracadabra' if x not in 'abc'}`

**Dictionaries, Dict Comprehensions**
- Key-value pairs: `tel = {'jack': 4098, 'sape': 4139}`, `dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])`
- Dict Comprehensions: `{x: x**2 for x in (2, 4, 6)}`

**Looping Techniques**
- Loop through key, value pairs: `dict.items()`
- Loop through index, value pairs: `enumerate(iterable)`
- Loop through more sequences at the same time: `zip(*iterables)`
- Loop in reverse: `reversed(sequence)`
- Loop in sorted: `sorted(iterable)`
- Loop in unique sorted: `sorted(set([iterable]))`

**More on Conditions**
- Membership tests: `in`, `not in`
- Identity tests: `is`, `is not`
- Chain comparisons: `a < b == c`
- Assignment inside expressions must be done with the **walrus** operator `:=`: `if (n := len(a)) > 10: ...`

**Comparing Sequences and Other Types**
- Example:
  ```python
  (1, 2, 3)              < (1, 2, 4)
  [1, 2, 3]              < [1, 2, 4]
  'ABC' < 'C' < 'Pascal' < 'Python'
  (1, 2, 3, 4)           < (1, 2, 4)
  (1, 2)                 < (1, 2, -1)
  (1, 2, 3)             == (1.0, 2.0, 3.0)
  (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
  ```

## Modules

**Creating and Using Modules**
- Create a module: save code in a `.py` file.
- Within a module, the module’s name (as a string) is available as the value of the global variable `__name__`.
- The name of the **main** module is `__main__`.
- Import module: `import module_name`
- Access functions: `module_name.function_name()`
- Example:
  ```python
  import fibo
  fibo.fib(1000)
  ```

**Module Attributes**
- `__name__`: Module's name.
- Example: `fibo.__name__`

**Import Variants**
- Import specific functions:
  ```python
  from fibo import fib, fib2
  fib(500)
  ```
- Import all names: `from fibo import *`
- Import as another name: `import numpy as np`

**Executing Modules as Scripts**
- Add:
  ```python
  if __name__ == "__main__":
      import sys
      fib(int(sys.argv[1]))
  ```

**The Module Search Path**
1. Tuple of names of all modules that are compiled into Python: `sys.builtin_module_names`
2. List of strings that specifies the search path for modules, `sys.path` is initialized from these locations:
   1. The directory containing the input script (or the current directory when no file is specified).
   2. `PYTHONPATH` (a list of directory names, with the same syntax as the shell variable `PATH`).
   3. The installation-dependent default (by convention including a `site-packages` directory, handled by the `site` module).

**Standard Modules and Packages**
- Use `sys` for system-specific functions.
- List contents: `dir(module)`
- List the names of built-in functions and variables: `import builtins; dir(builtins)`
- **Packages** are a way of structuring Python’s module namespace by using "dotted module names": they are hierarchical directories with `__init__.py`.

**Intra-package References**
- You can write relative imports, with the from module import name form of import statement.
- These imports use leading dots to indicate the current and parent packages involved in the relative import.
- From the surround module for example, you might use:
  ```python
  from . import echo
  from .. import formats
  from ..filters import equalizer
  ```

## Input and Output

**Fancier Output Formatting**
- **Formatted String Literals (f-strings)**:
  ```python
  year = 2024
  event = 'Conference'
  f'Results of the {year} {event}'
  ```

- **str.format() Method**:
  ```python
  'We are the {} who say "{}!"'.format('knights', 'Ni')
  ```

**Reading and Writing Files**
- **Opening Files**: 
  ```python
  f = open('workfile', 'w', encoding="utf-8")
  ```

- **Writing to a File**:
  ```python
  f.write('This is a test\n')
  ```

- **Reading from a File**:
  ```python
  with open('workfile', 'r', encoding="utf-8") as f:
      read_data = f.read()
  ```

- **Using JSON for Structured Data**:
  ```python
  import json
  json.dump(data, f)
  data = json.load(f)
  ```

## Errors and Exceptions

**Syntax Errors**
- Parsing errors: `SyntaxError`
- Example:
  ```python
  while True print('Hello world')
  ```

**Exceptions**
- Runtime errors: `ZeroDivisionError`, `NameError`, `TypeError`

**Handling Exceptions**
- `try`, `except`, `else`, `finally`
  ```python
  try:
      x = int(input("Enter a number: "))
  except ValueError:
      print("Invalid number")
  ```

**Raising Exceptions**
- Use `raise` to trigger exceptions
  ```python
  raise ValueError("Error message")
  ```

**User-defined Exceptions**
- Create custom exceptions by subclassing `Exception`

**Clean-up Actions**
- Use `finally` for clean-up tasks

## Classes

**Class Definition**
- Basic syntax:
  ```python
  class ClassName:
      <statement-1>
      .
      .
      .
      <statement-N>
  ```

**Creating Instances**
- Example:
  ```python
  x = MyClass()
  ```

**Instance Variables**
- Example:
  ```python
  class Dog:
      def __init__(self, name):
          self.name = name
          self.tricks = []    # creates a new empty list for each dog
      def add_trick(self, trick):
          self.tricks.append(trick)
  ```

**Inheritance**
- Example:
  ```python
  class DerivedClassName(BaseClassName):
      <statement-1>
      .
      .
      .
      <statement-N>
  ```

**Method Resolution Order**
- Depth-first, left-to-right, dynamic ordering using `super()`.

### Example: Creating a Class Based on builtin type `dict`

**Inheriting from `dict`**

- Basic Inheritance:
  ```python
  class MyDict(dict):
      pass

  d = MyDict()
  d['key'] = 'value'
  ```

**Overriding Methods**

- Customize behavior by overriding methods:
  ```python
  class MyDict(dict):
      def __setitem__(self, key, value):
          print(f'Setting {key} to {value}')
          super().__setitem__(key, value)

  d = MyDict()
  d['key'] = 'value'
  ```

**Using `collections.UserDict`**

- Another approach using `UserDict`:
  ```python
  from collections import UserDict

  class MyDict(UserDict):
      def __setitem__(self, key, value):
          print(f'Setting {key} to {value}')
          super().__setitem__(key, value)

  d = MyDict()
  d['key'] = 'value'
  ```

**Composition Over Inheritance**

- Composition alternative:
  ```python
  class MyDict:
      def __init__(self):
          self._dict = {}

      def __setitem__(self, key, value):
          print(f'Setting {key} to {value}')
          self._dict[key] = value

      def __getitem__(self, key):
          return self._dict[key]

  d = MyDict()
  d['key'] = 'value'
  ```

## Tour of the Standard Library

**Operating System Interface**
- `os`: Interact with the operating system.
  ```python
  import os
  os.getcwd()  # Current directory
  os.system('mkdir test')  # Run system command
  ```

**File Wildcards**
- `glob`: File list from wildcard search.
  ```python
  import glob
  glob.glob('*.py')
  ```

**Command Line Arguments**
- `sys.argv`: List of command-line arguments.
  ```python
  import sys
  print(sys.argv)
  ```

**String Pattern Matching**
- `re`: Regular expressions.
  ```python
  import re
  re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
  ```

**Internet Access**
- `urllib.request`: Retrieve data.
  ```python
  from urllib.request import urlopen
  with urlopen('http://example.com') as response:
      for line in response:
          print(line.decode('utf-8'))
  ```

**Output Formatting**
- `reprlib`, `pprint`, `textwrap`, `locale` for customizable, readable output.

**Templating**
- `string.Template` for simple string substitutions, `substitute()`, and `safe_substitute()` methods.

**Working with Binary Data**
- `struct` module for binary data packing/unpacking.

**Multi-threading**
- `threading` module for concurrent execution.

**Logging**
- `logging` module for versatile logging configurations.

**Weak References**
- `weakref` module for references that don't prevent garbage collection.

**Tools for Lists**
- `array`, `collections.deque`, `bisect`, `heapq` for specialized list operations.

**Decimal Arithmetic**
- `decimal` module for precise decimal arithmetic.

## Virtual Environments and Packages

**Introduction**
- Virtual environments allow for isolated Python installations per project to avoid conflicts between dependencies.

**Creating Virtual Environments**
- Use `venv` module:
  ```bash
  python -m venv tutorial-env
  ```
- Activate:
  - Windows: `tutorial-env\Scripts\activate`
  - Unix/Mac: `source tutorial-env/bin/activate`
- Deactivate:
  ```bash
  deactivate
  ```

**Managing Packages with pip**
- Install packages:
  ```bash
  python -m pip install package_name
  ```
- List installed packages:
  ```bash
  python -m pip list
  ```
- Save/Install dependencies:
  ```bash
  python -m pip freeze > requirements.txt
  python -m pip install -r requirements.txt
  ```

## Built-in Functions

Python provides a range of built-in functions that are always available. Here are a few key examples:

- **abs(x)**: Return the absolute value of a number.
- **all(iterable)**: Return `True` if all elements are true.
- **any(iterable)**: Return `True` if any element is true.
- **enumerate(iterable, start=0)**: Return an enumerate object.
- **len(s)**: Return the length of an object.
- **max(iterable, *[, key, default])**: Return the largest item.
- **min(iterable, *[, key, default])**: Return the smallest item.
- **print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)**: Print objects.

For a full list and detailed descriptions, visit the [Python Documentation](https://docs.python.org/3/library/functions.html).

## Built-in Constants

**Core Constants**
- `False`: Boolean false value.
- `True`: Boolean true value.
- `None`: Represents the absence of a value.
- `NotImplemented`: Return this from binary methods when the operation is not implemented for the provided types.
- `Ellipsis`: The `...` object, used in extended slicing.
- `__debug__`: True if Python is not started with an `-O` option.

**Constants from the `site` Module**
- `quit()`, `exit()`: Exit the interpreter.
- `copyright`, `credits`, `license`: Provide information about Python's licensing.

For more details, visit the [Python Documentation](https://docs.python.org/3/library/constants.html).

## Built-in Types

**Truth Value Testing**
- Objects evaluated as `False`: `None`, `False`, `0`, `0.0`, `''`, `()`, `[]`, `{}`, `set()`, `range(0)`.
- Custom `__bool__()` and `__len__()` methods can override default behavior.

**Boolean Operations**
- `and`, `or`, `not` with short-circuit behavior.

**Comparisons**
- Operators: `<`, `<=`, `>`, `>=`, `==`, `!=`, `is`, `is not`, `in`, `not in`.

### Boolean Type
- **Boolean Values**: `True`, `False`
- **Operations**: `and`, `or`, `not`

### Numeric Types
- **int**: Integer, unlimited precision
- **float**: Floating-point number
- **complex**: Complex numbers, `a + bj`
- **Operations**: Standard arithmetic (`+`, `-`, `*`, `/`), power (`**`), modulo (`%`)

### Sequence Types
- **list**, **tuple**, **range**
- **Operations**: Indexing, slicing, concatenation, repetition, membership (`in`, `not in`)

### Iterator, Generator Types
- **Iterators**: Objects with `__iter__()` and `__next__()`
- **Generators**: Functions with `yield` to produce items lazily

### Text Sequence Type
- **str**: Immutable sequences of Unicode code points

### Binary Sequence Types
- **bytes**, **bytearray**, **memoryview**
- **Operations**: Similar to text sequences, plus specific byte manipulation

### Set Types
- **set**, **frozenset**
- **Operations**: Union, intersection, difference, symmetric difference

### Mapping Types
- **dict**: Key-value pairs, supports various operations and methods

### Context Manager Types
- **with** statement: Ensures resource management (e.g., file operations)
- Implement with `__enter__()` and `__exit__()`

### Type Annotation Types
- **PEP 484**: Static type checking with `typing` module

### Special Attributes, Regular Dunder Methods
- **Common Dunders**: `__init__()`, `__str__()`, `__repr__()`, `__len__()`, `__getitem__()`, `__setitem__()`, `__delitem__()`
- **Attributes**: `__doc__`, `__dict__`, `__name__`, `__module__`

For detailed explanations and more examples, visit the [Python Documentation](https://docs.python.org/3/library/stdtypes.html).

### Built-in Exceptions

**Core Exception Hierarchy**
- **BaseException**: Root of all exceptions.
- **Exception**: Standard error, all custom exceptions should inherit from this.
- **ArithmeticError**: Base for numeric errors (`OverflowError`, `ZeroDivisionError`).
- **LookupError**: Base for invalid key/index (`IndexError`, `KeyError`).

**Common Exceptions**
- **AssertionError**: Failed `assert` statement.
- **AttributeError**: Invalid attribute reference.
- **EOFError**: Unexpected end of input.
- **ImportError / ModuleNotFoundError**: Issues with imports.
- **IndexError**: Out-of-range sequence index.
- **KeyError**: Missing dictionary key.
- **MemoryError**: Out of memory.
- **NameError**: Undefined variable.
- **OSError**: Operating system error.
- **TypeError**: Inappropriate operation for type.
- **ValueError**: Correct type, but inappropriate value.

**Advanced Features**
- **Exception Context**: `__context__`, `__cause__`, `__suppress_context__` for chained exceptions.

For a complete list and detailed explanations, visit the [Python Documentation](https://docs.python.org/3/library/exceptions.html).

## Text Processing Services

**Modules Overview**
- **string**: Common string operations, constants, formatting, and templates.
- **re**: Regular expressions for advanced string matching and manipulation.
- **difflib**: Tools for comparing sequences, useful for comparing text files.
- **textwrap**: Functions for wrapping and formatting text.
- **unicodedata**: Unicode database access.
- **stringprep**: Internet string preparation.
- **readline**: GNU readline interface for interactive input editing.
- **rlcompleter**: Completion function for readline.

For detailed information, visit the [Python Documentation](https://docs.python.org/3/library/text.html).

### `string` Module

**Common String Operations**
- **Constants**:
  - `string.ascii_letters`: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  - `string.digits`: '0123456789'
  - `string.punctuation`: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

- **Custom String Formatting**:
  ```python
  'We are the {} who say "{}!"'.format('knights', 'Ni')
  ```

- **Template Strings**:
  ```python
  from string import Template
  t = Template('$who likes $what')
  t.substitute(who='tim', what='kung pao')
  ```

### `re` Module

**Regular Expression Operations**
- **Basic Syntax**:
  ```python
  import re
  re.search(r'\bword\b', 'A word in a sentence')
  ```

- **Functions**:
  - `re.match()`: Determine if the RE matches at the beginning of the string.
  - `re.search()`: Scan through a string, looking for any location where this RE matches.
  - `re.findall()`: Find all substrings where the RE matches.
  - `re.sub()`: Replace matches with a string.

- **Compiling Regular Expressions**:
  ```python
  pattern = re.compile(r'\bword\b')
  pattern.search('A word in a sentence')
  ```

- **Match Objects**:
  ```python
  match = re.search(r'\bword\b', 'A word in a sentence')
  if match:
      print(match.group())
  ```

For more details, visit the [Python Documentation](https://docs.python.org/3/library/text.html).

## Data Types

**Overview**
The modules described in this chapter provide a variety of specialized data types such as dates and times, fixed-type arrays, heap queues, double-ended queues, and enumerations. Python also offers built-in types like `dict`, `list`, `set`, `frozenset`, `tuple`, `str`, `bytes`, and `bytearray`.

### Detailed Modules

**datetime**
- **Purpose**: Manipulate dates and times.
- **Key Types**: `date`, `time`, `datetime`, `timedelta`, `tzinfo`.
- **Usage**:
  ```python
  from datetime import datetime
  now = datetime.now()
  print(now)
  ```

**calendar**
- **Purpose**: General calendar-related functions.
- **Usage**:
  ```python
  import calendar
  print(calendar.month(2024, 7))
  ```

**collections**
- **Purpose**: High-performance container datatypes.
- **Key Types**: `namedtuple`, `deque`, `Counter`, `OrderedDict`, `defaultdict`, `ChainMap`.
- **Usage**:
  ```python
  from collections import Counter
  count = Counter('abracadabra')
  print(count)
  ```

**collections.abc**
- **Purpose**: Abstract Base Classes for containers.
- **Key Classes**: `Iterable`, `Iterator`, `Sequence`, `MutableSequence`, `Mapping`, `MutableMapping`, `Set`, `MutableSet`.
- **Usage**:
  ```python
  from collections.abc import Iterable
  isinstance([], Iterable)  # True
  ```

### More Information
For more details, visit the [Python Documentation](https://docs.python.org/3/library/datatypes.html).

## Functional Programming Modules

**Overview**
The modules in this chapter support a functional programming style and operations on callables.

**Key Modules**

**itertools**
- **Purpose**: Functions creating iterators for efficient looping.
- **Key Functions**: `count()`, `cycle()`, `repeat()`, `chain()`, `islice()`, `zip_longest()`.
- **Usage**:
  ```python
  import itertools
  for i in itertools.count(10):
      if i > 15:
          break
      print(i)
  ```

**functools**
- **Purpose**: Higher-order functions and operations on callable objects.
- **Key Functions**: `reduce()`, `partial()`, `lru_cache()`, `cmp_to_key()`.
- **Usage**:
  ```python
  from functools import lru_cache

  @lru_cache(maxsize=None)
  def fibonacci(n):
      if n < 2:
          return n
      return fibonacci(n-1) + fibonacci(n-2)
  print(fibonacci(10))
  ```

**operator**
- **Purpose**: Standard operators as functions.
- **Key Functions**: Arithmetic, comparison, and logical operators (`add()`, `sub()`, `mul()`, `truediv()`, `eq()`, `lt()`, `not_()`, etc.).
- **Usage**:
  ```python
  import operator
  result = operator.add(1, 2)
  print(result)  # Output: 3
  ```

For detailed information, visit the [Python Documentation](https://docs.python.org/3/library/functional.html).

## File and Directory Access

**Overview**
This chapter covers modules for disk file and directory operations.

### Key Modules

**pathlib**
- **Purpose**: Object-oriented filesystem paths.
- **Usage**:
  ```python
  from pathlib import Path
  path = Path('/etc')
  print(path.exists())
  ```

**os.path**
- **Purpose**: Common pathname manipulations.

**fileinput**
- **Purpose**: Iterate over lines from multiple input streams.

**stat**
- **Purpose**: Interpreting `stat()` results.

**filecmp**
- **Purpose**: File and directory comparisons.

**tempfile**
- **Purpose**: Generate temporary files and directories.

**glob**
- **Purpose**: Unix style pathname pattern expansion.

**fnmatch**
- **Purpose**: Unix filename pattern matching.

**linecache**
- **Purpose**: Random access to text lines.

**shutil**
- **Purpose**: High-level file operations.

For more details, visit the [Python Documentation](https://docs.python.org/3/library/filesys.html).

## File Formats

**Overview**
This chapter includes modules for parsing various file formats not related to markup languages or e-mail.

**Key Modules**

**csv**
- **Purpose**: Read and write CSV files.
- **Usage**:
  ```python
  import csv
  with open('data.csv', newline='') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
          print(row)
  ```

**configparser**
- **Purpose**: Parse configuration files.
- **Usage**:
  ```python
  import configparser
  config = configparser.ConfigParser()
  config.read('example.ini')
  print(config['section']['key'])
  ```

**tomllib**
- **Purpose**: Parse TOML files.
- **Usage**:
  ```python
  import tomllib
  with open('example.toml', 'rb') as f:
      data = tomllib.load(f)
  ```

**netrc**
- **Purpose**: Parse netrc authentication files.
- **Usage**:
  ```python
  import netrc
  credentials = netrc.netrc()
  ```

**plistlib**
- **Purpose**: Generate and parse Apple .plist files.
- **Usage**:
  ```python
  import plistlib
  with open('example.plist', 'rb') as f:
      data = plistlib.load(f)
  ```

For more details, visit the [Python Documentation](https://docs.python.org/3/library/fileformats.html).

## Generic Operating System Services

**Overview**
This chapter covers modules providing interfaces to OS features, modeled after Unix or C interfaces, available on most systems.

### Key Modules

**os**
- **Purpose**: Miscellaneous OS interfaces.
- **Usage**:
  ```python
  import os
  os.listdir('.')
  ```

**io**
- **Purpose**: Core tools for working with streams (text and binary I/O).

**time**
- **Purpose**: Time access and conversions.
- **Usage**:
  ```python
  import time
  print(time.time())
  ```

**argparse**
- **Purpose**: Command-line option and argument parsing.

**getopt**
- **Purpose**: C-style parser for command-line options.

**logging**
- **Purpose**: Logging facility for Python applications.

**platform**
- **Purpose**: Access underlying platform’s identifying data.

**ctypes**
- **Purpose**: A foreign function library for Python.

For more details, visit the [Python Documentation](https://docs.python.org/3/library/allos.html).

## Concurrent Execution

**Overview**
Support for concurrent execution of code, suited for both CPU-bound and IO-bound tasks.

### Key Modules

**threading**
- **Purpose**: Thread-based parallelism.
- **Key Features**: Thread objects, locks, conditions, semaphores, barriers.
- **Usage**:
  ```python
  import threading
  def worker():
      print("Worker thread")
  t = threading.Thread(target=worker)
  t.start()
  ```

**multiprocessing**
- **Purpose**: Process-based parallelism.
- **Key Features**: Process class, synchronization, pools.
- **Usage**:
  ```python
  from multiprocessing import Process
  def worker():
      print("Worker process")
  p = Process(target=worker)
  p.start()
  ```

**concurrent.futures**
- **Purpose**: High-level interface for asynchronously executing functions.
- **Key Features**: ThreadPoolExecutor, ProcessPoolExecutor.
- **Usage**:
  ```python
  from concurrent.futures import ThreadPoolExecutor
  with ThreadPoolExecutor() as executor:
      future = executor.submit(pow, 2, 3)
      print(future.result())
  ```

**asyncio**
- **Purpose**: Asynchronous I/O, event loop, coroutines, and tasks.
- **Usage**:
  ```python
  import asyncio
  async def main():
      print("Hello")
      await asyncio.sleep(1)
      print("World")
  asyncio.run(main())
  ```

For more details, visit the [Python Documentation](https://docs.python.org/3/library/concurrency.html).

## Miscellaneous Modules

### `asyncio`
- **Purpose**: Asynchronous I/O, event loop, coroutines, tasks.
- **Usage**:
  ```python
  import asyncio
  async def main():
      print("Hello")
      await asyncio.sleep(1)
      print("World")
  asyncio.run(main())
  ```

[More details](https://docs.python.org/3/library/asyncio.html)

### `json`
- **Purpose**: JSON (de)serialization.
- **Usage**:
  ```python
  import json
  data = {'key': 'value'}
  json_str = json.dumps(data)
  data_back = json.loads(json_str)
  ```

[More details](https://docs.python.org/3/library/json.html)

### `typing`
- **Purpose**: Type hints and type checking.
- **Usage**:
  ```python
  from typing import List
  def greet(names: List[str]) -> None:
      for name in names:
          print(f"Hello, {name}")
  ```

[More details](https://docs.python.org/3/library/typing.html)

### `unittest`
- **Purpose**: Unit testing framework.
- **Usage**:
  ```python
  import unittest
  class TestStringMethods(unittest.TestCase):
      def test_upper(self):
          self.assertEqual('foo'.upper(), 'FOO')
  if __name__ == '__main__':
      unittest.main()
  ```

[More details](https://docs.python.org/3/library/unittest.html)

### `unittest.mock`
- **Purpose**: Mocking objects in tests.
- **Usage**:
  ```python
  from unittest.mock import MagicMock
  mock = MagicMock()
  mock.method()
  mock.method.assert_called_once()
  ```

[More details](https://docs.python.org/3/library/unittest.mock.html)

### `sys`
- **Purpose**: System-specific parameters and functions.
- **Usage**:
  ```python
  import sys
  print(sys.version)
  sys.exit(0)
  ```

[More details](https://docs.python.org/3/library/sys.html)

### `dataclasses`
- **Purpose**: Data classes for boilerplate code reduction.
- **Usage**:
  ```python
  from dataclasses import dataclass
  @dataclass
  class Point:
      x: int
      y: int
  p = Point(1, 2)
  ```

[More details](https://docs.python.org/3/library/dataclasses.html)

### `abc`
- **Purpose**: Abstract Base Classes.
- **Usage**:
  ```python
  from abc import ABC, abstractmethod
  class MyAbstractClass(ABC):
      @abstractmethod
      def do_something(self):
          pass
  ```

[More details](https://docs.python.org/3/library/abc.html)

### `ast`
- **Purpose**: Abstract Syntax Trees.
- **Usage**:
  ```python
  import ast
  tree = ast.parse("x = 1 + 2")
  ast.dump(tree)
  ```

[More details](https://docs.python.org/3/library/ast.html)

## End
