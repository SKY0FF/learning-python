import math

class MyGraf():
    def __init__(self, lst_vertex, lst_edge, lst_values):
        self.lst_vertex = lst_vertex
        self.adjacency_matrix = []
        for i in range(len(self.lst_vertex)):
            self.adjacency_matrix.append([math.inf]*len(self.lst_vertex))

        for i in range(len(lst_values)):
            self.adjacency_matrix[self.lst_vertex.index((lst_edge[i])[0])][self.lst_vertex.index((lst_edge[i])[1])] = lst_values[i]
            self.adjacency_matrix[self.lst_vertex.index((lst_edge[i])[1])][self.lst_vertex.index((lst_edge[i])[0])] = lst_values[i]

    def __get_link_v(self, v):
        for i, weight in enumerate(self.adjacency_matrix[v]):
            if weight > 0:
                yield i
    
    def __mini(self, T, ch):
        x = -1
        m = math.inf
        for i, t in enumerate(T):
            if t < m and i not in ch:
                m = t
                x = i
        return x

    def deykster(self, vert):
        l = len(self.lst_vertex)
        T = [math.inf] * l
        v = self.lst_vertex.index(vert)
        ch = {v}
        T[v] = 0
        M = [0]*l
        while v != -1:
            for i in self.__get_link_v(v):
                if i not in ch:
                    w = T[v] + self.adjacency_matrix[v][i]
                    if w < T[i]:
                        T[i] = w
                        M[i] = v
            v = self.__mini(T, ch)
            if v >= 0:
                ch.add(v)
        return T

    
    def __str__(self):
        x = ""
        for i in range(len(self.adjacency_matrix)): 
            for j in range(len(self.adjacency_matrix)):
                if self.adjacency_matrix[i][j] != math.inf:
                    x += f"{self.adjacency_matrix[i][j]}"
                else:
                    x += "0"
            x += '\n'
        return x

graf = MyGraf(["A", "B", "C", "D", "E", "F"], ["AC", "AD", "AB", "BC", "CE", "CF", "DF", "EF"], [1, 3, 3, 4, 7, 5, 2, 4])#ввод с клавиатуры
print(graf)
print(graf.deykster("A"))
