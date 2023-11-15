class List():
    class Item():
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item
        
    def __init__(self):
        self.first_time = None
        self.count = 0

    def append(self, value):
        if self.count == 0:
            self.first_time = self.Item(value)
        else:
            item = self.first_time
            while item.next_item:
                item = item.next_item
            item.next_item = self.Item(value)
        self.count += 1
    
    def insert(self, value, index):
        if self.count == 0:
            self.first_time = self.Item(value)
            self.count += 1
        else:
            item = self.first_time
            x = 0
            if x == index:
                item.value = value
            elif self.count <= index:
                while item.next_item:
                    item = item.next_item
                item.next_item = self.Item(value)
                self.count += 1
            else:
                while x != index:
                    x += 1
                    item = item.next_item
                item.value = value

    def remove(self, value):
        item = self.first_time
        while item.value != value:
            item = item.next_item
        while item.next_item:
            item2 = item.next_item
            item.value = item2.value
            item = item2.next_item
        #for i in range(self.count):


      #хз, но вообще просто проверять в цикле пока self.value != value ну тоесть значение из метода ремув и значение в подклассе айтем не совпадут, а потом просто удалить, и переменные которые после идут ссылки там нужно будет поменять да

    def index(self, value):
        #должен возвращать индекс элемента со значение value
        pass

    def __str__(self) -> str:
        x = ""
        item = self.first_time
        for i in range(self.count):
            x += f"{item.value} ,"
            item = item.next_item
        return f"[{x}] , count={self.count}"#нужно дододелать
    
lst = List()
lst.append(9)
lst.append("lox")
lst.append(True)

print(lst, "\n")

lst.insert("sam lox", 5)
lst.remove("lox")

print(lst)