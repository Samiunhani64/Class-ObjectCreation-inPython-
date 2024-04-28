class Box:
    def __init__(self,currName,currrollNo,currdbmsMarks,currpythonMarks,currcMarks,currosMarks,currcnMarks):
        self.name=currName
        self.rollNo=currrollNo
        self.dbmsMarks=currdbmsMarks
        self.pythonMarks=currpythonMarks
        self.cMarks=currcMarks
        self.osMarks=currosMarks
        self.cnMarks=currcnMarks
        
Student1=Box("Harika","5A1",78,67,77,89,46)
print(Student1.name,Student1.rollNo,Student1.dbmsMarks,Student1.pythonMarks,Student1.cMarks,Student1.osMarks,Student1.cnMarks)


Student2=Box("Swapna","5A2",38,65,97,59,41)
print(Student2.name,Student2.rollNo,Student2.dbmsMarks,Student2.pythonMarks,Student2.cMarks,Student2.osMarks,Student2.cnMarks) 


Student3=Box("Sushma","5A3",88,95,47,89,31)
print(Student3.name,Student3.rollNo,Student3.dbmsMarks,Student3.pythonMarks,Student3.cMarks,Student3.osMarks,Student3.cnMarks)
