# Flask Levels

## Table of Contents

- [Flask Levels](#flask-levels)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
    - [Novice](#novice)
    - [Intermediate](#intermediate)
    - [Advanced](#advanced)
    - [Expert](#expert)
  - [Details](#details)
    - [Novice Level: Flask](#novice-level-flask)
      - [1. How to create a basic Flask application using routes and views](#1-how-to-create-a-basic-flask-application-using-routes-and-views)
      - [2. Understanding HTTP methods (GET, POST, PUT, DELETE) and how to implement them in Flask](#2-understanding-http-methods-get-post-put-delete-and-how-to-implement-them-in-flask)
      - [3. Using Flask's built-in templating engine to display data dynamically](#3-using-flasks-built-in-templating-engine-to-display-data-dynamically)
      - [4. Implementing basic form handling in Flask](#4-implementing-basic-form-handling-in-flask)
      - [5. Connecting Flask to a database using SQLAlchemy](#5-connecting-flask-to-a-database-using-sqlalchemy)
      - [6. Understanding how to debug Flask applications using error handling and logging](#6-understanding-how-to-debug-flask-applications-using-error-handling-and-logging)
    - [Intermediate Level: Flask](#intermediate-level-flask)
      - [1. Basic Understanding of Request/Response Cycles in Web Applications](#1-basic-understanding-of-requestresponse-cycles-in-web-applications)
      - [2. Familiarity with Flask Extensions and How to Use Them](#2-familiarity-with-flask-extensions-and-how-to-use-them)
      - [3. Ability to Use Flask's Built-In Templating Engine for Rendering HTML](#3-ability-to-use-flasks-built-in-templating-engine-for-rendering-html)
      - [4. Understanding of How to Interact with a Database Using Flask's ORM (SQLAlchemy)](#4-understanding-of-how-to-interact-with-a-database-using-flasks-orm-sqlalchemy)
      - [5. Knowledge of Authentication and Security Considerations in Flask Applications](#5-knowledge-of-authentication-and-security-considerations-in-flask-applications)
      - [6. Understanding of Flask's Routing System and Ability to Define Complex Routes](#6-understanding-of-flasks-routing-system-and-ability-to-define-complex-routes)
    - [Advanced Level: Flask](#advanced-level-flask)
      - [1. Advanced Knowledge of Flask's Application Context and Request Context](#1-advanced-knowledge-of-flasks-application-context-and-request-context)
      - [2. Ability to Implement and Configure Flask Extensions to Optimize Performance and Add Additional Functionality](#2-ability-to-implement-and-configure-flask-extensions-to-optimize-performance-and-add-additional-functionality)
      - [3. Understanding of How to Use Flask's Blueprints to Design Scalable Applications](#3-understanding-of-how-to-use-flasks-blueprints-to-design-scalable-applications)
      - [4. Expertise in Integrating Flask with Other Technologies and Platforms](#4-expertise-in-integrating-flask-with-other-technologies-and-platforms)
      - [5. Mastery of Flask's Jinja2 Templating Engine](#5-mastery-of-flasks-jinja2-templating-engine)
      - [6. Strong Knowledge of Security Best Practices and How to Implement Them in Flask Applications](#6-strong-knowledge-of-security-best-practices-and-how-to-implement-them-in-flask-applications)
    - [Expert Level: Flask](#expert-level-flask)
      - [1. Advanced Use of Flask Extensions and Plugins](#1-advanced-use-of-flask-extensions-and-plugins)
      - [2. Mastery of Flask Blueprints and Their Application in Larger Projects](#2-mastery-of-flask-blueprints-and-their-application-in-larger-projects)
      - [3. Expertise in Creating Custom Flask Decorators and Error Handlers](#3-expertise-in-creating-custom-flask-decorators-and-error-handlers)
      - [4. In-Depth Knowledge of Flask's Request Handling and Response Generation Processes](#4-in-depth-knowledge-of-flasks-request-handling-and-response-generation-processes)
      - [5. Advanced Flask Security Implementations, Including Authentication and Authorization](#5-advanced-flask-security-implementations-including-authentication-and-authorization)
      - [6. Experience Integrating Flask with Other Technologies, Such as Frontend Frameworks and Databases](#6-experience-integrating-flask-with-other-technologies-such-as-frontend-frameworks-and-databases)

## Overview

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require
particular tools or libraries. It has no database abstraction layer, form validation, or any other components where
pre-existing third-party libraries provide common functions.

However, Flask supports extensions that can add application features as if they were implemented in Flask itself.
Extensions exist for object-relational mappers, form validation, upload handling, various open authentication
technologies and several common framework related tools.

Before, please practice the [Flask slides of Code Maven](https://code-maven.com/slides/python/flask).

### Novice

- How to create a basic Flask application using routes and views
- Understanding HTTP methods (GET, POST, PUT, DELETE) and how to implement them in Flask
- Using Flask's built-in templating engine to display data dynamically
- Implementing basic form handling in Flask
- Connecting Flask to a database using SQLAlchemy
- Understanding how to debug Flask applications using error handling and logging.

### Intermediate

- Basic understanding of request/response cycles in web applications.
- Familiarity with Flask extensions and how to use them.
- Ability to use Flask's built-in templating engine for rendering HTML.
- Understanding of how to interact with a database using Flask's ORM or SQL Alchemy.
- Knowledge of authentication and security considerations in Flask applications.
- Understanding of Flask's routing system and ability to define complex routes.

### Advanced

- Advanced knowledge of Flask's application context and request context.
- Ability to implement and configure Flask extensions to optimize performance and add additional functionality.
- Understanding of how to use Flask's blueprints to design scalable applications.
- Expertise in integrating Flask with other technologies and platforms such as Flask-SQLAlchemy and Flask-RESTful.
- Mastery of Flask's Jinja2 templating engine to create dynamic web pages with ease.
- Strong knowledge of security best practices and understanding of how to implement them in Flask applications.

### Expert

- Advanced use of Flask extensions and plugins
- Mastery of Flask Blueprints and their application in larger projects
- Expertise in creating custom Flask decorators and error handlers
- In-depth knowledge of Flask's request handling and response generation processes
- Advanced Flask security implementations, including authentication and authorization
- Experience integrating Flask with other technologies, such as frontend frameworks and databases

## Details

### Novice Level: Flask

#### 1. How to create a basic Flask application using routes and views

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

#### 2. Understanding HTTP methods (GET, POST, PUT, DELETE) and how to implement them in Flask

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/get_example', methods=['GET'])
def get_example():
    return "This is a GET request"

@app.route('/post_example', methods=['POST'])
def post_example():
    data = request.form['data']
    return f"Received POST request with data: {data}"

@app.route('/put_example', methods=['PUT'])
def put_example():
    data = request.form['data']
    return f"Received PUT request with data: {data}"

@app.route('/delete_example', methods=['DELETE'])
def delete_example():
    return "This is a DELETE request"

if __name__ == '__main__':
    app.run(debug=True)
```

#### 3. Using Flask's built-in templating engine to display data dynamically

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name='Flask')

if __name__ == '__main__':
    app.run(debug=True)
```

**index.html**:

```html
<!doctype html>
<html>
<head>
    <title>Flask Template</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```

#### 4. Implementing basic form handling in Flask

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
```

**form.html**:

```html
<!doctype html>
<html>
<head>
    <title>Form Handling</title>
</head>
<body>
    <form action="/submit" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

#### 5. Connecting Flask to a database using SQLAlchemy

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.route('/')
def home():
    user = User.query.first()
    return f"Hello, {user.name}!" if user else "No users found"

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

#### 6. Understanding how to debug Flask applications using error handling and logging

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    try:
        return 1 / 0  # Intentional error
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return render_template('error.html', error=e)

if __name__ == '__main__':
    app.run(debug=True)
```

**error.html**:

```html
<!doctype html>
<html>
<head>
    <title>Error</title>
</head>
<body>
    <h1>An error occurred: {{ error }}</h1>
</body>
</html>
```

### Intermediate Level: Flask

#### 1. Basic Understanding of Request/Response Cycles in Web Applications

Understanding the request/response cycle is fundamental. When a client sends a request to the server, Flask handles the request and sends back a response.

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify(message=f"Hello, {name}!")

if __name__ == '__main__':
    app.run(debug=True)
```

In this example:

- The client sends a GET request to `/greet`.
- The server processes the request, retrieves the `name` parameter, and responds with a JSON message.

#### 2. Familiarity with Flask Extensions and How to Use Them

Flask extensions add functionality to the Flask framework. Here, we'll use Flask-Mail to send emails.

```python
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your@example.com'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/send_mail')
def send_mail():
    msg = Message('Hello', sender='your@example.com', recipients=['to@example.com'])
    msg.body = "This is a test email sent from a Flask application."
    mail.send(msg)
    return "Mail sent!"

if __name__ == '__main__':
    app.run(debug=True)
```

#### 3. Ability to Use Flask's Built-In Templating Engine for Rendering HTML

Using Flask's built-in templating engine (Jinja2) to render HTML pages dynamically.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Home Page')

if __name__ == '__main__':
    app.run(debug=True)
```

**index.html**:

```html
<!doctype html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>Welcome to the {{ title }}</h1>
</body>
</html>
```

#### 4. Understanding of How to Interact with a Database Using Flask's ORM (SQLAlchemy)

Using SQLAlchemy to interact with a database.

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.route('/')
def home():
    users = User.query.all()
    return f"Number of users: {len(users)}"

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

#### 5. Knowledge of Authentication and Security Considerations in Flask Applications

Implementing basic authentication using Flask-Login.

```python
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'mysecret'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return f'Hello, {current_user.username}!'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

**login.html**:

```html
<!doctype html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <form method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

#### 6. Understanding of Flask's Routing System and Ability to Define Complex Routes

Defining complex routes with variables and methods.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {subpath}'

if __name__ == '__main__':
    app.run(debug=True)
```

### Advanced Level: Flask

#### 1. Advanced Knowledge of Flask's Application Context and Request Context

Understanding the difference between application context and request context, and how to use them effectively.

```python
from flask import Flask, g, request

app = Flask(__name__)

@app.before_request
def before_request():
    g.user = 'admin'  # Set a global variable for the request

@app.route('/')
def index():
    return f"Hello, {g.user}! This request is from {request.remote_addr}"

if __name__ == '__main__':
    with app.app_context():
        # Application context: global app setup
        print("Application context setup complete")

    app.run(debug=True)
```

#### 2. Ability to Implement and Configure Flask Extensions to Optimize Performance and Add Additional Functionality

Using Flask-Caching to improve performance with caching.

```python
from flask import Flask
from flask_caching import Cache

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)

@app.route('/')
@cache.cached(timeout=60)
def index():
    return "This is a cached response."

if __name__ == '__main__':
    app.run(debug=True)
```

#### 3. Understanding of How to Use Flask's Blueprints to Design Scalable Applications

Organizing a Flask application with Blueprints for modular design.

```python
from flask import Flask, Blueprint, render_template

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@auth.route('/login')
def login():
    return render_template('login.html')

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(auth, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
```

#### 4. Expertise in Integrating Flask with Other Technologies and Platforms

Creating a RESTful API with Flask-RESTful and integrating with Flask-SQLAlchemy.

```python
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
api = Api(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {'id': user.id, 'name': user.name}

    def post(self):
        data = request.get_json()
        new_user = User(name=data['name'])
        db.session.add(new_user)
        db.session.commit()
        return {'id': new_user.id, 'name': new_user.name}, 201

api.add_resource(UserResource, '/user/<int:user_id>', '/user')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

#### 5. Mastery of Flask's Jinja2 Templating Engine

Using advanced features of Jinja2 to create dynamic and reusable templates.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
```

**index.html**:

```html
<!doctype html>
<html>
<head>
    <title>User List</title>
</head>
<body>
    <h1>User List</h1>
    <ul>
    {% for user in users %}
        <li>{{ user.name }} - {{ user.age }} years old</li>
    {% endfor %}
    </ul>
</body>
</html>
```

#### 6. Strong Knowledge of Security Best Practices and How to Implement Them in Flask Applications

Implementing security best practices like CSRF protection and secure password storage.

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'mysecret'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
csrf = CSRFProtect(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route('/')
def index():
    return "Welcome to the secure Flask application!"

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

**register.html**:

```html
<!doctype html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <form method="post">
        {{ form.hidden_tag() }}
        <p>
            {{ form.username.label }}<br>
            {{ form.username(size=32) }}
        </p>
        <p>
            {{ form.password.label }}<br>
            {{ form.password(size=32) }}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
</body>
</html>
```

### Expert Level: Flask

#### 1. Advanced Use of Flask Extensions and Plugins

Leveraging advanced features of Flask extensions, such as Flask-Migrate for database migrations.

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)

if __name__ == '__main__':
    app.run(debug=True)
```

**Command Line:**

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

#### 2. Mastery of Flask Blueprints and Their Application in Larger Projects

Using Blueprints to organize a large Flask application.

```python
from flask import Flask, Blueprint, render_template

main = Blueprint('main', __name__)
admin = Blueprint('admin', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@admin.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(admin, url_prefix='/admin')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
```

#### 3. Expertise in Creating Custom Flask Decorators and Error Handlers

Creating a custom decorator and an error handler.

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

def require_apikey(view_function):
    def decorated_function(*args, **kwargs):
        if request.args.get('apikey') == 'mysecretapikey':
            return view_function(*args, **kwargs)
        else:
            return jsonify({"error": "Unauthorized access"}), 401
    return decorated_function

@app.route('/secure-data')
@require_apikey
def secure_data():
    return jsonify({"data": "This is secured data."})

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

#### 4. In-Depth Knowledge of Flask's Request Handling and Response Generation Processes

Customizing request handling and response generation.

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.before_request
def before_request():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

@app.after_request
def after_request(response):
    response.headers['X-Custom-Header'] = 'CustomValue'
    return response

@app.route('/data', methods=['POST'])
def data():
    data = request.get_json()
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)
```

#### 5. Advanced Flask Security Implementations, Including Authentication and Authorization

Implementing JWT authentication and role-based authorization.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import jwt
from functools import wraps
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'supersecretkey'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='user')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({"message": "Token is missing!"}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query.filter_by(username=data['username']).first()
        except:
            return jsonify({"message": "Token is invalid!"}), 403
        return f(current_user, *args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    @token_required
    def decorated(current_user, *args, **kwargs):
        if current_user.role != 'admin':
            return jsonify({"message": "Admin access required!"}), 403
        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        token = jwt.encode({
            'username': user.username,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    return jsonify({"message": "Invalid credentials!"}), 401

@app.route('/admin', methods=['GET'])
@admin_required
def admin_page(current_user):
    return jsonify({"message": f"Welcome, admin {current_user.username}!"})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

#### 6. Experience Integrating Flask with Other Technologies, Such as Frontend Frameworks and Databases

Integrating Flask with React for a full-stack application.

**Backend (Flask):**

```python
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data')
def get_data():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True)
```

**Frontend (React):**

```javascript
import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/data')
      .then(response => response.json())
      .then(data => setData(data.message));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>{data ? data : "Loading..."}</p>
      </header>
    </div>
  );
}

export default App;
```

**package.json (for React):**

```json
{
  "name": "frontend",
  "version": "1.0.0",
  "main": "index.js",
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-scripts": "4.0.3"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "proxy": "http://127.0.0.1:5000"
}
```
