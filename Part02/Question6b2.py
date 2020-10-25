#Calculating max GPA in DSA subject without using for loop
D = {
    "2016-CS-700" : [("DSA",3), ("Algo",2.5), ("AI",3)],
    "2016-CS-701" : [("LA",3), ("Algo",3.5), ("PF",2.8)],
    "2016-CS-710" : [("OOP",3), ("DB",3.5), ("PF",2.8)],
    "2016-CS-708" : [("Algo",2.5), ("DSA",3.7), ("AI",3)]
}

def calcGPA(subjectList):
    if not subjectList:
        return -1.0
    subject = subjectList.pop()
    if subject[0] == "DSA":
        return subject[1]
    return calcGPA(subjectList)

def DicIterate(dictionary):
    if not dictionary:
        return -1.0
    student = dictionary.popitem()
    DSAGPA = calcGPA(student[1])
    nextDSAGPA = DicIterate(dictionary)
    if nextDSAGPA > DSAGPA:
        return nextDSAGPA
    else:
        return DSAGPA

result = DicIterate(D)

if result != -1.0:
    print("The Max Grade in DSA is >> " + str(result))

