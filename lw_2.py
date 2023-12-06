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
#tpl = tuple(input("Введите кортеж, между элементами поставьте пробел: ").split())
#item = input("Введите элемент: ")
#def get_part_of_tuple(tpl, item):
#    tpl = list(map(str, tpl))
#    x = []
#    if (tpl.index(item)+1) < len(tpl):
#        x.append(tpl[tpl.index(item)+1])
#    else:
#        x = ["Следующих элементов в кортеже нет!"]
#    if (tpl.index(item)+2) < len(tpl):
#        x.append(tpl[tpl.index(item)+2])
#    if (tpl.index(item)+3) < len(tpl):
#        x.append(tpl[tpl.index(item)+3])
#    return tuple(x)
#
#print(get_part_of_tuple(tpl, item))

#task3
#item = set(input("Введите число, которое нужно проверить, между цифрами в числе поставьте пробел: ").split())
#def is_true_number(item):
#    st = set({"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B"})
#    if st.issuperset(item):
#        return "Число записано корректно!"
#    else:
#        return "Число записано некорректно!"
#print(is_true_number(item))

#task4
lst = list(input("Введите слова, между ними поставьте пробел: ").split())
st = set(lst)
print(lst)
print(st)