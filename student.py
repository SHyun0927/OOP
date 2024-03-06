class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, students):
        if len(self.students) < self.max_students:
            self.students.append(students)
            return True
        return False
    
    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.grade
        return total / len(self.students)

    
s1 = Student(name="Tim", age=19, grade=95)
s2 = Student(name="Bill", age=20, grade=75)
s3 = Student(name="Jill", age=21, grade=65)

# print(Student.get_grade(s1))
# print(Student.get_grade(s2))
# print(Student.get_grade(s3))

# instantiate course object
course1 = Course(name="Computer Science", max_students=2)

# add students to the course
course1.add_student(s1)
course1.add_student(s2)
course1.add_student(s3)

# for student in course1.students:
    # print(student.name)


# print(course1.students[0].name)

print(f"the average grade in {course1.name} is {course1.get_average_grade()}")