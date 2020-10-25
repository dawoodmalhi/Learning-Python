list0 = [
    {"V":"S001"}, 
    {"V": "S002"}, 
    {"VI": "S001"}, 
    {"VI": "S005"}, 
    {"VII":"S005"}, 
    {"V":"S009"}, 
    {"VIII":"S007"}
]
uniqueList = []
for i in range(0, len(list0), 1):
    if ("".join(list0[i].values()) not in uniqueList):
        uniqueList.append("".join(list0[i].values()))
print(uniqueList)
