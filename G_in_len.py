class Vertex:
    
    def __init__(self, val):
        self.Value = val
        self.Hit = False
        self.level = 0

class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size# максимальное количество вершин
        self.m_adjacency = [[0] * size for _ in range(size)] # матрица смежности  0 отсутствие ребра 1 наличие
        self.vertex = [None] * size # хранит вершины

    def AddVertex(self, v): # сперва преобразуем в класс вертекс
        if not None in self.vertex:
            return False
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                break
        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex
        return


    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v): # получает на вход индекс
        self.vertex[v] = None  # ваш код удаления вершины со всеми её рёбрами
        for i in range(len(self.m_adjacency[v])):
            if self.m_adjacency[v][i] != 0:
                self.m_adjacency[v][i] = 0
        for j in range(len(self.m_adjacency)):
            if self.m_adjacency[j][v] == 1:
                self.m_adjacency[j][v] = 0
        # ваш код удаления вершины со всеми её рёбрами
        return


    def IsEdge(self, v1, v2):
        if self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1:
            return True
        # True если есть ребро между вершинами v1 и v2
        return False

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
        # добавление ребра между вершинами v1 и v2
        return

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0
        # удаление ребра между вершинами v1 и v2
        return

    def DFirstSearch(self,VFrom, VTo,result):
        if len(self.vertex) == 0:
            return result
        if VFrom >= len(self.vertex) or VTo >= len(self.vertex):
            return result
        if VFrom < 0 or VTo < 0:
            return result
        if VFrom == VTo and  self.IsEdge(VFrom,VTo) is True:
            node_from = self.vertex[VFrom]
            node_from.Hit = True
            result.append(node_from)
            return result

        if self.vertex[VFrom].Hit is False:
            result.append(self.vertex[VFrom])
            node_from = self.vertex[VFrom]
        else:
            node_from = result[0]

        if node_from.Hit is False:
            node_from.Hit = True

        edges = 0
        for i in range(len(self.m_adjacency[VFrom])):
            if self.m_adjacency[VFrom][i] == 1 and self.vertex[i].Hit is False:
                edges += 1
        if edges == 0:
            result.pop(len(result)-1)
            if len(result) >= 1:
                node_from = result[len(result)-1]
            if len(result) == 0:
                return result
            for i in range(len(self.vertex)):
                if self.vertex[i] == node_from:
                    VFrom = i
        if self.IsEdge(VFrom,VTo) is False:
            for i in range(len(self.m_adjacency[VFrom])):
                if self.m_adjacency[VFrom][i] == 1 and self.vertex[i].Hit is False:
                    return self.DFirstSearch(i, VTo,result)
            result.pop(0)
            if len(result) == 0:
                for i in range(len(self.vertex)):
                    self.vertex[i].Hit = False
                return []
            else:
                result[0].Hit = True
                for i in range(len(self.vertex)):
                    if self.vertex[i] == result[0]:
                        VFrom = i
                return self.DFirstSearch(VFrom,VTo,result)
        if self.IsEdge(VFrom,VTo):
           self.vertex[VTo].Hit = True
           result.append(self.vertex[VTo])
           for i in range(len(self.vertex)):
               self.vertex[i].Hit = False
           return result
    def DepthFirstSearch(self,VFrom, VTo):
        rezult = self.DFirstSearch(VFrom, VTo,[])
        return rezult

    def BreadthFirstSearch(self, VFrom, VTo):
        if self.m_adjacency[VFrom].count(0) == len(self.m_adjacency) or self.m_adjacency[VTo].count(0) == len(self.m_adjacency):  # если у начального и конечного элемента
            return []  # нет связей с остальными
        if VFrom == VTo:# проверяем если ввод и вывод ссылается на себя , равны
            if self.m_adjacency[VFrom].count(0) == len(self.m_adjacency):# если ребер никуда нет возврашаем отсутствие пути
                return []
            else:
                return [self.vertex[VFrom], self.vertex[VTo]]# если ребра есть поиск из узла в него же возвращает либо пустой список, либо список из двух элементов, если есть ребро само в себя, как для узла D.
        res = [] # итоговый список всех узлов графа поиска в ширину
        res.append(self.vertex[VFrom])  # добавляем в итоговый-промежуточный массив графф с которого начинаем поиск
        count_graf = -1 # счетчик показывает какое ребро естьв списке
        for i in res:  # бежим по этому списку
            if i.Hit != True:  # пробегаем по нему если стоит отметка что еще не смотрели hit != True
                i.Hit = True  # ставим флаг что просмотрено
                for j in self.m_adjacency[self.vertex.index(i)]:  # пробегаем по массиву где ребра этого графа
                    count_graf += 1 # показывает индекс еденицы
                    if j == 1 and self.vertex[count_graf].Hit != True and self.vertex[count_graf] not in res:  # если есть ребро и соответственно смежный граф но в списке его еще нет
                        res.append(self.vertex[count_graf])  # добавляем его в итоговый промежуточный список
                        self.vertex[count_graf].level = i.level + 1  # ставим отметку какой уровень
                count_graf = -1  # при выходе из цикла сбрасываем счетчик
        res_way = [] # итоговый список узлов кратчайщего пути
        res_way.insert(0, self.vertex[VTo]) # добавляем в список последний узел с него начинаем поиск
        index_way = VTo # bндекс списка ребер конечного узла
        count_way = -1
        while True:
            for i in self.m_adjacency[index_way]: #бежим по списку ребер конечного узла
                count_way += 1
                if i == 1: # находим ребро
                    if self.vertex[count_way].level == 0: # если это конечное ребро оно у нас под индексом 0 то поиск закончен путь найден
                        res_way.insert(0, self.vertex[count_way]), # добавляем эл в начало спписка
                        if self.vertex[VFrom] not in res_way or self.vertex[VTo] not in res_way:  # если начальный и конечный элемент не входят в итоговый список значит пути нет
                            for k in self.vertex: # обнуляем показатели графоф левел и уровни до начального состояния чтобы при следующем запуске функции все работало
                                k.level = 0
                                k.Hit = False
                            return []
                        else:
                            for k in self.vertex: # обнуляем показатели графоф левел и уровни до начального состояния смотри в тесте функцию test_my_peper_B2
                                if k is None:
                                    continue
                                k.level = 0
                                k.Hit = False
                            return res_way
                    if self.vertex[count_way].level == self.vertex[index_way].level - 1 and self.vertex[count_way] not in res_way: # ищем по ребру граф с уровнем меньше на 1
                        res_way.insert(0, self.vertex[count_way]) #  добавляем его в список
                        index_way = count_way #  переходим на пробег по нему меняя массив self.m_adjacency[index_way]
                        count_way = -1 #  обнуляем счетчик ребер  для очередного цикла поиска пути self.m_adjacency[index_way]
                        break


    # def BFirstSearch(self, VFrom, VTo,visited,queue,chouse_vertex):
    #     # узлы задаются позициями в списке vertex
    #     # возвращается список узлов -- путь из VFrom в VTo
    #     # или [] если пути нету
    #     chouse_vertex.Hit = True
    #     visited.append(chouse_vertex)
    #     if self.IsEdge(VFrom,VTo):
    #         visited.append(self.vertex[VTo])
    #         for i in range(len(self.vertex)):
    #             self.vertex[i].Hit = False
    #         return visited

    #     for i in range(len(self.m_adjacency[VFrom])):
    #         if self.m_adjacency[VFrom][i] == 1 and self.vertex[i].Hit is False:
    #             queue.append(self.vertex[i])

    #     if len(queue) != 0:
    #         chouse_vertex = queue[0]
    #         chouse_vertex.Hit = True
    #         queue.pop(0)
    #         for i in range(len(self.vertex)):
    #             if self.vertex[i] == chouse_vertex:
    #                 VFrom = i
    #         return self.BFirstSearch(VFrom, VTo,visited,queue, chouse_vertex)
    #     if len(queue) == 0 and chouse_vertex.Hit is True:
    #         for i in range(len(self.vertex)):
    #             self.vertex[i].Hit = False
    #         return []
    #     return self.BFirstSearch(VFrom, VTo,visited,queue, chouse_vertex)
    # def clear_way(self,inp_array,r,ret):
    #     if len(inp_array) ==0:
    #         return ret
    #     if len(inp_array) == 1:
    #         ret.append(r[0])
    #         return ret
    #     if self.IsEdge(inp_array[0],inp_array[1]):
    #         ret.append(r[0])
    #         r.pop(0)
    #         inp_array.pop(0)
    #         return self.clear_way(inp_array,r,ret)
    #     else:
    #         inp_array.pop(0)
    #         r.pop(0)
    #         return self.clear_way(inp_array,r,ret)



    # def BreadthFirstSearch(self, VFrom, VTo):
    #     if  not 1 in self.m_adjacency[VFrom]:
    #         return []
    #     if  not 1 in self.m_adjacency[VTo]:
    #             return []
    #     if VFrom == VTo:
    #         return [self.vertex[VFrom], self.vertex[VTo]]
    #     result = self.BFirstSearch(VFrom, VTo,[],[], self.vertex[VFrom])
    #     neighbours = []
    #     for i in range(len( result)):
    #         for j in range(len(self.vertex)):
    #             if result[i] == self.vertex[j]:
    #                 neighbours.append(j)
    #     ret_result = self.clear_way(neighbours,result,[])

    #     return ret_result


