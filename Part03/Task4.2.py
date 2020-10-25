#even elements of list

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

c = [elem for elem in a if elem % 2 == 0]

print("Even elements of list are : " + str(c))