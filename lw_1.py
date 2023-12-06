#task 1
class List():
    class Item():
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item
        
    def __init__(self):
        self.first_item = None
        self.count = 0

    def append(self, value):
        if self.count == 0:
            self.first_item = self.Item(value)
        else:
            item = self.first_item
            while item.next_item:
                item = item.next_item
            item.next_item = self.Item(value)
        self.count += 1
    
    def insert(self, value, index):
        if self.count == 0:
            self.append(value)
        else:
            item = self.first_item
            x = 0
            if x == index:
                self.first_item = self.Item(value, item)
                self.count += 1
            elif self.count <= index:
                self.append(value)
            else:
                while x+1 != index:    
                    x += 1
                    item = item.next_item
                item.next_item = self.Item(value, item.next_item)
                self.count += 1

    def remove(self, value):#если элемент нужно удалить которого нет, то он упадет!!!
        item = self.first_item
        if item.value == value:
            self.first_item = item.next_item
        while item.value != value:
            if item.next_item.value == value:
                break
            else:
                item = item.next_item
        item2 = item.next_item
        item.next_item = item2.next_item
        self.count -= 1

    def index(self, value):
        item = self.first_item
        if item.value == value:
            return 0
        x = 0
        while item.value != value:
            item = item.next_item
            x += 1
        return x

    def __str__(self, var=None) -> str:
        if var != None:
            return var
        else:
            x = ""
            item = self.first_item
            for i in range(self.count):
                if item.next_item:
                    x += f"{item.value}, "
                    item = item.next_item
                else:
                    x += f"{item.value}"
            return f"[{x}]"

lst = List()
lst.append(9)
lst.append(True)

print(lst, "\n")

lst.insert("IT-cube", 5)
lst.append(2023)
lst.remove(9)
lst.append(2007)

print(lst, "\n")

lst.insert("IT-circle", 1)

print(lst, "\n")

print(f"{lst.index(2023)}\n")

#task 2
def sort(lst):
    if len(lst)>1:
        mid = len(lst)//2
        lefthalf = lst[:mid]
        righthalf = lst[mid:]

        sort(lefthalf)
        sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                lst[k]=lefthalf[i]
                i=i+1
            else:
                lst[k]=righthalf[j]
                j += 1
            k += 1

        while i<len(lefthalf):
            lst[k]=lefthalf[i]
            i += 1
            k += 1

        while j<len(righthalf):
            lst[k]=righthalf[j]
            j += 1
            k += 1

lst = [54,26,93,17,77,31,44,55,20]
print(f"Список до сортировки: {lst}")
sort(lst)
print(f"Список после сортировки: {lst}")