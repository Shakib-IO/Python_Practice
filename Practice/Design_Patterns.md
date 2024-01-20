# Design Patterns
1. **Creational Patterns**: Facilitate flexible object creation and code reuse.
2. **Structural Patterns**: Assembling objects and classes into larger structures while retaining their adaptability and efficiency.
3. **Behavioral Patterns**: Efficient interaction and allocation of responsibilities between objects, ensuring effective communication.

#### Creational Patterns
1. **Singleton Pattern**: Ensures that a class has only one instance and provides a global point of access to that instance.
2. **Factory Method Pattern**: Defines an interface for creating objects, allowing subclasses to decide which class to instantiate.
3. **Abstract Factory Pattern**: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
4. **Builder Pattern**: Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
5. **Prototype Pattern**: Creates new objects by copying an existing object, avoiding the overhead of creating objects from scratch.

#### Structural Patterns
1. **Adapter Pattern**: Converts the interface of a class into another interface that clients expect, enabling classes with incompatible interfaces to work together.
2. **Bridge Pattern**: Decouples an abstraction from its implementation, allowing both to evolve independently.
3. **Composite Pattern**: Composes objects into tree structures to represent part-whole hierarchies, making it easier to work with individual objects and compositions.
4. **Decorator Pattern**: Dynamically adds responsibilities to objects, providing a flexible alternative to subclassing for extending functionality.
5. **Facade Pattern**: Provides a simplified interface to a complex subsystem, making it easier to use and understand.
6. **Flyweight Pattern**: Shares instances of objects to support large numbers of fine-grained objects efficiently.
7. **Proxy Pattern**: provide a substitute or placeholder for another object to control access to the original object.

#### Behavioral Patterns
1. **Chain of Responsibility Pattern**: Creates a chain of objects that can handle requests, avoiding coupling the sender with its receivers.
2. **Command Pattern**: Turns a request into a stand-alone object, allowing parameterization of clients with different requests.
3. **Interpreter Pattern**: Defines a grammar for a language and an interpreter to interpret sentences in the language.
4. **Iterator Pattern**: Provides a way to access elements of a collection without exposing its underlying representation.
5. **Mediator Pattern**: Defines an object that centralizes communication between multiple objects, reducing direct dependencies between them.
6. **Memento Pattern**: Captures and restores an object’s internal state, allowing it to be restored to a previous state.
7. **Observer Pattern**: Defines a dependency between objects, ensuring that when one object changes state, all its dependents are notified and updated automatically.
8. **State Pattern**: Allows an object to change its behavior when its internal state changes, enabling cleaner, more maintainable conditional logic.
9. **Strategy Pattern**: Defines a family of algorithms, encapsulates each one and makes them interchangeable. Clients can choose an algorithm from this family without modifying their code.
10. **Template Method Pattern**: Defines the structure of an algorithm in a superclass but lets subclasses override specific steps of the algorithm.
11. **Visitor Pattern**: Separates an algorithm from an object structure, allowing new operations to be added without modifying the objects themselves.
