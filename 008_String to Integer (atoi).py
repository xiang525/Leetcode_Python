class Solution:
    # @return an integer

    def atoi(self, str):
        s = str.strip()
        if len(s) == 0:
            return 0
        INT_MAX, INT_MIN = 2147483647, -2147483648
        sign = 1
        if s[0] in '+-':
            if s[0] == '-':
                sign = -1
            s = s[1:]
        if s.isdigit():
            res = int(s)
        else:
            i = 0
            while s[i].isdigit():
                i += 1
            if i != 0:
                s = s[0:i]
                res = int(s)
            else:
                return 0
        if res > INT_MAX:
            return INT_MIN if sign == -1 else INT_MAX
        return sign * res
