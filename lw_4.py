import hashlib, re
while True:  
    data = '1212312334'
    print(hash(data))
    #m = hashlib.sha256()
    #m.update(data.encode())
    #m.digest()
    #print(re.sub(r'[a-z]', '', m.hexdigest()))
#size = 25
#datap = [[],]*size
#print(datap)
#class Dict():
#     
#    def __init__(self): 
#        self.__size = 25 
#        self.__data = [[],] * self.__size#список в списке там значение, а хэш который генериться его индексы
#    
#    def add(self):
#        #тут на вход значение, к нему вычисляется хэш и сохраняется в словарь
#        pass
#
#    def get(self):
#        #тут вывод по ключу вывод значения
#        pass