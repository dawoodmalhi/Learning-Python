#finding common elements by oneline of code

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

[c.append(valueA) for valueA in a for valueB in b if valueA == valueB and valueA not in c]

print("Common Elements are : " + str(c))