class Solution:

    def allPathsSourceTarget(self, graph):
        Solution.le = len(graph) - 1
        Solution.ret_lst = []
        nodelist = [x for x in range(len(graph))]
        stacks = [0]
        self.checks(graph, stacks)
        return Solution.ret_lst

    def checks(self, graph_list, stacks):
        while len(stacks) > 0:
            last = stacks[len(stacks) - 1]
            next_lst = graph_list[last]
            for i in next_lst:
                if i == Solution.le:
                    copy = stacks[:]
                    copy.append(i)
                    Solution.ret_lst.append(copy)
                else:
                    stacks.append(i)[]
                    self.checks(graph_list, stacks)
                    stacks.pop()
            return False


lst = [[2, 3, 4, 6], [], [3, 4, 5, 6], [5, 6], [5, 6], [], []]
s = Solution()
print(s.allPathsSourceTarget(lst))
