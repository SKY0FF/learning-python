import random

#task 1

lst = []
for i in range(10):
    lst.append(random.randint(0, 100))

print(lst)

def is_multiple_three(item):
    if (item % 3) == 0:
        return True
    else:
        return False

print(list(filter(is_multiple_three, lst)), "\n")


#task 2
lst = []
for i in range(10):
    lst.append(random.randint(0, 100))

print(lst)

def minus(item):
    return item-1

print(list(map(minus, lst)), "\n")

#task 3
lst = ["Клюшин Захар", "Погосян Ника", "Барабанова Эльвира", "Ванюхин Дмитрий", "Чумаков Максим", "Никулова Анастасия", "Морозова Софья", "Третьяков Антон", "Борисова Ульяна", "Александрук Дмитрий"]
y = 1 #пока что не зачем

def lower2(item): #делает список с нижним регистром
    return item.lower()

def split2(item): #делает список с первым словом того списка
    lst2 = item.split()
    lst2.remove(lst2[1])
    return lst2

 #вывод списка с нижним регистром

lst_2 = list(map(split2, lst)) #создание списка с первым слово списка lst
 #вывод списка с первым слово списка lst


symb = "у" #символ который нужно найти 
x = 0 #для работы
for i in range(10):
    if symb in lst_2[x][0]: #если symb есть в списке списка то вывод да
        print(x, '-', lst[x])
    x += 1