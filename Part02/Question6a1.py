#printing GPA of students with using for loop
D = {
    "2016-CS-700" : [("DSA",3), ("Algo",2.5), ("AI",3)],
    "2016-CS-701" : [("LA",3), ("Algo",3.5), ("PF",2.8)],
    "2016-CS-710" : [("OOP",3), ("DB",3.5), ("PF",2.8)]
}

for v in D.keys():
    totalGPA = 0
    for t in D[v]:
        totalGPA += t[1]
    avgGPA = totalGPA / 3
    print("Student Reg. No " + v + " : GPA " + str(avgGPA))
