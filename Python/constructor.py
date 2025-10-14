class student:
    def __init__(self,name,course):
        self.name = name
        self.course=course
    def prints(self):
        print(f'The student name is {self.name} and the course name is {self.course}')

s =student("Xyz","Python")
s.prints()
s2 =student("abc","Java")
s2.prints()