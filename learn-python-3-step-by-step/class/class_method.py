class Student:
    pass_score = 40.0
    # from_string_coumter = 0
    def __init__(self, roll, first_name, last_name, score):
        self.roll = roll
        self.first_name = first_name
        self.last_name = last_name
        self.score = score
        self.email = first_name.lower() + "." + last_name + "_" + str(roll) + "@schooldomain.com"
        
    def name(self):
        return self.first_name + " " + self.last_name
    
    def pass_or_fail(self):
        if self.score >= Student.pass_score:
            return "Passed"
        else:
            return "Failded"
    @classmethod
    def update_score(cls, new_score):
        cls.pass_score = new_score
        
    # @classmethod
    # def from_string(cls,str_student):
    #     str_roll, str_first_name, str_last_name, str_score = str_student.split(",")
    #     s = Student(int(str_roll), str_first_name, str_last_name, float(str_score))
    #     # cls.from_string_coumter += 1
    #     return s
    
    @staticmethod
    def from_string(str_student):
        str_roll, str_first_name, str_last_name, str_score = str_student.split(",")
        s = Student(int(str_roll), str_first_name, str_last_name, float(str_score))
        # cls.from_string_coumter += 1
        return s
        
str1 = "1,James,Smith,67.5"
str2 = "2,David,Smith,76.75"
str3 = "3,James,Johnson,90.50"

s1 = Student.from_string(str1)
s2 = Student.from_string(str2)
s3 = Student.from_string(str3)

s4 = Student(4, 'FName', 'LName', 90.0)

print(s1.email, s2.email, s3.email, sep='\n')
# print(Student.from_string_coumter)
# s1 = Student(1, 'Suhel', 'Mansuri', 75.0)
# s2 = Student(2, 'Alisha', 'Eric', 35.5)

# print(Student.pass_score)
# Student.update_score(70.0)
# print(Student.pass_score)