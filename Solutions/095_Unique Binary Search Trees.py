class Solution:
    # @return an integer

    def numTrees(self, n):
        # numOfTrees[i] == j means for n is i, there are j unique
        # binary search trees for it.
        numOfTrees = [1, 1, 2]
        nextTrying = len(numOfTrees)
        while nextTrying <= n:
            # Comptute how many unique binary search trees are there for
            # n == nextTrying.
            count = 0
            for center in xrange(nextTrying):
                count += numOfTrees[center] * \
                    numOfTrees[nextTrying - center - 1]
            numOfTrees.append(count)
            nextTrying += 1
        return numOfTrees[n]
