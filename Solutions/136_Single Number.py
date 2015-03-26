import operator
class Solution:
    # @param A, a list of integer
    # @return an integer

    def singleNumber(self, A):
        ## This is a dic implementation
        # dic = {}
        # for i in A:
        #     dic[i]=dic.get(i, 0) + 1
        # for k in dic:
        #     if dic[k] == 1:
        #         return k
        ## This is the implementation in lambda
        # return reduce(lambda x, y: operator.xor(x,y), A)
        ## This is the most efficient way using reduce
        return reduce(operator.xor, A)

s = Solution()
print s.singleNumber([1,2,2,3,3])