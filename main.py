from lw_1 import List

lst = List()
lst.append(9)
lst.append(True)

print(lst, "\n")

lst.insert("IT-cube", 5)
lst.append(2023)
lst.remove(9)

print(lst, "\n")

lst.insert("IT-circle", 1)

print(lst, "\n")

print(lst.index(2023))