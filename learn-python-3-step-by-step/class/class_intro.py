class Student:
    def __init__(self, roll, first_name, last_name):
        self.roll = roll
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name.lower() + "." + last_name + "_" + str(roll) + "@schooldomain.com"
        
    def name(self):
        return self.first_name + " " + self.last_name

s1 = Student(1, 'Suhel', 'Mansuri')
s2 = Student(2, 'Alisha', 'Eric')


# s1.roll = 1
# s1.first_name = 'Suhel'
# s1.last_name = 'Mansuri'

# s2.roll = 2
# s2.first_name = 'Raj'
# s2.last_name = 'Patel'


# print(s1.roll, s1.first_name, s1.last_name)
# print(s2.roll, s2.first_name, s2.last_name)

#student.name(s1)

print(s1.roll, s1.name(), s1.email, type(s1))
print(s2.roll, s2.name(), s2.email, type(s2))
# print(s1.roll, Student.name(s1), s1.email, type(s1))
# print(s2.roll, Student.name(s2), s2.email, type(s2))