# Python for Data Analytics

## Table of Contents

- [Python for Data Analytics](#python-for-data-analytics)
  - [Table of Contents](#table-of-contents)
  - [A Beginner's Guide](#a-beginners-guide)
    - [Beginner's Introduction](#beginners-introduction)
    - [1. Python Basics](#1-python-basics)
      - [Syntax and Basic Data Types](#syntax-and-basic-data-types)
      - [Functions](#functions)
      - [Classes](#classes)
      - [Summary Table of Type Transitions](#summary-table-of-type-transitions)
      - [Importing Modules](#importing-modules)
      - [Handling Exceptions](#handling-exceptions)
    - [2. Working with Files](#2-working-with-files)
    - [3. Working with JSON and XML Formats](#3-working-with-json-and-xml-formats)
      - [JSON (JavaScript Object Notation)](#json-javascript-object-notation)
      - [XML (eXtensible Markup Language)](#xml-extensible-markup-language)
    - [4. Setting Up Your Local Development Environment](#4-setting-up-your-local-development-environment)
  - [An Intermediate Guide](#an-intermediate-guide)
    - [Intermediate's Introduction](#intermediates-introduction)
    - [1. DataFrame and Pandas](#1-dataframe-and-pandas)
      - [DataFrame](#dataframe)
      - [Pandas Library](#pandas-library)
    - [2. NumPy Library](#2-numpy-library)
    - [3. Basics of Matplotlib](#3-basics-of-matplotlib)
    - [4. Mutable and Immutable Types](#4-mutable-and-immutable-types)
    - [5. Basic Operations with Pandas/NumPy](#5-basic-operations-with-pandasnumpy)
      - [Using Pandas](#using-pandas)
      - [Using NumPy](#using-numpy)
    - [6. Export DataFrame to CSV](#6-export-dataframe-to-csv)
    - [7. Build Basic Visualizations](#7-build-basic-visualizations)
    - [8. Extract Data from Databases](#8-extract-data-from-databases)
  - [An Advanced Guide](#an-advanced-guide)
    - [Advanced's Introduction](#advanceds-introduction)
    - [1. Advanced Python Features](#1-advanced-python-features)
      - [Lambda Functions](#lambda-functions)
      - [Iterators](#iterators)
      - [Python Comprehensions](#python-comprehensions)
    - [2. Logging](#2-logging)
    - [3. Working with REST API](#3-working-with-rest-api)
    - [4. Advanced Data Operations with Pandas/NumPy](#4-advanced-data-operations-with-pandasnumpy)
      - [Merge](#merge)
      - [Reshape](#reshape)
      - [Functions](#functions-1)
    - [5. Advanced Visualizations in Python](#5-advanced-visualizations-in-python)
    - [6. Best Practices and Refactoring Python Code](#6-best-practices-and-refactoring-python-code)
      - [Best Practices](#best-practices)
      - [Refactoring Example](#refactoring-example)

## A Beginner's Guide

### Beginner's Introduction

Python is a versatile and powerful programming language widely used in data analysis, web development, automation, and more. This guide will help you get started with the basics of Python, working with files, and manipulating JSON and XML data structures.

### 1. Python Basics

#### Syntax and Basic Data Types

Python's syntax is straightforward and easy to learn. Let's start with a simple "Hello, World!" program and explore basic data types.

```python
# Hello, World!
print("Hello, World!")

# Basic Data Types
bool_value = True
int_value = 42
float_value = 3.14
complex_value = 3 + 4j
str_value = "Python is fun! 😊"  # immutable
bytes_value = b"Python is fun! \xf0\x9f\x98\x8a"  # immutable
byte_array = bytearray(bytes_value)
list_value = [1, 2, 3, 4, 5]
tuple_value = (1, 2, 3)  # immutable
set_value = {1, 2, 3}
frozenset_value = frozenset({1, 2, 3})  # immutable
dict_value = {"key": "value", "another_key": 42}
```

#### Functions

Functions are reusable blocks of code that perform specific tasks.

```python
def greet(name):
    return f"Hello, {name}!"

# greet's type is "function"

print(greet("Alice"))
```

#### Classes

Classes are used to create objects, providing a means of bundling data and functionality together.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return f"{self.name} says woof!"

# Dog's type is "type"

my_dog = Dog("Buddy", 3)  # my_dog's type is "class"
print(my_dog.bark())  # my_dog.bark's type is "method"
```

#### Summary Table of Type Transitions

| **Element**                    | **Definition Phase Type**        | **Class Level Type**             | **Instance Level Type**      |
|--------------------------------|----------------------------------|----------------------------------|------------------------------|
| **Regular Function**           | `function`                       | `function`                       | N/A                          |
| **Instance Method**            | `function`                       | `function`                       | `method`                     |
| **Class Method**               | `function` with `@classmethod`   | `method`                         | `method`                     |
| **Static Method**              | `function` with `@staticmethod`  | `function`                       | `function`                   |
| **Class**                      | `type`                           | `type`                           | N/A                          |
| **Instance**                   | N/A                              | N/A                              | `class`                      |
| **Abstract Class**             | `ABCMeta`                        | `ABCMeta`                        | N/A                          |
| **Abstract Method**            | `function` with `@abstractmethod`| `function`                       | `method`                     |
| **Concrete Class**             | `ABCMeta`                        | `ABCMeta`                        | `ConcreteClass`              |
| **Concrete Method**            | `function` with `@abstractmethod`| `function`                       | `method`                     |

#### Importing Modules

Modules allow you to organize your code into separate files and reuse code across multiple programs.

```python
import math

print(math.sqrt(16))  # Output: 4.0
```

#### Handling Exceptions

Exceptions are errors that occur during program execution. Handling exceptions allows your program to run smoothly even when an error occurs.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```

### 2. Working with Files

Reading from and writing to files is a common task in data analytics.

```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, file!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### 3. Working with JSON and XML Formats

#### JSON (JavaScript Object Notation)

JSON is a lightweight data-interchange format that is easy to read and write.

```python
import json

# Writing JSON data
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Reading JSON data
with open("data.json", "r") as json_file:
    data = json.load(json_file)
    print(data)
```

#### XML (eXtensible Markup Language)

XML is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable.

```python
import xml.etree.ElementTree as ET

# Creating XML data
data = ET.Element("data")
item1 = ET.SubElement(data, "item")
item1.set("name", "item1")
item1.text = "This is item 1"

tree = ET.ElementTree(data)
tree.write("data.xml")

# Reading XML data
tree = ET.parse("data.xml")
root = tree.getroot()

for item in root:
    print(item.tag, item.attrib, item.text)
```

### 4. Setting Up Your Local Development Environment

To set up your local Python development environment, follow these steps:

1. **Install Python**: Download and install Python from the official [Python website](https://www.python.org/downloads/).

2. **Install an IDE or Text Editor**: Popular choices include [Visual Studio Code](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/), and [Sublime Text](https://www.sublimetext.com/).

3. **Install Required Packages**: Use Python's package manager, pip, to install packages. For example, to install the `requests` package, run:
   ```bash
   pip install requests
   ```

4. **Verify Installation**: Open your IDE or text editor and run a simple Python script to verify the installation.

```python
print("Python setup is successful!")
```

## An Intermediate Guide

### Intermediate's Introduction

Welcome to the intermediate guide for Python data analytics! This guide will cover essential tools and techniques such as DataFrame operations, Pandas, NumPy, Matplotlib basics, and data extraction from databases. By the end, you will be able to perform data manipulation, export data to CSV, create basic visualizations, and extract data from databases.

### 1. DataFrame and Pandas

#### DataFrame

A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes.

```python
import pandas as pd

# Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print(df)
```

#### Pandas Library

Pandas is a powerful data manipulation and analysis library.

```python
# Basic Operations with Pandas
print(df.head())  # Display the first few rows
print(df.describe())  # Summary statistics

# Aggregations
print(df.groupby("City")['Age'].mean())
```

### 2. NumPy Library

NumPy is the fundamental package for scientific computing in Python.

```python
import numpy as np

# Creating a NumPy array
array = np.array([1, 2, 3, 4, 5])
print(array)

# Basic Operations with NumPy
print(np.mean(array))  # Mean
print(np.sum(array))   # Sum
print(np.max(array))   # Max
```

### 3. Basics of Matplotlib

Matplotlib is a plotting library for creating static, animated, and interactive visualizations.

```python
import matplotlib.pyplot as plt

# Basic Plot
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Basic Line Plot')
plt.savefig("plot.png")
# plt.show()
```

### 4. Mutable and Immutable Types

Understanding mutable and immutable types is crucial for data manipulation.

```python
# Immutable type: tuple
immutable_tuple = (1, 2, 3)
# immutable_tuple[0] = 4  # This will raise an error

# Mutable type: list
mutable_list = [1, 2, 3]
mutable_list[0] = 4  # This will work
print(mutable_list)
```

### 5. Basic Operations with Pandas/NumPy

#### Using Pandas

```python
# Adding a new column
df["Salary"] = [50000, 60000, 70000]

# Filtering rows
filtered_df = df[df["Age"] > 28]
print(filtered_df)
```

#### Using NumPy

```python
# Element-wise operations
array2 = np.array([5, 4, 3, 2, 1])
print(array + array2)  # Addition
print(array * array2)  # Multiplication
```

### 6. Export DataFrame to CSV

Exporting data to CSV format is straightforward with Pandas.

```python
# Exporting DataFrame to CSV
df.to_csv("output.csv", index=False)
```

### 7. Build Basic Visualizations

Creating basic visualizations helps in data analysis and presentation.

```python
# Bar Plot
df["Age"].plot(kind="bar")
plt.xlabel('Index')
plt.ylabel('Age')
plt.title('Bar Plot of Ages')
plt.savefig("Bar_Plot_of_Ages.png")
# plt.show()

# Scatter Plot
plt.scatter(df["Age"], df["Salary"])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Scatter Plot of Age vs Salary')
plt.savefig("Scatter_Plot_of_Age_vs_Salary.png")
# plt.show()
```

### 8. Extract Data from Databases

Extracting data from databases typically involves using SQL queries with libraries like `sqlite3` for SQLite databases.

```python
import sqlite3

# Connecting to the database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Creating a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Inserting data
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 30)")
conn.commit()

# Querying data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Closing the connection
conn.close()
```

## An Advanced Guide

### Advanced's Introduction

Welcome to the advanced guide for Python data analytics! This guide will cover advanced Python features such as lambda functions, iterators, comprehensions, logging, and working with REST APIs. You will also learn advanced data operations with Pandas/NumPy, interacting with web services, building advanced visualizations, and best practices for refactoring Python code.

### 1. Advanced Python Features

#### Lambda Functions

Lambda functions are small anonymous functions defined with the `lambda` keyword.

```python
# Lambda Function Example
square = lambda x: x ** 2
print(square(5))  # Output: 25
```

#### Iterators

Iterators are objects that allow you to traverse through all the elements of a collection.

```python
# Iterator Example
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
```

#### Python Comprehensions

Comprehensions provide a concise way to create lists, dictionaries, and sets.

```python
# List Comprehension
squares = [x ** 2 for x in range(10)]
print(squares)

# Dictionary Comprehension
square_dict = {x: x ** 2 for x in range(10)}
print(square_dict)
```

### 2. Logging

Logging is crucial for tracking events that happen when some software runs.

```python
import logging

# Configuring Logging
logging.basicConfig(level=logging.INFO)

# Using Logging
logging.info("This is an info message")
logging.error("This is an error message")
```

### 3. Working with REST API

Interacting with web services using REST APIs is a common task in data analytics.

```python
import requests

# Making a GET request
response = requests.get('https://api.example.com/data')
if response.status_code == 200:
    data = response.json()
    print(data)

# Making a POST request
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://api.example.com/submit', json=payload)
print(response.status_code)
```

### 4. Advanced Data Operations with Pandas/NumPy

#### Merge

Merging DataFrames allows you to combine data from multiple sources.

```python
import pandas as pd

# Creating DataFrames
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
})

df2 = pd.DataFrame({
    'A': ['A1', 'A2', 'A3'],
    'C': ['C1', 'C2', 'C3']
})

# Merging DataFrames
merged_df = pd.merge(df1, df2, on='A', how='inner')
print(merged_df)
```

#### Reshape

Reshaping data using functions like `pivot` and `melt`.

```python
# Creating a DataFrame
df = pd.DataFrame({
    'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
    'B': ['one', 'one', 'two', 'two', 'one', 'one'],
    'C': ['small', 'large', 'small', 'small', 'small', 'large'],
    'D': [1, 2, 2, 3, 3, 4]
})

# Pivot Table
pivot_df = df.pivot_table(values='D', index=['A', 'B'], columns=['C'], fill_value=0)
print(pivot_df)
```

#### Functions

Applying functions to DataFrames.

```python
# Defining a function
def add_ten(x):
    return x + 10

# Applying the function to a DataFrame column
df['D'] = df['D'].apply(add_ten)
print(df)
```

### 5. Advanced Visualizations in Python

Creating advanced visualizations helps in deeper data insights.

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data
tips = sns.load_dataset('tips')

# Advanced Visualization: Pair Plot
sns.pairplot(tips, hue='sex')
plt.show()

# Advanced Visualization: Heatmap
correlation_matrix = tips.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.show()
```

### 6. Best Practices and Refactoring Python Code

Following best practices and refactoring code improves readability, maintainability, and performance.

#### Best Practices

- **Write Readable Code**: Use meaningful variable names and comments.
- **Follow PEP 8**: Adhere to the Python style guide.
- **Modularize Code**: Break code into functions and classes.
- **Use Virtual Environments**: Isolate dependencies.

#### Refactoring Example

Original Code:

```python
data = [1, 2, 3, 4, 5]
result = []
for i in data:
    result.append(i * 2)
print(result)
```

Refactored Code:

```python
# Using List Comprehension
result = [i * 2 for i in data]
print(result)
```
