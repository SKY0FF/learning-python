class MyGraf():
    def __init__(self, lst_vertex, lst_edge, lst_values):#lst_verte - строчный список с одним символом в элементе, lst_edge - строчный список с ребрами, lst_values - такой длина как ребра, и соответствует положениюю ребер  ВСЁ С КЛАВИАТУРЫ
        self.lst_vertex = lst_vertex
        self.lst_edge = lst_edge
        self.lst_values = lst_values
        self.adjacency_matrix = []
        for i in range(len(lst_vertex)):#заполенение нулями матрицы
            self.adjacency_matrix.append([0]*len(lst_vertex))
        
        self.lst_edge_1 = []
        self.lst_edge_2 = []
        for i in range(len(lst_edge)):#вынос в отдельные списки первое и второе значения ребра
            self.lst_edge_1.append((self.lst_edge[i])[0])
            self.lst_edge_2.append((self.lst_edge[i])[1])
    

        for j in range(len(lst_vertex)):
            if lst_vertex[0] in self.lst_edge_1[j]:
                self.adjacency_matrix[0][j] = 1
        #for i in range(len(self.adjacency_matrix)): 
        #    for j in range(len(self.adjacency_matrix)):
        #        self.adjacency_matrix[i][j] = j
        #тут матрица смежности -> в поле класса

    def deykster(self):
        pass
    
    def __str__(self):
        x = ""
        for i in range(len(self.adjacency_matrix)): 
            for j in range(len(self.adjacency_matrix)):
                x += f"{self.adjacency_matrix[i][j]}"
            x += '\n'
        return f"{x}{self.lst_edge_1}\n{self.lst_edge_2}"
        #вывод матрицы смежности

graf = MyGraf(["A", "B", "C", "D"], ["AC", "AD", "AB", "CB"], [5, 6, 6, 9])
print(graf)