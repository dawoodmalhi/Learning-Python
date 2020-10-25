#Calculating max GPA in DSA subject with using for loop
D = {
    "2016-CS-700" : [("DSA",3), ("Algo",2.5), ("AI",3)],
    "2016-CS-701" : [("LA",3), ("Algo",3.5), ("PF",2.8)],
    "2016-CS-710" : [("OOP",3), ("DB",3.5), ("PF",2.8)],
    "2016-CS-708" : [("Algo",2.5), ("DSA",3.7), ("AI",3)]
}

maxDSA = -1.0

for v in D.keys():
    for t in D[v]:
        if t[0] == "DSA" and t[1] > maxDSA:
            maxDSA = t[1]

if not maxDSA == -1.0:
    print("The Max Grade in DSA is >> " + str(maxDSA))