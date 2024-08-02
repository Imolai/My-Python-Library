# Python Design Patterns

## Contents

- [Python Design Patterns](#python-design-patterns)
  - [Contents](#contents)
  - [Foreword](#foreword)
  - [Patterns](#patterns)
    - [1. Abstract Factory](#1-abstract-factory)
    - [2. Builder](#2-builder)
    - [3. Factory Method](#3-factory-method)
    - [4. Prototype](#4-prototype)
    - [5. Singleton](#5-singleton)
    - [6. Adapter](#6-adapter)
    - [7. Bridge](#7-bridge)
    - [8. Composite](#8-composite)
    - [9. Decorator](#9-decorator)
    - [10. Facade](#10-facade)
    - [11. Flyweight](#11-flyweight)
    - [12. Proxy](#12-proxy)
    - [13. Chain of Responsibility](#13-chain-of-responsibility)
    - [14. Command](#14-command)
    - [15. Interpreter](#15-interpreter)
    - [16. Iterator](#16-iterator)
    - [17. Mediator](#17-mediator)
    - [18. Memento](#18-memento)
    - [19. Observer](#19-observer)
    - [20. State](#20-state)
    - [21. Strategy](#21-strategy)
    - [22. Template Method](#22-template-method)
    - [23. Visitor](#23-visitor)
  - [Further Readings](#further-readings)

## Foreword

Software architecture design patterns offer common solutions to frequently occurring software
development problems. These patterns help make the code flexible, reusable, and maintainable. Below
is a summary of the most common software architecture design patterns, each illustrated with
practical Python code examples.

Here is the comprehensive summary of software architecture design patterns in English, each with a
brief description and practical Python code examples.

## Patterns

### 1. Abstract Factory

**Name:** Abstract Factory

**Purpose:** To create families of related objects without specifying their concrete classes.

**Benefits:** Promotes dependency decoupling and code reusability.

**Use Cases:** When you need to create families of related objects.

```python
class Chair:
    def sit_on(self):
        raise NotImplementedError

class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian Chair"

class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a Modern Chair"

class Sofa:
    def lie_on(self):
        raise NotImplementedError

class VictorianSofa(Sofa):
    def lie_on(self):
        return "Lying on a Victorian Sofa"

class ModernSofa(Sofa):
    def lie_on(self):
        return "Lying on a Modern Sofa"

class FurnitureFactory:
    def create_chair(self):
        raise NotImplementedError

    def create_sofa(self):
        raise NotImplementedError

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()

    def create_sofa(self):
        return VictorianSofa()

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()

def client_code(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    print(chair.sit_on())
    print(sofa.lie_on())

client_code(VictorianFurnitureFactory())  # Victorian Furniture
client_code(ModernFurnitureFactory())  # Modern Furniture
```

### 2. Builder

**Name:** Builder

**Purpose:** To create complex objects step by step.

**Benefits:** Simplifies the creation of complex objects and makes it more readable.

**Use Cases:** When an object has many configuration options.

```python
class House:
    def __init__(self):
        self.windows = 0
        self.doors = 0
        self.rooms = 0

    def __str__(self):
        return f"House with {self.windows} windows, {self.doors} doors and {self.rooms} rooms"

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def set_windows(self, windows):
        self.house.windows = windows
        return self

    def set_doors(self, doors):
        self.house.doors = doors
        return self

    def set_rooms(self, rooms):
        self.house.rooms = rooms
        return self

    def build(self):
        return self.house

builder = HouseBuilder()
house = builder.set_windows(4).set_doors(2).set_rooms(5).build()
print(house)  # House with 4 windows, 2 doors and 5 rooms
```

### 3. Factory Method

**Name:** Factory Method

**Purpose:** To hide the creation logic and delegate the task of instantiation to subclasses.

**Benefits:** Reduces the direct instantiation of objects and promotes code reusability.

**Use Cases:** When a class needs to create dependent objects.

```python
class Animal:
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()
        else:
            raise ValueError("Unknown animal type")

dog = AnimalFactory.create_animal('dog')
print(dog.speak())  # Woof!
```

### 4. Prototype

**Name:** Prototype

**Purpose:** To clone objects from existing instances to avoid complex instantiation.

**Benefits:** Speeds up object creation and reduces complex instantiation logic.

**Use Cases:** When many similar objects need to be created.

```python
import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototype1(Prototype):
    def __init__(self, field):
        self.field = field

prototype1 = ConcretePrototype1("Value")
clone = prototype1.clone()
print(clone.field)  # Value
```

### 5. Singleton

**Name:** Singleton

**Purpose:** Ensures that only one instance of a class exists.

**Benefits:** Prevents multiple instantiations of a class, useful for configurations or logging.

**Use Cases:** Configuration management, logging, database connections.

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # True
```

### 6. Adapter

**Name:** Adapter

**Purpose:** To reconcile different interfaces.

**Benefits:** Allows different systems or classes to work together.

**Use Cases:** When existing classes need to be used in a new environment.

```python
class EuropeanSocket:
    def plug_in(self):
        return "220V"

class USASocket:
    def plug_in(self):
        return "110V"

class Adapter(EuropeanSocket, USASocket):
    def plug_in(self):
        return super().plug_in()

european_socket = EuropeanSocket()
usa_socket = USASocket()
adapter = Adapter()

print(european_socket.plug_in())  # 220V
print(usa_socket.plug_in())  # 110V
print(adapter.plug_in())  # 110V
```

### 7. Bridge

**Name:** Bridge

**Purpose:** To separate implementations and abstractions so they can be developed independently.

**Benefits:** Allows independent modifications and extensions of abstractions and implementations.

**Use Cases:** When a class hierarchy and an implementation hierarchy need to be handled separately.

```python
class Remote:
    def __init__(self, device):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

class TV:
    def turn_on(self):
        print("TV is on")

class Radio:
    def turn_on(self):
        print("Radio is on")

tv_remote = Remote(TV())
radio_remote = Remote(Radio())

tv_remote.turn_on()  # TV is on
radio_remote.turn_on()  # Radio is on
```

### 8. Composite

**Name:** Composite

**Purpose:** To treat individual objects and compositions of objects uniformly.

**Benefits:** Enables hierarchical structures, such as trees, to be managed.

**Use Cases:** When hierarchical data structures need to be managed.

```python
class Component:
    def operation(self):
        raise NotImplementedError

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Composite({'+'.join(results)})"

leaf1 = Leaf()
leaf2 = Leaf()
composite = Composite()
composite.add(leaf1)
composite.add(leaf2)
print(composite.operation())  # Composite(Leaf+Leaf)
```

### 9. Decorator

**Name:** Decorator

**Purpose:** To add new functionality to an object dynamically without modifying its structure.

**Benefits:** Provides flexibility in extending an object's functionality.

**Use Cases:** When additional functionality needs to be added to objects at runtime.

```python
class Component:
    def operation(self):
        raise NotImplementedError

class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"

class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"

class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"

component = ConcreteComponent()
decoratorA = ConcreteDecoratorA(component)
decoratorB = ConcreteDecoratorB(decoratorA)
print(decoratorB.operation())  # ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))
```

### 10. Facade

**Name:** Facade

**Purpose:** To provide a simple interface to a complex system.

**Benefits:** Hides complexity and makes the system easier to use.

**Use Cases:** When a complex subsystem needs to be made easy to use.

```python
class Subsystem1:
    def operation1(self):
        return "Subsystem1: Ready!"

class Subsystem2:
    def operation2(self):
        return "Subsystem2: Go!"

class Facade:
    def __init__(self):
        self._subsystem1 = Subsystem1()
        self._subsystem2 = Subsystem2()

    def operation(self):
        results = []
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation2())
        return "\n".join(results)

facade = Facade()
print(facade.operation())
```

### 11. Flyweight

**Name:** Flyweight

**Purpose:** To efficiently manage large numbers of similar objects by sharing common parts.

**Benefits:** Reduces memory

 usage and increases performance.

**Use Cases:** When managing a large number of similar objects.

```python
class Flyweight:
    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state):
        s = str(self._shared_state)
        u = str(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.")

class FlyweightFactory:
    _flyweights = {}

    @staticmethod
    def get_flyweight(shared_state):
        key = tuple(sorted(shared_state.items()))
        if not key in FlyweightFactory._flyweights:
            FlyweightFactory._flyweights[key] = Flyweight(shared_state)
        return FlyweightFactory._flyweights[key]

factory = FlyweightFactory()
flyweight1 = factory.get_flyweight({"type": "Car", "color": "red"})
flyweight2 = factory.get_flyweight({"type": "Car", "color": "red"})
flyweight1.operation("LicensePlate1")
flyweight2.operation("LicensePlate2")
```

### 12. Proxy

**Name:** Proxy

**Purpose:** To control access to another object.

**Benefits:** Provides control and optimization over access.

**Use Cases:** When access needs to be restricted or optimized.

```python
class Subject:
    def request(self):
        raise NotImplementedError

class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request.")

class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")

real_subject = RealSubject()
proxy = Proxy(real_subject)
proxy.request()
```

### 13. Chain of Responsibility

**Name:** Chain of Responsibility

**Purpose:** To pass a request along a chain of handlers.

**Benefits:** Decouples senders and receivers of requests.

**Use Cases:** When a request can be handled by multiple objects.

```python
class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if self._successor:
            self._successor.handle(request)

class ConcreteHandler1(Handler):
    def handle(self, request):
        if request == "R1":
            print("ConcreteHandler1 handled request R1")
        else:
            super().handle(request)

class ConcreteHandler2(Handler):
    def handle(self, request):
        if request == "R2":
            print("ConcreteHandler2 handled request R2")
        else:
            super().handle(request)

handler_chain = ConcreteHandler1(ConcreteHandler2())
handler_chain.handle("R1")
handler_chain.handle("R2")
handler_chain.handle("RX")
```

### 14. Command

**Name:** Command

**Purpose:** To encapsulate a request as an object.

**Benefits:** Decouples the sender and receiver of a command.

**Use Cases:** Event-driven systems, undo-redo functionality.

```python
class Command:
    def execute(self):
        raise NotImplementedError

class Light:
    def on(self):
        print("Light is on")

    def off(self):
        print("Light is off")

class LightOnCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.on()

class LightOffCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.off()

class RemoteControl:
    def __init__(self):
        self._commands = {}

    def set_command(self, button, command):
        self._commands[button] = command

    def press_button(self, button):
        if button in self._commands:
            self._commands[button].execute()

light = Light()
remote = RemoteControl()
remote.set_command("ON", LightOnCommand(light))
remote.set_command("OFF", LightOffCommand(light))
remote.press_button("ON")
remote.press_button("OFF")
```

### 15. Interpreter

**Name:** Interpreter

**Purpose:** To interpret the syntax and semantics of a given language.

**Benefits:** Enables handling of simple languages.

**Use Cases:** Text editors, configuration files, simple programming languages.

```python
class Context:
    def __init__(self, input):
        self.input = input
        self.output = 0

class AbstractExpression:
    def interpret(self, context):
        raise NotImplementedError

class TerminalExpression(AbstractExpression):
    def interpret(self, context):
        context.output += int(context.input)

context = Context("42")
expression = TerminalExpression()
expression.interpret(context)
print(context.output)  # 42
```

### 16. Iterator

**Name:** Iterator

**Purpose:** To provide a way to access the elements of a collection sequentially without exposing its underlying representation.

**Benefits:** Provides a uniform interface for different collections.

**Use Cases:** Traversing collections.

```python
class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        if self._index < len(self._collection):
            item = self._collection[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

class Iterable:
    def __init__(self, collection):
        self._collection = collection

    def __iter__(self):
        return Iterator(self._collection)

iterable = Iterable([1, 2, 3])
for item in iterable:
    print(item)  # 1 2 3
```

### 17. Mediator

**Name:** Mediator

**Purpose:** To regulate communication between multiple objects through a central point.

**Benefits:** Reduces the number of direct relationships between classes.

**Use Cases:** Event-driven systems, GUI applications.

```python
class Mediator:
    def notify(self, sender, event):
        raise NotImplementedError

class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component2 = component2
        self._component1.set_mediator(self)
        self._component2.set_mediator(self)

    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers B")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers A and C")
            self._component1.do_a()
            self._component2.do_c()

class BaseComponent:
    def __init__(self):
        self._mediator = None

    def set_mediator(self, mediator):
        self._mediator = mediator

class Component1(BaseComponent):
    def do_a(self):
        print("Component 1 does A")
        self._mediator.notify(self, "A")

    def do_b(self):
        print("Component 1 does B")
        self._mediator.notify(self, "B")

class Component2(BaseComponent):
    def do_c(self):
        print("Component 2 does C")
        self._mediator.notify(self, "C")

    def do_d(self):
        print("Component 2 does D")
        self._mediator.notify(self, "D")

component1 = Component1()
component2 = Component2()
mediator = ConcreteMediator(component1, component2)

component1.do_a()
component2.do_d()
```

### 18. Memento

**Name:** Memento

**Purpose:** To save and restore an object's internal state without revealing its implementation.

**Benefits:** Enables state restoration, such as undo functionality.

**Use Cases:** Text editors, state restoration.

```python
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self, state):
        self._state = state

    def save(self):
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

originator = Originator("State1")
memento = originator.save()
originator.set_state("State2")
print(originator.get_state())  # State2
originator.restore(memento)
print(originator.get_state())  # State1
```

### 19. Observer

**Name:** Observer

**Purpose:** To allow an object to notify multiple observers when its state changes.

**Benefits:** Helps in tracking state changes and handling notifications.

**Use Cases:** GUI applications, event handling, notification systems.

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

class Observer:
    def update(self):
        raise NotImplementedError

class ConcreteObserver(Observer):
    def update(self):
        print("Observer notified")

subject = Subject()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)
subject.notify()
```

### 20. State

**Name:** State

**Purpose:** To alter an object's behavior when its internal state changes.

**

Benefits:** Allows for state management and dynamic behavior changes.

**Use Cases:** State-dependent behaviors.

```python
class State:
    def handle(self, context):
        raise NotImplementedError

class ConcreteStateA(State):
    def handle(self, context):
        context.state = ConcreteStateB()

class ConcreteStateB(State):
    def handle(self, context):
        context.state = ConcreteStateA()

class Context:
    def __init__(self, state):
        self.state = state

    def request(self):
        self.state.handle(self)

context = Context(ConcreteStateA())
context.request()
print(type(context.state))  # ConcreteStateB
context.request()
print(type(context.state))  # ConcreteStateA
```

### 21. Strategy

**Name:** Strategy

**Purpose:** To encapsulate different algorithms and enable their interchange without modifying the client class.

**Benefits:** Provides flexibility in algorithm selection.

**Use Cases:** Complex algorithms or operations that may change.

```python
class Strategy:
    def execute(self, data):
        raise NotImplementedError

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return f"Strategy A: {data}"

class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return f"Strategy B: {data}"

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.execute(data)

context = Context(ConcreteStrategyA())
print(context.execute_strategy("Test"))  # Strategy A: Test
context.set_strategy(ConcreteStrategyB())
print(context.execute_strategy("Test"))  # Strategy B: Test
```

### 22. Template Method

**Name:** Template Method

**Purpose:** To define the steps of an algorithm in a method, deferring the concrete steps to subclasses.

**Benefits:** Ensures reusability of algorithm structure.

**Use Cases:** When the order of steps in an algorithm needs to be reused.

```python
class AbstractClass:
    def template_method(self):
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.required_operations2()

    def base_operation1(self):
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation2(self):
        print("AbstractClass says: But I let subclasses override some operations")

    def required_operations1(self):
        raise NotImplementedError

    def required_operations2(self):
        raise NotImplementedError

class ConcreteClass1(AbstractClass):
    def required_operations1(self):
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self):
        print("ConcreteClass1 says: Implemented Operation2")

class ConcreteClass2(AbstractClass):
    def required_operations1(self):
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self):
        print("ConcreteClass2 says: Implemented Operation2")

def client_code(abstract_class: AbstractClass):
    abstract_class.template_method()

client_code(ConcreteClass1())
client_code(ConcreteClass2())
```

### 23. Visitor

**Name:** Visitor

**Purpose:** To define a new operation without changing the classes of the elements on which it operates.

**Benefits:** Allows adding new operations to existing classes without modifying them.

**Use Cases:** When new operations need to be added to different classes.

```python
class Visitor:
    def visit_concrete_element_a(self, element):
        raise NotImplementedError

    def visit_concrete_element_b(self, element):
        raise NotImplementedError

class ConcreteVisitor1(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"{element.exclusive_method_of_concrete_element_a()} + ConcreteVisitor1")

    def visit_concrete_element_b(self, element):
        print(f"{element.special_method_of_concrete_element_b()} + ConcreteVisitor1")

class ConcreteVisitor2(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"{element.exclusive_method_of_concrete_element_a()} + ConcreteVisitor2")

    def visit_concrete_element_b(self, element):
        print(f"{element.special_method_of_concrete_element_b()} + ConcreteVisitor2")

class Element:
    def accept(self, visitor):
        raise NotImplementedError

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

    def exclusive_method_of_concrete_element_a(self):
        return "A"

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

    def special_method_of_concrete_element_b(self):
        return "B"

def client_code(elements, visitor):
    for element in elements:
        element.accept(visitor)

elements = [ConcreteElementA(), ConcreteElementB()]
visitor1 = ConcreteVisitor1()
visitor2 = ConcreteVisitor2()

client_code(elements, visitor1)
client_code(elements, visitor2)
```

This summary covers the most common design patterns with practical Python code examples, helping to
understand and apply them in real-world software development scenarios.

## Further Readings

1. [Python Design Patterns](https://python-patterns.guide/)
2. [All 23 OOP software design patterns with examples in Python](https://medium.com/@cautaerts/all-23-oop-software-design-patterns-with-examples-in-python-cac1d3f4f4d5)
3. [Design Patterns in Python](https://refactoring.guru/design-patterns/python)
4. [Mastering Python Design Patterns: Craft essential Python patterns by following core design principles , Third Edition](https://www.packtpub.com/en-us/product/mastering-python-design-patterns-9781837639618)
