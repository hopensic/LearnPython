from leecode.common.common_class import MultiTreeNode


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        lst = []
        m = MultiTreeNode(tiles, '_')
        lst.append(m)
        num = 0
        while (True):
            if (len(lst) == 0):
                break
            t = lst.pop()
            num += 1
            for s in set(t.remain):
                child = MultiTreeNode(t.remain.replace(s, '', 1), s)
                t.add_child(child)
                lst.append(child)

        return num - 1


so = Solution()

string = "AAABBC"
print(so.numTilePossibilities(string))
