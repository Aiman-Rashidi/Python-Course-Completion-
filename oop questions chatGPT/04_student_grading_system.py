class Student:
    def __init__(self, name="anonymous", marks=[0, 0, 0]):
        print("constructor called")
        self.name = name
        self.marks = marks

    @property
    def name(self):
        print("name property called")
        return self._name
    
    @name.setter
    def name(self, value):
        print("name setter called")
        if not isinstance(value, str) or not value.isalpha():
            raise ValueError("name must be a string with letter only.")
        self._name = value

    @property
    def marks(self):
        print("marks property called")
        return self._marks.copy()
    
    @marks.setter
    def marks(self, value):
        print("marks setter called")
        if not isinstance(value, list):
            raise ValueError("marks must be provided as a list.")
        for mark in value:
            if not isinstance(mark, (int, float)):
                raise ValueError("each mark must be a number.")
            if not 0 <= mark <= 100:
                raise ValueError("marks must fall in [0, 100]")
        self._marks = value.copy()

    @property
    def average(self):
        print("average property called")
        return sum(self.marks) / len(self.marks) if self.marks else 0
    
    @property
    def grade(self):
        print("grade property called")
        avg = self.average
        if avg >= 90:
            return "A"
        elif 75 <= avg < 90:
            return "B"
        elif 60 <= avg < 75:
            return "C"
        elif 40 <= avg < 60:
            return "D"
        else:
            return "F"
        
# s1 = Student()
# print(s1.name)
# print(s1.marks)
# print(s1.average)
# print(s1.grade)
        
s1 = Student("Aiman", [90, 80])
print(s1.name)
print(s1.marks)
print(s1.average)
print(s1.grade)

# # With setter method (valid values)
# s1.marks = [40, 40, 40]
# print(s1.average)
# print(s1.grade)
# print(s1.marks)

# # # # With setter method (invalid one)
# # s1.marks = [-8, 90, 30]
# # print(s1.average)
# # print(s1.grade)
# # print(s1.marks)