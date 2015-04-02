class Solution:
    # @return an integer

    def numTrees(self, n):
        ## Recursive way
        # TIME LIMITATION ERROR
        # if n == 0:
        #     return 1
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # count = 0
        # for i in range(n):
        #     count += self.numTrees(i)*self.numTrees(n-i-1)
        # return count
        
        # numOfTrees[i] == j means for n is i, there are j unique
        # binary search trees for it.
        ## Iterative way
        numOfTrees = [1, 1, 2]
        nextTrying = len(numOfTrees)
        while nextTrying <= n:
            # Comptute how many unique binary search trees are there for
            # n == nextTrying.
            # f(3) = f(0)*f(2) + f(1)*f(1) + f(2)*f(0)
            count = 0
            for center in xrange(nextTrying):
                count += numOfTrees[center] * \
                    numOfTrees[nextTrying - center - 1]
            numOfTrees.append(count)
            nextTrying += 1
        return numOfTrees[n]
    

