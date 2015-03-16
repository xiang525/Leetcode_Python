# class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]

    #     def fourSum(self, num, target):
    #         numLen, res, dict = len(num), set(), {}
    #         if numLen < 4:
    #             return []
    #         num.sort()
    #         for p in range(numLen):
    #             for q in range(p + 1, numLen):
    #                 if num[p] + num[q] not in dict:
    #                     dict[num[p] + num[q]] = [(p, q)]
    #                 else:
    #                     dict[num[p] + num[q]].append((p, q))
    #         print dict
    #         for i in range(numLen):
    #             for j in range(i + 1, numLen - 2):
    #                 T = target - num[i] - num[j]
    #                 if T in dict:
    #                     for k in dict[T]:
    #                         if k[0] > j:
    #                             res.add((num[i], num[j], num[k[0]], num[k[1]]))
    #         return [list(i) for i in res]


class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]

    def fourSum(self, num, target):
        numLen, dic = len(num), {}
        res = []
        if numLen < 4:
            return []
        # num.sort()
        for p in range(numLen):
            for q in range(p + 1, numLen):
                if num[p] + num[q] not in dic:
                    dic[num[p] + num[q]] = [(p, q)]
                else:
                    dic[num[p] + num[q]].append((p, q))
        keyList = dic.keys()
        for i in dic.keys():
            if target-i in dic.keys():
                for j in dic[i]:
                    for k in dic[target-i]:
                        if len(set(list(j) + list(k))) == 4:
                            s = list(j) + list(k)
                            # print s 
                            l = [num[n] for n in s]
                            l.sort()
                            res.append(l)
        result = []
        for i in res:
            if i not in result:
                result.append(i)
        return result