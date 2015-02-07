class Solution:
    # @return a boolean

    def isValid(self, s):
        lookup, stack = {")": "(", "}": "{", "]": "["}, []
        for i in s:
            if i not in lookup:
                stack.append(i)
            else:
                if len(stack) == 0 or stack.pop() != lookup[i]:
                    return False
        return len(stack) == 0

    """
    naive way
    """
    # def isValid(self, s):
    # # match = [("(",")"),("[","]"),("{","}")]
    # match = {")": "(", "]": "[", "}": "{"}
    # stack = []
    # for c in s:
    #     if c not in match:
    #         stack.append(c)
    #     else:
    #         if len(stack) == 0:
    #             return False
    #         elif stack.pop() != match[c]:
    #             return False
    # if len(stack) == 0:
    #     return True
    # else:
    #     return False