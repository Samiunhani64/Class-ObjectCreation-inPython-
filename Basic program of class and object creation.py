class Box:
    def __init__(self,currName,currRollNum,currDBMSMarks,currOSMarks):
        self.name=currName
        self.rollno=currRollNum
        self.dbmsmarks=currDBMSMarks
        self.osMarks=currOSMarks

student1 = Box("sam",34, 65,78)
print(student1.name)
print(student1.rollno)
print(student1.dbmsmarks)

student2 = Box("hani",99, 39,55)
print(student2.name)
print(student2.rollno)
print(student2.osMarks)
