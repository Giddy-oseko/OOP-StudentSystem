Constructors and Destructors in Object-Oriented Programming (OOP)
1. Introduction
In OOP, every object goes through a lifecycle: it is created, used, and eventually destroyed.
Constructors and destructors manage the beginning and end of an object’s life.
They ensure that objects are properly initialized and cleaned up.
2. Constructor (__init__)
Definition
A constructor is a special method automatically called when an object is created.
Its main purpose is to initialize attributes and perform any setup required for the object.
Syntax
Python
class ClassName:
    def __init__(self, parameters):
        # Initialize attributes
        self.attribute = value
Key Features
Always named __init__.
Automatically invoked when an object is created.
Can accept parameters to customize object initialization.
Helps avoid repetitive code.
Types of Constructors
Default Constructor: Takes no parameters.
Python
class Student:
    def __init__(self):
        self.name = "Unknown"
        self.age = 0
Parameterized Constructor: Takes parameters to initialize attributes.
Python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Giddy", 22)
Example
Python
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        print(f"{self.name} has joined FSST")

student1 = Student("Giddy", 22, "Information Science")
Output:

Giddy has joined FSST
Best Practices
Keep constructors simple; only initialize attributes.
Avoid heavy computation inside constructors.
Use parameterized constructors for flexibility.
3. Destructor (__del__)
Definition
A destructor is a special method automatically called when an object is destroyed.
Its main purpose is to release resources, such as closing files or freeing memory.
Syntax
Python
class ClassName:
    def __del__(self):
        # Cleanup code
Key Features
Always named __del__.
Automatically invoked when the object goes out of scope or is deleted.
Used less often in Python because Python has garbage collection, which handles memory cleanup automatically.
Example
Python
class Student:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} has joined FSST")

    def __del__(self):
        print(f"{self.name} has left FSST")

student1 = Student("Giddy")
del student1
Output:

Giddy has joined FSST
Giddy has left FSST
When Destructor is Called
When del is used on the object.
When the program ends and the object goes out of scope.
4. Differences Between Constructor and Destructor
Feature
Constructor (__init__)
Destructor (__del__)
When called
When object is created
When object is destroyed
Purpose
Initialize object attributes
Cleanup resources before destruction
Parameters
Can take arguments
Only self
Return
None
None
Frequency
Commonly used
Less common
5. Real-Life Analogy
Constructor: Buying and setting up a new phone (installing apps, setting a name).
Destructor: Recycling or switching off the phone when you no longer need it.
6. Common Use-Cases
Constructors
Initializing student information, account details, or configuration settings.
Setting up default values for objects.
Destructors
Closing database connections or files.
Cleaning up temporary resources when the object is no longer needed.
7. Example: Student System
Python
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        print(f"{self.name} has joined FSST")

    def __del__(self):
        print(f"{self.name} has left FSST")

student1 = Student("Giddy", 22, "Information Science")
student2 = Student("Lara", 20, "Journalism")

# Delete one object explicitly
del student1

# The second object will be deleted automatically when program ends
Output:

Giddy has joined FSST
Lara has joined FSST
Giddy has left FSST
Lara has left FSST
8. Summary
Constructor (__init__): Initializes an object at creation.
Destructor (__del__): Cleans up an object before destruction.
Together, they manage the lifecycle of an object in OOP.
Proper use of constructors and destructors ensures clean, maintainable, and efficient code.