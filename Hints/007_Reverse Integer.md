### Problem:

Reverse digits of an integer.

Example1: x = 123, return 321

Example2: x = -123, return -321

Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

### Hints:
* Thinking about negative numbers
* Thinking about overflow problems `-2**31+1 < x < 2**31-1`
* Thinking about begin with zeros

Take advantage of python, convert int to str, convert str to int, reverse str `[::-1]`

#### References:

#### Tags:
Math
