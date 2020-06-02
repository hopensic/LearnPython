from collections import Counter
from typing import List

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode


class Vertex:
    def __init__(self, val):
        self.val = val
        self.adjacency_list = []
        self.in_degree = 0

    def add_adjacency(self, vertex: 'Vertex'):
        self.adjacency_list.append(vertex)

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
        for _ in range(len(self.vertex_dic)):
            v = self.get_indegree_withzeor()
            # 没有找到入度为0的顶点
            if not v:
                return False
            del self.vertex_dic[v.val]
            # 将v的邻接列表的入度减1
            for vertex in v.adjacency_list:
                vertex.del_indegree()
        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dagraph = DAGraph()
        for i in range(numCourses):
            vertex = Vertex(i)
            dagraph.add_Vertex(vertex)

        for prerequisite in prerequisites:
            dagraph.vertex_dic[prerequisite[1]].add_adjacency(dagraph.vertex_dic[prerequisite[0]])
            dagraph.vertex_dic[prerequisite[0]].add_indegree()

        return dagraph.topo_sort()


numCourses = 6
prerequisites = []
s1 = Solution()
print(s1.canFinish(numCourses, prerequisites))
