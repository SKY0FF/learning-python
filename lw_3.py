class MyGraf():
    def __init__(self, lst_vertex, lst_edge, lst_values):#lst_verte - строчный список с одним символом в элементе, lst_edge - строчный список с ребрами, lst_values - такой длина как ребра, и соответствует положениюю ребер  ВСЁ С КЛАВИАТУРЫ
        self.lst_vertex = lst_vertex
        self.lst_edge = lst_edge
        self.lst_values = lst_values
        self.adjacency_matrix = []
        for i in range(len(lst_vertex)):
            self.adjacency_matrix.append([0]*len(lst_vertex))
        #тут матрица смежности -> в поле класса

    def deykster(self):
        pass
    
    def __str__(self):
        x = ""
        for i in range(len(self.adjacency_matrix)): 
            for j in range(len(self.adjacency_matrix)):
                x += f"{self.adjacency_matrix[i][j]}"
            x += '\n'
        return x
        #вывод матрицы смежности

graf = MyGraf(["A", "B", "C", "D"], ["AC", "AD", "AB", "CB"], [5, 6, 6, 9])
print(graf)