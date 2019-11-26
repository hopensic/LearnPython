class Solution:
    def partitionLabels(self, S: str) -> list:
        dic_list = []
        for ch in S:
            is_new = True
            for idx, dic in enumerate(dic_list):
                # 如果ch在字典列表中，将该字典合并，并且清空后面的字典
                # 如果ch不在字典列表中，将该字符新建一个字典
                if ch in dic:
                    z = {}
                    # 合并字典
                    for d in dic_list[idx:]:
                        z.update(d)
                    # 将字符数的统计值加1
                    z[ch] += 1
                    # 清空idx之后的字典列表
                    dic_list[idx:] = []
                    # 将新字典追加到dic_list中
                    dic_list.append(z)
                    is_new = False
                    break;
            if is_new is True:
                dic_list.append({ch: 1})

        return [sum(dic.values()) for dic in dic_list]


string = "ababcbacadefegdehijhklij"
s = Solution()
print(s.partitionLabels(string))
