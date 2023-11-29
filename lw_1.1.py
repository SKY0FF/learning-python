class List():
    class Item():
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item
        
    def __init__(self):
        self.first_item = None
        self.count = 0
    
    def add_first_time(self, value):
        self.first_item = self.Item(value)
        self.count += 1

    def append(self, value):
        if self.count == 0:
            self.add_first_time(value)
        else:
            item = self.first_item
            while item.next_item:
                item = item.next_item
            item.next_item = self.Item(value)
            self.count += 1
    
    def insert(self, value, index):
        if self.count == 0:
            self.add_first_time(value)
        else:
            item = self.first_item
            x = 0
            if x == index:
                item2 = self.first_item
                self.first_item = self.Item(value, item2)
                self.count += 1
            elif self.count <= index:
                self.append(value)
            else:
                while x != index:
                    if x+1 == index:
                        break
                    else:
                        x += 1
                        item = item.next_item
                item2 = item.next_item
                item.next_item = self.Item(value, item2)
                self.count += 1

    def remove(self, value):
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
