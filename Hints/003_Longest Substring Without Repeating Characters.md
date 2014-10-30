### Problem:
> Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

### Hints:
First find a char, if it has been visited before, then compare the substring from its last appearance to the position it visited with the substring from this position to the same length substrings. For example, "dabcabcd", visited from the beginning, and then at the 5th position, it finds out "a" has been explored before, then get the substring from "a" to "a" which is "abc", now get the same length string from the second "a", which is "abc", then compare them whether they are the same or not. Update the maximum length variable. 

Use hashtable to indicate whether a char has been visited or not.

Use a `ord` build-in function to find out its Unicode value.

```python
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = 0
        maxlen = 0
        hashtable = [-1 for i in range(256)]
        for i in range(len(s)):
            if hashtable[ord(s[i])] != -1:
                while start <= hashtable[ord(s[i])]:
                    hashtable[ord(s[start])] = -1
                    start += 1
            if i - start + 1 > maxlen: maxlen = i - start + 1
            hashtable[ord(s[i])] = i
        return maxlen
```
```python
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = 0
        maxlen = 0
        dict = {}
        for i in range(len(s)):
            dict[s[i]] = -1
        for i in range(len(s)):
            if dict[s[i]] != -1:
                while start <= dict[s[i]]:
                    dict[s[start]] = -1
                    start += 1
            if i - start + 1 > maxlen: maxlen = i - start + 1
            dict[s[i]] = i
        return maxlen
```
#### Note:
* What if a char appears in several places, and how can you compare them? For example: "abcbaabcba", the maximum substring is "abcba".

* How to update the hashtable?
#### References:

#### Tags:
**hashtable**, **string**
