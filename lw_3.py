import math

class MyGraf():
    def __init__(self, lst_vertex, lst_edge, lst_values):
        self.lst_vertex = lst_vertex
        self.adjacency_matrix = []
        for i in range(len(self.lst_vertex)):
            self.adjacency_matrix.append([0]*len(self.lst_vertex))

        for i in range(len(lst_values)):
            self.adjacency_matrix[self.lst_vertex.index((lst_edge[i])[0])][self.lst_vertex.index((lst_edge[i])[1])] = lst_values[i]
            self.adjacency_matrix[self.lst_vertex.index((lst_edge[i])[1])][self.lst_vertex.index((lst_edge[i])[0])] = lst_values[i]
    
    #def get_free_vertex(self, vert):
    #    x = []
    #    for i in range(len(self.lst_vertex)):
    #        if self.adjacency_matrix[vert][i] != 0:
    #            x.append(i)
    #    return x
#
    #def deykster(self, initial_vertex, final_vertex):
    #    start = self.lst_vertex.index(initial_vertex)
    #    last = self.lst_vertex.index(final_vertex)
    #    free = self.get_free_vertex(start)
    #    
#
    #    return self.get_free_vertex(start)
#
#
#
    #    #вывести сам путь(ab, bc, cd) и его длину

    def arg_min(self, T, S):
            amin = -1
            m = math.inf  # максимальное значение
            for i, t in enumerate(T):
                if t < m and i not in S:
                    m = t
                    amin = i
        
            return amin

    def deykster(self):
        #import math
#
        #N = len(self.lst_vertex)  # число вершин в графе
        #T = [math.inf]*N   # последняя строка таблицы
#
        #v = 0       # стартовая вершина (нумерация с нуля)
        #S = {v}     # просмотренные вершины
        #T[v] = 0    # нулевой вес для стартовой вершины
        #M = [0]*N   # оптимальные связи между вершинами
#
        #while v != -1:          # цикл, пока не просмотрим все вершины
        #    for j, dw in enumerate(self.adjacency_matrix[v]):   # перебираем все связанные вершины с вершиной v
        #        if j not in S:           # если вершина еще не просмотрена
        #            w = T[v] + dw
        #            if w < T[j]:
        #                T[j] = w
        #                M[j] = v        # связываем вершину j с вершиной v
#
        #    v = self.arg_min(T, S)            # выбираем следующий узел с наименьшим весом
        #    if v >= 0:                    # выбрана очередная вершина
        #        S.add(v)                 # добавляем новую вершину в рассмотрение

        #print(T, M, sep="\n")
        M = [0, 3, 0, 2]
        # формирование оптимального маршрута:
        start = 2
        end = 3
        P = [end]
        print(P[-1])
        while end != start:
            end = M[P[-1]]
            P.append(end)

        return P
    
    def __str__(self):
        x = ""
        for i in range(len(self.adjacency_matrix)): 
            for j in range(len(self.adjacency_matrix)):
                x += f"{self.adjacency_matrix[i][j]}"
            x += '\n'
        return x

graf = MyGraf(["A", "B", "C", "D"], ["AC", "AD", "AB", "CB"], [5, 6, 6, 9])
graf.deykster()
print(graf)