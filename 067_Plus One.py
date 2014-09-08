class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits

    def plusOne(self, digits):
    	digits = [str(i) for i in digits]
        st = "".join(digits)
        val = int(st) + 1
        return map(int, str(val))
