# constructors_destructors.py

class Student:
    # Constructor
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        print(f"[Constructor] {self.name} has been created and joined {self.course}")

    # Method to display info
    def display_info(self):
        print("Student Info:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print("--------------------------")

    # Destructor
    def __del__(self):
        print(f"[Destructor] {self.name} object is being destroyed")


# Creating objects
student1 = Student("Giddy", 22, "Information Science")
student2 = Student("Lara", 20, "Journalism")

# Using methods
student1.display_info()
student2.display_info()

# Deleting one object manually
del student1

print("Program still running...")

# student2 will be deleted automatically when program ends

