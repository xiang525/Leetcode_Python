### Problem:
> Given an array of integers, find two numbers such that they add up to a specific target number.
>
> The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
>
> You may assume that each input would have exactly one solution.
>
> Input: numbers={2, 7, 11, 15}, target=9
>
> Output: index1=1, index2=2 

### Hints:
An naive way is pick one _number1_ and then find the number _target - number1_. This will cost O(n^2).

```python
class Solution:
    # @return a tuple, (index1, index2)

    def twoSum(self, num, target):
        for i in num:
            if target - i in num:
                return (num.index(i) + 1, num.index(target - i) + 1)
        return (-1, -1)
```
__ISSUE__: Time Limit Exceeded, since the array will be large enough, and you cannot find from its beginning without have a proper order of that array.

So before compare the sum and the target, we need to sort the list first.

```python
class Solution:
    # @return a tuple, (index1, index2)

    def twoSum(self, num, target):
        for i in sorted(num, reverse=True):
            if target - i in num:
                return (num.index(i) + 1, num.index(target - i) + 1)
        return (-1, -1)
```

Another way is to think about using two pointers, one is from beginning, and another one from the end of the SORTED list. And then return the index of its 

```python
class Solution:
    # @return a tuple, (index1, index2)

    def twoSum(self, num, target):
        index = []
        numtosort = num[:] 	# deep copy
        numtosort.sort()	# sort list
        i = 0				# pointer at beginning
        j = len(numtosort) - 1 # pointer at end
        while i < j:
            if numtosort[i] + numtosort[j] == target:
                for k in range(0, len(num)):
                    if num[k] == numtosort[i]:
                        index.append(k)
                        break
                for k in range(len(num) - 1, -1, -1):
                    if num[k] == numtosort[j]:
                        index.append(k)
                        break
                index.sort()
                break
            elif numtosort[i] + numtosort[j] < target:
                i = i + 1
            elif numtosort[i] + numtosort[j] > target:
                j = j - 1
        return (index[0] + 1, index[1] + 1)
```

#### Note:
* the index should plus one.
* the possible range of target should between the first two sum of sorted list, and last two sum of sorted list.
* we could assume that the list number are all non-negatives.
* there may exist two or more number which are the same, be careful when handling the index. Especially do not use `list.index(x)`. 

#### References:

#### Tags:
**list**, **sorted list**