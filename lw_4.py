class MyDict:
     
    def __init__(self) -> None: 
        self.__size = 25 
        self.__data = [[],] * self.__size#список в списке там значение, а хэш который генериться его индексы

    def __str__(self) -> str:
        return str(self.__data)
    
    def __get_hash(self, key):
        return sum([ord(j) * ((i + (i-1)) | 3) for i, j in enumerate(key)])

    def add(self, key, value):
        m = self.__get_hash(key)
        while m >= len(self.__data):
            self.__data.append([])
        self.__data[m] = [[key, value], ]

    def get(self, key):
        m = self.__get_hash(key)
        return self.__data[m]

my_dict = MyDict()
my_dict.add('str', 5)
my_dict.add('908', 'asd')
my_dict.add('ton', 'tonka')
my_dict.add('ton', 'ton')
my_dict.add('1', 123)
my_dict.add('bool', True)
print(my_dict.get('ton'))
print(my_dict)
