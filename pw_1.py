import random

#task 1
lst_1 = []
for i in range(10):
    lst_1.append(random.randint(0, 100))

print(lst_1)

max_1 = lst_1.index(max(lst_1))
min_1 = lst_1.index(min(lst_1))

v = 0

if max_1 > min_1:
    while max_1 >= min_1:
        v += lst_1[min_1]
        min_1 +=1
elif max_1 < min_1:
    while max_1 <= min_1:
        v += lst_1[max_1]
        max_1 += 1
print(v)


#task 2

lst_2 = []
for i in range(10):
    lst_2.append(random.randint(0, 100))

print("\n", lst_2)

lst_2.remove(max(lst_2))

print(lst_2)


#task 3

lst_3 = []
for i in range(10):
    lst_3.append(random.randint(0, 100))

print("\n", lst_3)

lst_3.reverse()

print(lst_3)

lst_4 = []
for i in range(10):
    lst_4.append(random.randint(0, 100))

print("\n", lst_4)

for index, value in enumerate(lst_4):
    print(index, value, end="\n")
    
x = 9

for i in range(10):
    lst_4.append(lst_4[x])
    x -= 1

for i in range(10):
    lst_4.remove(lst_4[i-1])
    
#for i in range(10):
#    
#    lst_4.append(lst_4[i])
#    lst_4.remove(lst_4[i])

print(lst_4)