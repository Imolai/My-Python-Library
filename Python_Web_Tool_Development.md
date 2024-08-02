# Tool development with Python.Web

## Table of Contents

- [Tool development with Python.Web](#tool-development-with-pythonweb)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Tool Development's Tech Stack](#tool-developments-tech-stack)
  - [Flask](#flask)
    - [Key Concepts](#key-concepts)
      - [1. Setting Up Flask](#1-setting-up-flask)
      - [2. Creating a Simple Flask Application](#2-creating-a-simple-flask-application)
      - [3. URL Routing](#3-url-routing)
      - [4. HTTP Methods](#4-http-methods)
      - [5. Templates](#5-templates)
      - [6. Static Files](#6-static-files)
      - [7. Form Handling](#7-form-handling)
      - [8. Redirects and Errors](#8-redirects-and-errors)
      - [9. Sessions](#9-sessions)
      - [10. Extending Flask by SQLAlchemy](#10-extending-flask-by-sqlalchemy)
        - [SQLObject](#sqlobject)
      - [11. Extending Flask by Flask-Security](#11-extending-flask-by-flask-security)
        - [Step 1: Install Required Packages](#step-1-install-required-packages)
        - [Step 2: Set Up Your Flask Application](#step-2-set-up-your-flask-application)
        - [Step 3: Create Templates](#step-3-create-templates)
        - [Step 4: Configure Email Settings (Optional)](#step-4-configure-email-settings-optional)
        - [Step 5: Create Initial Users and Roles](#step-5-create-initial-users-and-roles)
        - [Step 6: Restrict Access with Roles](#step-6-restrict-access-with-roles)
        - [Step 7: Run the Application](#step-7-run-the-application)
      - [Flask-Security Conclusion](#flask-security-conclusion)
    - [Common Patterns and Best Practices](#common-patterns-and-best-practices)
      - [Application Factory](#application-factory)
      - [Blueprints](#blueprints)
      - [Configuration Management](#configuration-management)
      - [Error Handling](#error-handling)
      - [Logging](#logging)
    - [Flask Conclusion](#flask-conclusion)
  - [Security](#security)
    - [`Flask` Security Headers Setup](#flask-security-headers-setup)
    - [`requests` Managing Security Headers](#requests-managing-security-headers)
    - [Security Summary](#security-summary)
  - [Jinja2](#jinja2)
    - [Jinja Basics](#jinja-basics)
      - [Basic Templating Example](#basic-templating-example)
      - [Additional Jinja Features](#additional-jinja-features)
    - [Jinja Conclusion](#jinja-conclusion)
  - [JavaScript](#javascript)
    - [Introduction to JavaScript](#introduction-to-javascript)
    - [Core Concepts](#core-concepts)
    - [Enhancing User Interactions with JavaScript](#enhancing-user-interactions-with-javascript)
    - [Integration with Flask](#integration-with-flask)
    - [JavaScript Conclusion](#javascript-conclusion)
  - [SQLite](#sqlite)
    - [Introduction to SQLite](#introduction-to-sqlite)
      - [1. Understanding SQLite's Basic Syntax and Commands](#1-understanding-sqlites-basic-syntax-and-commands)
      - [2. Managing Indexes and Constraints](#2-managing-indexes-and-constraints)
      - [3. Backing Up and Restoring SQLite Databases](#3-backing-up-and-restoring-sqlite-databases)
      - [4. Intermediate Level Concepts](#4-intermediate-level-concepts)
    - [SQLite in Python](#sqlite-in-python)
      - [1. Connecting to a Database](#1-connecting-to-a-database)
      - [2. Creating Tables](#2-creating-tables)
      - [3. Inserting (Create) Data](#3-inserting-create-data)
      - [4. Retrieving (Read) Data](#4-retrieving-read-data)
      - [5. Updating Data](#5-updating-data)
      - [6. Deleting Data](#6-deleting-data)
      - [7. Using Context Managers](#7-using-context-managers)
      - [8. Managing Transactions](#8-managing-transactions)
      - [9. Best Practices](#9-best-practices)
    - [Using SQLite in a Flask Application](#using-sqlite-in-a-flask-application)
      - [1. Setting Up Flask and SQLite](#1-setting-up-flask-and-sqlite)
      - [2. Creating a Simple Model](#2-creating-a-simple-model)
      - [3. CRUD Operations in Flask](#3-crud-operations-in-flask)
      - [4. Running the Flask Application](#4-running-the-flask-application)
    - [SQLite Conclusion](#sqlite-conclusion)
  - [Jira](#jira)
    - [Introduction to Python Jira Basics](#introduction-to-python-jira-basics)
    - [Installing the JIRA Module](#installing-the-jira-module)
    - [Basic Usage](#basic-usage)
    - [Jira Conclusion](#jira-conclusion)

## Introduction

This is not a generic Python Web description, but a specific one around a specific topic.
I created this doc for my preparation for a job, which was a Tool Development with Python.Web.

## Tool Development's Tech Stack

- Python for backend development, [Flask](#flask)
- Jinja for templating, [Jinja2](#jinja2)
- JavaScript for frontend interactions, [JavaScript](#javascript)
- SQLite for database management, [SQLite](#sqlite)
- Integration with JIRA for ticket creation and email notifications for issues founds, [Jira](#jira)
- Standard FOSS libraries such as requests, Flask, sqlobject, PyTorch/fasta
- Detect security misconfigurations, secrets embedded in JS code, IPs hosting admin consoles,
  and those returning 404s/503s, [Security](#security)

## Flask

Flask is a lightweight web framework for Python, known for its simplicity and flexibility.
It allows developers to build web applications quickly and with minimal overhead.
Flask is often chosen for its modular design and the ability to scale applications as needed.

### Key Concepts

#### 1. Setting Up Flask

To get started with Flask, you first need to install it:

```bash
pip install Flask
```

#### 2. Creating a Simple Flask Application

The following example in `flask_app_hello.py` demonstrates how to create a basic Flask application:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask World!'

if __name__ == '__main__':
    app.run(debug=True)
```

In this code:

- `Flask(__name__)` creates a Flask application instance.
- `@app.route('/')` defines a route for the root URL.
- `hello_world()` is a view function that returns a simple string.

If you start it, it will show on the console:

```console
$ chmod +x flask_app_hello.py.py
$ ./flask_app_hello.py
 * Serving Flask app 'flask_app_hello'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 234-567-891
```

And you can open in your browser the URL: <http://127.0.0.1:5000/>, where the *"Hello, Flask World!"* text will be displayed.

> For production deployment of a Flask application, you should use a production **WSGI** server instead of the built-in development server. Common WSGI servers include **[Gunicorn](https://gunicorn.org/)** and **[uWSGI](https://uwsgi-docs.readthedocs.io/)** *(full list is in [Deploying to Production](https://flask.palletsprojects.com/en/latest/deploying/))*. Additionally, you can use a reverse proxy like **Nginx** or **Apache** to serve your application.

To start an application, e.g. named "[flaskr](https://flask.palletsprojects.com/en/latest/tutorial/factory/#id1)" by Flask:

```bash
$ flask --app flaskr run --debug
```

Visit <http://127.0.0.1:5000/hello> in a browser and you should see the "Hello, World!" message.

> Follow the **[Flask Tutorial](https://flask.palletsprojects.com/en/latest/tutorial/)** for further steps.

#### 3. URL Routing

Flask uses decorators to bind URLs to functions:

```python
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'
```

In this example, `<username>` is a variable part of the URL, which is passed to the view function as an argument.

#### 4. HTTP Methods

Flask supports different HTTP methods (GET, POST, etc.):

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Processing login'
    else:
        return 'Login page'
```

This code allows the `/login` route to handle both GET and POST requests.

#### 5. Templates

Flask integrates with the **Jinja2** templating engine to separate HTML from Python code:

```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
```

And the corresponding `hello.html` template:

```html
<!doctype html>
<html>
  <head><title>Hello</title></head>
  <body>
    <h1>Hello, {{ name }}!</h1>
  </body>
</html>
```

In this setup, `render_template` renders an HTML file with the given context.

#### 6. Static Files

Flask serves static files from the `static` folder:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

This line in an HTML template includes a CSS file from the `static` directory.

#### 7. Form Handling

To handle form data, Flask uses the `request` object:

```python
from flask import request

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    return f'Submitted: {username}'
```

In this example, form data is accessed using `request.form`.

#### 8. Redirects and Errors

Flask provides utilities for redirects and error handling:

```python
from flask import redirect, url_for, abort

@app.route('/redirect_me')
def redirect_me():
    return redirect(url_for('hello_world'))

@app.route('/not_found')
def not_found():
    abort(404)
```

Here, `redirect` and `url_for` handle URL redirection, and `abort` generates HTTP errors.

#### 9. Sessions

Flask supports server-side sessions:

```python
from flask import session

@app.route('/set_session')
def set_session():
    session['username'] = 'admin'
    return 'Session set'

@app.route('/get_session')
def get_session():
    username = session.get('username', 'Guest')
    return f'Logged in as {username}'
```

Sessions are used to store data across requests.

#### 10. Extending Flask by SQLAlchemy

Flask can be extended with various libraries for database interaction, authentication, etc., like **`Flask-SQLAlchemy`**.

Flask extensions are usually named *"Flask-Foo"* or *"Foo-Flask"*. You can search **[PyPI](https://pypi.org)** for packages tagged with **[Framework::Flask](https://pypi.org/search/?c=Framework+%3A%3A+Flask)**.

**Flask-SQLAlchemy** is an extension for Flask that adds support for **SQLAlchemy** to your application. It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks.

**Flask-SQLAlchemy** is a popular **Object Relational Manager** (**ORM**) for providing an object interface to your database.
**SQLAlchemy** integrates well with other **Flask** extensions and libraries, such as **Flask-Migrate** for database migrations and **Flask-Security** for user authentication and role management.

To get started with **Flask-SQLAlchemy**, you first need to install it:

```bash
pip install Flask-SQLAlchemy
```

After, the code:

```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
```

In this example, SQLAlchemy is used for the **ORM** functionality. Theoretically, we could use **SQLObject** too.

##### SQLObject

> While **SQLObject** is also an **ORM** for Python and can be used with Flask, it does not have the same level of integration, community support, or ecosystem compatibility as SQLAlchemy.
*SQLObject is less commonly used in modern Flask applications*, which means fewer resources and examples are available for developers.

#### 11. Extending Flask by Flask-Security

##### Step 1: Install Required Packages

First, you need to install Flask-Security and its dependencies:

```bash
pip install Flask Flask-SQLAlchemy Flask-Security-Too
```

##### Step 2: Set Up Your Flask Application

Create a basic Flask application and configure it to use Flask-SQLAlchemy and Flask-Security.

```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECURITY_PASSWORD_SALT'] = 'my_precious_two'

db = SQLAlchemy(app)

# Define models
roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.route('/')
@login_required
def home():
    return render_template('index.html')

if __name__ == '__main__':
    db.create_all()
    app.run()
```

##### Step 3: Create Templates

Create basic HTML templates for login and home pages.

**templates/index.html**

```html
<!doctype html>
<html>
  <head><title>Home</title></head>
  <body>
    <h1>Welcome!</h1>
    <p>You are logged in.</p>
    <a href="{{ url_for('security.logout') }}">Logout</a>
  </body>
</html>
```

**templates/security/login_user.html**

Flask-Security will look for specific templates in the `security` directory. You can customize the default templates as needed. Here is a simple example for the login form:

```html
<!doctype html>
<html>
  <head><title>Login</title></head>
  <body>
    <h1>Login</h1>
    <form action="{{ url_for('security.login') }}" method="POST">
      {{ render_field_with_errors(form.email) }}
      {{ render_field_with_errors(form.password) }}
      {{ render_field_with_errors(form.remember) }}
      {{ render_field_with_errors(form.next) }}
      {{ form.hidden_tag() }}
      <input type="submit" value="Login"/>
    </form>
  </body>
</html>
```

##### Step 4: Configure Email Settings (Optional)

If you want to use Flask-Security's features like email confirmation, password reset, etc., configure your email settings in `app.config`:

```python
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-password'
app.config['SECURITY_EMAIL_SENDER'] = 'your-email@example.com'
```

##### Step 5: Create Initial Users and Roles

You can create initial users and roles by adding some script to initialize the database:

```python
@app.before_first_request
def create_user():
    db.create_all()
    if not user_datastore.find_user(email='admin@example.com'):
        user_datastore.create_user(email='admin@example.com', password='password')
    db.session.commit()
```

##### Step 6: Restrict Access with Roles

You can restrict access to certain routes based on roles:

```python
from flask_security import roles_required

@app.route('/admin')
@roles_required('admin')
def admin():
    return 'Admin Page'
```

##### Step 7: Run the Application

Finally, run your Flask application:

```bash
python app.py
```

#### Flask-Security Conclusion

Using **Flask-Security**, you can quickly set up a robust user authentication and role management system. It provides many features out of the box and integrates seamlessly with Flask-SQLAlchemy, making it a powerful tool for managing user sessions and permissions in your Flask applications.

### Common Patterns and Best Practices

#### Application Factory

Using an application factory is a best practice to create a Flask application:

```python
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)

    return app
```

This pattern improves the modularity and testing of your application.

#### Blueprints

Blueprints allow you to organize your application into modules:

```python
from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return 'Main Index'
```

Registering the blueprint in the application:

```python
app.register_blueprint(bp)
```

#### Configuration Management

Using different configuration settings for different environments:

```python
class Config:
    SECRET_KEY = 'your_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

app.config.from_object('config.DevelopmentConfig')
```

#### Error Handling

Centralized error handling improves maintainability:

```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
```

#### Logging

Setting up logging for better debugging and monitoring:

```python
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
```

### Flask Conclusion

Flask's minimalistic approach allows developers to create robust web applications while providing the flexibility to integrate with various tools and libraries as needed. Its simplicity, combined with powerful extensions, makes it a popular choice for web development in Python.

## Security

Security of web applications, especially in relation to HTTP Strict Transport Security (HSTS), Content Security Policy (CSP) and other security headers.
In short:

1. **HSTS (HTTP Strict Transport Security)**:
   - This is a security header for web applications that tells browsers to always use only the HTTPS protocol to connect to a given website, thus preventing man-in-the-middle attacks and protocol downgrade attacks.
   - Example header setting: `Strict-Transport-Security: max-age=31536000; includeSubDomains`

2. **CSP (Content Security Policy)**:
   - This is a security mechanism that helps prevent XSS (Cross-Site Scripting) and other code injection attacks by specifying which sources are allowed to load and run content from.
   - Example header setting: `Content-Security-Policy: default-src 'self'; script-src 'self' 'https://trusted.cdn.com';`

3. **Other security headers**:
   - **X-Content-Type-Options**: Prevents the browser from automatically guessing the content type, thus reducing the chance of MIME type attacks. Example: `X-Content-Type-Options: nosniff`
   - **X-Frame-Options**: Prevents the web page from being displayed in an iframe, thus protecting against clickjacking attacks. Example: `X-Frame-Options: DENY`
   - **X-XSS-Protection**: activate the browser's built-in XSS protection. Example: `X-XSS-Protection: 1; mode=block`
   - **Referrer-Policy**: Controls how referrer information is forwarded. Example: `Referrer-Policy: no-referrer`

Knowing and using these headers will help to increase the security of web applications and prevent common attacks. It is worth familiarising yourself with each of them in detail so that you can apply appropriate security measures when developing and operating web applications.

### `Flask` Security Headers Setup

In the Flask application you can easily set up security headers. To do this, you should use the `Flask-Talisman` extension, which makes it easy to set HSTS, CSP and other security headers.

Installation:

```bash
pip install flask-talisman
```

Example application:

```python
from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
talisman = Talisman(app, 
                    content_security_policy={
                        'default-src': '\'self\',
                        'script-src': [
                            '\'self\'',
                            'https://trusted.cdn.com'
                        ]
                    })

@app.route('/')
def home():
    return "Hello, Secure World!"

if __name__ == '__main__':
    app.run()
```

In this example, `Flask-Talisman` takes care of setting HSTS, CSP and other security headers.

### `requests` Managing Security Headers

The `requests` directory is normally used to send HTTP requests in Python. While setting security headers is not particularly relevant when using `requests` (since these headers are set on the server side), it is important to understand how to manage responses and control headers.

Example of sending requests and checking headers:

```python
import requests

url = 'https://example.com'

response = requests.get(url)

# Check the security headers in the reply
print(response.headers.get('Strict-Transport-Security'))
print(response.headers.get('Content-Security-Policy'))
print(response.headers.get('X-Content-Type-Options'))
print(response.headers.get('X-Frame-Options'))
print(response.headers.get('X-XSS-Protection'))
print(response.headers.get('Referrer-Policy'))
```

This code sends a GET request to the specified URL and prints the security headers in the response.

### Security Summary

- In **Flask** applications, you can easily set up security headers with the `Flask-Talisman` extension.
- Using the **requests** directory, you can check the security headers in the response, which helps to make sure that the server is using the correct security headers.

These tools and methods will help ensure that your web applications developed in Python are secure.

## Jinja2

### Jinja Basics

Jinja is a powerful templating engine often used with the Flask framework for web application development. Here are some basic examples of how to use Jinja in a Flask application:

#### Basic Templating Example

1. **Installing Flask and Jinja**:
   Install the Flask framework, which comes with Jinja integrated.

   ```bash
   pip install Flask
   ```

2. **Creating a Flask Application**:
   Create a simple Flask application that uses Jinja templates.

   ```python
   from flask import Flask, render_template

   app = Flask(__name__)

   @app.route('/')
   def home():
       return render_template('index.html', title='Home Page', message='Hello, Jinja!')

   if __name__ == '__main__':
       app.run(debug=True)
   ```

3. **Creating a Jinja Template**:
   Create a template in the `index.html` file within the `templates` folder.

   ```html
   <!doctype html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>{{ title }}</title>
   </head>
   <body>
       <h1>{{ message }}</h1>
   </body>
   </html>
   ```

#### Additional Jinja Features

1. **Control Structures**:
   Jinja supports if-else structures, loops, and other control structures.

   ```html
   <ul>
   {% for item in items %}
       <li>{{ item }}</li>
   {% endfor %}
   </ul>
   ```

2. **Filters and Tests**:
   Jinja offers various filters and tests for manipulating variables.

   ```html
   <p>{{ my_string | upper }}</p>
   <p>{{ my_list | length }}</p>
   ```

3. **Macros**:
   You can use macros to increase the reusability of templates.

   ```html
   {% macro render_item(item) %}
       <li>{{ item }}</li>
   {% endmacro %}

   <ul>
   {% for item in items %}
       {{ render_item(item) }}
   {% endfor %}
   </ul>
   ```

### Jinja Conclusion

Using Jinja in Flask applications provides a powerful and flexible solution for templating needs. A thorough understanding of Jinja can significantly contribute to your success in development tasks and professional interviews.

To prepare, it's beneficial to explore Jinja's features and its integration in Flask applications through practice projects.

## JavaScript

### Introduction to JavaScript

JavaScript is a versatile, high-level, interpreted programming language primarily known for its role in web development, enabling dynamic content and interactive user experiences. Despite its inception as a simple scripting language for web pages, JavaScript has evolved into a powerful language for both frontend and backend development.

### Core Concepts

1. **Variables and Data Types**:
   JavaScript supports dynamic typing, meaning a variable can hold any type of data. Use `let` and `const` for block-scoped variables.

   ```javascript
   let name = "John"; // String
   const age = 30; // Number
   let isActive = true; // Boolean
   ```

2. **Functions**:
   Functions in JavaScript can be declared in multiple ways, including function declarations, function expressions, and arrow functions.

   ```javascript
   // Function Declaration
   function greet() {
       console.log("Hello, World!");
   }

   // Function Expression
   const greet = function() {
       console.log("Hello, World!");
   };

   // Arrow Function
   const greet = () => {
       console.log("Hello, World!");
   };
   ```

3. **Objects and Arrays**:
   Objects are collections of key-value pairs, while arrays are ordered lists of values.

   ```javascript
   // Object
   let person = {
       name: "John",
       age: 30,
       greet: function() {
           console.log("Hello, " + this.name);
       }
   };
   person.greet();

   // Array
   let numbers = [1, 2, 3, 4, 5];
   console.log(numbers[0]); // Output: 1
   ```

4. **Asynchronous Programming**:
   JavaScript handles asynchronous operations using callbacks, promises, and async/await syntax.

   ```javascript
   // Using Promises
   fetch('https://api.example.com/data')
       .then(response => response.json())
       .then(data => console.log(data))
       .catch(error => console.error('Error:', error));

   // Using async/await
   async function fetchData() {
       try {
           let response = await fetch('https://api.example.com/data');
           let data = await response.json();
           console.log(data);
       } catch (error) {
           console.error('Error:', error);
       }
   }
   fetchData();
   ```

5. **Event Handling**:
   JavaScript allows for event-driven programming through event listeners.

   ```javascript
   document.getElementById("myButton").addEventListener("click", function() {
       alert("Button was clicked!");
   });
   ```

6. **DOM Manipulation**:
   JavaScript can directly manipulate the Document Object Model (DOM) to dynamically update the content of a web page.

   ```javascript
   // Changing the content of an element
   document.getElementById("myDiv").innerHTML = "New Content";
   ```

7. **Modules**:
   JavaScript ES6 introduced modules, which allow you to split your code into separate files and import/export functionality as needed.

   ```javascript
   // Exporting a function from a module (math.js)
   export function add(a, b) {
       return a + b;
   }

   // Importing and using the function in another file
   import { add } from './math.js';
   console.log(add(2, 3)); // Output: 5
   ```

### Enhancing User Interactions with JavaScript

JavaScript is essential for creating interactive and dynamic web applications. Here are a few ways it enhances user interactions:

1. **Form Validation**:
   JavaScript can validate user input on the client side, providing immediate feedback without requiring a server round-trip.

   ```javascript
   document.getElementById("myForm").addEventListener("submit", function(event) {
       let email = document.getElementById("email").value;
       if (!validateEmail(email)) {
           alert("Invalid email address!");
           event.preventDefault();
       }
   });

   function validateEmail(email) {
       let re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
       return re.test(email);
   }
   ```

2. **Dynamic Content Loading**:
   JavaScript can fetch data from a server and update the web page content without reloading the entire page, enhancing the user experience.

   ```javascript
   document.getElementById("loadButton").addEventListener("click", function() {
       fetch('/api/data')
           .then(response => response.json())
           .then(data => {
               document.getElementById("content").innerHTML = data.content;
           })
           .catch(error => console.error('Error:', error));
   });
   ```

3. **Animations and Transitions**:
   JavaScript can create smooth animations and transitions to improve the visual appeal and interactivity of a web page.

   ```javascript
   document.getElementById("animateButton").addEventListener("click", function() {
       let box = document.getElementById("box");
       box.style.transition = "transform 2s";
       box.style.transform = "translateX(100px)";
   });
   ```

4. **Interactive Graphics**:
   Libraries like D3.js and Chart.js allow developers to create interactive data visualizations.

   ```javascript
   var ctx = document.getElementById('myChart').getContext('2d');
   var myChart = new Chart(ctx, {
       type: 'bar',
       data: {
           labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
           datasets: [{
               label: '# of Votes',
               data: [12, 19, 3, 5, 2, 3],
               backgroundColor: [
                   'rgba(255, 99, 132, 0.2)',
                   'rgba(54, 162, 235, 0.2)',
                   'rgba(255, 206, 86, 0.2)',
                   'rgba(75, 192, 192, 0.2)',
                   'rgba(153, 102, 255, 0.2)',
                   'rgba(255, 159, 64, 0.2)'
               ],
               borderColor: [
                   'rgba(255, 99, 132, 1)',
                   'rgba(54, 162, 235, 1)',
                   'rgba(255, 206, 86, 1)',
                   'rgba(75, 192, 192, 1)',
                   'rgba(153, 102, 255, 1)',
                   'rgba(255, 159, 64, 1)'
               ],
               borderWidth: 1
           }]
       },
       options: {
           scales: {
               y: {
                   beginAtZero: true
               }
           }
       }
   });
   ```

### Integration with Flask

In a Flask application, JavaScript often interacts with backend routes via AJAX or Fetch API for asynchronous data fetching. This integration enables a seamless user experience by dynamically updating parts of the web page without requiring a full page reload.

```javascript
// Example using Fetch API to interact with Flask backend
fetch('/api/data', {
    method: 'GET'
})
    .then(response => response.json())
    .then(data => {
        // Process the data
        console.log(data);
    })
    .catch(error => console.error('Error:', error));
```

### JavaScript Conclusion

JavaScript is a critical tool for modern web development, providing the interactivity and responsiveness that users expect from contemporary web applications. Its integration with a Python Flask backend, combined with its ability to handle asynchronous operations, event-driven programming, and modularity, makes it indispensable for creating robust, dynamic web applications. By mastering these fundamental concepts and practices, you will be well-prepared to tackle JavaScript-related questions in professional interviews and effectively leverage JavaScript in your projects.

## SQLite

### Introduction to SQLite

SQLite is a lightweight, self-contained, and serverless database engine. It is widely used in various applications for its simplicity and efficiency. This introduction covers the essential aspects of SQLite, aiming to provide a solid foundation for understanding and utilizing SQLite in professional environments. 

#### 1. Understanding SQLite's Basic Syntax and Commands

SQLite uses standard SQL syntax with some unique extensions. Below are basic commands and their usage:

- **Creating a Database and Table:**

```sql
-- Create a new SQLite database
sqlite3 my_database.db

-- Create a new table
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL
);
```

- **Inserting Data:**

```sql
INSERT INTO employees (name, position, salary) VALUES ('John Doe', 'Software Engineer', 75000);
```

- **Updating Data:**

```sql
UPDATE employees SET salary = 80000 WHERE name = 'John Doe';
```

- **Deleting Data:**

```sql
DELETE FROM employees WHERE name = 'John Doe';
```

- **Retrieving Data:**

```sql
SELECT * FROM employees;
SELECT name, salary FROM employees WHERE position = 'Software Engineer';
```

#### 2. Managing Indexes and Constraints

Indexes improve query performance, and constraints ensure data integrity.

- **Creating Indexes:**

```sql
CREATE INDEX idx_position ON employees (position);
```

- **Adding Constraints:**

```sql
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT UNIQUE NOT NULL
);
```

#### 3. Backing Up and Restoring SQLite Databases

- **Backup:**

```sql
.backup main backup_file.db
```

- **Restore:**

```sql
.restore main backup_file.db
```

#### 4. Intermediate Level Concepts

- **Understanding SQL Commands:**

Complex queries involve commands such as `SELECT`, `FROM`, `WHERE`, `GROUP BY`, and `ORDER BY`.

```sql
SELECT position, AVG(salary) FROM employees GROUP BY position ORDER BY AVG(salary) DESC;
```

- **SQLite Specific Features:**

SQLite supports dynamic typing and uses a small set of storage classes: `NULL`, `INTEGER`, `REAL`, `TEXT`, and `BLOB`.

```sql
-- Example of dynamic typing
INSERT INTO employees (name, position, salary) VALUES ('Alice', 'Manager', '85000'); -- Salary stored as TEXT
```

- **Creating Views, Triggers, and Indexes:**

```sql
-- Create a view
CREATE VIEW high_salaries AS SELECT name, salary FROM employees WHERE salary > 70000;

-- Create a trigger
CREATE TRIGGER update_salary AFTER UPDATE ON employees
BEGIN
    UPDATE employees SET salary = NEW.salary WHERE id = OLD.id;
END;
```

- **Writing Complex Queries and Subqueries:**

```sql
SELECT name, (SELECT dept_name FROM departments WHERE departments.dept_id = employees.dept_id) AS department
FROM employees;
```

- **Best Practices for Performance Optimization:**

  - Use indexes for frequently queried columns.
  - Normalize data to reduce redundancy.
  - Utilize `EXPLAIN` to analyze query performance.
  - Regularly back up and optimize databases using the `VACUUM` command.

### SQLite in Python

Python offers robust support for SQLite through the `sqlite3` module, which provides an easy way to interact with SQLite databases. This chapter will guide you through the fundamental operations for using SQLite in Python, enabling you to integrate database functionality into your Python applications seamlessly.

#### 1. Connecting to a Database

To start using SQLite in Python, you first need to connect to a database. If the database file does not exist, SQLite will create it.

```python
import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('my_database.db')

# Create a cursor object to interact with the database
cursor = connection.cursor()
```

#### 2. Creating Tables

Creating tables in SQLite using Python is straightforward. You can execute SQL commands using the cursor object.

```python
# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        salary REAL
    )
''')

# Commit the changes
connection.commit()
```

> Basic CRUD Operations: Create, Read, Update, Delete.

#### 3. Inserting (Create) Data

Inserting data into an SQLite table can be done using parameterized queries to prevent SQL injection.

```python
# Insert data into the table
cursor.execute('''
    INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)
''', ('John Doe', 'Software Engineer', 75000))

# Commit the changes
connection.commit()
```

#### 4. Retrieving (Read) Data

Retrieving data from an SQLite database involves executing a `SELECT` statement and fetching the results.

```python
# Retrieve data
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)
```

#### 5. Updating Data

Updating data in an SQLite table is similar to inserting data, using parameterized queries.

```python
# Update data
cursor.execute('''
    UPDATE employees SET salary = ? WHERE name = ?
''', (80000, 'John Doe'))

# Commit the changes
connection.commit()
```

#### 6. Deleting Data

Deleting data from an SQLite table follows the same pattern as other operations.

```python
# Delete data
cursor.execute('''
    DELETE FROM employees WHERE name = ?
''', ('John Doe',))

# Commit the changes
connection.commit()
```

#### 7. Using Context Managers

Using context managers (`with` statements) ensures that the database connection is properly closed after operations are complete, even if an error occurs.

```python
import sqlite3

# Use context manager to handle connection
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)
    ''', ('Alice', 'Manager', 85000))
    connection.commit()
```

#### 8. Managing Transactions

SQLite in Python supports transactions, ensuring that a series of operations either all succeed or all fail, maintaining database integrity.

```python
try:
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)
        ''', ('Bob', 'Developer', 70000))
        cursor.execute('''
            INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)
        ''', ('Eve', 'Analyst', 65000))
        connection.commit()
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
```

#### 9. Best Practices

- **Use parameterized queries** to prevent SQL injection.
- **Handle exceptions** to ensure the application can gracefully manage errors.
- **Commit changes** frequently to avoid data loss.
- **Close connections** using context managers to ensure resources are properly released.

### Using SQLite in a Flask Application

Flask is a lightweight web framework for Python. Integrating SQLite with Flask involves setting up the database, creating models, and handling requests.

#### 1. Setting Up Flask and SQLite

```python
from flask import Flask, g
import sqlite3

app = Flask(__name__)

DATABASE = 'my_database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
```

#### 2. Creating a Simple Model

```python
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# schema.sql
"""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL
);
"""
```

#### 3. CRUD Operations in Flask

```python
from flask import request, jsonify

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    name = data['name']
    position = data['position']
    salary = data['salary']
    db = get_db()
    db.execute('INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)', (name, position, salary))
    db.commit()
    return jsonify({'status': 'Employee added'}), 201

@app.route('/employees', methods=['GET'])
def get_all_employees():
    db = get_db()
    cursor = db.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    return jsonify(employees), 200

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()
    new_salary = data['salary']
    db = get_db()
    db.execute('UPDATE employees SET salary = ? WHERE id = ?', (new_salary, id))
    db.commit()
    return jsonify({'status': 'Employee updated'}), 200

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    db = get_db()
    db.execute('DELETE FROM employees WHERE id = ?', (id,))
    db.commit()
    return jsonify({'status': 'Employee deleted'}), 200
```

#### 4. Running the Flask Application

```python
if __name__ == '__main__':
    app.run(debug=True)
```

### SQLite Conclusion

By understanding these basics and intermediate concepts, you will be well-equipped to handle SQLite in professional settings, ensuring efficient and reliable database management.

By integrating SQLite with Python, you can build powerful applications that leverage the simplicity and efficiency of SQLite for data storage and management. This chapter provides a foundation for performing basic and intermediate database operations, setting the stage for more advanced uses of SQLite in your Python projects.

## Jira

### Introduction to Python Jira Basics

As an experienced software developer, integrating JIRA with Python can significantly enhance your ability to manage and automate project tasks. JIRA, a popular issue and project tracking tool, can be interfaced with Python using the `jira` Python module, which is part of the `atlassian-python-api`. This integration allows for automation of issue creation, updates, and querying, making project management more efficient.

### Installing the JIRA Module

First, ensure you have the `jira` module installed. You can install it using pip:

```bash
pip install jira
```

### Basic Usage

1. **Connecting to JIRA**:
   To interact with a JIRA instance, you need to establish a connection using your credentials.

   ```python
   from jira import JIRA

   # Replace with your JIRA server URL and credentials
   jira_server = 'https://your-jira-instance.atlassian.net'
   jira_user = 'your-email@example.com'
   jira_api_token = 'your-api-token'

   jira = JIRA(server=jira_server, basic_auth=(jira_user, jira_api_token))
   ```

2. **Creating an Issue**:
   You can create a new issue in a JIRA project programmatically.

   ```python
   issue_dict = {
       'project': {'key': 'PROJECTKEY'},
       'summary': 'New issue from jira-python',
       'description': 'Look into this new issue',
       'issuetype': {'name': 'Task'},
   }
   new_issue = jira.create_issue(fields=issue_dict)
   print(f"Issue {new_issue.key} created.")
   ```

3. **Searching for Issues**:
   You can search for issues using JQL (JIRA Query Language).

   ```python
   jql_str = 'project=PROJECTKEY AND status="To Do"'
   issues = jira.search_issues(jql_str)

   for issue in issues:
       print(f"{issue.key}: {issue.fields.summary}")
   ```

4. **Updating an Issue**:
   You can update an existing issue's fields.

   ```python
   issue = jira.issue('PROJECTKEY-123')
   issue.update(summary='Updated summary', description='Updated description')
   print(f"Issue {issue.key} updated.")
   ```

5. **Adding a Comment**:
   Adding comments to an issue can be done with a simple command.

   ```python
   issue = jira.issue('PROJECTKEY-123')
   jira.add_comment(issue, 'This is a comment from the Python JIRA module.')
   print(f"Comment added to issue {issue.key}.")
   ```

6. **Transitioning an Issue**:
   You can transition an issue from one status to another.

   ```python
   issue = jira.issue('PROJECTKEY-123')
   transitions = jira.transitions(issue)
   for t in transitions:
       print(f"Transition ID: {t['id']}, Name: {t['name']}")

   # Assuming transition ID 31 corresponds to the desired transition
   jira.transition_issue(issue, '31')
   print(f"Issue {issue.key} transitioned.")
   ```

### Jira Conclusion

Integrating JIRA with Python using the `jira` module can streamline your project management tasks, allowing for automation and efficient handling of issues. Understanding these basics will help you leverage the power of JIRA in your Python projects and demonstrate your proficiency during professional interviews.
