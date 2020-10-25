#creating a new list and then printing
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = []

for elem in a:
    if elem < 5:
        b.append(elem)

for elem in b:
    print(elem)