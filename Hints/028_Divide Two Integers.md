### Problem:

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

### Hints:

1. like Eular's method
2. what if the divident or the divisor is negative?
3. consider time complexity

Instead of minus divisor one by one, use a faster way to minus its polynomial powers. like x^1, x^2, x^4,...
'''
        while a >= b:
            summing = b
            count = 1
            while summing + summing <= a:
                summing += summing
                count += count
            a -= summing
            res += count
'''
#### References:


#### Tags:
Math, Binary Search
