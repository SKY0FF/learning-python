import random

#task 4
lst_1 = []
for i in range(10):
    lst_1.append(random.randint(0, 100))

max = lst_1.index(max(lst_1))
min = lst_1.index(min(lst_1))

v = 0

if max > min:
    while max >= min:
        v += lst_1[min]
        min +=1
elif max < min:
    while max <= min:
        v += lst_1[max]
        max += 1
print(v)















#for index, value in enumerate(lst_1):
#    print(index, value, end="\n")

