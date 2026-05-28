class Student:
    def __init__(self, name: str, grade: int):
        self.name = name
        self.__grade = grade

    @property
    def score(self):
        return self.__grade
    
    @score.setter
    def score(self, num):
        if num > 0 and num <= 100:
            self.__grade = num
        else:
            raise ValueError ("Grade must be between 0 and 100")
        
    def __str__(self):
        return f"{self.name} {self.__grade}"
    
student = Student("Kola", 34)
print(student.score)
student.score = 45
print(student.score)