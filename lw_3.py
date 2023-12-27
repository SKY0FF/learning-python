class MyGraf():
    def __init__(self, lst_vertex, lst_edge, lst_values):#lst_verte - строчный список с одним символом в элементе, lst_edge - строчный список с ребрами, lst_values - такой длина как ребра, и соответствует положениюю ребер  ВСЁ С КЛАВИАТУРЫ
        self.lst_vertex = lst_vertex
        self.adjacency_matrix = []
        for i in range(len(self.lst_vertex)):#заполенение нулями матрицы
            self.adjacency_matrix.append([0]*len(self.lst_vertex))

        for i in range(len(lst_values)):
            self.adjacency_matrix[self.lst_vertex.index((lst_edge[i])[0])][self.lst_vertex.index((lst_edge[i])[1])] = lst_values[i]
            self.adjacency_matrix[self.lst_vertex.index((lst_edge[i])[1])][self.lst_vertex.index((lst_edge[i])[0])] = lst_values[i]


    def deykster(self, initial_vertex, final_vertex):
        #вывести сам путь(ab, bc, cd) и его длину

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