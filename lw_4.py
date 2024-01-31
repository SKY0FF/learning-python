class MyDict:
     
    def __init__(self): 
        self.__size = 25
        self.__data = [[],] * self.__size

    def __str__(self):
        return str(self.__data)
    
    def __get_hash(self, key):
        return sum([ord(j) * ((i + (i-1)) | 3) for i, j in enumerate(key)]) if sum([ord(j) * ((i + (i-1)) | 3) for i, j in enumerate(key)]) > 0 else sum([ord(j) * ((i + (i-1)) | 3) for i, j in enumerate(key)]) * -1

    def add(self, key, value):
        m = self.__get_hash(key)
        while m >= len(self.__data):
            self.__data.append([])
        self.__data[m].append([key, value])

    def get(self, key):
        try:
            m = self.__get_hash(key)
            if len(self.__data[m]) == 1:
                return self.__data[m][0][1]
            else:
                for i in range(len(self.__data[m])):
                    if self.__data[m][i][0] == key:
                        return self.__data[m][i][1]
        except:
            return None

my_dict = MyDict()
my_dict.add('str', 5)
my_dict.add('962', 'rubles')
my_dict.add('971', 'number')
my_dict.add('ton', 'ton')
my_dict.add('1', 123)
my_dict.add('bool', True)
print(my_dict)
print(my_dict.get('971'))
print(my_dict.get('ton'))
