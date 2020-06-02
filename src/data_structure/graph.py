from typing import List


class Vertex:
    def __init__(self, val):
        self.val = val
        self.adjacency_list = []
        self.in_degree = 0

    def add_adjacency(self, vertex: 'Vertex'):
        self.adjacency_list.append(vertex)

    def add_adjacency_list(self, adjacency_list: List):
        self.adjacency_list.extend(adjacency_list)
        for vertex in adjacency_list:
            vertex.add_indegree()

    def add_indegree(self):
        self.in_degree += 1


    def del_indegree(self):
        self.in_degree -= 1


class DAGraph:
    def __init__(self):
        self.vertex_dic = {}

    def add_Vertex(self, vertex: Vertex):
        self.vertex_dic[vertex.val] = vertex

    # 判断找到入度为0的顶点
    def get_indegree_withzeor(self):
        for v in self.vertex_dic.values():
            if v.in_degree == 0:
                return v
        return None

    def topo_sort(self):
        res = []
        for _ in range(len(self.vertex_dic)):
            v = self.get_indegree_withzeor()
            # 没有找到入度为0的顶点
            if not v:
                raise Exception
            res.append(v.val)
            del self.vertex_dic[v.val]
            # 将v的邻接列表的入度减1
            for vertex in v.adjacency_list:
                vertex.del_indegree()
        return res


vertex1 = Vertex(1)
vertex2 = Vertex(2)
vertex3 = Vertex(3)
vertex4 = Vertex(4)
vertex5 = Vertex(5)
vertex6 = Vertex(6)
vertex7 = Vertex(7)

adjacency_list1 = [vertex2, vertex3, vertex4]
adjacency_list2 = [vertex4, vertex5]
adjacency_list3 = [vertex6]
adjacency_list4 = [vertex3, vertex6, vertex7]
adjacency_list5 = [vertex4, vertex7]
adjacency_list7 = [vertex6]

vertex1.add_adjacency_list(adjacency_list1)
vertex2.add_adjacency_list(adjacency_list2)
vertex3.add_adjacency_list(adjacency_list3)
vertex4.add_adjacency_list(adjacency_list4)
vertex5.add_adjacency_list(adjacency_list5)
vertex7.add_adjacency_list(adjacency_list7)

dagraph = DAGraph()
dagraph.add_Vertex(vertex1)
dagraph.add_Vertex(vertex2)
dagraph.add_Vertex(vertex3)
dagraph.add_Vertex(vertex4)
dagraph.add_Vertex(vertex5)
dagraph.add_Vertex(vertex6)
dagraph.add_Vertex(vertex7)
print(dagraph.topo_sort())
