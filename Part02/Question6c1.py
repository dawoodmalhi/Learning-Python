#Calculating students that have AI GPA less than 2.5 using for loop
D = {
    "2016-CS-700" : [("DSA",3), ("Algo",2.5), ("AI",3)],
    "2016-CS-701" : [("AI",2.0), ("Algo",3.5), ("PF",2.8)],
    "2016-CS-710" : [("OOP",3), ("DB",3.5), ("AI",2.3)],
    "2016-CS-708" : [("Algo",2.5), ("DSA",3.7), ("AI",3)]
}

result = 0

for v in D.keys():
    for t in D[v]:
        if t[0] == "AI" and t[1] < 2.5:
            result += 1

print("There are " + str(result) + " Students that have AI GPA less than 2.5")