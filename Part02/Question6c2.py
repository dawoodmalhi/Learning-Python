#Calculating students that have AI GPA less than 2.5 without using for loop
D = {
    "2016-CS-700" : [("DSA",3), ("Algo",2.5), ("AI",3)],
    "2016-CS-701" : [("AI",2.0), ("Algo",3.5), ("PF",2.8)],
    "2016-CS-710" : [("OOP",3), ("DB",3.5), ("AI",2.3)],
    "2016-CS-708" : [("Algo",2.5), ("DSA",3.7), ("AI",3)]
}

def calcGPA(subjectList):
    if not subjectList:
        return False
    subject = subjectList.pop()
    if subject[0] == "AI" and subject[1] < 2.5:
        return True
    return calcGPA(subjectList)

def DicIterate(dictionary):
    if not dictionary:
        return 0
    student = dictionary.popitem()
    isLessGPA = calcGPA(student[1])
    if isLessGPA:
        return 1+DicIterate(dictionary)
    else:
        return 0+DicIterate(dictionary)

result = DicIterate(D)

print("There are " + str(result) + " Students that have AI GPA less than 2.5")