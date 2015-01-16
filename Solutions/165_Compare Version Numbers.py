class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer

    def compareVersion(self, version1, version2):
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        rv1, rv2 = 0, 0
        for i in range(len(v1)):
            rv1 += v1[i] * 0.1 ** i

        for j in range(len(v2)):
            rv2 += v2[j] * 0.1 ** j

        if rv1 > rv2:
            return 1
        elif rv1 < rv2:
            return -1
        else:
            return 0
