class Student:
    def __init__(self,rollNum):
        self.rollNum=rollNum
    def __eq__(self,other):
        return self.rollNum==other.rollNum

s1=Student(1254)
s2=Student(1254)
print(s1==s2)