#task 1
lst = []
for i in range(10):
    number = int(input())
    lst.append(number)

max_1 = lst.index(max(lst))
min_1 = lst.index(min(lst))

v = 0

if max_1 > min_1:
    while max_1 >= min_1:
        v += lst[min_1]
        min_1 +=1
elif max_1 < min_1:
    while max_1 <= min_1:
        v += lst[max_1]
        max_1 += 1
print(v, "\n")


#task 2
lst = []
for i in range(10):
    number = int(input())
    lst.append(number)

lst.remove(max(lst))

print(lst, "\n")


#task 3
lst = []
for i in range(10):
    number = int(input())
    lst.append(number)

lst.reverse()

print(lst, "\n")

lst = []
for i in range(10):
    number = input()
    lst.append(number)

x = 9

for i in range(10):
    lst.append(lst[x])
    x -= 1

for i in range(10):
    lst.remove(lst[i-1])

print(lst, "\n")


#task 4
lst = []
for i in range(10):
    number = int(input())
    lst.append(number)

def is_multiple_three(item):
    if (item % 3) == 0:
        return True
    else:
        return False

print(list(filter(is_multiple_three, lst)), "\n")


#task 5
lst = []
for i in range(10):
    number = int(input())
    lst.append(number)

def minus(item):
    return item-1

print(list(map(minus, lst)), "\n")

#task 6
lst = []
for i in range(10):
    number = input()
    lst.append(number)

def split2(item): #делает список с первым словом того списка
    lst2 = item.split()
    lst2.remove(lst2[1])
    return lst2

lst_2 = list(map(split2, lst)) #создание списка с первым слово списка lst

symb = "у" #символ который нужно найти 
x = 0 #для работы
for i in range(10):
    if symb in lst_2[x][0]: #если symb есть в списке списка то вывод да
        print(x, '-', lst[x])
    x += 1