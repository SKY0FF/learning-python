from lw_1 import List

lst = List()
lst.append(9)
lst.append("lox")
lst.append(True)

print(lst, "\n")

lst.insert("sam lox", 5)
lst.remove("lox")

print(lst)