# graff = SimpleGraph(10)
# graff.AddVertex(0)
# graff.AddVertex(1)
# graff.AddVertex(2)
# graff.AddVertex(3)
# graff.AddEdge(0, 1)
# graff.AddEdge(0, 2)
# graff.AddEdge(0, 3)

# print(graff.BreadthFirstSearch(0, 3))



# graff = SimpleGraph(6)
# graff.AddVertex(0)
# graff.AddVertex(1)
# graff.AddVertex(2)
# graff.AddVertex(3)
# graff.AddVertex(4)
# graff.AddEdge(0, 1)
# graff.AddEdge(0, 2)
# graff.AddEdge(2, 3)
# graff.AddEdge(3, 4)
# # graff.AddEdge(1, 4)
# print(graff.BreadthFirstSearch(0, 4))
# print(graff.BreadthFirstSearch(0, 4))

# graff = SimpleGraph(6)
# graff.AddVertex(0)
# graff.AddVertex(1)
# graff.AddVertex(2)
# graff.AddVertex(3)
# graff.AddVertex(4)
# graff.AddVertex(5)
# graff.AddEdge(0, 1)
# graff.AddEdge(0, 2)
# graff.AddEdge(0, 3)
# graff.AddEdge(4, 2)
# graff.AddEdge(0, 3)
# graff.AddEdge(1, 2)
# graff.AddEdge(2, 3)
# graff.AddEdge(3, 4)
# print(graff.BreadthFirstSearch(1, 5))

