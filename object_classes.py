# objects_classes.py

class Student:
    school_name = "FSST"
    total_students = 0

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        Student.total_students += 1

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"School: {Student.school_name}")
        print("----------------------")

    def study(self):
        print(f"{self.name} is studying {self.course}")

    def is_adult(self):
        if self.age >= 18:
            print(f"{self.name} is an adult")
        else:
            print(f"{self.name} is not an adult")


# Creating objects
student1 = Student("Giddy", 22, "Information Science")
student2 = Student("Brian", 17, "Computer Science")
student3 = Student("Lara", 20, "Journalism")

# Displaying info
student1.display_info()
student2.display_info()
student3.display_info()

# Using methods
student1.study()
student2.study()

student1.is_adult()
student2.is_adult()

# Display total students
print(f"Total Students: {Student.total_students}")