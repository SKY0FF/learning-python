import math

##task1
#a = int(input("Введите коэффицент a: "))
#b = int(input("Введите коэффицент b: "))
#c = int(input("Введите коэффицент c: "))
#
#def get_solution(a, b, c):
#    d = b*b - 4*a*c
#    if d < 0:
#        return "Корней нет"
#    else:
#        x1 = (-b + math.sqrt(d)) / (2*a)
#        x2 = (-b - math.sqrt(d)) / (2*a)
#    return x1, x2
#
#print(get_solution(a, b, c))

#task2
tpl = (1, "str", 1023, 9, True, 123, False)
item = int(input("Введите элемент: "))
def get_part_of_tuple(tpl, item):
    return tpl[tpl.index(item)+1], tpl[tpl.index(item)+2], tpl[tpl.index(item)+3]

print(get_part_of_tuple(tpl, item))

#task3