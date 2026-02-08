# class LapTop:
#     lapName1 = "Hp NoteBook"
#     graficsCard = "5Gb"

#     def on(self):
#         print("Lap in On")
#     def Off(self):
#         print("Lap in Off")

# l =LapTop()
# l.lapName1="Hp BookNote"
# print(l.lapName1)
# NotoLap = LapTop()
# NotoLap.lapName1="DEll"
# NotoLap.graficsCard="6GB"
# print(NotoLap.graficsCard)
# print(NotoLap.lapName1)



# Encapsulation
class Student:
    __marks = 0
    def addMarks(self,mark1,mark2,mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.__marks = mark1+mark2+mark3
    def totalMarks(self):
        return self.__marks
    
S1 = Student()
S1.addMarks(60,70,80)
S2 = Student()
S2.addMarks(80,55,99)
print(S1.totalMarks())
print(S2.totalMarks())
S1.__marks = 350
print(S1.totalMarks())
