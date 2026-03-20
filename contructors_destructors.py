# constructors_destructors.py

class Student:
    # Constructor
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        print(f"Constructor called: {self.name} has joined FSST")

    # Method to display student information
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

    # Destructor
    def __del__(self):
        print(f"Destructor called: {self.name} has left FSST")


student1 = Student("Giddy", 22, "Information Science")
student2 = Student("Lara", 20, "Journalism")

student1.display_info()
student2.display_info()

del student1
