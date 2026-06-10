class Student:
    count = 0
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.count += 1 

    
    def get_status(self):
        if self.grade >=60:
            return "Pass"
        else:
            return "Fail"
    @staticmethod
    def is_valid_grade(grade):
        if grade >= 0 and grade <=100:
            return True
        else:
            return False
    
    @classmethod
    def from_string(cls, data):
        name, grade = data.split(",")
        grade = int(grade)
        
        if not cls.is_valid_grade(grade):
            raise ValueError ("Invalid grade")
        
        return cls(name, grade)

s = Student.from_string("Jennifer, 15")
s = Student.from_string("Jenra, 23")
s = Student.from_string("Mike, 13")
print (f"{s.name}, {s.grade}")
print(Student.count)

    