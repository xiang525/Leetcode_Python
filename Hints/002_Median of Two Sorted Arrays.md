### Problem:
 > There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

### Hints:
First we need to know what is median. 
> The median of a finite list of numbers can be found by arranging all the observations from lowest value to highest value and picking the middle one (e.g., the median of {3, 3, 5, 9, 11} is 5). If there is an even number of observations, then there is no single middle value; the median is then usually defined to be the mean of the two middle values (the median of {3, 5, 7, 9} is (5 + 7) / 2 = 6), which corresponds to interpreting the median as the fully trimmed mid-range. [wikipedia](http://en.wikipedia.org/wiki/Median)

Then a simple implementation should be like this:
```python
class Solution:
    # @return a float

    def findMedianSortedArrays(self, A, B):
        temp = sorted(A + B)
        if len(temp) % 2 == 0:
            return (temp[len(temp) / 2] + temp[len(temp) / 2 - 1]) / 2.0
        else:
            return temp[len(temp) / 2]
```
However we should think about the complexity of this implementation, it seems OK, but the `sorted()` function cost O(n log (n)), which is not the required operation cost.

Think about recursive way to solve this problem
For example, if we want to find the 7th number of two list A = [1,3,4,5]; B = [2,4,6,8,9,10]. Let x be the 7th number, then choose the third number of each list, and then compare them. 4<6, it means 1,3,4 are not the 7th number, then compare A=[5], B = [2,4,6,8,9,10], and find 4(7-3)th number. And do the recursive way.

```python
class Solution:
    # @return a float

    def getKth(self, A, B, k):
        lenA = len(A)
        lenB = len(B)
        if lenA > lenB:
            return self.getKth(B, A, k)
        if lenA == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])
        pa = min(k / 2, lenA)
        pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)

    def findMedianSortedArrays(self, A, B):
        lenA = len(A)
        lenB = len(B)
        if (lenA + lenB) % 2 == 1:
            return self.getKth(A, B, (lenA + lenB) / 2 + 1)
        else:
            # must multiply 0.5 for return a float else it will return an int
            return (self.getKth(A, B, (lenA + lenB) / 2) + self.getKth(A, B, (lenA + lenB) / 2 + 1)) * 0.5
```

#### References:

#### Tags:
**list**, **recursion**
