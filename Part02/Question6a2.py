#printing GPA of students without using for loop
D = {
    "2016-CS-700" : [("DSA",3), ("Algo",2.5), ("AI",3)],
    "2016-CS-701" : [("LA",3), ("Algo",3.5), ("PF",2.8)],
    "2016-CS-710" : [("OOP",3), ("DB",3.5), ("PF",2.8)]
}

def calcGPA(subjectList):
    if not subjectList:
        return 0
    return subjectList.pop()[1] + calcGPA(subjectList)

def DicIterate(dictionary):
    if not dictionary:
        return 
    student = dictionary.popitem()
    avgGPA = calcGPA(student[1]) / 3
    print("Student Reg. No " + student[0] + " : GPA " + str(avgGPA))
    DicIterate(dictionary)


DicIterate(D)
