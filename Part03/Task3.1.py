#randomly generating lists and finding common elements
import random

a = []
b = []


for i in range(0,10):
    a.append(random.randint(1,20))
    b.append(random.randint(1,20))

print("List 1 : " + str(a))
print("List 2 : " + str(b))

c = []

for valueA in a:
    for valueB in b:
        if valueA == valueB:
            if valueA not in c:
                c.append(valueA)

print("Common Elements are : " + str(c))