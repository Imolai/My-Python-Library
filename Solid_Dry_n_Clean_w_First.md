# SOLID, DRY and Clean Code with FIRST tests

## Contents

- [SOLID, DRY and Clean Code with FIRST tests](#solid-dry-and-clean-code-with-first-tests)
  - [Contents](#contents)
  - [About SOLID and DRY](#about-solid-and-dry)
  - [SOLID and DRY Principles in Python](#solid-and-dry-principles-in-python)
    - [1. **Single Responsibility Principle (SRP)**: Each class should have only one responsibility.](#1-single-responsibility-principle-srp-each-class-should-have-only-one-responsibility)
    - [2. **Open/Closed Principle (OCP)**: Classes should be open for extension but closed for modification.](#2-openclosed-principle-ocp-classes-should-be-open-for-extension-but-closed-for-modification)
    - [3. **Liskov Substitution Principle (LSP)**: Subclasses should be replaceable with their base classes.](#3-liskov-substitution-principle-lsp-subclasses-should-be-replaceable-with-their-base-classes)
    - [4. **Interface Segregation Principle (ISP)**: Don’t force classes to implement interfaces they don’t use.](#4-interface-segregation-principle-isp-dont-force-classes-to-implement-interfaces-they-dont-use)
    - [5. **Dependency Inversion Principle (DIP)**: High-level modules should depend on abstractions, not concrete implementations.](#5-dependency-inversion-principle-dip-high-level-modules-should-depend-on-abstractions-not-concrete-implementations)
    - [6. **Don't Repeat Yourself (DRY)**: Avoid repeating code; use shared logic instead.](#6-dont-repeat-yourself-dry-avoid-repeating-code-use-shared-logic-instead)
    - [How to Enforce SOLID Principles in Development](#how-to-enforce-solid-principles-in-development)
  - [About Clean Code](#about-clean-code)
  - [Clean Code Principles](#clean-code-principles)
  - [Clean Code Examples in Python](#clean-code-examples-in-python)
    - [1. **Simplicity**](#1-simplicity)
    - [2. **Meaningful Names**](#2-meaningful-names)
    - [3. **Small Functions**](#3-small-functions)
    - [4. **Don't Repeat Yourself (DRY)**](#4-dont-repeat-yourself-dry)
    - [5. **Minimizing Side Effects**](#5-minimizing-side-effects)
    - [6. **Readable Code over Comments**](#6-readable-code-over-comments)
    - [Advantages of Clean Code](#advantages-of-clean-code)
  - [Clean Code in comments and docstrings](#clean-code-in-comments-and-docstrings)
    - [Key Points about Comments in Clean Code](#key-points-about-comments-in-clean-code)
    - [Key Points about Docstrings in Clean Code](#key-points-about-docstrings-in-clean-code)
    - [Examples of Good Comment and Docstring Usage](#examples-of-good-comment-and-docstring-usage)
      - [1. **Minimal and Meaningful Comments**](#1-minimal-and-meaningful-comments)
      - [2. **Good Docstring Example**](#2-good-docstring-example)
    - [3. **Avoid Redundant Comments**](#3-avoid-redundant-comments)
    - [Clean Code Best Practices for Comments and Docstrings](#clean-code-best-practices-for-comments-and-docstrings)
    - [About FIRST](#about-first)
  - [What is FIRST?](#what-is-first)
  - [Python Code Examples for FIRST Principles](#python-code-examples-for-first-principles)
    - [1. **Fast**:](#1-fast)
    - [2. **Independent**:](#2-independent)
    - [3. **Repeatable**:](#3-repeatable)
    - [4. **Self-validating**:](#4-self-validating)
    - [5. **Timely**:](#5-timely)
  - [TDD is included](#tdd-is-included)

## About SOLID and DRY

**SOLID** is a collection of five principles introduced by Robert C. Martin (Uncle Bob) to enhance the structure and maintainability of object-oriented code.

1. **Single Responsibility Principle (SRP)**: A class should have only one responsibility.
2. **Open/Closed Principle (OCP)**: Entities should be open for extension but closed for modification.
3. **Liskov Substitution Principle (LSP)**: Subtypes should be replaceable by their base types.
4. **Interface Segregation Principle (ISP)**: Don’t force clients to depend on interfaces they don’t use.
5. **Dependency Inversion Principle (DIP)**: High-level modules should depend on abstractions, not concrete implementations.

Together, these principles promote flexible, scalable, and easily maintainable code.

**DRY** (Don't Repeat Yourself) is a principle aimed at reducing code duplication by ensuring that each piece of knowledge or logic is expressed only once.
Repetition leads to redundancy, increasing the risk of inconsistencies and errors during updates or maintenance.
By following DRY, developers create more efficient, maintainable, and modular code, ensuring that changes need to be made in only one place when requirements evolve.

## SOLID and DRY Principles in Python

### 1. **Single Responsibility Principle (SRP)**: Each class should have only one responsibility.
   ```python
   class ReportGenerator:
       def generate(self, data):
           return f"Report: {data}"

   class ReportSaver:
       def save(self, report):
           with open('report.txt', 'w') as f:
               f.write(report)
   ```

### 2. **Open/Closed Principle (OCP)**: Classes should be open for extension but closed for modification.
   ```python
   class Shape:
       def area(self):
           pass

   class Circle(Shape):
       def area(self):
           return "Circle area"

   class Square(Shape):
       def area(self):
           return "Square area"
   ```

### 3. **Liskov Substitution Principle (LSP)**: Subclasses should be replaceable with their base classes.
   ```python
   class Bird:
       def fly(self):
           pass

   class Sparrow(Bird):
       def fly(self):
           return "Flying"

   class Ostrich(Bird):  # Violation of LSP
       def fly(self):
           raise Exception("Can't fly")
   ```

### 4. **Interface Segregation Principle (ISP)**: Don’t force classes to implement interfaces they don’t use.
   ```python
   class Printer:
       def print(self):
           pass

   class Scanner:
       def scan(self):
           pass

   class MultiFunctionPrinter(Printer, Scanner):
       def print(self):
           return "Printing"
       def scan(self):
           return "Scanning"
   ```

### 5. **Dependency Inversion Principle (DIP)**: High-level modules should depend on abstractions, not concrete implementations.
   ```python
   class Database:
       def connect(self):
           pass

   class MySQLDatabase(Database):
       def connect(self):
           return "Connected to MySQL"

   class Application:
       def __init__(self, db: Database):
           self.db = db
       def run(self):
           return self.db.connect()
   ```

### 6. **Don't Repeat Yourself (DRY)**: Avoid repeating code; use shared logic instead.
   ```python
   def calculate_area(width, height):
       return width * height

   print(calculate_area(5, 10))
   print(calculate_area(3, 6))
   ```

### How to Enforce SOLID Principles in Development

To enforce the SOLID principles during development, you can use the following methods and tools:

1. **Code Reviews**: Regular code reviews help identify and correct sections where SOLID principles are violated. Experienced developers can point out problematic design or code structure.

2. **Automated Static Code Analysis Tools**:
   - **Pylint, Flake8, SonarQube**: These tools analyze the code and warn of violations or bad practices, such as a class having too many responsibilities (SRP) or incorrect handling of inheritance (LSP).

3. **Unit Testing**: Writing good unit tests forces developers to create modular, testable code. Difficulty in testing a piece of code often indicates a violation of one of the SOLID principles.

4. **Refactoring Tools**: IDEs and coding tools like PyCharm or VSCode support refactoring, which helps to enforce SOLID principles without breaking too much of the codebase.

5. **Development Guidelines and Best Practices**: Establishing shared guidelines and practices that specifically encourage adherence to SOLID principles helps maintain clean code and proper architecture.

6. **Design Patterns**: Using proven design patterns (e.g., Factory, Strategy, Dependency Injection) promotes the observance of SOLID principles, especially Open/Closed and Dependency Inversion.

7. **CI/CD with Tests**: Tools like Jenkins or GitLab CI can run automated code checks and unit tests during commits to ensure the code aligns with the SOLID principles.

These methods and tools help developers create structured, maintainable code that adheres to the SOLID principles.

## About Clean Code

**Clean Code** refers to code that is easy to understand, maintain, and extend.
The principles outlined by Robert C. Martin (also) emphasize the readability and simplicity of the code.
Clean code should follow certain principles that enhance the quality of the development process, reduce errors, and facilitate future modifications.

## Clean Code Principles

1. **Simplicity**: The code should reflect the simplest solution to the problem without unnecessary complexity.
2. **Meaningful Names**: Variables, functions, and class names should be self-explanatory, making it clear what the code is doing.
3. **Small Functions**: Functions should be short and focused on doing only one thing.
4. **Don’t Repeat Yourself (DRY)**: Avoid repeating the same code; reuse logic instead.
5. **Minimizing Side Effects**: Functions should only modify variables they are responsible for and should avoid hidden side effects.
6. **Readable Code over Comments**: Well-written code should document itself, requiring fewer comments.

## Clean Code Examples in Python

### 1. **Simplicity**
Avoid complex code and opt for simple solutions.

**Bad Example**:
```python
def calculate_total_price(price, tax_rate):
    if tax_rate > 0:
        total = price + (price * tax_rate)
    else:
        total = price
    return total
```

**Good Example (Simplified)**:
```python
def calculate_total_price(price, tax_rate):
    return price + (price * tax_rate)
```

### 2. **Meaningful Names**
Use names that clearly describe the purpose of the variable or function.

**Bad Example**:
```python
def f(x):
    return x * x
```

**Good Example**:
```python
def calculate_square(number):
    return number * number
```

### 3. **Small Functions**
Each function should focus on a single responsibility.

**Bad Example**:
```python
def process_data(data):
    clean_data = [d.strip() for d in data]
    result = [int(d) for d in clean_data if d.isdigit()]
    return sum(result)
```

**Good Example**:
```python
def clean_data(data):
    return [d.strip() for d in data]

def filter_numeric_data(clean_data):
    return [int(d) for d in clean_data if d.isdigit()]

def process_data(data):
    return sum(filter_numeric_data(clean_data(data)))
```

### 4. **Don't Repeat Yourself (DRY)**
Avoid duplicating code, instead use shared logic.

**Bad Example**:
```python
def get_area_of_square(side):
    return side * side

def get_area_of_rectangle(width, height):
    return width * height
```

**Good Example**:
```python
def calculate_area(width, height=None):
    if height is None:
        height = width
    return width * height
```

### 5. **Minimizing Side Effects**
Avoid modifying external variables or state.

**Bad Example**:
```python
counter = 0

def increment_counter():
    global counter
    counter += 1
```

**Good Example**:
```python
def increment(counter):
    return counter + 1
```

### 6. **Readable Code over Comments**
The code should be self-explanatory, reducing the need for comments.

**Bad Example**:
```python
def add(a, b):
    # adds a and b
    return a + b
```

**Good Example**:
```python
def add_numbers(first_number, second_number):
    return first_number + second_number
```

### Advantages of Clean Code

- Easier to maintain and test.
- More understandable and accessible to other developers in the team.
- Reduces the likelihood of errors and simplifies debugging.

Applying Clean Code principles requires constant attention but makes the development process much smoother in the long run.

## Clean Code in comments and docstrings

According to **Clean Code**, comments and docstrings should be used sparingly and only when truly necessary. The philosophy behind Clean Code emphasizes that **well-written code should be self-explanatory**, meaning the structure, logic, and naming conventions should make the code easily understandable without the need for excessive comments. Here's the good approach regarding comments and docstrings according to Clean Code principles:

### Key Points about Comments in Clean Code
1. **Comments Are Often a Failure**: Robert C. Martin suggests that comments often indicate a failure to make the code itself clear. If you need a comment to explain what the code does, the code might need refactoring to be more understandable.

2. **Good Code Should Be Self-Explanatory**: By using clear, meaningful names for variables, functions, and classes, as well as breaking down complex logic into smaller, focused functions, the need for comments is reduced. The goal is that another developer can read the code and understand what it does without relying on comments.

3. **Comments Should Not Explain "What" the Code Does**: If a comment explains *what* the code does, it usually means the code could be improved. Instead, comments should focus on explaining **why** certain decisions were made or on clarifying complex business logic that can't be simplified in the code itself.

4. **Avoid Redundant or Obsolete Comments**: Comments that repeat what the code does or become outdated as the code evolves are counterproductive. They can mislead developers or create confusion. Keeping comments in sync with code changes can be difficult, so it's better to write clean, clear code instead.

5. **Use Comments for Clarifications or Warnings**: Comments are useful for explaining non-obvious decisions, highlighting potential pitfalls, or providing important contextual information about external constraints (e.g., reasons for an optimization). They are also helpful for warning other developers about potential risks.

### Key Points about Docstrings in Clean Code
1. **Docstrings Should Be Brief and Precise**: While comments should be minimal, **docstrings** (especially in Python) are important for documenting public APIs—functions, classes, and modules. A good docstring briefly describes the purpose of the function or class, its arguments, return values, and exceptions (if applicable).

2. **Use Docstrings to Explain Purpose and Usage**: Unlike comments, which may describe more complex internal logic, docstrings are intended to explain *how* and *why* to use the function or class. They serve as part of the API documentation and should provide enough context for users of the code.

3. **Docstrings Should Focus on the "What" and "How"**: Docstrings should not explain what the code *internally* does but should explain the purpose and how to use the function, class, or module.

### Examples of Good Comment and Docstring Usage

#### 1. **Minimal and Meaningful Comments**
```python
def calculate_discount(price, discount_rate):
    # Cap the discount to a maximum of 50%
    if discount_rate > 0.5:
        discount_rate = 0.5
    return price - (price * discount_rate)
```
Here, the comment explains *why* the discount is capped, which is not immediately obvious from the code itself.

#### 2. **Good Docstring Example**
```python
def calculate_area(width, height):
    """
    Calculate the area of a rectangle.
    
    Args:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    
    Returns:
        float: The area of the rectangle.
    """
    return width * height
```
The docstring clearly explains the purpose of the function, its arguments, and the return value without describing the internal implementation.

### 3. **Avoid Redundant Comments**
**Bad Example**:
```python
def add_numbers(a, b):
    # This function adds two numbers
    return a + b
```
This comment is redundant because the function name and code are already self-explanatory.

### Clean Code Best Practices for Comments and Docstrings
1. **Use Meaningful Names**: Choose names for variables, functions, and classes that describe their purpose and eliminate the need for comments.
2. **Keep Functions Small and Focused**: Small, focused functions often make comments unnecessary because each function has a clear purpose.
3. **Write Docstrings for Public APIs**: Docstrings are especially important for functions and classes that others will use, providing usage guidance and context.
4. **Explain Intent in Comments**: When comments are needed, focus on explaining the intent behind the code, not the mechanics of how it works.
5. **Avoid Redundancy**: Don't repeat the code in comments. Instead, use comments to provide context or clarification for decisions that are not obvious.

In short, **Clean Code promotes the use of clear, self-documenting code** that minimizes the need for comments and leverages concise, informative docstrings where appropriate, especially in public-facing APIs.

### About FIRST

**FIRST** is an acronym that outlines key principles for writing effective unit tests. These principles ensure that unit tests are reliable, easy to maintain, and valuable during the development process. By following the FIRST principles, developers can ensure their tests are efficient and provide fast feedback.

## What is FIRST?

**FIRST** stands for:
1. **Fast**: Unit tests should execute quickly, providing immediate feedback to developers. Slow tests can disrupt the development process and discourage frequent testing.
2. **Independent**: Tests should not rely on the outcome of other tests. Each test should run independently, ensuring that one failure doesn't cascade into multiple failures.
3. **Repeatable**: Unit tests should consistently yield the same result, no matter how often they are executed or the environment in which they run.
4. **Self-validating**: A unit test should automatically determine whether it passes or fails without human interpretation. It should return a clear true/false result.
5. **Timely**: Unit tests should be written as soon as possible, preferably before the production code (as per Test-Driven Development).

## Python Code Examples for FIRST Principles

### 1. **Fast**:
Write lightweight tests that focus on specific functions without external dependencies (e.g., databases or networks).

```python
def add_numbers(a, b):
    return a + b

def test_add_numbers():
    assert add_numbers(2, 3) == 5  # This test runs instantly
```

### 2. **Independent**:
Ensure each test operates independently of others, avoiding shared state.

```python
def test_first_operation():
    result = add_numbers(2, 3)
    assert result == 5

def test_second_operation():
    result = add_numbers(4, 6)
    assert result == 10
```
Each test operates on its own data, ensuring independence.

### 3. **Repeatable**:
Tests should produce the same result every time, regardless of external factors.

```python
def test_repeatable():
    assert add_numbers(10, 5) == 15  # This will always return the same result
```

### 4. **Self-validating**:
The test should automatically check correctness and return clear pass/fail results.

```python
def test_self_validating():
    assert add_numbers(1, 1) == 2  # No manual checking, the assert evaluates correctness
```

### 5. **Timely**:
Write tests before or during the development of the function, ensuring they accompany the code.

```python
# TDD Example: Write the test before implementing the function
def test_timely():
    assert add_numbers(3, 7) == 10  # Fail first, then implement the function
```

By adhering to the **FIRST** principles, unit tests remain fast, independent, reliable, and serve as a strong foundation for building high-quality software.

## TDD is included

The **"Timely"** principle in **FIRST** is essentially one of the key principles of **TDD (Test-Driven Development)**.
It means that tests are written on time, i.e., before or during the development of the code.
This perfectly aligns with the TDD methodology, which dictates that development starts with writing tests and then building the code based on the tests.

The three steps of TDD are:
1. Write a test that initially **fails**.
2. Write the minimum code necessary to pass the test.
3. Refactor the code while keeping the test passing.

The **Timely** principle emphasizes that testing is not an afterthought but an early and integral part of the development process, exactly as TDD prescribes.
Therefore, we can indeed say that the **"Timely"** principle is equivalent to the TDD approach.
