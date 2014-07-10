class Solution:
    # @return a string
    def longestPalindrome(self, s):
        
        def checkPalindrome(inputString = ""):
            if inputString[::-1] == inputString:
                return True
            else:
                return False
         
        palindromeString = ""
        maxLength = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if checkPalindrome(s[i:j+1]):
                        if len(s[i: j+1]) > maxLength:
                            palindromeString = s[i: j+1]
        return palindromeString
                        
                    
s = Solution()
print s.longestPalindrome("12112")