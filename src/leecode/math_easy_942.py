from collections import Counter


class Solution:
    def diStringMatch(self, S: str) -> list:
        le = len(S) + 1
        lst = [x for x in range(0, le)]
        count = Counter(S)
        i_count = count['I']
        d_count = count['D']
        if i_count == 0:
            return sorted(lst, reverse=True)
        if d_count == 0:
            return lst
        if S[-1] == 'I':
            i_list = lst[0:i_count + 1]
            d_list = lst[:(-1) * (d_count + 1):-1]
        else:
            i_list = lst[0:i_count]
            d_list = sorted(lst[i_count:], reverse=True)

        ret_list = []
        index_i = 0
        index_d = 0
        for x in S:
            if x == 'I':
                ret_list.append(i_list[index_i])
                index_i += 1
            if x == 'D':
                ret_list.append(d_list[index_d])
                index_d += 1
        if S[-1] == 'I':
            ret_list.append(i_list[-1])
        else:
            ret_list.append(d_list[-1])

        return ret_list


# string = "IDIDIDDD"
string = "D"

s = Solution()
print(s.diStringMatch(string))
