class Solution:
    # @param tokens, a list of string
    # @return an integer

    # def evalRPN(self, tokens):
    #     while len(tokens) > 2:
    #         for i in tokens:
    #             if i in ["+", "-", "*", "/"]:
    #                 index = tokens.index(i)
    #                 res = eval(
    #                     tokens[index - 2] + tokens[index] + tokens[index - 1])
    #                 tokens.pop(index - 2)
    #                 tokens.pop(index - 2)
    #                 tokens.pop(index - 2)
    #                 tokens.insert(index - 2, str(res))
    #     return tokens[0]
    def evalRPN(self, tokens):
        numerals, operators = [], {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                numerals.append(int(token))
            else:
                x, y = numerals.pop(), numerals.pop()
                numerals.append(int(operators[token](y * 1.0, x)))
        return numerals.pop()
