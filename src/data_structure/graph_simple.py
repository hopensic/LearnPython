from collections import defaultdict


# 找入席为0的顶点
def get_indegree_withzero(indegree_dic: dict):
    for v, indegree in indegree_dic.items():
        if indegree == 0:
            return v
    return None


# 拓扑排序
def topo_sort(vertexes_dict: dict, indegree_dic: dict):
    res = []
    for _ in range(len(vertexes_dict)):
        v = get_indegree_withzero(indegree_dic)
        # 没有找到入度为0的顶点
        if not v:
            raise Exception
        res.append(v)
        # 将v的邻接列表的入度减1
        for neibour in vertexes_dict[v]:
            indegree_dic[neibour] -= 1
        # 删除节点dict
        del vertexes_dict[v]
        # 删除入度dict，
        del indegree_dic[v]

    return res


# vertexes = ['1', '2', '3', '4', '5', '6', '7']
vertexes_adjacency_lst = [['1', '2', '3', '4'],
                          ['2', '4', '5'],
                          ['3', '6'],
                          ['4', '3', '6', '7'],
                          ['5', '4', '7'],
                          ['6'],
                          ['7', '6']]

vertex_adjacency_dic = {lst[0]: lst[1:] for lst in vertexes_adjacency_lst}
vertex_indegree_dic = {lst[0]: 0 for lst in vertexes_adjacency_lst}
for adjacency_lst in vertexes_adjacency_lst:
    for vertex in adjacency_lst[1:]:
        vertex_indegree_dic[vertex] += 1

lst = topo_sort(vertex_adjacency_dic, vertex_indegree_dic)
print(lst)
