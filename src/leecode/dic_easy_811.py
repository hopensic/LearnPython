class Solution:
    def subdomainVisits(self, cpdomains):
        dic = {}
        lst = []
        for domain in cpdomains:
            lt = domain.split(" ")
            num = int(lt[0])
            dm = lt[1]
            idx = dm.index('.')
            for i in range(dm.count('.')):
                k = dm[idx + 1:]
                idx = dm.find('.', idx + 1)
                if k in dic:
                    dic[k] += num
                else:
                    dic[k] = num
        for domain in cpdomains:
            lt = domain.split(" ")
            num = int(lt[0])
            dm = lt[1]
            if dm in dic:
                dic[dm] += num
            else:
                dic[dm] = num
        for k, v in dic.items():
            lst.append(str(v) + ' ' + k)

        return lst


lst2 = ['2777 nak.mkw.co', '654 yaw.lmm.ca']
s = Solution()
print(s.subdomainVisits(lst2))
