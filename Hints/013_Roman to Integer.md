### Problem:
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

### Hints:
Read the wikipedia first: [Roman Numerals](http://en.wikipedia.org/wiki/Roman_numerals)

I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000.
For example:  
2015 = 1000 + 1000 + 10 + 5 = MMXV  
2014 = 1000 + 1000 + 10 + 5 - 1 = MMXIV  
2013 = 1000 + 1000 + 10 + 1 + 1 + 1 = MMXIII

Notice that 4 = IV = V-I  
Generally, Roman Numerals are represent by descending order. If a pair of the two letters are in ascending order, 
the result is the substraction the smaller one from the larger one.

First make some assumptions:
1. The number is an integer;  
2. The range of the integers is from 1 to 3999, which is I to 3999 = 1000 + 1000 + 1000 + 1000 - 100 + 100 - 10 + 10 - 1
= MMMCMXCIX  
3. Question: what's the maximum number Roman numerals can represent? 

#### References:

#### Tags:

