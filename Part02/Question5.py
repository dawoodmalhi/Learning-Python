list0  = [
    'STRING',
    'Nigga',
    'AdiVaSi',
    'seski',
    'Abc'
]

resultList = [string.lower() for string in list0 if len(string)>5 ]
print(resultList)