# graff = SimpleGraph(7)
# graff.AddVertex(0)
# graff.AddVertex(1)
# graff.AddVertex(2)
# graff.AddVertex(3)
# graff.AddVertex(4)
# graff.AddVertex(5)
# graff.AddVertex(6)
# graff.AddEdge(0, 1)
# graff.AddEdge(0, 2)
# graff.AddEdge(1, 2)
# graff.AddEdge(2, 3)
# graff.AddEdge(3, 4)
# graff.AddEdge(4, 5)
# graff.AddEdge(5, 6)
# print(graff.BreadthFirstSearch(2, 6))
# print(graff.BreadthFirstSearch(2, 6))

# graff = SimpleGraph(5)
# graff.AddVertex(0)
# graff.AddVertex(1)
# graff.AddVertex(2)
# graff.AddVertex(3)
# graff.AddVertex(4)
# graff.AddEdge(4, 3)
# graff.AddEdge(2, 3)
# graff.AddEdge(4, 3)
# graff.AddEdge(4, 1)
# graff.AddEdge(0, 2)
# print(graff.BreadthFirstSearch(4, 0))
# print(graff.DepthFirstSearch(4, 0))
# print(graff.BreadthFirstSearch(0, 4))
# print(graff.BreadthFirstSearch(3, 4))

# graff = SimpleGraph(5)
# graff.AddVertex(0)
# graff.AddVertex(1)
# graff.AddVertex(2)
# graff.AddVertex(3)
# graff.AddVertex(4)
# graff.AddEdge(0, 1)
# # graff.AddEdge(0, 2)
# graff.AddEdge(0, 3)
# graff.AddEdge(1, 0)
# graff.AddEdge(1, 3)
# graff.AddEdge(1, 4)
# # graff.AddEdge(2, 0)
# # graff.AddEdge(2, 4)
# graff.AddEdge(3, 0)
# graff.AddEdge(3, 1)
# # graff.AddEdge(3, 2)
# graff.AddEdge(3, 3)
# graff.AddEdge(3, 4)
# graff.AddEdge(4, 1)
# graff.AddEdge(4, 3)
# print(graff.DepthFirstSearch(0, 2))
# print(graff.DepthFirstSearch(3, 0))