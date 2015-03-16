### Problem:

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

### Hints:

1. what if the value is 0?
2. define a variable named reachable, which is the maximum index you can reach at this moment

from its first index, make the reachable to be the max of reachable and index + value. If the next index is less than reachable, then reture false, otherwise return true.

#### References:

#### Tags:

