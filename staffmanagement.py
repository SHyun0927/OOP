class staff:
    number_of_staffs = 0
    retirement_age = 65
    def __init__(self, name, age, employee_id, dob, title):
        self.name = name
        self.age = age
        self.employee_id = employee_id
        self.dob = dob
        self.title = title

        staff.num_of_staffs


    def print_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Employee ID: ", self.employee_id)
        print("Date of Birth: ", self.dob)
        print("Title: ", self.title)

    def num_of_staffs(self):
        staff.number_of_staffs += 1

    def total_staffs(self):
        return staff.num_of_staffs


class management(staff):
    def __init__(self, name, age, employee_id, dob, title, car):
        super().__init__(name, age, employee_id, dob, title)
        self.car = car

    def print_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Employee ID: ", self.employee_id)
        print("Date of Birth: ", self.dob)
        print("Title: ", self.title)
        print("Car: ", self.car)

class clerical(staff):
    def __init__(self, name, age, employee_id, dob, title, typing_speed):
        super().__init__(name, age, employee_id, dob, title)
        self.typing_speed = typing_speed

    def print_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Employee ID: ", self.employee_id)
        print("Date of Birth: ", self.dob)
        print("Title: ", self.title)
        print("Typing Speed: ", self.typing_speed)

class factory(staff):
    pass

a = management("Jane", 22, "ID007", "20/12/2000", "Managing Director", "Jaguar")
a.print_details()
print()

b = clerical("Tim", 17, "ID119", "01/01/2005", "Secretary", 123)
b.print_details()
print()

c = factory("Jake", 16, "ID125", "17/08/2006", "Labourer")
c.print_details()
print()